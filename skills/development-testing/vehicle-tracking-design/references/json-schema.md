# JSON 数据结构规范

> Read when: Step 3 构建 JSON 数据结构时

脚本 `scripts/generate_tracking_xlsx.py` **同时支持嵌套格式（推荐）和扁平格式**，自动检测转换。

## 格式 A：嵌套格式（推荐）

```json
{
  "app_name": "App Store",
  "events": [
    {
      "event_id": "evt_001",
      "event_name": "appstore_launch",
      "event_chinese_name": "App Store 启动/入口",
      "trigger_condition": "用户通过任意入口启动 App Store",
      "control_type": "入口触发",
      "control_id": "appstore_icon",
      "page_name": "系统桌面 / 消息中心",
      "module": "5.1.11 首页",
      "analysis_purpose": "分析各渠道入口流量占比",
      "core_metric": "入口 UV 占比",
      "data_category": "车辆使用数据",
      "properties": [
        {"prop_name": "entry_type", "prop_chinese_name": "入口类型", "type": "string", "example_value": "desktop_icon"},
        {"prop_name": "screen", "prop_chinese_name": "屏幕编号", "type": "int", "example_value": "0"}
      ]
    }
  ],
  "paths": [
    {
      "path_id": "PATH_001",
      "path_name": "首页Banner引流路径",
      "path_description": "用户从首页通过Banner进入详情并安装",
      "core_indicator": "Banner CVR = banner_click UV / banner_display UV",
      "conversion_target": "15%",
      "data_category": "车辆使用数据",
      "steps": [
        {"step_order": 1, "event_id": "evt_005", "event_name": "home_page_view", "description": "用户进入首页"}
      ]
    }
  ],
  "funnels": [
    {
      "funnel_id": "FUNNEL_001",
      "funnel_name": "核心下载转化漏斗",
      "funnel_description": "从首页到安装成功的完整转化链路",
      "primary_metric": "整体安装转化率 = Step5 UV / Step1 UV",
      "optimization_target": "提升 Step2→Step3 转化",
      "data_category": "车辆使用数据",
      "steps": [
        {"step_order": 1, "step_name": "首页曝光", "event_id": "evt_005", "description": "App Store首页PV"}
      ]
    }
  ],
  "relations": [
    {
      "relation_id": "REL_001",
      "relation_name": "Banner 引流 → 详情页到达",
      "from_event": "evt_007",
      "to_event": "evt_008",
      "relation_type": "因果关系(点击跳转)",
      "description": "用户点击 Banner 后应到达对应应用详情页",
      "params": "banner_id,app_id,click_time",
      "analysis_purpose": "分析 Banner 引流效果",
      "data_category": "车辆使用数据"
    }
  ]
}
```

## 格式 B：扁平格式（直接映射 Excel 列）

```json
{
  "app_name": "账号APP",
  "events": [
    {
      "event_id": "ACC_001",
      "event_name": "账号登录",
      "event_desc": "用户完成账号密码登录",
      "analysis_purpose": "分析登录成功率",
      "core_metric": "登录成功率 = 成功UV / 尝试UV",
      "params": "user_id,login_type,screen,trigger_method",
      "params_desc": "用户ID,登录方式,屏幕编号,触发方式",
      "data_category": "车辆使用数据"
    }
  ],
  "paths": [
    {
      "path_id": "PATH_001",
      "path_name": "首次使用路径",
      "path_desc": "注册→绑定→首页",
      "key_nodes": "注册,绑定,首页",
      "conversion_target": "80%",
      "tracking_events": "ACC_001,ACC_201,ACC_101",
      "analysis_metric": "路径完成率",
      "data_category": "车辆使用数据"
    }
  ],
  "funnels": [
    {
      "funnel_id": "FUNNEL_001",
      "funnel_name": "车辆绑定漏斗",
      "funnel_steps": "1.开始绑定;2.扫码;3.确认;4.完成",
      "step_desc": "用户发起绑定到绑定成功",
      "tracking_events": "ACC_201,ACC_202,ACC_203,ACC_204",
      "conversion_metric": "各步骤转化率",
      "optimization_target": "减少扫码失败",
      "data_category": "车辆使用数据"
    }
  ],
  "relations": [
    {
      "rel_id": "REL_001",
      "rel_type": "消息→功能",
      "source_event": "ACC_501(消息接收)",
      "target_event": "ACC_301(服务预约开始)",
      "relation_desc": "用户收到服务提醒消息后，点击进入服务预约",
      "params": "message_id,user_id,click_time,landing_page,action",
      "analysis_purpose": "分析消息推送对功能使用的引导效果",
      "data_category": "车辆使用数据"
    }
  ]
}
```

## 检测规则

| 特征 | 格式 |
|------|------|
| `events[0].properties` 为数组 | 嵌套格式 A |
| `events[0].params` 为字符串 | 扁平格式 B |
| `paths[0].steps` 为数组 | 嵌套格式 A |
| `paths[0].key_nodes` 为字符串 | 扁平格式 B |
