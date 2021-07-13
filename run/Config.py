boring = []


def isStaff(id):
    engineer = {
        "1688852895879505": "孙张鑫"
    }
    return (True, engineer[id]) if (id in engineer.keys()) else (False, None)


def getCpname(id):
    CP = {
        "R:10696051419036328": "测试一",
        "R:10696050954024943": "测试二",
        "R:1970325093109066": "通知模拟",
        "R:191062836": "群机器人测试",
        "R:10696050773030645": "企业微信聊天记录内测群",
        "R:10696049918015539": "宁波源理&合宙Air820UG",
        "R:10696049918015746": "彬其对讲机&合宙",
        "R:10696049918018623": "合宙Luat线上支持群-3",
        "R:10696049918016954": "合宙Luat线上支持群-2",
        "R:10696049918015782": "合宙Luat线上支持群-1",
        "R:10696049918015950": "杭州塔石&合宙Air720UH（Air302）",
        "R:10696049918015589": "杭州超翔&合宙Air720UG",
        "R:10696049918017177": "速锐得&合宙：Air724UG ",
        "R:10696050214025072": "重庆谦雅科技&合宙AIR722UG",
        "R:10696049918015545": "乐今&合宙724学生卡",
        "R:10696049918018913": "合宙-聚亚科技技术交流群",
        "R:10696049918015553": "国恒&合宙:Air720UH（充电桩）",
        "R:10696050359023403": "苏州奥丁电力&合宙Air724UG",
        "R:10696049918015952": "南潮&合宙:Cat.1",
        "R:10696051361023640": "亮钻&合宙：Air724UGI",
        "R:10696051423020995": "长本&合宙724售货机",
        "R:10696049824032389": "泰山科技&合宙Air724UG 电源控制器",
        "R:10696049918016366": "飞蜂智能&合宙Air720UH垃圾箱监控",
        "R:10696049918016708": "泰为&合宙Tracker724UG&530",
        "R:10696049918015991": "柜电&合宙 AIR724 电池定位器",
        "R:10696051760512397": "易联星拓@合宙Cat.1支持群",
        "R:10696049918015591": "无锡必创&合宙:Air724UG",
        "R:10696049918015551": "杭州鲁尔&合宙Air724UG",
        "R:10696049918018555": "乐摇摇（杭州）&合宙Air724UG（Lua）",
        "R:10696049918016004": "千鸣&合宙724快递柜",
        "R:10696050205038196": "能加&合宙：Air724UG",
        "R:10696049918016650": "汇智伟业&合宙：724UG（定位器）",
        "R:10696049918018548": "力通达&合宙724/202",
        "R:10696049715032581": "翎盟 724UG 技术对接群",
        "R:10696049918017387": "大连楼兰&合宙",
        "R:10696049918015743": "九州&合宙:技术支持",
        "R:10696052365031174": "顺舟&合宙:智慧路灯Cat.1",
        "R:10696049918019277": "普乐特&合宙：724UG（工控机）",
        "R:10696049918016950": "杭州智诺&合宙Air720SG（724UG）",
        "R:10696049918017339": "阿尔丰&合宙：Cat.1(云喇叭)",
        "R:10696051729036196": "乔安&合宙 Air724UG 4G IPC",
        "R:10696049918018596": "华鹏&联通&合宙724充电桩",
        "R:10696049918017896": "安凌讯&合宙 Air724UG",
        "R:10696049918015773": "广州云山&合宙～Air720SL",
        "R:10696052422259943": "杭州聚通恒科技&合宙Air724UG(Lua）",
        "R:10696049918015574": "掇月&合宙：Air720UH-廖瑞",
        "R:10696049918016016": "金卡&合宙280S智能表",
        "R:10696049615020111": "赫曦&合宙720UG",
        "R:10696050507033657": "金丰机电&合宙AIR820UG",
        "R:10696049244021170": "联百&合宙Air724UG 防盗器",
        "R:10696049918016421": "浙江智电生态&合宙 CAT1模块",
        "R:10696052020025343": "芯航达&合宙:Cat.1技术支持",
        "R:10696052020024411": "振申科技&合宙Air724UG 智慧医疗 ",
        "R:10696049918015776": "万物互联&合宙:Air724UG",
        "R:10696049244022452": "长源&合宙：Air724UG",
        "R:10696049918018546": "无锡联好&合宙Air720UG",
        "R:10696050839020222": "云智易联&合宙：Air724UG",
        "R:10696049918015932": "自连&合宙:Cat.1",
        "R:10696049918015738": "合宙企业群-月河电器",
        "R:10696049918019051": "普信智能&合宙Air722UG",
        "R:10696053073021048": "徐州鼎源云桥&合宙Air724UG扫码支付",
        "R:10696049918016383": "河北纳源&合宙Air724UG",
        "R:10696049918016692": "嘉则&合宙724",
        "R:10696049918016007": "沃瑞特&合宙:Air722UG(定位器)",
        "R:10696049918017391": "杭州天马&合宙Air724UG",
        "R:10696049918016400": "广州赛通&合宙：Air720H(DTU)",
        "R:10696049918016971": "微弗&合宙:技术支持",
        "R:10696049918016013": "临沂跃水&合宙Air724UG",
        "R:10696049918015542": "浙江利尔达&合宙Air820UGLua（BMS）",
        "R:10696049918017920": "鱼跃&合宙208S血压计血糖仪",
        "R:10696049918016550": "成都西米&合宙:艾灸仪Air720UH",
        "R:10696053321021651": "青岛谷发&合宙Air720UH",
        "R:10696053148020663": "合肥中午&合宙:Cat.1支持",
        "R:10696049481015478": "迈向新科技&合宙724UG",
        "R:10696049918015760": "喜视科技&合宙  724UG",
        "R:10696049918017881": "上海拜米&合宙 Air724UG",
        "R:10696049918015995": "上海智引&合宙 Air724UG",
        "R:10696049739025185": "思启威&扫码支付Air720SG",
        "R:10696049918018345": "优和创&合宙Cat1",
        "R:10696049918016347": "途泰&合宙：Air720UH(定位器)",
        "R:10696049269022814": "泉州安达&合宙:Cat.1 DTMF",
        "R:10696049918016338": "上海点都&合宙：Air724UGI",
        "R:10696049370024022": "卓雷电子&合宙Air724UG",
        "R:10696049370025918": "动力智能@合宙Air724支持群",
        "R:10696050350021603": "广州晓网&合宙：Air724UG-NFM",
        "R:10696049918015619": "智网&合宙724云喇叭",
        "R:10696049785024153": "天津欧宜&合宙：Air722UG",
        "R:10696049918015847": "佛山玉玄宫@合宙-720Sh",
        "R:10696050893028685": "维特智能&合宙Air724UG",
        "R:10696049918016394": "广州宇昊&合宙:724UG(充电桩）",
        "R:10696049918016639": "天星北斗&合宙:Air724UG sdk",
        "R:10696049918015657": "南京纳龙&合宙:cat1",
        "R:10696049918015556": "杭州齐腾&合宙Air724UG",
        "R:10696052424030916": "欧恩&合宙：Air724UG",
        "R:10696050080020188": "氢芯&合宙724",
        "R:10696049918017170": "微信通&合宙内部群",
        "R:10696049918015735": "新案&合宙:70迈Air722UG",
        "R:10696049918017734": "凯利客户内部沟通群",
        "R:10696049918016694": "深圳比巴&合宙:Cat.1智能广播",
        "R:10696049918016533": "山东宏卡&合宙：Air720UH/724UG",
        "R:10696049918018532": "西阔&合宙724充电桩",
        "R:10696049854020368": "格美通&合宙Air724UG 售货机",
        "R:10696049918017223": "成都任意多彩门&合宙：Air724UG",
        "R:10696049918015572": "海控&合宙 Air724UG",
        "R:10696049918017845": "凯歌&合宙：控制器技术支持",
        "R:10696050077018171": "淮通&合宙Air724UG/Air202S",
        "R:10696051975032432": "浩讯通讯&Air724",
        "R:10696049918017730": "杭州华牧养殖&合宙:Cat.1",
        "R:10696049918017423": "智谷联&合宙：Air724UG(云喇叭)",
        "R:10696049918015559": "九安&合宙:IPC Cat.1",
        "R:10696049918015586": "如金&合宙：Air724UG",
        "R:10696049918018599": "红誉科技&合宙724共享充电宝",
        "R:10696049918016542": "轨物&合宙724",
        "R:10696052269020407": "科莱德&合宙：Air720SG(DTU)",
        "R:10696049231021276": "百思桥&合宙：Air724UG",
        "R:10696052365033127": "飞优雀&合宙技术对接群",
        "R:10696052097030038": "魔蛋&合宙724",
        "R:10696051764480203": "泉州时刻@合宙Cat1新群",
        "R:10696052757028763": "隆盛&合宙：Air724UG",
        "R:10696049918016962": "南京软方&合宙：Air720SH Android",
        "R:10696049918015610": "乐普&合宙：Air724UG",
        "R:10696049918016695": "安徽蓝盾&合宙Air720SL",
        "R:10696049918016538": "南京驰特&合宙724",
        "R:10696049918018540": "永安行－联通－合宙 724UG",
        "R:10696049918016002": "名能节能&合宙  720UH  DTU",
        "R:10696049918015547": "斯普锐&合宙724云喇叭",
        "R:10696050573022689": "珠海京澳&Air724UG 远程控制网关 ",
        "R:10696049918016702": "逸卡&合宙724UGI",
        "R:10696051755582249": "超影科技&合宙Air724UG-安全帽智能穿",
        "R:10696049918016343": "常州数点测控&合宙：Air724UG",
        "R:10696050883022313": "途泰&星舆&合宙:Cat.1 CSDK 高精度定位",
        "R:10696049918016689": "蓝微&合宙：Air820UG",
        "R:10696049817019544": "山东瀚臻&合宙:Cat.1支持",
        "R:10696049435030045": "南京傲屹电子&合宙Air724UG",
        "R:10696049918015855": "友先达&合宙 724模块，电表，水表 LUAT",
        "R:10696049918015750": "快松果&九州:合宙Air720UH电单车",
        "R:10696049918015565": "维拍&合宙：Air720SL",
        "R:10696052236027176": "海银智慧&合宙：Air724UG",
        "R:10696050042024648": "微天地&合宙724",
        "R:10696049918017735": "上德智能&合宙：Air720UG",
        "R:10696050058019864": "雪暴&合宙:扫码支付Cat.1",
        "R:10696049918018600": "道中科技&合宙：Air720SH(售货机)",
        "R:10696049918015739": "易洁&合宙:Cat.1",
        "R:10696051749700032": "台蜂科技&九州:合宙Air722/820UG",
        "R:10696049918016019": "杭州行云电源&合宙Air724",
        "R:10696049918018594": "上海汉枫&合宙Air720UH",
        "R:10696049918015757": "四川辰鳗&合宙：Air724UG",
        "R:10696049918015775": "易码通支付&合宙:Air724UG",
        "R:10696049918017736": "中电利达&合宙Air724UG",
        "R:10696049918016701": "江苏比特达&合宙Air724ug+Air530Z",
        "R:10696049918018557": "神州安付&合宙:8910 C开发",
        "R:10696049918018619": "广东劲瘦&合宙Air724UG/720D 售货机",
        "R:10696049918018347": "凯龙高科&合宙Air722UG+Air530Z",
        "R:10696049918015540": "杭州超天&合宙Air724UG（Lua）",
        "R:10696049918016401": "杭州海康保泰&合宙Air724UG",
        "R:10696051303020802": "合肥君莫&合宙AIR722UG",
        "R:10696049918017889": "惠尔信&合宙：Air724UG",
        "R:10696052857030000": "中渠环保&合宙:Cat.1支持",
        "R:10696049918016698": "宁波爱购&合宙：Air724UG",
        "R:10696049918016369": "俊利锋&合宙:共享洗衣机724 Lua",
        "R:10696049918017183": "多度&合宙：Air720UG—CSDK",
        "R:10696049918016975": "飞沃&合宙 :724UG",
        "R:10696051729503043": "极翼机器人@合宙720SE技术支持群",
        "R:10696052127023020": "远方动力&九州&合宙CAT1",
        "R:10696052127022676": "麟凰&世智&合宙724",
        "R:10696049918015558": "万汇&合宙:720SL行车记录仪",
        "R:10696049918016687": "杭州柏来&合宙Air720UG（724UG）",
        "R:10696049918015605": "青岛量谷&合宙Air724UG",
        "R:10696049918015623": "金恒&合宙Air724UG/Air530 安全帽",
        "R:10696049918016333": "瑞德物联&合宙:Air724UG定位器",
        "R:10696050637019382": "深圳信科&合宙：Air724UG",
        "R:10696049918016360": "凯利&合宙:Cat.1 PoC",
        "R:10696049918015780": "易安充&合宙:Air724UG",
        "R:10696049918017390": "深圳有控&合宙Air724UG",
        "R:10696049351020406": "上海鲑鱼&合宙Air722UG",
        "R:10696049918016642": "郑州睿讯微&合宙 Air724",
        "R:10696049918015560": "位创&合宙:Air722UG(定位器)",
        "R:10696049918015532": "欧孚&合宙:定位工牌Air724UG",
        "R:10696049918016332": "杭州和展&合宙Air724UG",
        "R:10696049918015588": "南京爱普雷德&合宙:Cat.1 Lua录音",
        "R:10696051322042153": "野芯&合宙Air720SG 路由器 ",
        "R:10696050732027862": "创美佳&合宙：Air724UG",
        "R:10696049918019050": "思特&合宙724学生卡（csdk）",
        "R:10696049918015550": "安心智能&合宙Air724UG",
        "R:10696049918017185": "青岛意想意创&合宙CAT1",
        "R:10696049918016636": "杭州若格&合宙Air720SG",
        "R:10696051089026411": "菏泽峥艳电力&合宙：Air724UG",
        "R:10696050379036584": "乐辉智能@合宙Cat1支持群",
        "R:10696049850059408": "上海移宇&合宙Air724UG",
        "R:10696049918016637": "阳西逢源&合宙：Air724",
        "R:10696049918015964": "杭州三众&合宙Air724UG",
        "R:10696049918013592": "泉州奔腾&合宙:Air724UG(安防门禁对讲机)",
        "R:10696049918016003": "易木&合宙720ug售货机",
        "R:10696053167018848": "派诺&合宙：Air724UG",
        "R:10696051734581320": "上海正泰@合宙技术支持群",
        "R:10696050452024808": "玉环与礼&合宙Air202S",
        "R:10696049918018590": "四川四美&合宙Air724UG",
        "R:10696051726699919": "优必胜&合宙：Air724UG(气体监测)",
        "R:10696051727517717": "成诺智家&九州:合宙Air724UG",
        "R:10696051524030142": "赣商&合宙724充电桩",
        "R:10696049918017900": "徐州安高&合宙:Cat.1支持",
        "R:10696052379028474": "安控电子&合宙Air724UG DTU",
        "R:10696052379027066": "易清洁&合宙：Air724UG",
        "R:10696049918017846": "优路加&合宙Air724ug 车载预警器",
        "R:10696049918015751": "北京群辉科技&九州：合宙Air724UG",
        "R:10696049918015965": "上海亨果&合宙：Air724UG",
        "R:10696052672024125": "思鸿辉&合宙:Cat.1支持",
        "R:10696052246024671": "中山启维&合宙:Air724UG",
        "R:10696049918013614": "山树生态&合宙:Cat.1支持",
        "R:10696049918016705": "济南钧然&合宙720UH",
        "R:10696049918015779": "山东潍微&合宙：Air720H",
        "R:10696049918018547": "深智联&合宙:Cat.1",
        "R:10696049918016725": "科大讯飞&合宙:Air724UG",
        "R:10696049918015781": "成都谱讯&合宙：Air724UG",
        "R:10696049918016365": "智云&合宙Air724UG",
        "R:10696049918015772": "屹菲&合宙:Cat.1药盒",
        "R:10696051743677958": "交通通信&九州:合宙Air720UH",
        "R:10696049918015936": "嘉兴智行&合宙724充电桩",
        "R:10696050136021611": "酷鱼互动&合宙722UG",
        "R:10696050793018808": "亿家网络&合宙:Air724UG",
        "R:10696049918016344": "西安扬德&合宙:Cat.1支持",
        "R:10696049918016651": "杭州辰远&合宙Air724UG",
        "R:10696052347020542": "兴宇腾&合宙：Air720SL",
        "R:10696052609033126": "艾牧(艾格多)&合宙:Air724UG AT",
        "R:10696049918015938": "重庆矗博&合宙:Air724",
        "R:10696049918018918": "步科&达勤:合宙Cat.1",
        "R:10696051655023551": "泛恩&合宙724",
        "R:10696050073025921": "微信通&合宙：码夫系统对接",
        "R:10696049918016377": "山东昊润&合宙:Air720UH",
        "R:10696049918018605": "任联&合宙724/302",
        "R:10696049918015835": "飞鱼&合宙，云喇叭 724",
        "R:10696050345030039": "上海晨裹&合宙724充电桩",
        "R:10696049918015554": "浙江臻万&合宙Air720UG",
        "R:10696049918015555": "中科信通&合宙：Air724UG",
        "R:10696049918017166": "威派格&合宙智能表",
        "R:10696049918015747": "天下父母&九州：合宙AIR724UG技术交流",
        "R:10696049918017168": "四川科道&合宙Air820UG-NFM",
        "R:10696049918015966": "源谷&合宙：Air722UG",
        "R:10696049745024816": "北京首贝&合宙:Air724UG AT",
        "R:10696052724023369": "江苏源坤&合宙CAT1",
        "R:10696049918015581": "真灼&合宙724学生卡",
        "R:10696051734534136": "厦门利成智能@合宙724UG支持群",
        "R:10696049918016696": "常州天正&合宙Air720G（724UG）",
        "R:10696049918017890": "青岛晨诺&合宙:Cat.1",
        "R:10696049918018902": "东视&合宙Air724",
        "R:10696050722025000": "易享物联&合宙：Air720SG",
        "R:10696049918015836": "鑫兴&合宙：智能开关【刘晨旭",
        "R:10696053312024876": "山东兰动&合宙Air720SL DTU",
        "R:10696049918015978": "杭州小竹&合宙Air724UG",
        "R:10696049918015606": "杭州海鸟&合宙Air724UG",
        "R:10696049918015783": "黑皮钛&合宙：Air724UG+720UG",
        "R:10696052431025829": "凯利&合宙Air724UG",
        "R:10696049918015954": "云帆合力&合宙Air202S",
        "R:10696052865030525": "科恒&合宙724",
        "R:10696049918016726": "天津汇诚&合宙:Air202F",
        "R:10696049918016406": "德百祺&合宙：Air722UG(定位器)",
        "R:10696051916024997": "蓬力农业&合宙：Air724UG",
        "R:10696049239034801": "浙江巨感&合宙Air724UG",
        "R:10696049918014577": "银尔达&合宙:Cat.1 DTU",
        "R:10696049716022561": "浙江恒达&合宙Air724UG",
        "R:10696052246031957": "山东赛为&合宙Air724UG（AT）",
        "R:10696049918015614": "金坤科创&合宙：Air724UG",
        "R:10696049918015602": "浙江简简捷&合宙",
        "R:10696050041066411": "LuatIDE体验群",
        "R:10696049918015568": "中科智城&合宙Air724UG",
        "R:10696050041067483": "德高&合宙：Air720H",
        "R:10696052616024479": "河南禾识&合宙：Air724UG",
        "R:10696049918016546": "合宙&西博:Air722UG(定位器)",
        "R:10696049918017383": "武汉朗宇&合宙:Cat.1 DTU(含GPS)",
        "R:10696049918015744": "艾思科米&九州:合宙Air720UH",
        "R:10696052564025942": "依爱消防电子&合宙AIR724UG-NFM",
        "R:10696052699026927": "国正&合宙724智慧用电",
        "R:10696049918015740": "苏州国网&合宙：Air724UG",
        "R:10696049918016653": "天空社&合宙：Air722UG",
        "R:10696052893018284": "格瑞浦创&合宙724环境监测",
        "R:10696051781046224": "仰邦&合宙Air724UG",
        "R:10696052197021268": "神博&合宙：Air724UG",
        "R:10696053130023299": "微尘物联&合宙Air724UG 定位手环",
        "R:10696052699026717": "弈力&合宙724BMS",
        "R:10696049918015745": "天华世纪&合宙:Air724UG",
        "R:10696053266023636": "纽曼&合宙4G模组724",
        "R:10696049918017731": "上海垄欣&合宙Air722UG-NFC",
        "R:10696050677025564": "遨科&合宙Air722UG",
        "R:10696051747499582": "行臻科技&九州:合宙Air720UG",
        "R:10696052458025464": "重庆研巴&合宙Air724UG",
        "R:10696049918015577": "秦皇岛小马物联&合宙Air724UG",
        "R:10696051723702728": "富联&合宙724",
        "R:10696051725711777": "合宙Luat直播互动群",
        "R:10696049918015590": "满泰&合宙：Air724UG",
        "R:10696051750698463": "西妍@合宙技术720UH支持群",
        "R:10696049690032686": "安徽金屹通信&合宙AIR724UG-NFM",
        "R:10696049918015981": "百励华&合宙：Air724UG LUA开发",
        "R:10696049918015569": "北京友联青岛友勤&合宙Air724UG",
        "R:10696052405036836": "百灵佳&合宙：Air720UH",
        "R:10696053148023180": "警安&合宙：Air724UG",
        "R:10696049918018565": "天能电池&合宙Air724UG（DTU）",
        "R:10696049918016656": "红黄蓝电子&Air724UG",
        "R:10696050338026174": "浙江微松&合宙Air720UG",
        "R:10696049918016543": "天津电气科学研究院技术支持群",
        "R:10696050730020687": "北京美刻&九州:合宙Air800HS",
        "R:10696051628050248": "无锡龙华&合宙Air720UH",
        "R:10696049918015988": "未来物联&合宙:Cat.1",
        "R:10696049918015996": "鼎尚&合宙Air724xx",
        "R:10696049348018311": "壹芯电子&合宙技术支持群",
        "R:10696049918016017": "杭州欧格迈&合宙Air724（DTU）",
        "R:10696049630023699": "一度自动化&合宙Air724UG垃圾箱监控 ",
        "R:10696049918018556": "苏州芸华&合宙：Air724UG",
        "R:10696051765686592": "上海为道代理商技术支持群",
        "R:10696050381020832": "顶点微光&合宙:Cat.1",
        "R:10696049658020325": "江苏远大&合宙",
        "R:10696049918015939": "东莞佳芯&合宙：Air724UG",
        "R:10696053377023394": "金证智付&壹芯&合宙CAT1",
        "R:10696051107020731": "熊猫通信&合宙724网关",
        "R:10696052893017626": "合宙Luat线上支持群-4",
        "R:10696050921022980": "追踪者&合宙：Air724UG",
        "R:10696049918017379": "浙江兰科&合宙Air724UG",
        "R:10696049918018559": "艺镜&合宙:724UG(报警器)",
        "R:10696049918018597": "杭州柯林&合宙Air724UG",
        "R:10696049423033339": "渔易&合宙：Air724UG",
        "R:10696050603022435": "灵动高科&合宙Air724UG 共享电子称",
        "R:10696050603023151": "依沃科技&合宙724UG",
        "R:10696049918016686": "桂林啄木鸟&合宙：Air722UG",
        "R:10696049918015535": "安马达&合宙:Air724电动车",
        "R:10696050898043138": "北京达有力 &壹芯&合宙Air720UH",
        "R:10696052450031344": "广州锋雷&合宙:Air720UH",
        "R:10696049265020608": "明信科技&合宙：Air724UG",
        "R:10696052450033751": "智连安全&合宙：Air724UG",
        "R:10696049679018322": "旭鑫微&合宙：Air724UG",
        "R:10696049679020925": "瑞杰凯&合宙Air720UG",
        "R:10696049583035675": "合宙Luat技术交流微信群",
        "R:10696051571021748": "速华威&合宙：Air724UG（定位电话）",
        "R:10696049918017855": "郑州兴邦&合宙:Air724UG",
        "R:10696051663031123": "四维智联&合宙:Cat.1",
        "R:10696049918019055": "杭州安之博&合宙Air722UG",
        "R:10696049918017842": "安徽国德净水&合宙Air724UG",
        "R:10696049507023467": "晟益通&合宙724UG",
        "R:10696049379021644": "赋思科技&合宙Air724UG DTU",
        "R:10696049918015538": "杭州富连&合宙Air724UG",
        "R:10696052396021291": "昆山微电子&合宙:Air720SG AT",
        "R:10696051877023852": "苏州小工匠&合宙:共享车位锁Cat.1",
        "R:10696053351028560": "合肥卅河机电&合宙:Cat.1",
        "R:10696049918016709": "上海翌朵&合宙Air724UGI",
        "R:10696051877025548": "嘉阳电子&合宙",
        "R:10696053300027435": "上海沙蝶&合宙:净水板Cat.1",
        "R:10696049918016535": "巨思睿&合宙 724 夹子报警器",
        "R:10696050294040132": "广州锋雷&合宙：Air720UH",
        "R:10696051883018547": "云飞科技&合宙Air530 智慧农业",
        "R:10696053316020577": "无锡泰普&九州恒信：AIR724技术交流",
        "R:10696051509025882": "锐盟医疗&合宙Air724UG 智慧医疗",
        "R:10696049918016951": "仰歌&合宙:Cat.1 IPC",
        "R:10696049569019792": "桂林电子&合宙724",
        "R:10696053392022143": "上海迦立&合宙Air724UG-NFM",
        "R:10696049475023548": "郑州霍普&合宙Air724UG（Luat）",
        "R:10696049918016666": "江西雷米&合宙cat1模块",
        "R:10696051578023258": "西安万硕&合宙：Air720UG",
        "R:10696049830017411": "合宙与驴充充技术沟通群",
        "R:10696049515023087": "广州嘉阳&合宙:Cat.1云广播",
        "R:10696049918018536": "联众智能&合宙：Air720H(广告机)",
        "R:10696053328018642": "杭州贝特&合宙Air724UG",
        "R:10696049275031205": "深圳惠昌&合宙：Air724UG",
        "R:10696053176019197": "杭州聚声&合宙Air724UG",
        "R:10696049918017901": "浙江金开&合宙Air724UG（820UG）",
        "R:10696049918017406": "杭州研江&合宙Air724UG（720D）",
        "R:10696051150203958": "万龙电气&合宙724",
        "R:10696049918015761": "苏打生活&合宙:Cat.1",
        "R:10696052754032533": "河南四三零机器人&合宙：Air724UG",
        "R:10696049918015960": "湖州佳格&合宙Air202S",
        "R:10696049918015985": "温州物华&合宙Air724UG",
        "R:10696049918018351": "华尔博思&合宙:Cat.1学生卡",
        "R:10696049918019060": "路帆电子&合宙：724UG",
        "R:10696050047026968": "中原动力&合宙Air724UG",
        "R:10696049424031703": "泉州佳乐@合宙Cat1模块支持群",
        "R:10696049424031894": "原玄智能&合宙724UG",
        "R:10696051741704798": "巩诚&合宙定位器",
        "R:10696050701029705": "赛贝&合宙724智慧用电",
        "R:10696049918019063": "安徽行一能源&合宙Air724UG",
        "R:10696051719488600": "福州和达@合宙Cat1技术支持群",
        "R:10696050701031306": "浙江笛虎&合宙Air724UG",
        "R:10696051191025396": "容知日新-合宙cat1交流群",
        "R:10696049918016536": "成都烈火&合宙：Air724UG",
        "R:10696049424031746": "芯联讯&合宙：Air202S+Air724UG",
        "R:10696052731026735": "正通智能&合宙：Air724UG",
        "R:10696049515022924": "深圳国芯通达&合宙Air724UG LED控制卡",
        "R:10696049918016376": "广州盛路&合宙：Air724UG（数据采集）",
        "R:10696049918015552": "羲皇&合宙724售货机",
        "R:10696052851023843": "科湃腾&合宙Air724UG",
        "R:10696051978023219": "杭州施湾&合宙Air724UG",
        "R:10696049346020548": "常安集团&合宙Air724UG",
        "R:10696049918015622": "成都畅行&合宙724UG",
        "R:10696052429026208": "天津时空经纬&合宙:Cat.4",
        "R:10696051421017817": "吉大赛恩&合宙:Cat.1",
        "R:10696049918015546": "蜜连&合宙720UG",
        "R:10696050866021926": "中里&合宙724智能头盔",
        "R:10696049918019273": "杭州中芯微&合宙Air720UH AT",
        "R:10696050177020540": "军创自动化@合宙Air724UG",
        "R:10696049918016640": "咻电&合宙：Air720UG",
        "R:10696050205038260": "虹桥导航技术&合宙Air724UG",
        "R:10696050231052497": "水韵科技&合宙:NB Air302",
        "R:10696049370026923": "莱斯&合宙:Air720SD技术支持",
        "R:10696051362023129": "芝柯智能&合宙：Air724UG(数据采集)",
        "R:10696050136020474": "工之友&合宙：Air720UH",
        "R:10696049918015983": "数之路&合宙：Air724UG",
        "R:10696049918015734": "微开&合宙:Air724UG",
        "R:10696050695025710": "翎盟&合宙:Cat.1支持",
        "R:10696049918015768": "远洋&合宙:Cat.1",
        "R:10696050695025654": "亚通科技&合宙：Air720SD",
        "R:10696053232020803": "西安汉柏&合宙：Air720SL",
        "R:10696053232020638": "湖南易控&合宙Air724UG",
        "R:10696049700052261": "本松机电&合宙:Cat.1充电桩",
        "R:10696049918015769": "动联&合宙:Cat.1 POS",
        "R:10696051741495630": "永联@合宙720SHI支持群",
        "R:10696050116022657": "异通&合宙724路灯监控",
        "R:10696053283036660": "北京环创飞扬&合宙AIR820UG",
        "R:10696049918015832": "麦穗&合宙:Cat.1云喇叭",
        "R:10696051942022499": "科威尼迪&合宙：Air724UG",
        "R:10696052787023525": "恒创&合宙：Air202Se",
        "R:10696049679021532": "金华新创力&合宙：Air820UG",
        "R:10696050000020156": "新北方&九州:合宙Air720UH",
        "R:10696052818024899": "首科仪表@合宙724UG支持群",
        "R:10696053211031742": "陕西晨选&合宙：Air724UGI（重力柜售卖机）",
        "R:10696051720482083": "锑锑智能&合宙Air724UG-远程控制",
        "R:10696049918015986": "新日&合宙820UG",
        "R:10696052250023912": "健思研&合宙Air724UG 充电桩",
        "R:10696049918015566": "卓一&合宙Air724UG",
        "R:10696049697028202": "天津鲲鹏&合宙:Cat.1技术支持",
        "R:10696050763044980": "苏州比爱玛&合宙：Air724UG",
        "R:10696050005018575": "广州辰汇&合宙Air724UG",
        "R:10696052168018112": "硕物天成&合宙724",
        "R:10696049235028636": "华意视讯&合宙",
        "R:10696049235028374": "太原烁威&合宙:Cat.1 DTU",
        "R:10696052503021954": "深圳在那科技&合宙AIR720UH",
        "R:10696052503023935": "富运&合宙724",
        "R:10696051394028943": "瀚海&合宙724充电桩",
        "R:10696049597017029": "新起点电子&合宙Air202S 智慧电表",
        "R:10696049918015592": "宏威创&合宙：Air720UH",
        "R:10696053078034108": "安保达&合宙Air720UG 呼叫报警器",
        "R:10696053234018989": "长铄科技&九州:合宙Air724UG",
        "R:10696050804025948": "杭州智合优联&合宙Air724UG AT",
        "R:10696050379039532": "野芯&合宙Air820UG",
        "R:10696049918017205": "武汉北斗&合宙724风电监控",
        "R:10696052034040701": "极限口腔医疗&合宙CAT1模块",
        "R:10696052034042268": "君岳物联&合宙：Air724UG(售货机)",
        "R:10696052034041752": "湖南拓疆&合宙：Air724UG",
        "R:10696050419025696": "泰锦优&合宙724UG",
        "R:10696050570020944": "湖南中谷&合宙：Air724UG",
        "R:10696049918017870": "中科慈航&合宙",
        "R:10696051879023120": "苏州安家物联&合宙：Air724UG",
        "R:10696052195027593": "江苏银蕨智能&合宙Air820UG",
        "R:10696050379039560": "杭州松美&合宙Air720UG（DTU）",
        "R:10696051744527461": "剑灵科技&九州:合宙Air724UG",
        "R:10696049918015580": "便捷神&合宙：Air720UH",
        "R:10696049918015576": "上海卡硕&合宙Air724UG",
        "R:10696051725600914": "云谷电力@合宙720H技术支持群",
        "R:10696053077016188": "深圳成隆&&合宙Air724UG 充电桩",
        "R:10696049918016340": "三晶&合宙  Air724UG",
        "R:10696053232019970": "天津博邦&九州：合宙 AIR800HS",
        "R:10696051081037747": "一俊物联&合宙:Air724UG",
        "R:10696050403034788": "大连驭凤&新明华&合宙Air720SG",
        "R:10696051771020724": "中铁信&合宙Air530Z",
        "R:10696051771021771": "中铁信安&合宙:Air530",
        "R:10696049435034491": "今创&合宙724",
        "R:10696051942023154": "华君智慧&合宙：Air724UG+Air530H",
        "R:10696049435035619": "华伟沃电&合宙:Cat.1",
        "R:10696049918017404": "引力波&合宙：Air722UG",
        "R:10696052057026960": "合肥智赞&合宙CAT1",
        "R:10696050232020084": "华创时代&合宙：Air724UG(IPC)",
        "R:10696051357026292": "山西方圆村&合宙:Cat.1 Lua",
        "R:10696052663057170": "千字文&合宙Air720SGI 口罩机",
        "R:10696052197020316": "千字&合宙Air720SGI",
        "R:10696049918015541": "臻享云&合宙：Air720UG(共享充电宝)",
        "R:10696049918018349": "川智&合宙724DTU",
        "R:10696052869033282": '国工能源&合宙:Cat.1 DTU',
        "R:10696049918015993": '宜通世纪&合宙：Air720U-DTU',
        "R:10696052304032575": "博观&合宙724UG网关",
        "R:10696052271033059": '烟台昊联&合宙：Air724UG',
        "R:10696051049025322": "科台斯&合宙Air720UH",
        "R:10696052420027472": "海信达&合宙Air720HI 智慧工业",
        "R:10696051618024526": "常州奥研&合宙：Air724UG",
        "R:10696050110030457": "北京融拓物联&九州:合宙Air720SL",
        "R:10696050517021568": "青岛沐华医疗&合宙:Air724UG Lua",
        "R:10696050517021722": '重庆荣冠&合宙:Cat.1 C-SDK',
        "R:10696050517022428": "能数科技&合宙724",
        "R:10696050851062313": '深圳飞安信&合宙：Air724UG',
        "R:10696049918016412": "彤心&合宙Air720SG（安卓）",
        "R:10696049751031331": "千字文&合宙：Air722UG(售卖机)",
        "R:10696049918013591": "上海电科&合宙:Cat.1 DTU",
        "R:10696049918017876": "郑州和动&合宙：Air724UG",
        "R:10696049918018537": "迪仕普&合宙：Air724UG",
        "R:10696052964047252": "捷思科技&合宙724UG",
        "R:10696051161030198": "阳西逢源&合宙：Air724UG",
        "R:10696051462022830": "珠海柏迅&合宙:Air820UG",
        "R:10696050492023857": "伟乐&合宙：Air720UG",
        "R:10696050963028575": "百宜&合宙Air724UG",
        "R:10696050963029716": "南京华助&合宙:Air720UH",
        "R:10696049918015562": "鼎合@中云技术群（Cat1和GPS群）",
        "R:10696051758773280": "上海乔沃&合宙：Air724UG",
        "R:10696053130029241": "温州精一智能&合宙Air724UG",
        "R:10696051356028021": "福建擎衣卫&合宙：Air820UG",
        "R:10696051996021264": "号令智能&合宙AirUG公网对讲机"
    }
    return CP[id] if id in CP.keys() else id


def isBoring(text):
    return (text in boring)


def test_isStaff(name):
    hz = [
        "盛玉霞", "孙志鹏", "沈园园",
        "祝平军", "王海洋", "曲振", "邓海",
        "谭立元", "郑治", "廖瑞", "周维华",
        "孙张鑫", "小助理", "伍珈沁", "王磊",
        "谢萧辉", "邓海", "刘嘉诚", "郑治", "黄何", "WHB", "石善振"
    ]
    return True if name in hz else False


staffList = [
    "盛玉霞", "孙志鹏", "沈园园",
    "祝平军", "王海洋", "曲振", "邓海",
    "谭立元", "郑治", "廖瑞", "周维华",
    "孙张鑫", "小助理", "伍珈沁", "王磊",
    "谢萧辉", "邓海", "刘嘉诚", "黄何"
]

hz_all_staff = ['李保正', '郑治', '陆相成', '陈媛媛', '旷文飞', '李武',
                '毛宇', '喻利华Lemon', '何晓洪', '陈玺', '何春梅', '李克正',
                '刁梦菡', '杨春丽', '陈功', '朱汪斌', '何祖秒', '安超', '陈旭东',
                '王雪峰', '伍珈沁', '李炜镪', '陈镇铖', '武壮壮', '王健', '范本玲',
                '葛云龙', '刘嘉诚', '黄何', '李怀恒', '张荣彪', '张恒', '靳志超',
                '谭立元', '秦鹏', '廖瑞', '周维华', '秦莉蓉', '王世茹', '曲振',
                '吴永', '郭文', '杨洁', '陈晨', '赵旭', '杨凤珍', '骆光圭',
                '顾志南', '闫国梁', '戴丽娜', '刘晨旭', '刘华', '盛玉霞', '叶竹茸',
                '楼康华', '陈红', '王小强', '鲍丽', '刘乐安', '闫俊杰', '祝平军',
                '梁健', '谢欢', '张涛', '朱天华', '熊晨', '孙志鹏', '金艺', '程蜜',
                '王帅', '周治冉', '张王强', '小助手', '李姣娣', '舒洁', '胡建慧',
                '陈之敏', '王磊', '邓海', '王海洋', '戎旺旺', '孙张鑫', '沈园园',
                '周伟', '邢智卓', '郑宏伟', '冯可认', '魏艳梅', '谢萧辉', '李俊', "WHB", "石善振"]

def test_isHZstaff(text):
    return (text in hz_all_staff)
