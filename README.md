# A Demo With Django

## Basic

1. 角色
    1. 诚信办
    2. 各部门
    
2. 权限
    1. 诚信办
        1. 创建基础信息条目
        2. 审核各部门的信息条目
        3. 提供被搜集信息的主体(自然人、企业)
        4. 对各部门的评分做权重，给出总分
        
    2. 各部门
        1. 创建信息条目，并等待审核
        2. (搜集并)录入信息
        3. 评分
        4. 上报总分到诚信办

## 基本数据结构

### department:
> 部门表

| 字段    | 类型         | 含义     |
| :---:   | :---:        | :---:    |
| id      | unsigned int | id       |
| title   | varchar(255) | 部门名称 |
| weigths | unsigned int | 权重     |

### person
> 个人表 

| 字段      | 类型         | 含义       |
| :---:     | :---:        | :---:      |
| id        | unsigned int | id         |
| name      | varchar(255) | 姓名       |
| sex       | tinyint(1)   | 性别1男2女 |
| id_number | char(18)     | 身份证号   |
| address   | varchar(255) | 地址       |
| token     | char(32)     | token      |

### info
> 元信息表

| 字段          | 类型         | 含义           |
| :---:         | :---:        | :---:          |
| id            | unsigned int | id             |
| department    | unsigned int | 部门id         |
| verify        | tinyint(1)   | 是否已经审核   |
| title         | varchar(255) | 标题           |
| desc          | varchar(255) | 描述           |
| remark        | varchar(255) | 额外信息       |
| score         | unsigned int | 分值           |
| maximum_score | unsigned int | 可获取做高分值 |

### score
> 评分表

| 字段   | 类型             | 含义   |
| :---:  | :---:            | :---:  |
| id     | unsigned int     | id     |
| person | unsigned int     | 个人id |
| score  | unsigned int     | 分数   |
| year   | tinyint(4)       | 年份   |
| month  | tinyint(2)       | 月份   |
| day    | tinyint(2)       | 天数   |
| time   | unsigned int(15) | 时间戳 |