from pandas import Timestamp


expected_results = {
    1: [
        {
            "close_time": Timestamp("2023-09-01 14:14:59.999000+0000", tz="UTC"),
            "open": 55306.46,
            "high": 55399.68,
            "low": 55217.22,
            "close": 55388.96,
            "volume": 276.690734,
            "quote_volume": 15295597.50785806,
            "trades": 0,
            "taker_buy_asset_volume": 145.211424,
            "taker_buy_quote_volume": 8027028.99029815,
            "returns": 0.0,
            "sma": 55388.96,
            "upper": 55388.96,
            "lower": 55388.96,
            "distance": 0.0,
            "side": 0,
            "strategy_returns": 0.0,
            "strategy_returns_tc": 0.0,
            "accumulated_returns": 1.0,
            "accumulated_strategy_returns": 1.0,
            "accumulated_strategy_returns_tc": 1.0,
            "margin_ratio": 0.0,
        },
        {
            "close_time": Timestamp("2023-09-01 14:19:59.999000+0000", tz="UTC"),
            "open": 55306.46,
            "high": 55399.68,
            "low": 55217.22,
            "close": 55388.96,
            "volume": 276.690734,
            "quote_volume": 15295597.50785806,
            "trades": 0,
            "taker_buy_asset_volume": 145.211424,
            "taker_buy_quote_volume": 8027028.99029815,
            "returns": 0.0,
            "sma": 55388.96,
            "upper": 55388.96,
            "lower": 55388.96,
            "distance": 0.0,
            "side": 0,
            "strategy_returns": 0.0,
            "strategy_returns_tc": 0.0,
            "accumulated_returns": 1.0,
            "accumulated_strategy_returns": 1.0,
            "accumulated_strategy_returns_tc": 1.0,
            "margin_ratio": 0.0,
        },
        {
            "close_time": Timestamp("2023-09-01 14:29:59.999000+0000", tz="UTC"),
            "open": 55388.95,
            "high": 55569.95,
            "low": 55388.95,
            "close": 55552.4,
            "volume": 149.363426,
            "quote_volume": 8288967.03877351,
            "trades": 1,
            "taker_buy_asset_volume": 82.67909,
            "taker_buy_quote_volume": 4588065.23181743,
            "returns": 0.002946423556387118,
            "sma": 55429.82000000001,
            "upper": 55511.54000000001,
            "lower": 55348.100000000006,
            "distance": 122.57999999999447,
            "side": -1,
            "strategy_returns": 0.0,
            "strategy_returns_tc": 0.0,
            "accumulated_returns": 1.002950768528602,
            "accumulated_strategy_returns": 1.0,
            "accumulated_strategy_returns_tc": 1.0,
            "margin_ratio": 0.004002528142238611,
        },
        {
            "close_time": Timestamp("2023-09-01 14:34:59.999000+0000", tz="UTC"),
            "open": 55550.89,
            "high": 56087.68,
            "low": 55550.89,
            "close": 55932.48,
            "volume": 692.924319,
            "quote_volume": 38726480.58078431,
            "trades": 0,
            "taker_buy_asset_volume": 411.223017,
            "taker_buy_quote_volume": 22979821.33981915,
            "returns": 0.006818529518377586,
            "sma": 55565.7,
            "upper": 55822.07115906435,
            "lower": 55309.32884093565,
            "distance": 366.7800000000061,
            "side": -1,
            "strategy_returns": -0.006818529518377586,
            "strategy_returns_tc": -0.006818529518377586,
            "accumulated_returns": 1.0098127857970252,
            "accumulated_strategy_returns": 0.993204663909056,
            "accumulated_strategy_returns_tc": 0.993204663909056,
            "margin_ratio": 0.004077834681277391,
        },
        {
            "close_time": Timestamp("2023-09-01 14:39:59.999000+0000", tz="UTC"),
            "open": 55932.48,
            "high": 56333.0,
            "low": 55932.48,
            "close": 56264.93,
            "volume": 603.660118,
            "quote_volume": 33896505.6971466,
            "trades": 0,
            "taker_buy_asset_volume": 356.915883,
            "taker_buy_quote_volume": 20037884.70780964,
            "returns": 0.005926179097336494,
            "sma": 55784.692500000005,
            "upper": 56177.559406502696,
            "lower": 55391.82559349731,
            "distance": 480.23749999999563,
            "side": -1,
            "strategy_returns": -0.005926179097336494,
            "strategy_returns_tc": -0.005926179097336494,
            "accumulated_returns": 1.0158148844101784,
            "accumulated_strategy_returns": 0.9873361612642192,
            "accumulated_strategy_returns_tc": 0.9873361612642192,
            "margin_ratio": 0.004114014876268444,
        },
        {
            "close_time": Timestamp("2023-09-01 14:44:59.999000+0000", tz="UTC"),
            "open": 56260.11,
            "high": 56317.43,
            "low": 56118.31,
            "close": 56168.82,
            "volume": 370.500359,
            "quote_volume": 20822485.25288953,
            "trades": 0,
            "taker_buy_asset_volume": 178.075904,
            "taker_buy_quote_volume": 10007121.78892216,
            "returns": -0.00170962942015996,
            "sma": 55979.6575,
            "upper": 56296.90479495825,
            "lower": 55662.41020504175,
            "distance": 189.16249999999854,
            "side": -1,
            "strategy_returns": 0.00170962942015996,
            "strategy_returns_tc": 0.00170962942015996,
            "accumulated_returns": 1.0140797010812264,
            "accumulated_strategy_returns": 0.9890255839449716,
            "accumulated_strategy_returns_tc": 0.9890255839449716,
            "margin_ratio": 0.004111708957739713,
        },
        {
            "close_time": Timestamp("2023-09-01 14:49:59.999000+0000", tz="UTC"),
            "open": 56168.82,
            "high": 56269.99,
            "low": 56080.96,
            "close": 56191.11,
            "volume": 324.51432,
            "quote_volume": 18225087.41727558,
            "trades": 0,
            "taker_buy_asset_volume": 145.064381,
            "taker_buy_quote_volume": 8146012.47892439,
            "returns": 0.0003967606653441501,
            "sma": 56139.335,
            "upper": 56283.225132740205,
            "lower": 55995.444867259794,
            "distance": 51.775000000001455,
            "side": -1,
            "strategy_returns": -0.0003967606653441501,
            "strategy_returns_tc": -0.0003967606653441501,
            "accumulated_returns": 1.0144821278464156,
            "accumulated_strategy_returns": 0.9886332553316708,
            "accumulated_strategy_returns_tc": 0.9886332553316708,
            "margin_ratio": 0.004104691162420367,
        },
        {
            "close_time": Timestamp("2023-09-01 14:54:59.999000+0000", tz="UTC"),
            "open": 56191.11,
            "high": 56200.0,
            "low": 56107.98,
            "close": 56145.0,
            "volume": 254.091606,
            "quote_volume": 14265787.89818125,
            "trades": 1,
            "taker_buy_asset_volume": 134.1124,
            "taker_buy_quote_volume": 7529521.30623853,
            "returns": -0.0008209293091875578,
            "sma": 56192.465000000004,
            "upper": 56244.314218894746,
            "lower": 56140.61578110526,
            "distance": -47.46500000000378,
            "side": 0,
            "strategy_returns": 0.0008209293091875578,
            "strategy_returns_tc": 0.0008209293091875578,
            "accumulated_returns": 1.0136496514828948,
            "accumulated_strategy_returns": 0.9894451865704871,
            "accumulated_strategy_returns_tc": 0.9894451865704871,
            "margin_ratio": 0.0,
        },
        {
            "close_time": Timestamp("2023-09-01 14:59:59.999000+0000", tz="UTC"),
            "open": 56145.0,
            "high": 56211.7,
            "low": 56106.97,
            "close": 56182.11,
            "volume": 270.145731,
            "quote_volume": 15171017.18758856,
            "trades": 0,
            "taker_buy_asset_volume": 168.231118,
            "taker_buy_quote_volume": 9447425.0774598,
            "returns": 0.0006607487960858385,
            "sma": 56171.759999999995,
            "upper": 56191.812316574265,
            "lower": 56151.707683425724,
            "distance": 10.35000000000582,
            "side": 0,
            "strategy_returns": 0.0,
            "strategy_returns_tc": 0.0,
            "accumulated_returns": 1.014319640592638,
            "accumulated_strategy_returns": 0.9894451865704871,
            "accumulated_strategy_returns_tc": 0.9894451865704871,
            "margin_ratio": 0.0,
        },
        {
            "close_time": Timestamp("2023-09-01 15:04:59.999000+0000", tz="UTC"),
            "open": 56182.12,
            "high": 56299.78,
            "low": 56172.09,
            "close": 56289.89,
            "volume": 298.797415,
            "quote_volume": 16804824.55255641,
            "trades": 0,
            "taker_buy_asset_volume": 139.83665,
            "taker_buy_quote_volume": 7864202.02549528,
            "returns": 0.0019165664875115606,
            "sma": 56202.027500000004,
            "upper": 56263.908712213364,
            "lower": 56140.14628778664,
            "distance": 87.86249999999563,
            "side": 0,
            "strategy_returns": 0.0,
            "strategy_returns_tc": 0.0,
            "accumulated_returns": 1.016265515727322,
            "accumulated_strategy_returns": 0.9894451865704871,
            "accumulated_strategy_returns_tc": 0.9894451865704871,
            "margin_ratio": 0.0,
        },
    ],
    10: [
        {
            "close_time": Timestamp("2023-09-01 14:14:59.999000+0000", tz="UTC"),
            "open": 55306.46,
            "high": 55399.68,
            "low": 55217.22,
            "close": 55388.96,
            "volume": 276.690734,
            "quote_volume": 15295597.50785806,
            "trades": 0,
            "taker_buy_asset_volume": 145.211424,
            "taker_buy_quote_volume": 8027028.99029815,
            "returns": 0.0,
            "sma": 55388.96,
            "upper": 55388.96,
            "lower": 55388.96,
            "distance": 0.0,
            "side": 0,
            "strategy_returns": 0.0,
            "strategy_returns_tc": 0.0,
            "accumulated_returns": 1.0,
            "accumulated_strategy_returns": 1.0,
            "accumulated_strategy_returns_tc": 1.0,
            "margin_ratio": 0.0,
        },
        {
            "close_time": Timestamp("2023-09-01 14:19:59.999000+0000", tz="UTC"),
            "open": 55306.46,
            "high": 55399.68,
            "low": 55217.22,
            "close": 55388.96,
            "volume": 276.690734,
            "quote_volume": 15295597.50785806,
            "trades": 0,
            "taker_buy_asset_volume": 145.211424,
            "taker_buy_quote_volume": 8027028.99029815,
            "returns": 0.0,
            "sma": 55388.96,
            "upper": 55388.96,
            "lower": 55388.96,
            "distance": 0.0,
            "side": 0,
            "strategy_returns": 0.0,
            "strategy_returns_tc": 0.0,
            "accumulated_returns": 1.0,
            "accumulated_strategy_returns": 1.0,
            "accumulated_strategy_returns_tc": 1.0,
            "margin_ratio": 0.0,
        },
        {
            "close_time": Timestamp("2023-09-01 14:29:59.999000+0000", tz="UTC"),
            "open": 55388.95,
            "high": 55569.95,
            "low": 55388.95,
            "close": 55552.4,
            "volume": 149.363426,
            "quote_volume": 8288967.03877351,
            "trades": 1,
            "taker_buy_asset_volume": 82.67909,
            "taker_buy_quote_volume": 4588065.23181743,
            "returns": 0.002946423556387118,
            "sma": 55429.82000000001,
            "upper": 55511.54000000001,
            "lower": 55348.100000000006,
            "distance": 122.57999999999447,
            "side": -1,
            "strategy_returns": 0.0,
            "strategy_returns_tc": 0.0,
            "accumulated_returns": 1.002950768528602,
            "accumulated_strategy_returns": 1.0,
            "accumulated_strategy_returns_tc": 1.0,
            "margin_ratio": 0.04013944442538307,
        },
        {
            "close_time": Timestamp("2023-09-01 14:34:59.999000+0000", tz="UTC"),
            "open": 55550.89,
            "high": 56087.68,
            "low": 55550.89,
            "close": 55932.48,
            "volume": 692.924319,
            "quote_volume": 38726480.58078431,
            "trades": 0,
            "taker_buy_asset_volume": 411.223017,
            "taker_buy_quote_volume": 22979821.33981915,
            "returns": 0.006818529518377586,
            "sma": 55565.7,
            "upper": 55822.07115906435,
            "lower": 55309.32884093565,
            "distance": 366.7800000000061,
            "side": -1,
            "strategy_returns": -0.006818529518377586,
            "strategy_returns_tc": -0.006818529518377586,
            "accumulated_returns": 1.0098127857970252,
            "accumulated_strategy_returns": 0.993204663909056,
            "accumulated_strategy_returns_tc": 0.993204663909056,
            "margin_ratio": 0.04469173459549476,
        },
        {
            "close_time": Timestamp("2023-09-01 14:39:59.999000+0000", tz="UTC"),
            "open": 55932.48,
            "high": 56333.0,
            "low": 55932.48,
            "close": 56264.93,
            "volume": 603.660118,
            "quote_volume": 33896505.6971466,
            "trades": 0,
            "taker_buy_asset_volume": 356.915883,
            "taker_buy_quote_volume": 20037884.70780964,
            "returns": 0.005926179097336494,
            "sma": 55784.692500000005,
            "upper": 56177.559406502696,
            "lower": 55391.82559349731,
            "distance": 480.23749999999563,
            "side": -1,
            "strategy_returns": -0.005926179097336494,
            "strategy_returns_tc": -0.005926179097336494,
            "accumulated_returns": 1.0158148844101784,
            "accumulated_strategy_returns": 0.9873361612642192,
            "accumulated_strategy_returns_tc": 0.9873361612642192,
            "margin_ratio": 0.04719350568838694,
        },
        {
            "close_time": Timestamp("2023-09-01 14:44:59.999000+0000", tz="UTC"),
            "open": 56260.11,
            "high": 56317.43,
            "low": 56118.31,
            "close": 56168.82,
            "volume": 370.500359,
            "quote_volume": 20822485.25288953,
            "trades": 0,
            "taker_buy_asset_volume": 178.075904,
            "taker_buy_quote_volume": 10007121.78892216,
            "returns": -0.00170962942015996,
            "sma": 55979.6575,
            "upper": 56296.90479495825,
            "lower": 55662.41020504175,
            "distance": 189.16249999999854,
            "side": -1,
            "strategy_returns": 0.00170962942015996,
            "strategy_returns_tc": 0.00170962942015996,
            "accumulated_returns": 1.0140797010812264,
            "accumulated_strategy_returns": 0.9890255839449716,
            "accumulated_strategy_returns_tc": 0.9890255839449716,
            "margin_ratio": 0.047027107371075544,
        },
        {
            "close_time": Timestamp("2023-09-01 14:49:59.999000+0000", tz="UTC"),
            "open": 56168.82,
            "high": 56269.99,
            "low": 56080.96,
            "close": 56191.11,
            "volume": 324.51432,
            "quote_volume": 18225087.41727558,
            "trades": 0,
            "taker_buy_asset_volume": 145.064381,
            "taker_buy_quote_volume": 8146012.47892439,
            "returns": 0.0003967606653441501,
            "sma": 56139.335,
            "upper": 56283.225132740205,
            "lower": 55995.444867259794,
            "distance": 51.775000000001455,
            "side": -1,
            "strategy_returns": -0.0003967606653441501,
            "strategy_returns_tc": -0.0003967606653441501,
            "accumulated_returns": 1.0144821278464156,
            "accumulated_strategy_returns": 0.9886332553316708,
            "accumulated_strategy_returns_tc": 0.9886332553316708,
            "margin_ratio": 0.04652671441712397,
        },
        {
            "close_time": Timestamp("2023-09-01 14:54:59.999000+0000", tz="UTC"),
            "open": 56191.11,
            "high": 56200.0,
            "low": 56107.98,
            "close": 56145.0,
            "volume": 254.091606,
            "quote_volume": 14265787.89818125,
            "trades": 1,
            "taker_buy_asset_volume": 134.1124,
            "taker_buy_quote_volume": 7529521.30623853,
            "returns": -0.0008209293091875578,
            "sma": 56192.465000000004,
            "upper": 56244.314218894746,
            "lower": 56140.61578110526,
            "distance": -47.46500000000378,
            "side": 0,
            "strategy_returns": 0.0008209293091875578,
            "strategy_returns_tc": 0.0008209293091875578,
            "accumulated_returns": 1.0136496514828948,
            "accumulated_strategy_returns": 0.9894451865704871,
            "accumulated_strategy_returns_tc": 0.9894451865704871,
            "margin_ratio": 0.0,
        },
        {
            "close_time": Timestamp("2023-09-01 14:59:59.999000+0000", tz="UTC"),
            "open": 56145.0,
            "high": 56211.7,
            "low": 56106.97,
            "close": 56182.11,
            "volume": 270.145731,
            "quote_volume": 15171017.18758856,
            "trades": 0,
            "taker_buy_asset_volume": 168.231118,
            "taker_buy_quote_volume": 9447425.0774598,
            "returns": 0.0006607487960858385,
            "sma": 56171.759999999995,
            "upper": 56191.812316574265,
            "lower": 56151.707683425724,
            "distance": 10.35000000000582,
            "side": 0,
            "strategy_returns": 0.0,
            "strategy_returns_tc": 0.0,
            "accumulated_returns": 1.014319640592638,
            "accumulated_strategy_returns": 0.9894451865704871,
            "accumulated_strategy_returns_tc": 0.9894451865704871,
            "margin_ratio": 0.0,
        },
        {
            "close_time": Timestamp("2023-09-01 15:04:59.999000+0000", tz="UTC"),
            "open": 56182.12,
            "high": 56299.78,
            "low": 56172.09,
            "close": 56289.89,
            "volume": 298.797415,
            "quote_volume": 16804824.55255641,
            "trades": 0,
            "taker_buy_asset_volume": 139.83665,
            "taker_buy_quote_volume": 7864202.02549528,
            "returns": 0.0019165664875115606,
            "sma": 56202.027500000004,
            "upper": 56263.908712213364,
            "lower": 56140.14628778664,
            "distance": 87.86249999999563,
            "side": 0,
            "strategy_returns": 0.0,
            "strategy_returns_tc": 0.0,
            "accumulated_returns": 1.016265515727322,
            "accumulated_strategy_returns": 0.9894451865704871,
            "accumulated_strategy_returns_tc": 0.9894451865704871,
            "margin_ratio": 0.0,
        },
    ],
}
