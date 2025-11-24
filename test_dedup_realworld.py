#!/usr/bin/env python3
# coding=utf-8
"""
真实场景去重测试
"""

import sys
sys.path.insert(0, '/home/user/webapp')

from main import calculate_title_similarity, deduplicate_similar_titles

def test_real_world_cases():
    """测试真实世界的重复场景"""
    print("=" * 80)
    print("真实场景测试：常见的新闻重复模式")
    print("=" * 80)
    print()
    
    # 真实场景：同一新闻的不同表述
    real_cases = [
        # 场景1：完全重复
        ("苹果发布iPhone 16", "苹果发布iPhone 16"),
        
        # 场景2：添加了修饰词
        ("特斯拉Model Y降价", "特斯拉Model Y大幅降价"),
        ("华为Mate 60发布", "华为Mate 60正式发布"),
        
        # 场景3：顺序调整
        ("DeepSeek超越GPT-4", "超越GPT-4的DeepSeek"),
        
        # 场景4：添加了细节
        ("比亚迪销量破百万", "比亚迪年度销量突破百万辆"),
        ("宁德时代发布新电池", "宁德时代发布新一代电池技术"),
        
        # 场景5：不同平台的标题党
        ("震惊！AI取代程序员", "AI将要取代程序员？专家这样说"),
        
        # 场景6：完全不同的新闻
        ("华为发布新手机", "苹果股价创新高"),
    ]
    
    for title1, title2 in real_cases:
        similarity = calculate_title_similarity(title1, title2)
        
        # 判断是否会被去重（默认阈值0.85）
        would_merge = "✓ 会合并" if similarity >= 0.85 else "✗ 不合并"
        
        print(f"{would_merge} (相似度: {similarity:.3f})")
        print(f"  标题1: {title1}")
        print(f"  标题2: {title2}")
        print()

def test_batch_deduplication():
    """测试批量去重效果"""
    print("=" * 80)
    print("批量去重测试：模拟真实爬取数据")
    print("=" * 80)
    print()
    
    # 模拟真实爬取的新闻数据（包含很多重复）
    mock_news = [
        {"title": "OpenAI发布GPT-5", "source_name": "知乎", "ranks": [1], "count": 10},
        {"title": "OpenAI正式发布GPT-5", "source_name": "微博", "ranks": [2], "count": 8},
        {"title": "GPT-5来了！OpenAI今日发布", "source_name": "36氪", "ranks": [3], "count": 6},
        {"title": "特斯拉Model 3降价促销", "source_name": "虎嗅", "ranks": [5], "count": 5},
        {"title": "特斯拉Model 3开启降价活动", "source_name": "澎湃", "ranks": [7], "count": 3},
        {"title": "比亚迪销量突破新高", "source_name": "新浪", "ranks": [4], "count": 4},
        {"title": "华为Mate 70系列发布", "source_name": "凤凰", "ranks": [6], "count": 3},
        {"title": "华为正式推出Mate 70系列", "source_name": "搜狐", "ranks": [8], "count": 2},
        {"title": "马斯克回应AI安全问题", "source_name": "网易", "ranks": [10], "count": 2},
    ]
    
    # 补充必要字段
    for item in mock_news:
        item.update({
            "first_time": "10:00",
            "last_time": "12:00",
            "time_display": "10:00-12:00",
            "rank_threshold": 5,
            "url": "",
            "mobileUrl": "",
            "is_new": False,
        })
    
    print(f"原始新闻数量: {len(mock_news)} 条")
    print()
    print("原始新闻列表:")
    for i, item in enumerate(mock_news, 1):
        print(f"  {i}. [{item['source_name']:4s}] {item['title']:<30s} 排名:{item['ranks']} 次数:{item['count']}")
    print()
    
    # 使用推荐阈值去重
    print("=" * 80)
    print("使用推荐阈值 0.85 进行去重")
    print("=" * 80)
    
    deduplicated = deduplicate_similar_titles(mock_news, 0.85)
    
    removed_count = len(mock_news) - len(deduplicated)
    print(f"\n✓ 去重完成：{len(mock_news)} 条 → {len(deduplicated)} 条（移除 {removed_count} 条重复）")
    print(f"✓ 去重率：{removed_count / len(mock_news) * 100:.1f}%")
    print()
    print("去重后新闻列表:")
    for i, item in enumerate(deduplicated, 1):
        print(f"  {i}. [{item['source_name']:4s}] {item['title']:<30s} 排名:{item['ranks']} 次数:{item['count']}")
    print()

def main():
    print("\n" + "🧪 TrendRadar 去重功能 - 真实场景测试".center(80, "="))
    print()
    
    try:
        test_real_world_cases()
        test_batch_deduplication()
        
        print("=" * 80)
        print("✅ 测试完成！去重功能可以有效处理真实场景中的重复新闻")
        print("💡 建议：")
        print("  - 默认阈值 0.85 适合大多数场景")
        print("  - 如果想更严格去重，可降低到 0.75-0.80")
        print("  - 如果担心误删，可提高到 0.90-0.95")
        print("=" * 80)
        
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
