#!/usr/bin/env python3
# coding=utf-8
"""
去重功能测试脚本
测试calculate_title_similarity和deduplicate_similar_titles函数
"""

import sys
sys.path.insert(0, '/home/user/webapp')

from main import calculate_title_similarity, deduplicate_similar_titles

def test_similarity():
    """测试相似度计算"""
    print("=" * 60)
    print("测试1: 标题相似度计算")
    print("=" * 60)
    
    test_cases = [
        ("华为发布新款手机", "华为发布新款手机", 1.0),  # 完全相同
        ("华为发布新款手机", "华为推出新款手机", 0.85),  # 高度相似
        ("特斯拉降价", "特斯拉Model 3降价", 0.7),  # 中等相似
        ("比亚迪新能源汽车销量突破", "苹果发布新iPhone", 0.2),  # 不相似
    ]
    
    for title1, title2, expected_threshold in test_cases:
        similarity = calculate_title_similarity(title1, title2)
        status = "✓" if similarity >= expected_threshold or (expected_threshold < 0.5 and similarity < 0.5) else "✗"
        print(f"{status} 相似度: {similarity:.3f}")
        print(f"   标题1: {title1}")
        print(f"   标题2: {title2}")
        print()

def test_deduplication():
    """测试去重功能"""
    print("=" * 60)
    print("测试2: 标题去重功能")
    print("=" * 60)
    
    # 模拟新闻数据
    test_titles = [
        {
            "title": "华为发布Mate 70系列手机",
            "source_name": "知乎",
            "ranks": [1, 2],
            "count": 5,
            "first_time": "10:00",
            "last_time": "12:00",
            "time_display": "10:00-12:00",
            "rank_threshold": 5,
            "url": "http://example.com/1",
            "mobileUrl": "",
            "is_new": False,
        },
        {
            "title": "华为正式发布Mate 70系列手机",
            "source_name": "微博",
            "ranks": [3],
            "count": 3,
            "first_time": "10:30",
            "last_time": "11:00",
            "time_display": "10:30-11:00",
            "rank_threshold": 5,
            "url": "http://example.com/2",
            "mobileUrl": "",
            "is_new": False,
        },
        {
            "title": "特斯拉Model 3降价促销",
            "source_name": "36氪",
            "ranks": [5],
            "count": 2,
            "first_time": "11:00",
            "last_time": "11:30",
            "time_display": "11:00-11:30",
            "rank_threshold": 5,
            "url": "http://example.com/3",
            "mobileUrl": "",
            "is_new": False,
        },
        {
            "title": "特斯拉Model 3开启降价促销活动",
            "source_name": "虎嗅",
            "ranks": [7],
            "count": 1,
            "first_time": "11:30",
            "last_time": "11:30",
            "time_display": "11:30",
            "rank_threshold": 5,
            "url": "http://example.com/4",
            "mobileUrl": "",
            "is_new": False,
        },
        {
            "title": "比亚迪销量突破新高",
            "source_name": "澎湃",
            "ranks": [2],
            "count": 4,
            "first_time": "09:00",
            "last_time": "12:00",
            "time_display": "09:00-12:00",
            "rank_threshold": 5,
            "url": "http://example.com/5",
            "mobileUrl": "",
            "is_new": False,
        },
    ]
    
    print(f"原始新闻数量: {len(test_titles)}")
    print()
    
    # 显示原始标题
    print("原始标题列表:")
    for i, item in enumerate(test_titles, 1):
        print(f"  {i}. [{item['source_name']}] {item['title']} (排名: {item['ranks']}, 次数: {item['count']})")
    print()
    
    # 测试不同阈值的去重效果
    thresholds = [0.75, 0.85, 0.95]
    
    for threshold in thresholds:
        print(f"\n{'=' * 60}")
        print(f"使用相似度阈值: {threshold}")
        print(f"{'=' * 60}")
        
        deduplicated = deduplicate_similar_titles(test_titles.copy(), threshold)
        
        print(f"去重后数量: {len(deduplicated)} (移除了 {len(test_titles) - len(deduplicated)} 条)")
        print()
        print("去重后标题列表:")
        for i, item in enumerate(deduplicated, 1):
            print(f"  {i}. [{item['source_name']}] {item['title']} (排名: {item['ranks']}, 次数: {item['count']})")
        print()

def main():
    """主测试函数"""
    print("\n" + "🔍 TrendRadar 去重功能测试".center(60, "="))
    print()
    
    try:
        test_similarity()
        test_deduplication()
        
        print("=" * 60)
        print("✅ 所有测试完成！")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
