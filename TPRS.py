PATTERN_DETECTION = {
    'stealth_accumulation': {
        'min_transactions': 3,
        'max_size_ratio': 0.2,
        'time_window': 3600
    },
    'distribution': {
        'min_transactions': 10,
        'min_unique_receivers': 5,
        'time_window': 7200
    },
    'wash_trading': {
        'min_cycle_length': 3,
        'max_time_between': 300,
        'min_volume': 1000
    }
}
