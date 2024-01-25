from pandas import Timestamp

expected_performance = 1.0
expected_outperformance = -0.016266

expected_optimization_results = ({"ma": 2.0, "sd": 1.0}, 1.0)

expected_results = [
    {
        "close_time": Timestamp("2023-09-01 14:09:59.999000+0000", tz="UTC"),
        "open": 55306.46,
        "high": 55399.68,
        "low": 55217.22,
        "close": 55388.96,
        "volume": 276.690734,
        "quote_volume": 15295597.50785806,
        "trades": 0.0,
        "taker_buy_asset_volume": 145.211424,
        "taker_buy_quote_volume": 8027028.99029815,
        "returns": 0.0,
        "sma": 55388.96,
        "upper": 55388.96,
        "lower": 55388.96,
        "distance": 0.0,
        "side": 0.0,
        "strategy_returns": 0.0,
        "strategy_returns_tc": 0.0,
        "accumulated_returns": 1.0,
        "accumulated_strategy_returns": 1.0,
        "accumulated_strategy_returns_tc": 1.0,
    },
    {
        "close_time": Timestamp("2023-09-01 14:14:59.999000+0000", tz="UTC"),
        "open": 55306.46,
        "high": 55399.68,
        "low": 55217.22,
        "close": 55388.96,
        "volume": 276.690734,
        "quote_volume": 15295597.50785806,
        "trades": 0.0,
        "taker_buy_asset_volume": 145.211424,
        "taker_buy_quote_volume": 8027028.99029815,
        "returns": 0.0,
        "sma": 55388.96,
        "upper": 55388.96,
        "lower": 55388.96,
        "distance": 0.0,
        "side": 0.0,
        "strategy_returns": 0.0,
        "strategy_returns_tc": 0.0,
        "accumulated_returns": 1.0,
        "accumulated_strategy_returns": 1.0,
        "accumulated_strategy_returns_tc": 1.0,
    },
    {
        "close_time": Timestamp("2023-09-01 14:19:59.999000+0000", tz="UTC"),
        "open": 55306.46,
        "high": 55399.68,
        "low": 55217.22,
        "close": 55388.96,
        "volume": 276.690734,
        "quote_volume": 15295597.50785806,
        "trades": 0.0,
        "taker_buy_asset_volume": 145.211424,
        "taker_buy_quote_volume": 8027028.99029815,
        "returns": 0.0,
        "sma": 55388.96,
        "upper": 55388.96,
        "lower": 55388.96,
        "distance": 0.0,
        "side": 0.0,
        "strategy_returns": 0.0,
        "strategy_returns_tc": 0.0,
        "accumulated_returns": 1.0,
        "accumulated_strategy_returns": 1.0,
        "accumulated_strategy_returns_tc": 1.0,
    },
    {
        "close_time": Timestamp("2023-09-01 14:29:59.999000+0000", tz="UTC"),
        "open": 55388.95,
        "high": 55569.95,
        "low": 55388.95,
        "close": 55552.4,
        "volume": 149.363426,
        "quote_volume": 8288967.03877351,
        "trades": 0.0,
        "taker_buy_asset_volume": 82.67909,
        "taker_buy_quote_volume": 4588065.23181743,
        "returns": 0.002946423556387118,
        "sma": 55443.44,
        "upper": 55632.164255992706,
        "lower": 55254.7157440073,
        "distance": 108.95999999999913,
        "side": 0.0,
        "strategy_returns": 0.0,
        "strategy_returns_tc": 0.0,
        "accumulated_returns": 1.002950768528602,
        "accumulated_strategy_returns": 1.0,
        "accumulated_strategy_returns_tc": 1.0,
    },
    {
        "close_time": Timestamp("2023-09-01 14:34:59.999000+0000", tz="UTC"),
        "open": 55550.89,
        "high": 56087.68,
        "low": 55550.89,
        "close": 55932.48,
        "volume": 692.924319,
        "quote_volume": 38726480.58078431,
        "trades": 0.0,
        "taker_buy_asset_volume": 411.223017,
        "taker_buy_quote_volume": 22979821.33981915,
        "returns": 0.006818529518377586,
        "sma": 55624.613333333335,
        "upper": 56182.33932961943,
        "lower": 55066.887337047236,
        "distance": 307.8666666666686,
        "side": 0.0,
        "strategy_returns": 0.0,
        "strategy_returns_tc": 0.0,
        "accumulated_returns": 1.0098127857970252,
        "accumulated_strategy_returns": 1.0,
        "accumulated_strategy_returns_tc": 1.0,
    },
    {
        "close_time": Timestamp("2023-09-01 14:39:59.999000+0000", tz="UTC"),
        "open": 55932.48,
        "high": 56333.0,
        "low": 55932.48,
        "close": 56264.93,
        "volume": 603.660118,
        "quote_volume": 33896505.6971466,
        "trades": 0.0,
        "taker_buy_asset_volume": 356.915883,
        "taker_buy_quote_volume": 20037884.70780964,
        "returns": 0.005926179097336494,
        "sma": 55916.60333333333,
        "upper": 56629.663784160104,
        "lower": 55203.54288250656,
        "distance": 348.32666666666773,
        "side": 0.0,
        "strategy_returns": 0.0,
        "strategy_returns_tc": 0.0,
        "accumulated_returns": 1.0158148844101784,
        "accumulated_strategy_returns": 1.0,
        "accumulated_strategy_returns_tc": 1.0,
    },
    {
        "close_time": Timestamp("2023-09-01 14:44:59.999000+0000", tz="UTC"),
        "open": 56260.11,
        "high": 56317.43,
        "low": 56118.31,
        "close": 56168.82,
        "volume": 370.500359,
        "quote_volume": 20822485.25288953,
        "trades": 0.0,
        "taker_buy_asset_volume": 178.075904,
        "taker_buy_quote_volume": 10007121.78892216,
        "returns": -0.00170962942015996,
        "sma": 56122.07666666667,
        "upper": 56464.24302990721,
        "lower": 55779.91030342613,
        "distance": 46.743333333331975,
        "side": 0.0,
        "strategy_returns": -0.0,
        "strategy_returns_tc": -0.0,
        "accumulated_returns": 1.0140797010812264,
        "accumulated_strategy_returns": 1.0,
        "accumulated_strategy_returns_tc": 1.0,
    },
    {
        "close_time": Timestamp("2023-09-01 14:49:59.999000+0000", tz="UTC"),
        "open": 56168.82,
        "high": 56269.99,
        "low": 56080.96,
        "close": 56191.11,
        "volume": 324.51432,
        "quote_volume": 18225087.41727558,
        "trades": 0.0,
        "taker_buy_asset_volume": 145.064381,
        "taker_buy_quote_volume": 8146012.47892439,
        "returns": 0.0003967606653441501,
        "sma": 56208.28666666666,
        "upper": 56308.89603866177,
        "lower": 56107.67729467155,
        "distance": -17.176666666659003,
        "side": 0.0,
        "strategy_returns": 0.0,
        "strategy_returns_tc": 0.0,
        "accumulated_returns": 1.0144821278464156,
        "accumulated_strategy_returns": 1.0,
        "accumulated_strategy_returns_tc": 1.0,
    },
    {
        "close_time": Timestamp("2023-09-01 14:54:59.999000+0000", tz="UTC"),
        "open": 56191.11,
        "high": 56200.0,
        "low": 56107.98,
        "close": 56145.0,
        "volume": 254.091606,
        "quote_volume": 14265787.89818125,
        "trades": 0.0,
        "taker_buy_asset_volume": 134.1124,
        "taker_buy_quote_volume": 7529521.30623853,
        "returns": -0.0008209293091875578,
        "sma": 56168.31,
        "upper": 56214.42846051117,
        "lower": 56122.19153948883,
        "distance": -23.30999999999767,
        "side": 0.0,
        "strategy_returns": -0.0,
        "strategy_returns_tc": -0.0,
        "accumulated_returns": 1.0136496514828948,
        "accumulated_strategy_returns": 1.0,
        "accumulated_strategy_returns_tc": 1.0,
    },
    {
        "close_time": Timestamp("2023-09-01 14:59:59.999000+0000", tz="UTC"),
        "open": 56145.0,
        "high": 56211.7,
        "low": 56106.97,
        "close": 56182.11,
        "volume": 270.145731,
        "quote_volume": 15171017.18758856,
        "trades": 0.0,
        "taker_buy_asset_volume": 168.231118,
        "taker_buy_quote_volume": 9447425.0774598,
        "returns": 0.0006607487960858385,
        "sma": 56172.74,
        "upper": 56221.622745421264,
        "lower": 56123.85725457873,
        "distance": 9.37000000000262,
        "side": 0.0,
        "strategy_returns": 0.0,
        "strategy_returns_tc": 0.0,
        "accumulated_returns": 1.014319640592638,
        "accumulated_strategy_returns": 1.0,
        "accumulated_strategy_returns_tc": 1.0,
    },
    {
        "close_time": Timestamp("2023-09-01 15:04:59.999000+0000", tz="UTC"),
        "open": 56182.12,
        "high": 56299.78,
        "low": 56172.09,
        "close": 56289.89,
        "volume": 298.797415,
        "quote_volume": 16804824.55255641,
        "trades": 0.0,
        "taker_buy_asset_volume": 139.83665,
        "taker_buy_quote_volume": 7864202.02549528,
        "returns": 0.0019165664875115606,
        "sma": 56205.666666666664,
        "upper": 56356.1919526928,
        "lower": 56055.141380640525,
        "distance": 84.22333333333518,
        "side": 0.0,
        "strategy_returns": 0.0,
        "strategy_returns_tc": 0.0,
        "accumulated_returns": 1.016265515727322,
        "accumulated_strategy_returns": 1.0,
        "accumulated_strategy_returns_tc": 1.0,
    },
]