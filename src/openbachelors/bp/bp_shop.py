from fastapi import APIRouter
from fastapi import Request

from ..const.json_const import true, false, null
from ..const.filepath import CONFIG_JSON, VERSION_JSON
from ..util.const_json_loader import const_json_loader
from ..util.player_data import player_data_decorator
import time
router = APIRouter()


@router.post("/shop/getSkinGoodList")
@player_data_decorator
async def shop_getSkinGoodList(player_data, request: Request):
    request_json = await request.json()
    # 加载皮肤商品列表数据
    try:
        skin_goods_data = const_json_loader["res/shop/SkinGoodList.json"].copy()
        response = skin_goods_data
    except:
        response = {"goodList": []}
    return response


@router.post("/shop/getFurniGoodList")
@player_data_decorator
async def shop_getFurniGoodList(player_data, request: Request):
    request_json = await request.json()
    # 加载家具商品列表数据
    try:
        furni_goods_data = const_json_loader["res/shop/FurniGoodList.json"].copy()
        response = furni_goods_data
    except:
        response = {"goods": [], "groups": []}
    return response


@router.post("/shop/getSocialGoodList")
@player_data_decorator
async def shop_getSocialGoodList(player_data, request: Request):
    request_json = await request.json()
    # 加载社交商品列表数据
    try:
        social_goods_data = const_json_loader["res/shop/SocialGoodList.json"].copy()
        response = social_goods_data
    except:
        response = {
            "goodList": [],
            "charPurchase": {
                "char_198_blackd": 6,
                "char_187_ccheal": 6,
                "char_260_durnar": 6,
            },
            "costSocialPoint": 99999999,
            "creditGroup": "creditGroup2",
        }
    return response


@router.post("/shop/getLowGoodList")
@player_data_decorator
async def shop_getLowGoodList(player_data, request: Request):
    request_json = await request.json()
    # 加载低价商品列表数据
    try:
        low_goods_data = const_json_loader["res/shop/LowGoodList.json"].copy()
        response = low_goods_data
    except:
        response = {
            "groups": [],
            "goodList": [],
            "shopEndTime": 2147483647,
            "newFlag": [],
        }
    return response


@router.post("/shop/getHighGoodList")
@player_data_decorator
async def shop_getHighGoodList(player_data, request: Request):
    request_json = await request.json()
    # 加载高价商品列表数据
    try:
        high_goods_data = const_json_loader["res/shop/HighGoodList.json"].copy()
        response = high_goods_data
    except:
        response = {
            "goodList": [],
            "progressGoodList": {},
            "newFlag": [],
        }
    return response


@router.post("/shop/getClassicGoodList")
@player_data_decorator
async def shop_getClassicGoodList(player_data, request: Request):
    request_json = await request.json()
    # 加载经典商品列表数据
    try:
        classic_goods_data = const_json_loader["res/shop/ClassicGoodList.json"].copy()
        response = classic_goods_data
    except:
        response = {
            "goodList": [],
            "progressGoodList": {},
            "newFlag": [],
        }
    return response


@router.post("/shop/getExtraGoodList")
@player_data_decorator
async def shop_getExtraGoodList(player_data, request: Request):
    request_json = await request.json()
    # 加载额外商品列表数据
    try:
        extra_goods_data = const_json_loader["res/shop/ExtraGoodList.json"].copy()
        response = extra_goods_data
    except:
        response = {
            "goodList": [],
            "newFlag": [],
            "lastClick": 1700000000,
        }
    return response


@router.post("/shop/getEPGSGoodList")
@player_data_decorator
async def shop_getEPGSGoodList(player_data, request: Request):
    request_json = await request.json()
    # 加载EPGS商品列表数据
    try:
        epgs_goods_data = const_json_loader["res/shop/EPGSGoodList.json"].copy()
        response = epgs_goods_data
    except:
        response = {
            "goodList": [],
        }
    return response


@router.post("/shop/getRepGoodList")
@player_data_decorator
async def shop_getRepGoodList(player_data, request: Request):
    request_json = await request.json()
    # 加载REP商品列表数据
    try:
        rep_goods_data = const_json_loader["res/shop/RepGoodList.json"].copy()
        response = rep_goods_data
    except:
        response = {
            "goodList": [],
            "newFlag": [],
        }
    return response


@router.post("/shop/getCashGoodList")
@player_data_decorator
async def shop_getCashGoodList(player_data, request: Request):
    request_json = await request.json()
    # 加载现金商品列表数据
    try:
        cash_goods_data = const_json_loader["res/shop/CashGoodList.json"].copy()
        response = cash_goods_data
    except:
        response = {
            "goodList": [],
        }
    return response


@router.post("/shop/getGPGoodList")
@player_data_decorator
async def shop_getGPGoodList(player_data, request: Request):
    request_json = await request.json()
    # 加载GP商品列表数据
    try:
        gp_goods_data = const_json_loader["res/shop/GPGoodList.json"].copy()
        response = gp_goods_data
    except:
        response = {
            "weeklyGroup": {},
            "monthlyGroup": {},
            "monthlySub": [],
            "levelGP": [],
            "oneTimeGP": [],
            "chooseGroup": [],
            "condtionTriggerGroup": [],
        }
    return response


@router.post("/shop/getGoodPurchaseState")
@player_data_decorator
async def shop_getGoodPurchaseState(player_data, request: Request):
    request_json = await request.json()
    # 加载商品购买状态数据
    try:
        purchase_state_data = const_json_loader["res/shop/GoodPurchaseState.json"].copy()
        response = purchase_state_data
    except:
        response = {
            "result": {},
        }
    return response


@router.post("/shop/getLMTGSGoodList")
@player_data_decorator
async def shop_getLMTGSGoodList(player_data, request: Request):
    request_json = await request.json()
    # 加载LMTGS商品列表数据
    try:
        lmtgs_goods_data = const_json_loader["res/shop/LMTGSGoodList.json"].copy()
        response = lmtgs_goods_data
    except:
        response = {
            "goodList": [],
        }
    return response



@router.post("/shop/buySkinGood")
@player_data_decorator
async def shop_buySkinGood(player_data, request: Request):
    request_json = await request.json()
    good_id = request_json.get('goodId')

    # 从JSON加载器获取皮肤商品列表
    try:
        skin_good_list = const_json_loader["res/shop/SkinGoodList.json"].copy()
    except:
        skin_good_list = {"goodList": []}

    # 查找商品并获取价格
    origin_price = 0
    for good in skin_good_list.get('goodList', []):
        if good.get('goodId') == good_id:
            origin_price = good.get('originPrice', 0)
            break

    # 扣除钻石并添加皮肤
    if good_id and len(good_id) > 3:
        skin_id = good_id[3:]  # 移除前缀如 "skin_"
        player_data["skin"]["characterSkins"][skin_id] = 1
        player_data["skin"]["skinTs"][skin_id] = int(time.time())

    player_data["status"]["androidDiamond"] -= origin_price
    player_data["status"]["iosDiamond"] -= origin_price

    response = {
        "playerDataDelta": {
            "deleted": {},
            "modified": {
                "skin": dict(player_data["skin"]),
                "status": {
                    "androidDiamond": player_data["status"]["androidDiamond"],
                    "iosDiamond": player_data["status"]["iosDiamond"]
                }
            }
        },
        "result": 0
    }

    return response


@router.post("/shop/buyLowGood")
@player_data_decorator
async def shop_buyLowGood(player_data, request: Request):
    request_json = await request.json()
    good_id = request_json.get('goodId')
    count = request_json.get('count', 1)

    # 从JSON加载器获取低价商品列表
    try:
        low_good_list = const_json_loader["res/shop/LowGoodList.json"].copy()
    except:
        low_good_list = {"goodList": []}

    # 处理购买逻辑
    for low_good in low_good_list.get('goodList', []):
        if low_good.get('goodId') == good_id:
            price = low_good.get('price', 0)
            player_data["status"]["lggShard"] -= price * count

            reward_id = low_good["item"]["id"]
            reward_count = low_good["item"]["count"] * count

            if reward_id in player_data["inventory"]:
                player_data["inventory"][reward_id] += reward_count
            else:
                player_data["inventory"][reward_id] = reward_count
            break

    response = {
        "playerDataDelta": {
            "deleted": {},
            "modified": {
                "skin": dict(player_data["skin"]),
                "status": dict(player_data["status"]),
                "shop": dict(player_data["shop"]),
                "troop": dict(player_data["troop"]),
                "inventory": dict(player_data["inventory"])
            }
        },
        "items": [],
        "result": 0
    }

    return response


@router.post("/shop/buyHighGood")
@player_data_decorator
async def shop_buyHighGood(player_data, request: Request):
    request_json = await request.json()
    good_id = request_json.get('goodId')
    count = request_json.get('count', 1)

    # 从JSON加载器获取高价商品列表
    try:
        high_good_list = const_json_loader["res/shop/HighGoodList.json"].copy()
    except:
        high_good_list = {"goodList": []}

    # 处理购买逻辑
    for high_good in high_good_list.get('goodList', []):
        if high_good.get('goodId') == good_id:
            price = high_good.get('price', 0)
            player_data["status"]["hggShard"] -= price * count

            reward_id = high_good["item"]["id"]
            reward_count = high_good["item"]["count"] * count

            if reward_id in player_data["inventory"]:
                player_data["inventory"][reward_id] += reward_count
            else:
                player_data["inventory"][reward_id] = reward_count
            break

    response = {
        "playerDataDelta": {
            "deleted": {},
            "modified": {
                "skin": dict(player_data["skin"]),
                "status": dict(player_data["status"]),
                "shop": dict(player_data["shop"]),
                "troop": dict(player_data["troop"]),
                "inventory": dict(player_data["inventory"])
            }
        },
        "items": [],
        "result": 0
    }

    return response


@router.post("/shop/buyExtraGood")
@player_data_decorator
async def shop_buyExtraGood(player_data, request: Request):
    request_json = await request.json()
    good_id = request_json.get('goodId')
    count = request_json.get('count', 1)

    # 从JSON加载器获取额外商品列表
    try:
        extra_good_list = const_json_loader["res/shop/ExtraGoodList.json"].copy()
    except:
        extra_good_list = {"goodList": []}

    # 处理购买逻辑
    for extra_good in extra_good_list.get('goodList', []):
        if extra_good.get('goodId') == good_id:
            price = extra_good.get('price', 0)
            player_data["inventory"]["4006"] -= price * count

            reward_id = extra_good["item"]["id"]
            reward_count = extra_good["item"]["count"] * count

            if reward_id in player_data["inventory"]:
                player_data["inventory"][reward_id] += reward_count
            else:
                player_data["inventory"][reward_id] = reward_count
            break

    response = {
        "playerDataDelta": {
            "deleted": {},
            "modified": {
                "skin": dict(player_data["skin"]),
                "status": dict(player_data["status"]),
                "shop": dict(player_data["shop"]),
                "troop": dict(player_data["troop"]),
                "inventory": dict(player_data["inventory"])
            }
        },
        "items": [],
        "result": 0
    }

    return response


@router.post("/shop/buyClassicGood")
@player_data_decorator
async def shop_buyClassicGood(player_data, request: Request):
    request_json = await request.json()
    good_id = request_json.get('goodId')
    count = request_json.get('count', 1)

    # 从JSON加载器获取经典商品列表
    try:
        classic_good_list = const_json_loader["res/shop/ClassicGoodList.json"].copy()
    except:
        classic_good_list = {"goodList": []}

    # 处理购买逻辑
    for classic_good in classic_good_list.get('goodList', []):
        if classic_good.get('goodId') == good_id:
            price = classic_good.get('price', 0)
            player_data["status"]["REP_COIN"] -= price * count

            reward_id = classic_good["item"]["id"]
            reward_count = classic_good["item"]["count"] * count

            if reward_id in player_data["inventory"]:
                player_data["inventory"][reward_id] += reward_count
            else:
                player_data["inventory"][reward_id] = reward_count
            break

    response = {
        "playerDataDelta": {
            "deleted": {},
            "modified": {
                "skin": dict(player_data["skin"]),
                "status": dict(player_data["status"]),
                "shop": dict(player_data["shop"]),
                "troop": dict(player_data["troop"]),
                "inventory": dict(player_data["inventory"])
            }
        },
        "items": [],
        "result": 0
    }

    return response


@router.post("/shop/buyFurniGroup")
@player_data_decorator
async def shop_buyFurniGroup(player_data, request: Request):
    request_json = await request.json()
    goods = request_json.get("goods", [])
    cost_type = request_json.get("costType")

    # 从JSON加载器获取家具商品列表
    try:
        furni_good_list = const_json_loader["res/shop/FurniGoodList.json"].copy()
    except:
        furni_good_list = {"goods": []}

    total_cost = 0

    # 计算总购买花费
    for good in goods:
        good_id = good.get("id")
        count = good.get("count", 0)
        for furni in furni_good_list.get("goods", []):
            if furni.get("goodid") == good_id:
                if cost_type == "DIAMOND":
                    total_cost += count * furni.get("priceDia", 0)
                elif cost_type == "COIN_FURN":
                    total_cost += count * furni.get("priceCoin", 0)

    # 扣除货币
    if cost_type == "DIAMOND":
        player_data["status"]["androidDiamond"] -= total_cost
    elif cost_type == "COIN_FURN":
        player_data["inventory"]["3401"] -= total_cost

    # 添加物品
    for good in goods:
        good_id = good.get("id")
        count = good.get("count", 0)
        # 确保FURNI结构存在
        if "FURNI" not in player_data:
            player_data["FURNI"] = {"info": []}
        if "info" not in player_data["FURNI"]:
            player_data["FURNI"]["info"] = []

        found = False
        for furni_info in player_data["FURNI"]["info"]:
            if furni_info.get("id") == good_id:
                furni_info["count"] += count
                found = True
                break
        if not found:
            player_data["FURNI"]["info"].append({
                "id": good_id,
                "count": count
            })

    response = {
        "playerDataDelta": {
            "deleted": {},
            "modified": {
                "skin": dict(player_data["skin"]),
                "status": dict(player_data["status"]),
                "shop": dict(player_data["shop"]),
                "troop": dict(player_data["troop"]),
                "inventory": dict(player_data["inventory"]),
                "FURNI": dict(player_data["FURNI"])
            }
        },
        "items": [],
        "result": 0
    }

    return response


@router.post("/shop/buyFurniGood")
@player_data_decorator
async def shop_buyFurniGood(player_data, request: Request):
    request_json = await request.json()
    good_id = request_json.get("goodId")
    buy_count = request_json.get("buyCount", 1)
    cost_type = request_json.get("costType")

    # 从JSON加载器获取家具商品列表
    try:
        furni_good_list = const_json_loader["res/shop/FurniGoodList.json"].copy()
    except:
        furni_good_list = {"goods": []}

    # 处理购买逻辑
    for good in furni_good_list.get("goods", []):
        if good.get("goodid") == good_id:
            price_dia = good.get("priceDia", 0)
            price_coin = good.get("priceCoin", 0)

            # 扣除货币
            if cost_type == "DIAMOND":
                player_data["status"]["androidDiamond"] -= buy_count * price_dia
            elif cost_type == "COIN_FURN":
                player_data["inventory"]["3401"] -= buy_count * price_coin

            # 确保FURNI结构存在
            if "FURNI" not in player_data:
                player_data["FURNI"] = {"info": []}
            if "info" not in player_data["FURNI"]:
                player_data["FURNI"]["info"] = []

            # 添加物品
            found = False
            for furni_info in player_data["FURNI"]["info"]:
                if furni_info.get("id") == good_id:
                    furni_info["count"] += buy_count
                    found = True
                    break
            if not found:
                player_data["FURNI"]["info"].append({
                    "id": good_id,
                    "count": buy_count
                })
            break

    response = {
        "playerDataDelta": {
            "deleted": {},
            "modified": {
                "skin": dict(player_data["skin"]),
                "status": dict(player_data["status"]),
                "shop": dict(player_data["shop"]),
                "troop": dict(player_data["troop"]),
                "inventory": dict(player_data["inventory"]),
                "FURNI": dict(player_data["FURNI"])
            }
        },
        "items": [],
        "result": 0
    }

    return response
