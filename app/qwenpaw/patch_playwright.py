import os
import re
import subprocess
import sys

def find_and_patch_config_file():
    """
    核心步骤：自动查找并修补Playwright的CDN配置文件。
    """
    print("🔍 正在定位Playwright的浏览器下载配置文件...")
    
    # 策略1：查找当前Python环境site-packages下的路径
    import site
    potential_paths = []
    for site_packages_dir in site.getsitepackages():
        # 这是标准的pip安装路径
        standard_path = os.path.join(site_packages_dir, 'playwright', 'driver', 'package', 'lib', 'server', 'registry', 'index.js')
        potential_paths.append(standard_path)
        # 也可能是用户安装路径
        user_site = site.getusersitepackages()
        user_path = os.path.join(user_site, 'playwright', 'driver', 'package', 'lib', 'server', 'registry', 'index.js')
        potential_paths.append(user_path)
    
    # 策略2：如果通过playwright命令本身定位其驱动路径（更准确）
    try:
        # 尝试通过 `playwright --path` 命令获取驱动路径（新版本Playwright支持）
        result = subprocess.run([sys.executable, '-m', 'playwright', '--path'], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            driver_path = result.stdout.strip()
            config_path = os.path.join(driver_path, 'package', 'lib', 'server', 'registry', 'index.js')
            potential_paths.insert(0, config_path)  # 插入到最前面，优先尝试
    except:
        pass  # 如果命令不支持，忽略，继续用其他策略
    
    target_file = None
    for path in potential_paths:
        if os.path.isfile(path):
            target_file = path
            print(f"✅ 找到配置文件：{target_file}")
            break
    
    if not target_file:
        print("⚠️  未能自动定位配置文件，无法替换镜像源。")
        return False
    
    # 开始修改文件
    try:
        with open(target_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 使用更灵活的正则表达式匹配可能的格式
        # 匹配类似 const PLAYWRIGHT_CDN_MIRRORS = [ ... ]; 的结构
        pattern = r'(const\s+PLAYWRIGHT_CDN_MIRRORS\s*=\s*\[)[^\]]*(\]\s*;)'
        match = re.search(pattern, content)
        
        if match:
            old_mirrors = match.group(0)
            new_mirrors = match.group(1) + "'https://registry.npmmirror.com/-/binary/playwright'" + match.group(2)
            content_new = content.replace(old_mirrors, new_mirrors)
            
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(content_new)
            
            print("✅ 成功将CDN镜像替换为国内源！")
            return True
        else:
            print("⚠️  在配置文件中未找到标准的 PLAYWRIGHT_CDN_MIRRORS 定义。")
            return False
            
    except Exception as e:
        print(f"❌ 修改配置文件时出错：{e}")
        return False

if __name__ == "__main__":
    find_and_patch_config_file()
