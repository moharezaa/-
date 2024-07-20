def merge_intervals(intervals):
    # اگر لیست بازه‌ها خالی باشد، خروجی نیز خالی خواهد بود
    if not intervals:
        return []

    # بازه‌ها را بر اساس نقطه شروع آنها مرتب می‌کنیم
    intervals.sort(key=lambda x: x[0])

    # لیست نهایی برای نگهداری بازه‌های ادغام شده
    merged = [intervals[0]]

    for current in intervals[1:]:
        # آخرین بازه در لیست ادغام شده‌ها
        last = merged[-1]

        # اگر بازه‌ها هم‌پوشانی دارند، آنها را ادغام می‌کنیم
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)

    return merged

# مثال
intervals = [(1, 3), (2, 6), (8, 10)]
print(merge_intervals(intervals))  # خروجی: [(1, 6), (8, 10)]
