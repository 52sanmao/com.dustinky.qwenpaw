# QwenPaw for fnOS

QwenPaw 飞牛 NAS 应用包，将 [QwenPaw](https://github.com/agentscope-ai/QwenPaw) 部署到飞牛 NAS 系统中。

## 简介

QwenPaw 是一款个人助理型产品，部署在您自己的环境中。支持多通道对话（钉钉、飞书、QQ、Discord、iMessage）、定时执行任务，能力由 Skills 决定且可无限扩展。数据全在本地，不依赖第三方托管，由 AgentScope 团队基于 AgentScope、AgentScope Runtime 与 ReMe 构建。

## 功能特性

- 多通道对话支持：钉钉、飞书、QQ、Discord、iMessage
- 定时执行任务
- Skills 能力扩展
- 本地数据存储，无需第三方托管
- 内置 Ollama 驱动支持
- Playwright 浏览器自动化支持

## 安装说明

### 前置要求

- 飞牛 NAS 系统 (版本 >= 0.9.21)
- 如需使用内置 Ollama 模型驱动，请先在飞牛应用商店中安装 **Ollama** 应用

### 安装步骤

1. 下载 `.fpk` 安装包
2. 在飞牛应用商店中上传安装
3. 安装过程中会自动配置内置的 Ollama 驱动及 Playwright
4. **进度条可能会在 55% 左右停留较长时间**，请耐心等待

### 安装后配置

安装完成后，请进入 QwenPaw 的**模型设置页面**，将 Ollama 的基础 URL 从默认的 `http://localhost:11434/v1` 修改为 `http://localhost:11435/v1` 才能正常连接。

## 配置选项

| 选项 | 说明 | 默认值 |
|------|------|--------|
| PyPI 安装源 | 选择 pip 安装源 | 清华源 |
| 日志级别 | 日志输出详细程度 | info |
| 工作进程数 | 根据 CPU 核心数设置 | 4 |

## 项目结构

```
com.dustinky.qwenpaw/
├── app/                    # 应用资源
│   ├── qwenpaw/           # 补丁脚本
│   └── ui/                # UI 资源
├── cmd/                    # 命令脚本
│   ├── install_callback   # 安装回调
│   ├── upgrade_callback   # 升级回调
│   ├── uninstall_callback # 卸载回调
│   ├── config_callback    # 配置回调
│   └── main               # 主程序入口
├── config/                 # 配置文件
├── wizard/                 # 安装向导配置
└── manifest               # 应用清单
```

## 相关链接

- [QwenPaw 项目主页](https://github.com/agentscope-ai/QwenPaw)
- [AgentScope 团队](https://github.com/agentscope-ai)
- [飞牛 NAS](https://www.fnnas.com/)

## 交流

QQ 群：[1091348192](https://qun.qq.com/universal-share/share?ac=1&authKey=eh3ZjF03sS5h3xycHBkJxllqsbpz0QJTTRMVjySNNDp4W3jtafZtnrRe9t%2BrHfmZ&busi_data=eyJncm91cENvZGUiOiIxMDkxMzQ4MTkyIiwidG9rZW4iOiJUM043MmdJbytIWTlndCtkaWgyV2pUQTgyeXh1YzVMR21SZGxEUjJuVHRjVW1WYTE3d3B1ODI4c28rSjdUQy9LIiwidWluIjoiODE1MjIzNTgifQ%3D%3D&data=zc5hDTqOp2xm6e7x-U_2Yl0KARi6A5uyvzlnyU6cfjAFK7qn4S8Zz5D9kvvSd9BlUXV7gKXlmPyfVQV2PA_IiQ&svctype=4&tempid=h5_group_info)

## 许可证

本项目采用 [Apache-2.0](LICENSE) 许可证。

QwenPaw 原项目同样采用 Apache-2.0 许可证。
