store = {}
store['timestamp']=1620915042
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=13']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=13
store['worker_id']=13
store['num_workers']=20
store['config']={'seed': 1253, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 1000, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.8473808765411377})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.1904821395874023})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.450857639312744})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.259488105773926})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7023, 'crossentropy': 1.8550251953125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1457022428512573})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.0798403024673462})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0686204433441162})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [40859, 17700, 33752, 29494, 273, 58812, 55839, 8359, 17937, 37113], 'labels': [-1, 8, 1, 8, 5, 3, 5, 8, 8, 0], 'scores': [0.5841064453125, 0.6004081964492798, 0.412853479385376, 0.7298070192337036, 0.8009344935417175, 0.6448430418968201, 0.7054235339164734, 0.7759557962417603, 0.6174004077911377, 0.6080576777458191]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.385775566101074})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.544109344482422})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.497537612915039})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.690821886062622})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6444, 'crossentropy': 2.1110595703125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2206567525863647})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2240543365478516})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2489864826202393})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [38807, 58329, 13192, 609, 40543, 14855, 45937, 28919, 36721, 19334], 'labels': [-1, 6, 7, 1, 6, 3, 7, 4, 2, 7], 'scores': [0.40901803970336914, 0.6695595979690552, 0.631950855255127, 0.46200162172317505, 0.6619598269462585, 0.4415624141693115, 0.49535834789276123, 0.5878435373306274, 0.5953084826469421, 0.5555417537689209]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.529292345046997})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.459659218788147})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.7300150394439697})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.7593727111816406})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.9590988159179688})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7891, 'crossentropy': 1.3869916015625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 0.8938153982162476})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.8048973083496094})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.7866383790969849})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 0.820949137210846})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [38642, 51635, 20301, 30895, 28881, 26113, 44157, 32209, 14120, 24435], 'labels': [-1, 3, 7, 3, 3, -1, 3, 3, 9, 3], 'scores': [0.6933208107948303, 0.6546573042869568, 0.4784584045410156, 0.7609211206436157, 0.8543383479118347, 0.31542932987213135, 0.6374343633651733, 0.6076619029045105, 0.7806844115257263, 0.7766614556312561]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.2404932975769043})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.3684638738632202})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.4949678182601929})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.6735742092132568})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7962, 'crossentropy': 1.1989591796875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.8939812183380127})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8480322360992432})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8246026039123535})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [51404, 11041, 1423, 22772, 44531, 18722, 5470, 32904, 54581, 50500], 'labels': [0, 0, 0, 9, 0, 9, 0, 9, 5, 3], 'scores': [0.5884422063827515, 0.708824872970581, 0.6054924130439758, 0.5287116765975952, 0.5067211389541626, 0.5075924396514893, 0.535679042339325, 0.4758409857749939, 0.42173510789871216, 0.5077806711196899]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.219083547592163})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.3907363414764404})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.4050960540771484})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.5541515350341797})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7854, 'crossentropy': 1.10289140625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.8823531866073608})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.8163777589797974})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.8074284791946411})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [43245, 52716, 4157, 23235, 52896, 55504, 15483, 12345, 46463, 13906], 'labels': [5, 0, 2, 5, 5, 2, 6, 3, 2, -1], 'scores': [0.5503907799720764, 0.631686806678772, 0.7039122581481934, 0.7162178754806519, 0.7024209499359131, 0.48299717903137207, 0.49672746658325195, 0.5641399025917053, 0.5937831401824951, 0.4767645597457886]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0144965648651123})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.237876534461975})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.154909372329712})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.3555599451065063})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8122, 'crossentropy': 0.9679294921875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 0.9141988754272461})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.7843419313430786})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.8025712370872498})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [11739, 9926, 4873, 4761, 41900, 45797, 52751, 27227, 59910, 47081], 'labels': [5, 6, 8, 8, 2, 5, 3, 4, 9, 5], 'scores': [0.5647597908973694, 0.49863123893737793, 0.581751823425293, 0.6652340292930603, 0.5071202516555786, 0.5810556411743164, 0.43874531984329224, 0.3298826217651367, 0.3743148446083069, 0.6512385606765747]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8031854629516602})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8023700714111328})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0201820135116577})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9075831174850464})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8757760524749756})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8779, 'crossentropy': 0.77986611328125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.711607813835144})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5915245413780212})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5514041185379028})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.5676493644714355})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [2636, 14623, 13004, 21421, 29300, 36398, 35597, 39208, 7631, 52389], 'labels': [8, 5, 8, 8, 3, 7, 2, 5, 1, 8], 'scores': [0.7931676506996155, 0.723092257976532, 0.5833041667938232, 0.8086729645729065, 0.7596333622932434, 0.6989418268203735, 0.5850778222084045, 0.6573603749275208, 0.410616397857666, 0.4015030264854431]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.866669237613678})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.953758716583252})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8856403827667236})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8907832503318787})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8607, 'crossentropy': 0.779993994140625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8417898416519165})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.796572208404541})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.7967395186424255})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [13024, 20973, 16882, 37974, 5740, 29681, 55894, 853, 28287, 5934], 'labels': [7, 8, 7, 2, 9, 2, 5, -1, 6, 5], 'scores': [0.4223896265029907, 0.3003023862838745, 0.486372172832489, 0.4019033908843994, 0.5159786343574524, 0.455885112285614, 0.3668200969696045, 0.3185688257217407, 0.2940773367881775, 0.4033949375152588]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7733129262924194})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7384170889854431})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7461398839950562})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8228940963745117})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7776044011116028})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8923, 'crossentropy': 0.70716728515625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6977704763412476})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5726929903030396})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.549048900604248})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5270535945892334})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [19146, 5474, 40498, 11485, 24047, 49111, 42990, 22593, 20999, 16539], 'labels': [9, 8, 2, -1, 4, -1, -1, 7, -1, -1], 'scores': [0.3928176760673523, 0.5636540055274963, 0.4648040533065796, 0.39799022674560547, 0.46031540632247925, 0.4496290683746338, 0.4476754665374756, 0.4530743956565857, 0.40494978427886963, 0.34858810901641846]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8095715045928955})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.757771372795105})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7994438409805298})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8765087127685547})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8745242357254028})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8992, 'crossentropy': 0.63420673828125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6698570251464844})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5888341665267944})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5578669309616089})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5278443098068237})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [19298, 42799, 24716, 13943, 21566, 23567, 5382, 45908, 38898, 32344], 'labels': [6, 2, 5, -1, 2, 5, 5, -1, 4, 5], 'scores': [0.664758026599884, 0.6504889726638794, 0.5185616612434387, 0.24597322940826416, 0.5309900641441345, 0.44894957542419434, 0.49018678069114685, 0.39649903774261475, 0.6247535347938538, 0.5362138450145721]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8833272457122803})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7959070205688477})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7390404343605042})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7522717714309692})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8791484236717224})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7553249597549438})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9002, 'crossentropy': 0.633393701171875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6957451701164246})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.549521803855896})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.48417139053344727})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.49534034729003906})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.5006706118583679})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [32878, 4421, 25724, 9318, 42078, 27765, 12935, 44948, 56949, 7484], 'labels': [9, 7, 1, 2, 4, 4, -1, 9, -1, -1], 'scores': [0.5077086687088013, 0.533790647983551, 0.37887585163116455, 0.4050016403198242, 0.6087049841880798, 0.5378625988960266, 0.362141489982605, 0.6864733099937439, 0.3163011074066162, 0.3976637125015259]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.780239462852478})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6234672665596008})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6871092319488525})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7282411456108093})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6977041959762573})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9187, 'crossentropy': 0.535}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6749400496482849})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5331442356109619})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5022690296173096})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4889369010925293})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [25065, 40035, 52319, 15769, 56362, 59722, 50973, 1832, 40050, 8691], 'labels': [0, -1, 2, 3, 0, -1, -1, -1, 9, 2], 'scores': [0.5828665792942047, 0.43521273136138916, 0.48900294303894043, 0.4439350366592407, 0.6114246249198914, 0.4596315622329712, 0.5470291376113892, 0.4429972171783447, 0.4887624979019165, 0.6970860362052917]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8346800804138184})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5981937050819397})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7547101378440857})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7461498379707336})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.777035653591156})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9158, 'crossentropy': 0.543839306640625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6632227301597595})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5050203800201416})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5047361850738525})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.48194295167922974})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [2092, 45422, 46237, 37184, 50414, 31291, 20855, 34052, 19937, 3947], 'labels': [3, 0, 8, -1, 9, -1, 6, 9, -1, 6], 'scores': [0.5593898296356201, 0.5199310779571533, 0.42955195903778076, 0.4657996892929077, 0.5221318602561951, 0.5110747814178467, 0.5725587010383606, 0.5741736888885498, 0.4697626829147339, 0.3027797341346741]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 0.9713953137397766})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7571059465408325})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6511765718460083})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6617080569267273})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7554589509963989})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8062877655029297})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9204, 'crossentropy': 0.55902587890625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6543930768966675})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5111643075942993})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.46950316429138184})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.45401328802108765})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.40811488032341003})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [25220, 40605, 18411, 19837, 46283, 40534, 38977, 17443, 54471, 30932], 'labels': [-1, -1, -1, -1, -1, 5, -1, -1, 8, 0], 'scores': [0.4569895267486572, 0.5068067312240601, 0.6412712931632996, 0.509175181388855, 0.4526444673538208, 0.5819362998008728, 0.5881528854370117, 0.4454460144042969, 0.5479586124420166, 0.37363749742507935]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7735739350318909})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.623682975769043})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5544825792312622})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6047143936157227})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6176142692565918})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6065177917480469})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9318, 'crossentropy': 0.465725390625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6662325859069824})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5207469463348389})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4770037829875946})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.41770368814468384})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4201429486274719})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [26898, 12600, 13516, 22057, 13799, 54981, 17748, 31469, 28814, 56065], 'labels': [7, 9, 3, 7, -1, 2, -1, -1, -1, -1], 'scores': [0.5744816064834595, 0.6123118996620178, 0.5759720206260681, 0.33157044649124146, 0.45807015895843506, 0.7536842823028564, 0.5411245822906494, 0.31525206565856934, 0.3065650463104248, 0.5081206560134888]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.776462197303772})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5993091464042664})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6298311948776245})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5789410471916199})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6408039331436157})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6370517015457153})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7007076740264893})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9296, 'crossentropy': 0.481725146484375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6711483001708984})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5459926724433899})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4424460530281067})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4068879187107086})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4279139041900635})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.36914169788360596})
store['active_learning_steps'][15]['eval_training']['best_epoch']=6
store['active_learning_steps'][15]['acquisition']={'indices': [46393, 52456, 55650, 24479, 56375, 5798, 13781, 55015, 45084, 46041], 'labels': [-1, 2, 8, 8, -1, 3, 8, 8, -1, 0], 'scores': [0.5282096862792969, 0.597148060798645, 0.48743730783462524, 0.6444857120513916, 0.6460455656051636, 0.5953205823898315, 0.6104037761688232, 0.4697696566581726, 0.4351966381072998, 0.3990294933319092]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8781412243843079})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6130868196487427})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6279698014259338})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6448776721954346})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7198203802108765})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9227, 'crossentropy': 0.51713173828125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.693418025970459})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.560897707939148})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5157788991928101})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5000969767570496})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [27167, 7259, 18598, 15832, 19324, 28525, 4183, 56914, 17112, 49734], 'labels': [3, 2, 9, 9, 2, 2, 2, 0, -1, 9], 'scores': [0.4397426247596741, 0.4575731158256531, 0.5680687427520752, 0.4877002239227295, 0.49208223819732666, 0.33957964181900024, 0.33772701025009155, 0.42093145847320557, 0.2280246615409851, 0.39258694648742676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9581393599510193})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.590844988822937})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5767937898635864})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5874515771865845})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6585707664489746})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5279916524887085})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6656020879745483})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6372140645980835})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.658484697341919})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9359, 'crossentropy': 0.4616234375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6130890250205994})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.4997871518135071})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.42656803131103516})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4232858419418335})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4015344977378845})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3726353049278259})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.3781281113624573})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3753759264945984})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [31509, 43781, 14654, 48189, 30214, 2780, 40593, 11729, 5789, 49062], 'labels': [-1, 4, -1, -1, 1, -1, -1, -1, -1, 5], 'scores': [0.42389750480651855, 0.4612724781036377, 0.528764009475708, 0.49209296703338623, 0.6153239607810974, 0.38804566860198975, 0.3861769437789917, 0.4855231046676636, 0.6292154788970947, 0.5322064757347107]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7280175685882568})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6111884117126465})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5903233289718628})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6082656383514404})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6767035722732544})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6879762411117554})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9282, 'crossentropy': 0.509274560546875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6496626138687134})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5501782298088074})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4573575258255005})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4314539134502411})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4080876410007477})
store['active_learning_steps'][18]['eval_training']['best_epoch']=5
store['active_learning_steps'][18]['acquisition']={'indices': [35649, 38597, 44345, 17231, 29287, 3367, 50144, 29227, 17467, 23656], 'labels': [3, 9, 4, 4, -1, 0, 9, 1, 3, 1], 'scores': [0.4360969662666321, 0.5354411005973816, 0.38168764114379883, 0.5612620115280151, 0.49043595790863037, 0.4975164532661438, 0.5328614115715027, 0.3106730580329895, 0.5612039566040039, 0.4448716640472412]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7848370671272278})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5659682750701904})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.46025219559669495})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5217843055725098})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5118755102157593})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5163295865058899})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9384, 'crossentropy': 0.413305615234375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5804370641708374})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.43558233976364136})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4309471547603607})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.42000526189804077})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.38066476583480835})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [25949, 36861, 55134, 22364, 45972, 57664, 26632, 51843, 40852, 21700], 'labels': [3, 8, -1, 0, 2, -1, -1, -1, 8, 7], 'scores': [0.3827025294303894, 0.34321725368499756, 0.519081711769104, 0.6385711431503296, 0.5089187622070312, 0.5065553188323975, 0.42707180976867676, 0.3818751573562622, 0.44106483459472656, 0.39644938707351685]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8257609605789185})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5249603986740112})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.52418053150177})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5659366250038147})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5409460067749023})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4929825961589813})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5067841410636902})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.585953950881958})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5876641273498535})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9451, 'crossentropy': 0.4342828125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5723088979721069})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4548358619213104})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.39600813388824463})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.35065773129463196})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.35288310050964355})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.33752697706222534})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3276703953742981})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.299070805311203})
store['active_learning_steps'][20]['eval_training']['best_epoch']=8
store['active_learning_steps'][20]['acquisition']={'indices': [40423, 22272, 15738, 7125, 50942, 7924, 34868, 8499, 51747, 18221], 'labels': [-1, 5, -1, 7, -1, 8, -1, 7, -1, -1], 'scores': [0.612037181854248, 0.4972013831138611, 0.6895257830619812, 0.5817349553108215, 0.5787396430969238, 0.7160135507583618, 0.3267035484313965, 0.487295925617218, 0.38932573795318604, 0.457891583442688]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9367952942848206})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5908715724945068})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5850169658660889})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5017956495285034})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5692534446716309})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5283493995666504})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5464527606964111})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9375, 'crossentropy': 0.453410009765625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6183046102523804})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4873759150505066})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.42325568199157715})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3977079391479492})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3456592559814453})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.3867204189300537})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [34744, 1705, 16488, 44366, 42703, 14546, 55268, 13991, 50945, 44799], 'labels': [4, -1, 9, -1, 0, 4, -1, 5, -1, -1], 'scores': [0.45935261249542236, 0.1963059902191162, 0.6260345578193665, 0.6119558811187744, 0.9217789471149445, 0.3509756922721863, 0.4556901454925537, 0.4879001975059509, 0.4183758497238159, 0.2994033694267273]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.951537013053894})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.569128155708313})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.535746693611145})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5686036348342896})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5854799747467041})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5355552434921265})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.604686975479126})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5883753895759583})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5915661454200745})
store['active_learning_steps'][22]['training']['best_epoch']=6
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9439, 'crossentropy': 0.430540771484375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6140058040618896})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4085753262042999})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.42127111554145813})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.35610532760620117})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.337323397397995})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3210221529006958})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.32569992542266846})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.2961360514163971})
store['active_learning_steps'][22]['eval_training']['best_epoch']=8
store['active_learning_steps'][22]['acquisition']={'indices': [39877, 7518, 26405, 33029, 55054, 14962, 18288, 22883, 16432, 34623], 'labels': [7, 9, 9, -1, 3, -1, 8, -1, 8, 0], 'scores': [0.6566076278686523, 0.5544096827507019, 0.7728638648986816, 0.4587869644165039, 0.7110499739646912, 0.44261419773101807, 0.6864731907844543, 0.5142397284507751, 0.6722445487976074, 0.4596666097640991]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9132031202316284})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5807771682739258})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4818705916404724})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5165111422538757})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4912711977958679})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.46894991397857666})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5601078271865845})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.506880521774292})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.534436821937561})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9437, 'crossentropy': 0.437042138671875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6568429470062256})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.46809130907058716})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.42010802030563354})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.37894773483276367})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3691118657588959})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3567611575126648})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.35266900062561035})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.334011435508728})
store['active_learning_steps'][23]['eval_training']['best_epoch']=8
store['active_learning_steps'][23]['acquisition']={'indices': [44797, 16002, 38997, 7113, 20171, 13489, 54576, 48662, 47100, 15878], 'labels': [-1, -1, -1, -1, 5, -1, 1, -1, 8, -1], 'scores': [0.3166764974594116, 0.46994006633758545, 0.4628002643585205, 0.5412254333496094, 0.745607852935791, 0.463495671749115, 0.584354043006897, 0.4099147319793701, 0.4684196710586548, 0.7158396244049072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8762397766113281})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5640339255332947})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5064076781272888})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.45392972230911255})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5361768007278442})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5521647930145264})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5229671597480774})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9391, 'crossentropy': 0.4091244873046875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6211992502212524})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4950774908065796})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.43774330615997314})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4087231159210205})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.39680060744285583})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3558584749698639})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [37294, 48900, 16109, 22155, 51976, 13093, 26633, 25138, 45520, 33818], 'labels': [-1, -1, -1, 3, -1, 3, -1, -1, -1, -1], 'scores': [0.4158090353012085, 0.21011364459991455, 0.4222205877304077, 0.482185959815979, 0.31271684169769287, 0.6437990069389343, 0.4335770010948181, 0.3278390169143677, 0.41160500049591064, 0.4726296067237854]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9034221172332764})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5469082593917847})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4943954348564148})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5041584968566895})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5441350936889648})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4980939030647278})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.943, 'crossentropy': 0.42093134765625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6574248671531677})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5228452086448669})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.42511996626853943})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.37017589807510376})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3739301562309265})
store['active_learning_steps'][25]['eval_training']['best_epoch']=4
store['active_learning_steps'][25]['acquisition']={'indices': [19752, 45057, 35196, 40046, 27916, 25990, 11485, 53324, 831, 39130], 'labels': [-1, 8, 7, 7, 8, -1, -1, 9, -1, 6], 'scores': [0.4279698133468628, 0.3716549277305603, 0.6066616773605347, 0.5155535340309143, 0.4074191451072693, 0.3744494915008545, 0.3594961166381836, 0.558733344078064, 0.4075911045074463, 0.5051290988922119]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9925999641418457})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5641740560531616})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4642006754875183})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5516889095306396})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4898286461830139})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.44763439893722534})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.48441001772880554})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5118420720100403})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44689929485321045})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4910767376422882})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5507611036300659})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.643779993057251})
store['active_learning_steps'][26]['training']['best_epoch']=9
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9494, 'crossentropy': 0.41036162109375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6158071756362915})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4400862455368042})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3816361427307129})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3489736318588257})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.33335262537002563})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3206409513950348})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.31803685426712036})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.2933485507965088})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3035709261894226})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.30147314071655273})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.2994334101676941})
store['active_learning_steps'][26]['eval_training']['best_epoch']=8
store['active_learning_steps'][26]['acquisition']={'indices': [11441, 19961, 37307, 26435, 17801, 6473, 19988, 37210, 15523, 58485], 'labels': [3, -1, 2, -1, 4, -1, 8, -1, -1, -1], 'scores': [0.637761116027832, 0.4522819519042969, 0.5921531319618225, 0.6046512126922607, 0.8312939405441284, 0.4367474317550659, 0.4696407914161682, 0.44688689708709717, 0.5215224623680115, 0.6742043495178223]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9345935583114624})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5795978307723999})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.48549684882164})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5116759538650513})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5677596926689148})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5096359252929688})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9443, 'crossentropy': 0.42511552734375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7070523500442505})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.49338358640670776})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.44749605655670166})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.40290898084640503})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4452275335788727})
store['active_learning_steps'][27]['eval_training']['best_epoch']=4
store['active_learning_steps'][27]['acquisition']={'indices': [54338, 51058, 53571, 13725, 37624, 39656, 48608, 41489, 49537, 53773], 'labels': [2, -1, -1, -1, -1, -1, 4, 2, 2, -1], 'scores': [0.45074108242988586, 0.522743821144104, 0.5227994918823242, 0.30311429500579834, 0.5387486219406128, 0.46038568019866943, 0.7549084424972534, 0.669123113155365, 0.5432655811309814, 0.3453623056411743]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8800028562545776})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.47748327255249023})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.41717827320098877})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.46009522676467896})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4528449475765228})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4465092420578003})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9491, 'crossentropy': 0.34795439453125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5863994359970093})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4404236674308777})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4063159227371216})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.35045522451400757})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3495216369628906})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [13878, 15796, 22991, 33594, 26676, 43095, 8879, 21351, 29439, 38182], 'labels': [4, -1, -1, 3, -1, -1, 3, -1, -1, -1], 'scores': [0.43643319606781006, 0.3435363173484802, 0.3662201166152954, 0.5305700302124023, 0.450736403465271, 0.4247598648071289, 0.47427797317504883, 0.4870189428329468, 0.46444398164749146, 0.42825639247894287]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9821596741676331})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.49071043729782104})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46503549814224243})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3597598373889923})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.41324007511138916})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4312271177768707})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4255724549293518})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9514, 'crossentropy': 0.3614836669921875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6563330292701721})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.42508822679519653})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.36067071557044983})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3387874960899353})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3372984528541565})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3433719277381897})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [18887, 42687, 5842, 47870, 21211, 16860, 39972, 5905, 44581, 48512], 'labels': [-1, 5, 1, -1, -1, 8, -1, -1, -1, 5], 'scores': [0.5417784452438354, 0.7895072102546692, 0.5361628830432892, 0.4163419008255005, 0.4084240794181824, 0.44448184967041016, 0.46809011697769165, 0.47282296419143677, 0.5868750214576721, 0.5776267051696777]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.978245198726654})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5180876851081848})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46571624279022217})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4454300105571747})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.45701202750205994})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5033121109008789})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5446298122406006})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9491, 'crossentropy': 0.4011281982421875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6331853866577148})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4170495271682739})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3889790177345276})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.35698479413986206})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3464928865432739})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.34832897782325745})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [46972, 54969, 48617, 16002, 47626, 50403, 36508, 45749, 9516, 16425], 'labels': [-1, 6, -1, -1, -1, -1, 5, -1, 3, -1], 'scores': [0.3402608633041382, 0.6333568692207336, 0.35827410221099854, 0.35781311988830566, 0.520211398601532, 0.5470917820930481, 0.7632619142532349, 0.5357445478439331, 0.42925310134887695, 0.333507776260376]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8523935675621033})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5256142616271973})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4567318558692932})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44810131192207336})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4908384680747986})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.41778552532196045})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4897681474685669})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44316914677619934})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4209049344062805})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9554, 'crossentropy': 0.3489609619140625}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6533809304237366})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4605475068092346})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4039393663406372})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.33416154980659485})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.34612128138542175})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3252856135368347})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.30218732357025146})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.29302215576171875})
store['active_learning_steps'][31]['eval_training']['best_epoch']=8
store['active_learning_steps'][31]['acquisition']={'indices': [46736, 46375, 17634, 37102, 1706, 28392, 6980, 7646, 20002, 14742], 'labels': [3, 0, 3, -1, -1, 3, 5, -1, -1, -1], 'scores': [0.29443585872650146, 0.44697999954223633, 0.4164740741252899, 0.5001855492591858, 0.3939704895019531, 0.5671437978744507, 0.6590944528579712, 0.38972365856170654, 0.5285946130752563, 0.4614149332046509]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0128414630889893})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.532404899597168})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4208926558494568})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3907162547111511})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41513651609420776})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4384874701499939})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4478871822357178})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9524, 'crossentropy': 0.3606269775390625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6435469388961792})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4679681062698364})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.42575937509536743})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39180225133895874})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3581085801124573})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3300767242908478})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [31794, 37584, 5688, 36990, 16031, 2475, 43546, 48594, 32747, 31413], 'labels': [2, 5, -1, -1, 0, -1, 2, 6, 8, 5], 'scores': [0.47317373752593994, 0.35007429122924805, 0.38546252250671387, 0.47228068113327026, 0.4981311559677124, 0.34192872047424316, 0.5232146382331848, 0.6571127772331238, 0.606899619102478, 0.3420361876487732]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9581115245819092})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5669089555740356})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.45804935693740845})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4373527467250824})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.43039190769195557})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.42683184146881104})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4166943430900574})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43410709500312805})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.47935372591018677})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42179712653160095})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9541, 'crossentropy': 0.360172802734375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5994793176651001})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.46878716349601746})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.40441474318504333})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3036147356033325})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.2984158992767334})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.32213902473449707})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.29947805404663086})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.26138314604759216})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.28186607360839844})
store['active_learning_steps'][33]['eval_training']['best_epoch']=8
store['active_learning_steps'][33]['acquisition']={'indices': [25522, 5434, 45050, 8417, 38912, 34050, 40202, 10455, 14210, 49064], 'labels': [-1, -1, -1, 6, -1, -1, 3, -1, -1, 8], 'scores': [0.49078142642974854, 0.6716281771659851, 0.5361831188201904, 0.7038978934288025, 0.6520818471908569, 0.6154070496559143, 0.4919961392879486, 0.14006417989730835, 0.8175622224807739, 0.8882585763931274]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9372422695159912})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4987349510192871})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41642987728118896})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40395209193229675})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3599434792995453})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4073013961315155})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42650043964385986})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.41112321615219116})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9568, 'crossentropy': 0.3359165771484375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6945784091949463})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4334712028503418})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.384652316570282})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3634370267391205})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.31573277711868286})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.34698939323425293})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3204807639122009})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [2202, 18266, 11538, 14341, 57781, 393, 54950, 44822, 21806, 870], 'labels': [1, -1, -1, 9, -1, -1, 8, 9, -1, -1], 'scores': [0.6122503280639648, 0.378168523311615, 0.33269989490509033, 0.5836043953895569, 0.3918527364730835, 0.2910120487213135, 0.6294499635696411, 0.5016499757766724, 0.34997981786727905, 0.40913188457489014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0303122997283936})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5447330474853516})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4292582869529724})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4401102662086487})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4284231662750244})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3970015347003937})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4080054759979248})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.42070651054382324})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.47940194606781006})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9552, 'crossentropy': 0.3486121337890625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.670335590839386})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.44186869263648987})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.39153042435646057})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.34562695026397705})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3289991319179535})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.2950703501701355})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.30406618118286133})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.29952529072761536})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [43575, 38889, 19570, 9726, 26560, 1031, 53560, 51380, 4949, 40144], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5654456615447998, 0.42953407764434814, 0.3891080617904663, 0.552736222743988, 0.41266798973083496, 0.4325007200241089, 0.4133564233779907, 0.40651535987854004, 0.5196500420570374, 0.5162904262542725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.1396098136901855})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5659165382385254})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4868367314338684})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.463651180267334})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4612642526626587})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4366488456726074})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4845302104949951})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5043749809265137})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4452885389328003})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9551, 'crossentropy': 0.354194091796875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6323691606521606})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.43139246106147766})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36849457025527954})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3758065104484558})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.32658806443214417})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3336825966835022})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3231923580169678})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2833469808101654})
store['active_learning_steps'][36]['eval_training']['best_epoch']=8
store['active_learning_steps'][36]['acquisition']={'indices': [7189, 34520, 6386, 47387, 22812, 48374, 58469, 20480, 55067, 55089], 'labels': [-1, 6, -1, 8, -1, -1, -1, -1, -1, -1], 'scores': [0.5449810028076172, 0.759419709444046, 0.5812826752662659, 0.5590975284576416, 0.5718033313751221, 0.4326462149620056, 0.48833346366882324, 0.5957047343254089, 0.5774640440940857, 0.5555126667022705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0687446594238281})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5996788144111633})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4237637519836426})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4616224765777588})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42002907395362854})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4043714702129364})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42513686418533325})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4651806950569153})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4468836486339569})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9522, 'crossentropy': 0.34452041015625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7252171635627747})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5247748494148254})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3791041970252991})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.39419716596603394})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3503541350364685})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.32458066940307617})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3250390887260437})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3184623718261719})
store['active_learning_steps'][37]['eval_training']['best_epoch']=8
store['active_learning_steps'][37]['acquisition']={'indices': [30821, 49890, 57599, 53419, 53777, 21002, 40203, 42798, 18256, 25721], 'labels': [-1, 5, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.33697283267974854, 0.7703005075454712, 0.7996506094932556, 0.5947102308273315, 0.682365894317627, 0.6536949872970581, 0.5666840076446533, 0.6301023364067078, 0.5439845323562622, 0.43085145950317383]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9375429153442383})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5387450456619263})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42741698026657104})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4141337275505066})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3895556330680847})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.386341392993927})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37698742747306824})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.45544373989105225})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40178221464157104})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42536675930023193})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9579, 'crossentropy': 0.3295229736328125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6019840240478516})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4168865382671356})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3654710054397583})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3299880623817444})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3116888403892517})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.28438544273376465})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.27995479106903076})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2680234909057617})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.24471361935138702})
store['active_learning_steps'][38]['eval_training']['best_epoch']=9
store['active_learning_steps'][38]['acquisition']={'indices': [1458, 14740, 5866, 19858, 41682, 52914, 30884, 27265, 58701, 42920], 'labels': [-1, 4, 5, -1, -1, 5, 2, -1, -1, -1], 'scores': [0.5712747573852539, 0.49325138330459595, 0.4793126583099365, 0.5518432855606079, 0.5695279836654663, 0.374778151512146, 0.7389296293258667, 0.5639022588729858, 0.38456642627716064, 0.7029579877853394]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.2275469303131104})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5947854518890381})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.46558430790901184})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4228115975856781})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4977142810821533})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4296209514141083})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.44920647144317627})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9522, 'crossentropy': 0.383976416015625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7264003753662109})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.48088783025741577})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.42215198278427124})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4018026888370514})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3502688407897949})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.41462820768356323})
store['active_learning_steps'][39]['eval_training']['best_epoch']=5
store['active_learning_steps'][39]['acquisition']={'indices': [3118, 1925, 45436, 28876, 6011, 32410, 25892, 10414, 49872, 54935], 'labels': [5, -1, -1, -1, -1, 9, -1, 9, -1, 8], 'scores': [0.44949477910995483, 0.5882782936096191, 0.4432336091995239, 0.42366230487823486, 0.5974667072296143, 0.2579948306083679, 0.6065351963043213, 0.3254193663597107, 0.35985279083251953, 0.4904928207397461]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9565806984901428})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5257863998413086})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.45419710874557495})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.44831332564353943})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3778822422027588})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42751502990722656})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4129679799079895})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4484931230545044})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.95, 'crossentropy': 0.34695126953125}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6351613402366638})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.44241195917129517})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3933483362197876})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.31883537769317627})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3186393976211548})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3063918948173523})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.35106566548347473})
store['active_learning_steps'][40]['eval_training']['best_epoch']=6
store['active_learning_steps'][40]['acquisition']={'indices': [36225, 44532, 47927, 18724, 21981, 24363, 360, 58394, 19852, 42477], 'labels': [-1, -1, -1, -1, -1, 6, -1, 8, -1, 3], 'scores': [0.39571166038513184, 0.49595797061920166, 0.5809711217880249, 0.3894333243370056, 0.5458089113235474, 0.44609588384628296, 0.4953795075416565, 0.4248516857624054, 0.4973219633102417, 0.36649757623672485]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0191054344177246})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5185068249702454})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4809040427207947})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38442349433898926})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42722558975219727})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.46878892183303833})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4340638518333435})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9513, 'crossentropy': 0.3658113525390625}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7033722400665283})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.517330527305603})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.43284082412719727})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.420104444026947})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3809412121772766})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.337050199508667})
store['active_learning_steps'][41]['eval_training']['best_epoch']=6
store['active_learning_steps'][41]['acquisition']={'indices': [28190, 38642, 48401, 2922, 7033, 34729, 9551, 19537, 8458, 59333], 'labels': [4, -1, -1, -1, 7, -1, -1, -1, 4, -1], 'scores': [0.451366662979126, 0.4940357208251953, 0.5337655544281006, 0.35868656635284424, 0.7188591957092285, 0.41548168659210205, 0.528647780418396, 0.4642103314399719, 0.5035860538482666, 0.3568603992462158]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.1215347051620483})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.578384518623352})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42838218808174133})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.42559975385665894})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3870213031768799})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.42067986726760864})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43583887815475464})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4130837917327881})
store['active_learning_steps'][42]['training']['best_epoch']=5
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9568, 'crossentropy': 0.3403394775390625}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.63916015625})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.47377607226371765})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3525521159172058})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3542845547199249})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.315114825963974})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3273250460624695})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.32082515954971313})
store['active_learning_steps'][42]['eval_training']['best_epoch']=5
store['active_learning_steps'][42]['acquisition']={'indices': [10576, 37489, 6902, 41134, 24155, 53820, 6262, 45652, 44489, 32162], 'labels': [-1, -1, -1, 6, 7, -1, -1, 7, -1, -1], 'scores': [0.3221226930618286, 0.36544370651245117, 0.4232672452926636, 0.4661383032798767, 0.31484562158584595, 0.3552827835083008, 0.4385793209075928, 0.43078625202178955, 0.23120343685150146, 0.4419901371002197]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0859596729278564})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6102393865585327})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.44182509183883667})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.408017098903656})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4025246798992157})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4036548137664795})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.413756787776947})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40603476762771606})
store['active_learning_steps'][43]['training']['best_epoch']=5
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9496, 'crossentropy': 0.37126181640625}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.700947642326355})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.454850435256958})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.40651869773864746})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.36791837215423584})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3832804262638092})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3565930724143982})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3383443057537079})
store['active_learning_steps'][43]['eval_training']['best_epoch']=7
store['active_learning_steps'][43]['acquisition']={'indices': [2039, 42606, 41433, 16103, 49777, 12891, 13942, 29036, 26516, 15659], 'labels': [1, 7, 9, -1, -1, -1, 4, -1, -1, -1], 'scores': [0.5443449020385742, 0.5443342328071594, 0.4110714793205261, 0.45510876178741455, 0.4192925691604614, 0.43379735946655273, 0.5742971897125244, 0.39361703395843506, 0.4415174722671509, 0.24509549140930176]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0305020809173584})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5456340312957764})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4270109534263611})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.40365785360336304})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.38296377658843994})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3843221664428711})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.404851496219635})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38675880432128906})
store['active_learning_steps'][44]['training']['best_epoch']=5
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9565, 'crossentropy': 0.3320040283203125}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6443897485733032})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4332515597343445})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.38361239433288574})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3516705632209778})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.33096981048583984})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30523985624313354})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3067343235015869})
store['active_learning_steps'][44]['eval_training']['best_epoch']=6
store['active_learning_steps'][44]['acquisition']={'indices': [45895, 48991, 49557, 17851, 17382, 35632, 54196, 56913, 34501, 5974], 'labels': [7, 2, -1, -1, -1, 0, -1, -1, -1, -1], 'scores': [0.41023576259613037, 0.5683664083480835, 0.5037378668785095, 0.4559110999107361, 0.6219189167022705, 0.534193754196167, 0.7431106567382812, 0.3294490575790405, 0.6566343307495117, 0.6054562330245972]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9758255481719971})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4836317002773285})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3797733187675476})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3742124140262604})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3956722319126129})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3573528528213501})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39512020349502563})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36571037769317627})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3424842357635498})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42371106147766113})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4022631347179413})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4012334942817688})
store['active_learning_steps'][45]['training']['best_epoch']=9
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9626, 'crossentropy': 0.3136754638671875}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6134077906608582})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4241446256637573})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.39154350757598877})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.30792689323425293})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.31291812658309937})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.2929445803165436})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2782156467437744})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2826678156852722})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25962212681770325})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2835922837257385})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27211111783981323})
store['active_learning_steps'][45]['eval_training']['best_epoch']=9
store['active_learning_steps'][45]['acquisition']={'indices': [22561, 5468, 55377, 44088, 47242, 47448, 51746, 52278, 40397, 39258], 'labels': [6, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.6800808906555176, 0.6050665378570557, 0.39036285877227783, 0.43596112728118896, 0.5527682304382324, 0.5335361957550049, 0.5741984248161316, 0.5623487234115601, 0.5351591110229492, 0.5382578372955322]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.01350998878479})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.49184906482696533})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41015446186065674})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35393959283828735})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3806880712509155})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3513028919696808})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4053444564342499})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37275925278663635})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35846948623657227})
store['active_learning_steps'][46]['training']['best_epoch']=6
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9577, 'crossentropy': 0.329127001953125}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5884486436843872})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3961559236049652})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.34572893381118774})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3358144164085388})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.30487799644470215})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34254899621009827})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29202109575271606})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28195852041244507})
store['active_learning_steps'][46]['eval_training']['best_epoch']=8
store['active_learning_steps'][46]['acquisition']={'indices': [24674, 53824, 21007, 44738, 14507, 52113, 17396, 4068, 28357, 547], 'labels': [-1, -1, -1, -1, -1, 7, 6, -1, 0, -1], 'scores': [0.3239986300468445, 0.4003748893737793, 0.4579983949661255, 0.38966310024261475, 0.47890937328338623, 0.3713414669036865, 0.474609911441803, 0.4850783348083496, 0.6329501867294312, 0.4308595061302185]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.1743674278259277})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6112862229347229})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4444041848182678})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4034922122955322})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3690962791442871})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3778303861618042})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37816131114959717})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.40714746713638306})
store['active_learning_steps'][47]['training']['best_epoch']=5
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9587, 'crossentropy': 0.3069448486328125}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6852220892906189})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.44184961915016174})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.39446842670440674})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3551744818687439})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.32818603515625})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3258952498435974})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34895074367523193})
store['active_learning_steps'][47]['eval_training']['best_epoch']=6
store['active_learning_steps'][47]['acquisition']={'indices': [47560, 59395, 1160, 22815, 57882, 37210, 18918, 28795, 706, 8894], 'labels': [-1, 8, 4, -1, 0, -1, -1, 2, -1, -1], 'scores': [0.4377925395965576, 0.37347084283828735, 0.5645670294761658, 0.5780402421951294, 0.34251320362091064, 0.48698270320892334, 0.38425111770629883, 0.43783923983573914, 0.44614577293395996, 0.4185032844543457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0550117492675781})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5009616017341614})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3917732536792755})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33421987295150757})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.367329478263855})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31500276923179626})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3530304729938507})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3765692114830017})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3546611964702606})
store['active_learning_steps'][48]['training']['best_epoch']=6
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9575, 'crossentropy': 0.30375869140625}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6873743534088135})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.44517815113067627})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3626381754875183})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.33629316091537476})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.31961411237716675})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.28598713874816895})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.29322734475135803})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2705385684967041})
store['active_learning_steps'][48]['eval_training']['best_epoch']=8
store['active_learning_steps'][48]['acquisition']={'indices': [53906, 12043, 28373, 58832, 635, 22162, 28371, 6466, 16022, 3510], 'labels': [8, -1, 4, 3, 5, -1, 3, 2, 8, 9], 'scores': [0.5023764371871948, 0.3343862295150757, 0.3227912187576294, 0.5574204921722412, 0.5471798777580261, 0.3531327247619629, 0.5480955839157104, 0.7034854292869568, 0.6414135694503784, 0.6393398642539978]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9406040906906128})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.46565091609954834})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38717055320739746})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3909580111503601})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4054686427116394})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40044015645980835})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9576, 'crossentropy': 0.357320361328125}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6594449281692505})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5500817894935608})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4608615040779114})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4210997521877289})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3938485383987427})
store['active_learning_steps'][49]['eval_training']['best_epoch']=5
store['active_learning_steps'][49]['acquisition']={'indices': [42793, 16732, 28666, 28746, 47599, 5013, 54628, 54043, 14484, 38379], 'labels': [4, -1, 5, -1, 0, 2, 4, 2, 2, -1], 'scores': [0.39107537269592285, 0.38341188430786133, 0.43144452571868896, 0.43657684326171875, 0.43069225549697876, 0.5198721289634705, 0.49334871768951416, 0.4392220973968506, 0.3768296241760254, 0.3435424566268921]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.196676254272461})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5607496500015259})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3974997103214264})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4219871461391449})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3877423405647278})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37859201431274414})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37594637274742126})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38390594720840454})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3859272003173828})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.44559645652770996})
store['active_learning_steps'][50]['training']['best_epoch']=7
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9592, 'crossentropy': 0.331510107421875}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5850346088409424})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.41302603483200073})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3488380014896393})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.36765432357788086})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35243162512779236})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.31312620639801025})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3172725439071655})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2916850447654724})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.28042492270469666})
store['active_learning_steps'][50]['eval_training']['best_epoch']=9
store['active_learning_steps'][50]['acquisition']={'indices': [55739, 34501, 47890, 25447, 36498, 8234, 45758, 36686, 41256, 51109], 'labels': [5, -1, -1, -1, -1, -1, -1, 6, -1, -1], 'scores': [0.5586862564086914, 0.4012577533721924, 0.7188764214515686, 0.5538455247879028, 0.6356542706489563, 0.5413308143615723, 0.6677172183990479, 0.5406951904296875, 0.6539000868797302, 0.5672964453697205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9715430736541748})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.45437878370285034})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41345730423927307})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36871466040611267})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33619147539138794})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33983951807022095})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3296494781970978})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3599799871444702})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37782061100006104})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3692655563354492})
store['active_learning_steps'][51]['training']['best_epoch']=7
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9642, 'crossentropy': 0.3078070556640625}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6540466547012329})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.44815903902053833})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3908185660839081})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3149542808532715})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31756505370140076})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2883574366569519})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2893369793891907})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24582359194755554})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2511044144630432})
store['active_learning_steps'][51]['eval_training']['best_epoch']=8
store['active_learning_steps'][51]['acquisition']={'indices': [18486, 43112, 58327, 37075, 44862, 47110, 26605, 31748, 26672, 56324], 'labels': [-1, -1, -1, -1, 0, -1, 8, 3, -1, 3], 'scores': [0.38439643383026123, 0.6312599778175354, 0.4589357376098633, 0.378639817237854, 0.45856764912605286, 0.5458135008811951, 0.589479923248291, 0.6362279057502747, 0.4283062219619751, 0.5087454915046692]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0548582077026367})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5404546856880188})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.42032390832901})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3872723877429962})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35915833711624146})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3588142991065979})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3610098361968994})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3667919635772705})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35191476345062256})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.349325954914093})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37939974665641785})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35118424892425537})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3511004149913788})
store['active_learning_steps'][52]['training']['best_epoch']=10
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9658, 'crossentropy': 0.318384375}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6417758464813232})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.45849210023880005})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.32013416290283203})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3270845413208008})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.288857638835907})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.26245376467704773})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.26458051800727844})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24654996395111084})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.27223479747772217})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24177825450897217})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.25201332569122314})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23490393161773682})
store['active_learning_steps'][52]['eval_training']['best_epoch']=12
store['active_learning_steps'][52]['acquisition']={'indices': [46738, 11889, 5361, 55368, 45801, 38920, 38316, 48482, 41982, 21417], 'labels': [-1, 5, -1, 8, 3, 7, 4, -1, -1, -1], 'scores': [0.4554710388183594, 0.6705904304981232, 0.3385918140411377, 0.48714613914489746, 0.5829572677612305, 0.7355155944824219, 0.6708806157112122, 0.4021298885345459, 0.48631757497787476, 0.3585944175720215]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1758785247802734})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5635615587234497})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.396389365196228})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3962401747703552})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33265167474746704})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31803712248802185})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3672815263271332})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.41866379976272583})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.37010273337364197})
store['active_learning_steps'][53]['training']['best_epoch']=6
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9617, 'crossentropy': 0.309376611328125}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6882695555686951})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4286095201969147})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3739463686943054})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3313274085521698})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3241175413131714})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3119460642337799})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2958282232284546})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2757936716079712})
store['active_learning_steps'][53]['eval_training']['best_epoch']=8
store['active_learning_steps'][53]['acquisition']={'indices': [6273, 21910, 36235, 48040, 37432, 27448, 29395, 43112, 6726, 53264], 'labels': [-1, -1, -1, -1, -1, 9, -1, -1, 6, -1], 'scores': [0.48104822635650635, 0.610042154788971, 0.3513979911804199, 0.420121431350708, 0.5461955070495605, 0.6247532963752747, 0.4018040895462036, 0.4403339624404907, 0.5539804697036743, 0.40787386894226074]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9833223819732666})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5155287981033325})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39114391803741455})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3686034083366394})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.31237590312957764})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34138986468315125})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3631269931793213})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34599757194519043})
store['active_learning_steps'][54]['training']['best_epoch']=5
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9614, 'crossentropy': 0.3123060546875}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6598893404006958})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4580598771572113})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4189605712890625})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3347123861312866})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33349722623825073})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3126046657562256})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30618584156036377})
store['active_learning_steps'][54]['eval_training']['best_epoch']=7
store['active_learning_steps'][54]['acquisition']={'indices': [58050, 11556, 47405, 14872, 50736, 22766, 22942, 15398, 30534, 42321], 'labels': [6, -1, -1, -1, -1, 4, -1, -1, 2, 5], 'scores': [0.6843580007553101, 0.4590117931365967, 0.4440643787384033, 0.4286069869995117, 0.6542546153068542, 0.3090365529060364, 0.560082197189331, 0.34307122230529785, 0.3849294185638428, 0.41025668382644653]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0802078247070312})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.6285730600357056})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39174512028694153})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41705185174942017})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3486422896385193})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3559577465057373})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39921465516090393})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.379276841878891})
store['active_learning_steps'][55]['training']['best_epoch']=5
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9617, 'crossentropy': 0.34064404296875}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6247634887695312})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40229135751724243})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3826606869697571})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3540393114089966})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3374464809894562})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3334025740623474})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.30913427472114563})
store['active_learning_steps'][55]['eval_training']['best_epoch']=7
store['active_learning_steps'][55]['acquisition']={'indices': [41772, 18556, 46393, 15450, 3555, 38375, 32646, 14630, 8800, 46858], 'labels': [5, -1, -1, 6, -1, -1, 5, -1, -1, -1], 'scores': [0.5872834920883179, 0.4564164876937866, 0.5827948451042175, 0.6064287424087524, 0.5373889803886414, 0.5232399106025696, 0.42055976390838623, 0.4407789707183838, 0.5837924480438232, 0.5523743629455566]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0181002616882324})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5569980144500732})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36772340536117554})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3595663607120514})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3248250484466553})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32475143671035767})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.338593453168869})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32224351167678833})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3248463273048401})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3820827603340149})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3660898208618164})
store['active_learning_steps'][56]['training']['best_epoch']=8
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9638, 'crossentropy': 0.293105224609375}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7175177335739136})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4707048535346985})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.37529170513153076})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32907044887542725})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3134578466415405})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.2864159941673279})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2942222058773041})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.28166717290878296})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2580980062484741})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.24971821904182434})
store['active_learning_steps'][56]['eval_training']['best_epoch']=10
store['active_learning_steps'][56]['acquisition']={'indices': [30075, 33182, 47929, 17339, 3333, 52439, 16616, 10082, 45005, 3317], 'labels': [-1, 9, -1, -1, -1, -1, -1, -1, 3, -1], 'scores': [0.6703641414642334, 0.6539645195007324, 0.5503384470939636, 0.38599252700805664, 0.3306664228439331, 0.5832352638244629, 0.48063039779663086, 0.5047228336334229, 0.6742600202560425, 0.5955842137336731]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0960023403167725})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.47601982951164246})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.41250258684158325})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3559573292732239})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33402395248413086})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3626859188079834})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3606763780117035})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.38236886262893677})
store['active_learning_steps'][57]['training']['best_epoch']=5
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.959, 'crossentropy': 0.3293119140625}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7248486280441284})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4521622061729431})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4155248701572418})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.34795835614204407})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.34937357902526855})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3166047930717468})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29392722249031067})
store['active_learning_steps'][57]['eval_training']['best_epoch']=7
store['active_learning_steps'][57]['acquisition']={'indices': [13488, 40538, 25421, 43126, 49677, 21307, 43897, 43950, 29542, 6354], 'labels': [-1, -1, 1, 3, -1, 4, 1, 9, 4, -1], 'scores': [0.4854695796966553, 0.43244385719299316, 0.19998562335968018, 0.6485427618026733, 0.3356451988220215, 0.35369235277175903, 0.6613724827766418, 0.5574870705604553, 0.32008886337280273, 0.3885918855667114]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1596295833587646})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.49146807193756104})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39002394676208496})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32628336548805237})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30759677290916443})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32100504636764526})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3382969796657562})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32202237844467163})
store['active_learning_steps'][58]['training']['best_epoch']=5
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9636, 'crossentropy': 0.3048789794921875}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6783555746078491})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4519219696521759})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3486008048057556})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3360070586204529})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3407438397407532})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.29891437292099})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3006255626678467})
store['active_learning_steps'][58]['eval_training']['best_epoch']=6
store['active_learning_steps'][58]['acquisition']={'indices': [16775, 59783, 22521, 3436, 26516, 58660, 11783, 42119, 15448, 24669], 'labels': [-1, 1, -1, 4, -1, 3, -1, -1, -1, 4], 'scores': [0.5500086545944214, 0.4837934374809265, 0.44961559772491455, 0.3193298876285553, 0.5846885442733765, 0.43469947576522827, 0.3255655765533447, 0.3582887649536133, 0.3578786849975586, 0.3066402077674866]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.0944997072219849})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5206074118614197})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3636775612831116})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4107595384120941})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33678770065307617})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3183286786079407})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33389872312545776})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33904188871383667})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3119421601295471})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3504156470298767})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3403577208518982})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.354089617729187})
store['active_learning_steps'][59]['training']['best_epoch']=9
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9662, 'crossentropy': 0.279012646484375}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6785356402397156})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4064120650291443})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3378846049308777})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3188627362251282})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.26984402537345886})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2809455394744873})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.26442575454711914})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25543004274368286})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2328968346118927})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.21006172895431519})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.23308536410331726})
store['active_learning_steps'][59]['eval_training']['best_epoch']=10
store['active_learning_steps'][59]['acquisition']={'indices': [7307, 15501, 49625, 18808, 24399, 39146, 19255, 46369, 39307, 1075], 'labels': [-1, -1, -1, -1, -1, -1, 9, 5, 8, 7], 'scores': [0.45784133672714233, 0.42941248416900635, 0.4832947850227356, 0.41806256771087646, 0.42724645137786865, 0.4730217456817627, 0.5166001915931702, 0.5379149913787842, 0.4827660322189331, 0.7045754790306091]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.058581829071045})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5453641414642334})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37117063999176025})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3219122290611267})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3306361138820648})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3235652446746826})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35756373405456543})
store['active_learning_steps'][60]['training']['best_epoch']=4
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9615, 'crossentropy': 0.3044196044921875}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6420236825942993})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.40350770950317383})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4019301235675812})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.35452258586883545})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3357504904270172})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.32557758688926697})
store['active_learning_steps'][60]['eval_training']['best_epoch']=6
store['active_learning_steps'][60]['acquisition']={'indices': [2632, 25150, 43388, 32758, 9782, 37141, 27337, 43112, 57748, 42860], 'labels': [-1, 2, 8, 5, 8, -1, -1, -1, -1, 9], 'scores': [0.39195895195007324, 0.46486181020736694, 0.39554381370544434, 0.33932584524154663, 0.4279899597167969, 0.39183831214904785, 0.3763880729675293, 0.4059213399887085, 0.43314874172210693, 0.38540875911712646]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.9869459867477417})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5153529644012451})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39064639806747437})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37053239345550537})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33999770879745483})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34326252341270447})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3527413010597229})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32744646072387695})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3397707939147949})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30794215202331543})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.362308144569397})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3380875289440155})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.37298083305358887})
store['active_learning_steps'][61]['training']['best_epoch']=10
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9639, 'crossentropy': 0.291438818359375}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6699310541152954})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4602140784263611})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3454052209854126})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.30958038568496704})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30129289627075195})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2737627327442169})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24188917875289917})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.22872045636177063})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2797597050666809})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2478460669517517})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.22945457696914673})
store['active_learning_steps'][61]['eval_training']['best_epoch']=8
store['active_learning_steps'][61]['acquisition']={'indices': [26061, 32707, 29676, 40492, 30900, 48006, 8628, 22607, 14414, 10332], 'labels': [-1, -1, -1, 6, 5, 6, 6, 4, -1, 6], 'scores': [0.37673425674438477, 0.4293818473815918, 0.4290819764137268, 0.5301809906959534, 0.6655687093734741, 0.5812475085258484, 0.3144288659095764, 0.5320237874984741, 0.4354943037033081, 0.5729258060455322]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.044335126876831})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4733954668045044})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3912266492843628})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3548072576522827})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.34391772747039795})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32184332609176636})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3108041286468506})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3211827874183655})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34045863151550293})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31105756759643555})
store['active_learning_steps'][62]['training']['best_epoch']=7
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.967, 'crossentropy': 0.2907656005859375}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6504870653152466})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.39983659982681274})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.31838172674179077})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3228296637535095})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27797234058380127})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25210124254226685})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25739139318466187})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26556843519210815})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2534407675266266})
store['active_learning_steps'][62]['eval_training']['best_epoch']=6
store['active_learning_steps'][62]['acquisition']={'indices': [21691, 9863, 53458, 55339, 8690, 7770, 14151, 15816, 55612, 40226], 'labels': [-1, -1, -1, -1, 8, -1, -1, -1, -1, -1], 'scores': [0.4205678105354309, 0.48490577936172485, 0.5740730166435242, 0.538296639919281, 0.45022666454315186, 0.37725770473480225, 0.31700485944747925, 0.5703050494194031, 0.4785194993019104, 0.31748420000076294]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.068652868270874})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.6027764081954956})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3768949508666992})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3413306772708893})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32464951276779175})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28552791476249695})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31779995560646057})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34340381622314453})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3077751398086548})
store['active_learning_steps'][63]['training']['best_epoch']=6
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9668, 'crossentropy': 0.2735111572265625}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.67511385679245})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4772476553916931})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4211570620536804})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34821900725364685})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3434659242630005})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.28051257133483887})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32330870628356934})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26692333817481995})
store['active_learning_steps'][63]['eval_training']['best_epoch']=8
store['active_learning_steps'][63]['acquisition']={'indices': [7972, 5943, 42472, 32341, 50981, 5800, 58360, 31418, 45069, 1706], 'labels': [6, -1, 2, -1, 4, 8, -1, 5, 4, -1], 'scores': [0.4961278438568115, 0.4324018955230713, 0.5677480697631836, 0.48923081159591675, 0.4598703980445862, 0.443986713886261, 0.3096948266029358, 0.49515560269355774, 0.48528599739074707, 0.3594179153442383]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.2131075859069824})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5539615154266357})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.39838707447052})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3684535026550293})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3216702342033386})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3103765845298767})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30375054478645325})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29490286111831665})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31758642196655273})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27741146087646484})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.33569133281707764})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3167981803417206})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3264213800430298})
store['active_learning_steps'][64]['training']['best_epoch']=10
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9671, 'crossentropy': 0.275488427734375}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6714608073234558})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4203396439552307})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.38030171394348145})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.31745660305023193})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27667272090911865})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.27175062894821167})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2604796588420868})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25349000096321106})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25512319803237915})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24904242157936096})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.22430837154388428})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26047730445861816})
store['active_learning_steps'][64]['eval_training']['best_epoch']=11
store['active_learning_steps'][64]['acquisition']={'indices': [14098, 7388, 47870, 26375, 44453, 45917, 1487, 14825, 59757, 57215], 'labels': [-1, -1, 9, -1, -1, 9, -1, 3, 2, -1], 'scores': [0.4062994718551636, 0.4174867272377014, 0.5824947357177734, 0.46291351318359375, 0.4352007508277893, 0.5916011929512024, 0.5047606229782104, 0.658525288105011, 0.6082007884979248, 0.4261200428009033]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 1.0710551738739014})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4951589107513428})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39709901809692383})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3339401185512543})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3461667597293854})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3294440507888794})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3106655478477478})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.318286269903183})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31719970703125})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3581564426422119})
store['active_learning_steps'][65]['training']['best_epoch']=7
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.29206728515625}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6246463060379028})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4284153878688812})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39516133069992065})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.29577845335006714})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33405056595802307})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2880474328994751})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2692320942878723})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.26291292905807495})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2831147313117981})
store['active_learning_steps'][65]['eval_training']['best_epoch']=8
store['active_learning_steps'][65]['acquisition']={'indices': [17382, 37361, 18119, 43592, 40463, 6818, 10382, 36498, 34755, 55916], 'labels': [6, 3, -1, -1, 3, -1, -1, 7, -1, -1], 'scores': [0.47780901193618774, 0.769912838935852, 0.429790735244751, 0.38282811641693115, 0.5489616990089417, 0.3376839756965637, 0.3411329984664917, 0.46835052967071533, 0.29589956998825073, 0.32563602924346924]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.1157668828964233})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5597293376922607})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3672580122947693})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30905961990356445})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30509382486343384})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2792331278324127})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2919059991836548})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28779667615890503})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2786206007003784})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28899794816970825})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3012791872024536})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28556716442108154})
store['active_learning_steps'][66]['training']['best_epoch']=9
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9667, 'crossentropy': 0.2807655517578125}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6324213743209839})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43057242035865784})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3234676122665405})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2916549742221832})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2827470302581787})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2410873919725418})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25583702325820923})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25499585270881653})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25260287523269653})
store['active_learning_steps'][66]['eval_training']['best_epoch']=6
store['active_learning_steps'][66]['acquisition']={'indices': [23456, 18657, 17248, 40530, 34641, 11271, 51462, 46851, 56014, 42646], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 5, -1], 'scores': [0.40686601400375366, 0.5492450594902039, 0.6088555753231049, 0.3748239278793335, 0.46326178312301636, 0.46050214767456055, 0.48016196489334106, 0.40580838918685913, 0.7489128112792969, 0.48266875743865967]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.2520047426223755})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5267454385757446})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3872910141944885})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34252625703811646})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30296725034713745})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31126561760902405})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29396748542785645})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3066570460796356})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30434367060661316})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30498531460762024})
store['active_learning_steps'][67]['training']['best_epoch']=7
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9672, 'crossentropy': 0.2766404296875}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6418312191963196})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42196139693260193})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34039855003356934})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.33878886699676514})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2968248724937439})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28293779492378235})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2587568461894989})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2796686887741089})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.23624280095100403})
store['active_learning_steps'][67]['eval_training']['best_epoch']=9
store['active_learning_steps'][67]['acquisition']={'indices': [53460, 32683, 26406, 58471, 47582, 29180, 38404, 12838, 47291, 9180], 'labels': [-1, -1, -1, 5, -1, 9, -1, -1, 1, 3], 'scores': [0.46085643768310547, 0.47059470415115356, 0.43289947509765625, 0.5362937450408936, 0.4534507989883423, 0.4405621290206909, 0.5060831308364868, 0.4895286560058594, 0.49077337980270386, 0.6965193748474121]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0308470726013184})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5490767359733582})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.38754066824913025})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33593326807022095})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2839413285255432})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.295869380235672})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3066955804824829})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30987268686294556})
store['active_learning_steps'][68]['training']['best_epoch']=5
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9652, 'crossentropy': 0.2831813232421875}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6323630213737488})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4668077230453491})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3992129862308502})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3803824782371521})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32294559478759766})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.28710615634918213})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3158732056617737})
store['active_learning_steps'][68]['eval_training']['best_epoch']=6
store['active_learning_steps'][68]['acquisition']={'indices': [29095, 15631, 52184, 48726, 40650, 19792, 22205, 20138, 23187, 5214], 'labels': [-1, -1, -1, 8, -1, 8, -1, -1, -1, -1], 'scores': [0.34244096279144287, 0.40565645694732666, 0.38259434700012207, 0.4426708221435547, 0.48835670948028564, 0.2970312833786011, 0.4393281936645508, 0.5271306037902832, 0.46502256393432617, 0.28844916820526123]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.1683520078659058})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.48025232553482056})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.36253622174263})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3420073986053467})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32344943284988403})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33086419105529785})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30982035398483276})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29781925678253174})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2992492616176605})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.289646714925766})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3079373240470886})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.325715035200119})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31778275966644287})
store['active_learning_steps'][69]['training']['best_epoch']=10
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.2736718505859375}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6896971464157104})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.41977646946907043})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3299142122268677})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.28883302211761475})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2718892991542816})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26200419664382935})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26371437311172485})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24352943897247314})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25192105770111084})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2168811857700348})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.22667378187179565})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.21865494549274445})
store['active_learning_steps'][69]['eval_training']['best_epoch']=10
store['active_learning_steps'][69]['acquisition']={'indices': [51816, 15306, 39595, 9992, 29594, 11068, 6591, 55120, 36726, 19837], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4839205741882324, 0.5139188766479492, 0.49773335456848145, 0.4595299959182739, 0.6589818000793457, 0.4522043466567993, 0.41316038370132446, 0.43623578548431396, 0.4619768261909485, 0.5892970561981201]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.078589916229248})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5277006030082703})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3888474702835083})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3154170513153076})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30222222208976746})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3020557165145874})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28642773628234863})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2968161106109619})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32335448265075684})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3181183636188507})
store['active_learning_steps'][70]['training']['best_epoch']=7
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9662, 'crossentropy': 0.2792123046875}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6247298717498779})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4192988872528076})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3422252833843231})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3108840584754944})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26780450344085693})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2854524850845337})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.266216516494751})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23584963381290436})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23132599890232086})
store['active_learning_steps'][70]['eval_training']['best_epoch']=9
store['active_learning_steps'][70]['acquisition']={'indices': [5223, 17684, 52463, 55268, 11330, 55908, 40112, 17780, 43060, 18448], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.41408300399780273, 0.5473400354385376, 0.4817582368850708, 0.5373883843421936, 0.4125216007232666, 0.45217299461364746, 0.39755237102508545, 0.5250071883201599, 0.6133978366851807, 0.5332928895950317]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.1576058864593506})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5449306964874268})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40571874380111694})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.34191134572029114})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31410709023475647})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3102789521217346})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.298565536737442})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3157614469528198})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3046737313270569})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3183533251285553})
store['active_learning_steps'][71]['training']['best_epoch']=7
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9673, 'crossentropy': 0.2864043212890625}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.668030858039856})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4599275588989258})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.37817710638046265})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.32246133685112})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31906765699386597})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3033068776130676})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2889060378074646})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2748052775859833})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2705148458480835})
store['active_learning_steps'][71]['eval_training']['best_epoch']=9
store['active_learning_steps'][71]['acquisition']={'indices': [7160, 45602, 7438, 34650, 35731, 47723, 41385, 41065, 8104, 54835], 'labels': [1, 5, 7, 2, 7, 8, -1, -1, 5, -1], 'scores': [0.6895579695701599, 0.7814600467681885, 0.4774909019470215, 0.5934959650039673, 0.28574857115745544, 0.5223484933376312, 0.39367520809173584, 0.3933480978012085, 0.44220051169395447, 0.5074808597564697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.1709799766540527})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5297973155975342})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3932914137840271})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3368936777114868})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3190802335739136})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3324034512042999})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3027721345424652})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27639496326446533})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2948167026042938})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3012966513633728})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2918017506599426})
store['active_learning_steps'][72]['training']['best_epoch']=8
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9702, 'crossentropy': 0.2594158447265625}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6650293469429016})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4480149745941162})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.35627999901771545})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3533715009689331})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.315388023853302})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3011191785335541})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2777072787284851})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25551968812942505})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27182430028915405})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25509804487228394})
store['active_learning_steps'][72]['eval_training']['best_epoch']=10
store['active_learning_steps'][72]['acquisition']={'indices': [39429, 373, 17365, 17402, 18502, 45919, 22575, 12461, 26303, 44], 'labels': [2, -1, 0, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.6516579985618591, 0.44813454151153564, 0.6257609128952026, 0.40659260749816895, 0.3010580539703369, 0.4848442077636719, 0.4695095419883728, 0.3491647243499756, 0.42197680473327637, 0.46757960319519043]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0275535583496094})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5438143014907837})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39237380027770996})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3027307391166687})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3075217604637146})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29038193821907043})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31584224104881287})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29348230361938477})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27850374579429626})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2751084864139557})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2914804518222809})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29772698879241943})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30255192518234253})
store['active_learning_steps'][73]['training']['best_epoch']=10
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9699, 'crossentropy': 0.250325439453125}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5853763818740845})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.40729597210884094})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3209478557109833})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29155898094177246})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27306780219078064})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25457096099853516})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.22167830169200897})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2120826244354248})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.20525911450386047})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2164096236228943})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.19084852933883667})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.20592889189720154})
store['active_learning_steps'][73]['eval_training']['best_epoch']=11
store['active_learning_steps'][73]['acquisition']={'indices': [54808, 48102, 23001, 16021, 27420, 36180, 2803, 10124, 44736, 26380], 'labels': [-1, 7, -1, -1, -1, -1, 3, 8, 5, -1], 'scores': [0.4066941738128662, 0.787775993347168, 0.4919389486312866, 0.6195711493492126, 0.6512502431869507, 0.5127559900283813, 0.46072834730148315, 0.5254808664321899, 0.39482879638671875, 0.32549208402633667]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1093227863311768})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5812636613845825})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3948575258255005})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3552979826927185})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30769994854927063})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30812209844589233})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28216856718063354})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32275229692459106})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2919786870479584})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2934127151966095})
store['active_learning_steps'][74]['training']['best_epoch']=7
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9675, 'crossentropy': 0.2776978759765625}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.636738657951355})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.42653805017471313})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.35158246755599976})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30795586109161377})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2981264591217041})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26431286334991455})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.269676148891449})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24815255403518677})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23782610893249512})
store['active_learning_steps'][74]['eval_training']['best_epoch']=9
store['active_learning_steps'][74]['acquisition']={'indices': [51121, 37977, 48638, 25800, 32918, 24976, 32776, 47886, 11346, 4646], 'labels': [-1, -1, 0, 1, 2, -1, 4, -1, 2, 2], 'scores': [0.5642449855804443, 0.32529544830322266, 0.6098718047142029, 0.6228211224079132, 0.6418905258178711, 0.38077449798583984, 0.5147194862365723, 0.31576263904571533, 0.4661611318588257, 0.6371726393699646]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.14593505859375})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5699615478515625})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4247397184371948})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3576645255088806})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.317355751991272})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28699222207069397})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3094899654388428})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28196942806243896})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2785572111606598})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2908565402030945})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.28387606143951416})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2740263342857361})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3034106492996216})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.25986960530281067})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.28040963411331177})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.31239190697669983})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.30436408519744873})
store['active_learning_steps'][75]['training']['best_epoch']=14
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9684, 'crossentropy': 0.3027530517578125}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.677654504776001})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.47657105326652527})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34776443243026733})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29432669281959534})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2761962413787842})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25819846987724304})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24138636887073517})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23710760474205017})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2245989739894867})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2226632684469223})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24222439527511597})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.22113093733787537})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.20016643404960632})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24772422015666962})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.21287523210048676})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2020310014486313})
store['active_learning_steps'][75]['eval_training']['best_epoch']=13
store['active_learning_steps'][75]['acquisition']={'indices': [14474, 13540, 15887, 18864, 10982, 1173, 19722, 32386, 25720, 14817], 'labels': [-1, 7, 2, -1, 1, -1, -1, 5, -1, 0], 'scores': [0.48874616622924805, 0.5281714200973511, 0.3787170946598053, 0.516332745552063, 0.5382091999053955, 0.39362311363220215, 0.5779011845588684, 0.5510663986206055, 0.5409435033798218, 0.3793973922729492]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.175948977470398})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6340764760971069})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40211614966392517})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34386998414993286})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29933786392211914})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3394196033477783})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2948540449142456})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3243441581726074})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2827552258968353})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2830848693847656})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2860832214355469})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32238030433654785})
store['active_learning_steps'][76]['training']['best_epoch']=9
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9691, 'crossentropy': 0.280640869140625}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6177529692649841})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39551687240600586})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35676056146621704})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34586966037750244})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30218127369880676})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2741314768791199})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2670603394508362})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.24796739220619202})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23814542591571808})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.21415452659130096})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2195073962211609})
store['active_learning_steps'][76]['eval_training']['best_epoch']=10
store['active_learning_steps'][76]['acquisition']={'indices': [17792, 39852, 6840, 10287, 17070, 15801, 52044, 28212, 46578, 21894], 'labels': [9, -1, -1, 7, -1, 7, 8, 2, 9, -1], 'scores': [0.44382643699645996, 0.4504510164260864, 0.38547229766845703, 0.4606691598892212, 0.6216550469398499, 0.5563170611858368, 0.34759126603603363, 0.6216153502464294, 0.19693565368652344, 0.3956575393676758]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.167543649673462})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5916213393211365})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.38690948486328125})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3219204545021057})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3324626088142395})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3147619366645813})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28828874230384827})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3341290354728699})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3072086274623871})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2899412214756012})
store['active_learning_steps'][77]['training']['best_epoch']=7
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9674, 'crossentropy': 0.2706769287109375}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6496444940567017})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.40753889083862305})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.34707656502723694})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3491869270801544})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30213019251823425})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2812304198741913})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2893100380897522})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25031808018684387})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26312190294265747})
store['active_learning_steps'][77]['eval_training']['best_epoch']=8
store['active_learning_steps'][77]['acquisition']={'indices': [29131, 22413, 59731, 3873, 4564, 13906, 36856, 1240, 34461, 16100], 'labels': [8, -1, 5, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5224239230155945, 0.4460022449493408, 0.6368973851203918, 0.5168513655662537, 0.5654528737068176, 0.5547254085540771, 0.5210509300231934, 0.3209105134010315, 0.4834555387496948, 0.43717730045318604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.1489768028259277})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5088851451873779})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39618101716041565})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3413662314414978})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3050321936607361})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2998587489128113})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31280505657196045})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3099004030227661})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2732803225517273})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27567243576049805})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30280518531799316})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2934531569480896})
store['active_learning_steps'][78]['training']['best_epoch']=9
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9707, 'crossentropy': 0.270620947265625}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6473721265792847})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.42234116792678833})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3264916241168976})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.32019615173339844})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.274172306060791})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26774895191192627})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2703242301940918})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24225564301013947})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.24840432405471802})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25618046522140503})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.23131945729255676})
store['active_learning_steps'][78]['eval_training']['best_epoch']=11
store['active_learning_steps'][78]['acquisition']={'indices': [47343, 34706, 35345, 50743, 23886, 7688, 36481, 44613, 49790, 21102], 'labels': [-1, -1, -1, 7, 1, -1, -1, -1, 2, 3], 'scores': [0.4489363431930542, 0.4863600730895996, 0.4320647716522217, 0.6118810772895813, 0.483315646648407, 0.4226357936859131, 0.27457094192504883, 0.3960615396499634, 0.5036641359329224, 0.617235541343689]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.105008602142334})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5554696321487427})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3568892180919647})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29714691638946533})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29513800144195557})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.29428771138191223})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2908834218978882})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3114898204803467})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2664846181869507})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26685279607772827})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2537573575973511})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25447800755500793})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26573446393013})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2861931025981903})
store['active_learning_steps'][79]['training']['best_epoch']=11
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9722, 'crossentropy': 0.2623945068359375}
store['active_learning_steps'][79]['eval_training']={}
store['active_learning_steps'][79]['eval_training']['epochs']=[]
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6773343682289124})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4294481575489044})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3429639935493469})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3116084933280945})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2575434148311615})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2483890950679779})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24054092168807983})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24208977818489075})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2164861559867859})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23129579424858093})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.21610257029533386})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.21434825658798218})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.20238551497459412})
store['active_learning_steps'][79]['eval_training']['best_epoch']=13
store['active_learning_steps'][79]['acquisition']={'indices': [38656, 19396, 27377, 16202, 636, 57410, 44148, 26836, 12054, 55791], 'labels': [5, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5202826261520386, 0.35034775733947754, 0.33749544620513916, 0.4201226234436035, 0.29978370666503906, 0.44908225536346436, 0.5716193318367004, 0.3918319344520569, 0.3945607542991638, 0.48568230867385864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.1558749675750732})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5599660873413086})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3665757477283478})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38757994771003723})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2977890372276306})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3080739974975586})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2668483257293701})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2722198963165283})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.275784432888031})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28922340273857117})
store['active_learning_steps'][80]['training']['best_epoch']=7
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.26628115234375}
store['active_learning_steps'][80]['eval_training']={}
store['active_learning_steps'][80]['eval_training']['epochs']=[]
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6409579515457153})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4812094271183014})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33375585079193115})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3393241763114929})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3084864020347595})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.289700448513031})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2871408462524414})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2651495337486267})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2651476562023163})
store['active_learning_steps'][80]['eval_training']['best_epoch']=9
store['active_learning_steps'][80]['acquisition']={'indices': [48915, 52140, 3810, 40935, 46148, 8968, 24462, 57881, 24426, 21011], 'labels': [2, 4, 3, 8, -1, -1, 2, -1, 5, -1], 'scores': [0.3445618152618408, 0.6232376098632812, 0.4888625144958496, 0.5291038751602173, 0.38602614402770996, 0.23621320724487305, 0.5035682916641235, 0.3709324598312378, 0.3190203905105591, 0.49090850353240967]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.1416746377944946})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5956483483314514})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3746090233325958})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28774499893188477})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27350711822509766})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28723663091659546})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2805928885936737})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28338295221328735})
store['active_learning_steps'][81]['training']['best_epoch']=5
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9692, 'crossentropy': 0.270736767578125}
store['active_learning_steps'][81]['eval_training']={}
store['active_learning_steps'][81]['eval_training']['epochs']=[]
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6901402473449707})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.44527578353881836})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3731224536895752})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34264323115348816})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34952202439308167})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30056893825531006})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.319258451461792})
store['active_learning_steps'][81]['eval_training']['best_epoch']=6
store['active_learning_steps'][81]['acquisition']={'indices': [18193, 55612, 57718, 29061, 3072, 8431, 18031, 25376, 3340, 42744], 'labels': [-1, -1, 7, 3, 4, -1, 4, -1, 4, -1], 'scores': [0.4120006561279297, 0.3635326623916626, 0.3967019319534302, 0.3388683795928955, 0.4936373233795166, 0.30472397804260254, 0.5066483616828918, 0.3271489143371582, 0.30672264099121094, 0.3197154998779297]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.215179681777954})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.6084933876991272})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.38717323541641235})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3020951449871063})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.293073832988739})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2995823323726654})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30613332986831665})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2784464657306671})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2924392521381378})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2687034606933594})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27294719219207764})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2732517123222351})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28313708305358887})
store['active_learning_steps'][82]['training']['best_epoch']=10
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9731, 'crossentropy': 0.25450712890625}
store['active_learning_steps'][82]['eval_training']={}
store['active_learning_steps'][82]['eval_training']['epochs']=[]
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6752049326896667})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.42735350131988525})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3470882177352905})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3782586455345154})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26174473762512207})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26350608468055725})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23919619619846344})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25768783688545227})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23563562333583832})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.22574840486049652})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.25828877091407776})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.19978055357933044})
store['active_learning_steps'][82]['eval_training']['best_epoch']=12
store['active_learning_steps'][82]['acquisition']={'indices': [43952, 47196, 55132, 13113, 25721, 35843, 53952, 10620, 45359, 33150], 'labels': [-1, -1, -1, -1, -1, 8, -1, -1, -1, 8], 'scores': [0.5263742208480835, 0.4497253894805908, 0.48975110054016113, 0.45727574825286865, 0.5178428888320923, 0.38623809814453125, 0.5203337669372559, 0.3798656463623047, 0.40455877780914307, 0.6655270457267761]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 1.1008787155151367})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5310019850730896})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4149709641933441})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33012330532073975})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2789381444454193})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2975298762321472})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30380022525787354})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34739524126052856})
store['active_learning_steps'][83]['training']['best_epoch']=5
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9709, 'crossentropy': 0.2682342041015625}
store['active_learning_steps'][83]['eval_training']={}
store['active_learning_steps'][83]['eval_training']['epochs']=[]
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.713729739189148})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4694943428039551})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3922809958457947})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36528679728507996})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33731383085250854})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3077555000782013})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3057500123977661})
store['active_learning_steps'][83]['eval_training']['best_epoch']=7
store['active_learning_steps'][83]['acquisition']={'indices': [29683, 45616, 10710, 41337, 57844, 54376, 50459, 53694, 41094, 25286], 'labels': [-1, 5, 8, 3, -1, -1, 8, 7, 5, -1], 'scores': [0.3871265649795532, 0.5728276968002319, 0.4109300971031189, 0.44354379177093506, 0.31614387035369873, 0.5120676755905151, 0.500704824924469, 0.6347459554672241, 0.498987078666687, 0.24423706531524658]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.2644684314727783})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6266963481903076})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.4234488010406494})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35295170545578003})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3172934949398041})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2912246286869049})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2910301685333252})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27585768699645996})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2872374653816223})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2873916029930115})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2790052890777588})
store['active_learning_steps'][84]['training']['best_epoch']=8
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9712, 'crossentropy': 0.27311982421875}
store['active_learning_steps'][84]['eval_training']={}
store['active_learning_steps'][84]['eval_training']['epochs']=[]
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7065321207046509})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4462277889251709})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3893803060054779})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29781222343444824})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.28671228885650635})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26873618364334106})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2921033799648285})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26780667901039124})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2665335536003113})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.230319082736969})
store['active_learning_steps'][84]['eval_training']['best_epoch']=10
store['active_learning_steps'][84]['acquisition']={'indices': [11271, 19006, 21594, 6386, 43123, 32619, 20746, 30545, 54264, 55788], 'labels': [-1, -1, -1, -1, -1, -1, 1, -1, 4, -1], 'scores': [0.42030221223831177, 0.2885476350784302, 0.443157434463501, 0.48715734481811523, 0.49956774711608887, 0.32703709602355957, 0.3688439130783081, 0.438315212726593, 0.45960766077041626, 0.48652970790863037]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0866303443908691})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.544704258441925})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31690919399261475})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3002815842628479})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26798468828201294})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23877829313278198})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25152719020843506})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26886892318725586})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.253152996301651})
store['active_learning_steps'][85]['training']['best_epoch']=6
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9699, 'crossentropy': 0.2543743896484375}
store['active_learning_steps'][85]['eval_training']={}
store['active_learning_steps'][85]['eval_training']['epochs']=[]
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7366278171539307})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.467059850692749})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.36799031496047974})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32021498680114746})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3222564458847046})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2899848222732544})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2745690643787384})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2817755937576294})
store['active_learning_steps'][85]['eval_training']['best_epoch']=7
store['active_learning_steps'][85]['acquisition']={'indices': [53990, 45749, 31975, 18724, 32984, 21374, 21316, 40221, 46441, 21527], 'labels': [-1, -1, -1, -1, -1, -1, -1, 2, -1, 2], 'scores': [0.4184880256652832, 0.4720032215118408, 0.4048883318901062, 0.29305386543273926, 0.31227564811706543, 0.468075156211853, 0.25467443466186523, 0.4131695032119751, 0.3701975345611572, 0.4538211226463318]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.225677728652954})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.579756498336792})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.4126036465167999})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3247714042663574})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3254093825817108})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2818772792816162})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2567678689956665})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2827625870704651})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2632948160171509})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2541552484035492})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30676835775375366})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25295621156692505})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26777106523513794})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3026992082595825})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2964083254337311})
store['active_learning_steps'][86]['training']['best_epoch']=12
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.2432491455078125}
store['active_learning_steps'][86]['eval_training']={}
store['active_learning_steps'][86]['eval_training']['epochs']=[]
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5825327038764954})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4371640384197235})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3264803886413574})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2585243582725525})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26139628887176514})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24010756611824036})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24196405708789825})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23057259619235992})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.22256220877170563})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.22470706701278687})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2281811237335205})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23292115330696106})
store['active_learning_steps'][86]['eval_training']['best_epoch']=9
store['active_learning_steps'][86]['acquisition']={'indices': [7186, 36967, 7308, 38061, 9966, 44301, 17070, 36055, 57455, 1600], 'labels': [-1, -1, 8, 2, 0, 4, -1, -1, 2, 0], 'scores': [0.3213679790496826, 0.5464825630187988, 0.5117053985595703, 0.7080747485160828, 0.4819102883338928, 0.3654983937740326, 0.6181261539459229, 0.6169272065162659, 0.5888693332672119, 0.5999927520751953]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 1.0440444946289062})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5167213082313538})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35750138759613037})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34891968965530396})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2750747799873352})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2547606825828552})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2578096389770508})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.264577180147171})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30425894260406494})
store['active_learning_steps'][87]['training']['best_epoch']=6
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.251559423828125}
store['active_learning_steps'][87]['eval_training']={}
store['active_learning_steps'][87]['eval_training']['epochs']=[]
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6617465019226074})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4049757122993469})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.373390257358551})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28129690885543823})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30740487575531006})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28659147024154663})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2746426463127136})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2677021026611328})
store['active_learning_steps'][87]['eval_training']['best_epoch']=8
store['active_learning_steps'][87]['acquisition']={'indices': [41195, 14062, 50079, 6948, 56664, 22283, 13653, 45685, 42682, 50801], 'labels': [-1, 8, -1, -1, -1, -1, -1, -1, 8, -1], 'scores': [0.3406156301498413, 0.6217567920684814, 0.3280911445617676, 0.34104812145233154, 0.3968390226364136, 0.4134432077407837, 0.3830108642578125, 0.326053261756897, 0.3964471220970154, 0.40281248092651367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1184943914413452})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.4845922589302063})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3998667001724243})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3053608536720276})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.26795756816864014})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2402263581752777})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24432358145713806})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24277247488498688})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.254147469997406})
store['active_learning_steps'][88]['training']['best_epoch']=6
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9751, 'crossentropy': 0.239002587890625}
store['active_learning_steps'][88]['eval_training']={}
store['active_learning_steps'][88]['eval_training']['epochs']=[]
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6621695756912231})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.44479256868362427})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.366536408662796})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3171345591545105})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2878573536872864})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26943814754486084})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2829558253288269})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2606140673160553})
store['active_learning_steps'][88]['eval_training']['best_epoch']=8
store['active_learning_steps'][88]['acquisition']={'indices': [21671, 57231, 39457, 12455, 44171, 9663, 13103, 59616, 29018, 19602], 'labels': [-1, -1, 0, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4041593074798584, 0.3599599599838257, 0.5088847875595093, 0.3450760841369629, 0.4271228313446045, 0.36434292793273926, 0.31853342056274414, 0.47486960887908936, 0.4798654317855835, 0.4975728988647461]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.118055820465088})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5834649205207825})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3714181184768677})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3377665877342224})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3271709084510803})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2920030951499939})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2773810923099518})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2690720558166504})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26041096448898315})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.272121787071228})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.24283148348331451})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2847454249858856})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2600376605987549})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3045310974121094})
store['active_learning_steps'][89]['training']['best_epoch']=11
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9724, 'crossentropy': 0.257715234375}
store['active_learning_steps'][89]['eval_training']={}
store['active_learning_steps'][89]['eval_training']['epochs']=[]
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5886365175247192})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4025677442550659})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3335484266281128})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30909156799316406})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2741447687149048})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2664095163345337})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2456938773393631})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24890422821044922})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24826166033744812})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23789158463478088})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.20755165815353394})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2035510241985321})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.21428409218788147})
store['active_learning_steps'][89]['eval_training']['best_epoch']=12
store['active_learning_steps'][89]['acquisition']={'indices': [7489, 12551, 29343, 50926, 46794, 46174, 1849, 43694, 27248, 6582], 'labels': [-1, -1, 5, 5, 8, 7, -1, -1, -1, 8], 'scores': [0.48358869552612305, 0.3978196382522583, 0.48048946261405945, 0.42234304547309875, 0.5446838736534119, 0.45905667543411255, 0.2498077154159546, 0.3335176706314087, 0.4896397590637207, 0.6012922525405884]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.0929465293884277})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5065951347351074})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.36642754077911377})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3460630774497986})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28403595089912415})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29488298296928406})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27158015966415405})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2925351858139038})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2563125789165497})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2672390341758728})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2832395136356354})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29743826389312744})
store['active_learning_steps'][90]['training']['best_epoch']=9
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9715, 'crossentropy': 0.2463703125}
store['active_learning_steps'][90]['eval_training']={}
store['active_learning_steps'][90]['eval_training']['epochs']=[]
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6368632316589355})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4476429224014282})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3457053303718567})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30498623847961426})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2692610025405884})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28177210688591003})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.26575833559036255})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2513227164745331})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2541283965110779})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.22798553109169006})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.21896842122077942})
store['active_learning_steps'][90]['eval_training']['best_epoch']=11
store['active_learning_steps'][90]['acquisition']={'indices': [36331, 51282, 21003, 19637, 52484, 29885, 34556, 25217, 53336, 23735], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.48413723707199097, 0.4412732720375061, 0.48501551151275635, 0.3158273696899414, 0.5342500805854797, 0.4079352617263794, 0.483731746673584, 0.4447615146636963, 0.4003440737724304, 0.5318926572799683]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.2338119745254517})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.664544403553009})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.35658693313598633})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2977445423603058})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2751128375530243})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26276981830596924})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2789009213447571})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2584150433540344})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24421356618404388})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2527904808521271})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25473126769065857})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30245527625083923})
store['active_learning_steps'][91]['training']['best_epoch']=9
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9726, 'crossentropy': 0.23339873046875}
store['active_learning_steps'][91]['eval_training']={}
store['active_learning_steps'][91]['eval_training']['epochs']=[]
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.522712230682373})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36245912313461304})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28038060665130615})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2659901976585388})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2776757478713989})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2438998818397522})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23807349801063538})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.22162580490112305})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23609435558319092})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.20303714275360107})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.21501865983009338})
store['active_learning_steps'][91]['eval_training']['best_epoch']=10
store['active_learning_steps'][91]['acquisition']={'indices': [22690, 13388, 51298, 38746, 21956, 21257, 45947, 2778, 6104, 52167], 'labels': [-1, 3, 5, 0, 5, -1, -1, -1, -1, -1], 'scores': [0.38422107696533203, 0.5187771916389465, 0.45396745204925537, 0.4076884686946869, 0.5820155143737793, 0.2793245315551758, 0.5822356939315796, 0.4054035544395447, 0.3302077054977417, 0.49272751808166504]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 1.005041241645813})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.550967812538147})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37503525614738464})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31388336420059204})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28219103813171387})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28310686349868774})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23727034032344818})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24161556363105774})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2530614137649536})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2502172291278839})
store['active_learning_steps'][92]['training']['best_epoch']=7
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9727, 'crossentropy': 0.2430226318359375}
store['active_learning_steps'][92]['eval_training']={}
store['active_learning_steps'][92]['eval_training']['epochs']=[]
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6945354342460632})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.41495686769485474})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32747727632522583})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3554178476333618})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2782267928123474})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2644839882850647})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.23547260463237762})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26335421204566956})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.21248212456703186})
store['active_learning_steps'][92]['eval_training']['best_epoch']=9
store['active_learning_steps'][92]['acquisition']={'indices': [46692, 52785, 15803, 37409, 53217, 10055, 14305, 7991, 54912, 35480], 'labels': [-1, -1, 1, -1, -1, -1, 8, -1, -1, 9], 'scores': [0.3683614730834961, 0.531690239906311, 0.47355639934539795, 0.4189809560775757, 0.3977987766265869, 0.5304356813430786, 0.4303911328315735, 0.4734005928039551, 0.5497190952301025, 0.33192604780197144]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.421412706375122})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.6029868125915527})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36665284633636475})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3508771061897278})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2811167240142822})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2935400903224945})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2636425495147705})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25282537937164307})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.244990274310112})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.2692634165287018})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2922353446483612})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.266040563583374})
store['active_learning_steps'][93]['training']['best_epoch']=9
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9717, 'crossentropy': 0.256202001953125}
store['active_learning_steps'][93]['eval_training']={}
store['active_learning_steps'][93]['eval_training']['epochs']=[]
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6724139451980591})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41268205642700195})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36015769839286804})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3073773980140686})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27867043018341064})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25610920786857605})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2779361605644226})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2464165985584259})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23210006952285767})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.21084722876548767})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.21753978729248047})
store['active_learning_steps'][93]['eval_training']['best_epoch']=10
store['active_learning_steps'][93]['acquisition']={'indices': [831, 49636, 28420, 33027, 14577, 9924, 18584, 32070, 29818, 21743], 'labels': [-1, -1, 1, -1, -1, 8, -1, -1, -1, -1], 'scores': [0.4912334680557251, 0.4922707676887512, 0.6847585439682007, 0.47197771072387695, 0.5014467835426331, 0.39518260955810547, 0.43348729610443115, 0.3295029401779175, 0.49011528491973877, 0.4318125247955322]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.2909018993377686})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.588092565536499})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4303334057331085})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3533659875392914})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3207194209098816})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2682289481163025})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26434558629989624})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28385838866233826})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24372035264968872})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2651253640651703})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26393723487854004})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2663227915763855})
store['active_learning_steps'][94]['training']['best_epoch']=9
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9727, 'crossentropy': 0.2404081787109375}
store['active_learning_steps'][94]['eval_training']={}
store['active_learning_steps'][94]['eval_training']['epochs']=[]
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7020062208175659})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.44828933477401733})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34676119685173035})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31441617012023926})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2814861536026001})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2448662668466568})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25351274013519287})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25577086210250854})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23595109581947327})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2275010645389557})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23290295898914337})
store['active_learning_steps'][94]['eval_training']['best_epoch']=10
store['active_learning_steps'][94]['acquisition']={'indices': [44873, 30016, 26100, 18052, 21983, 10724, 41424, 58157, 41575, 4961], 'labels': [-1, 4, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4950820207595825, 0.6129944324493408, 0.5538190007209778, 0.3205649256706238, 0.5031501650810242, 0.3184478282928467, 0.37773048877716064, 0.43627291917800903, 0.4503006935119629, 0.5768774747848511]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.2127561569213867})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5674240589141846})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3809664845466614})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3189281225204468})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2790483236312866})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2550201416015625})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2526734471321106})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2478100210428238})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23814517259597778})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24109438061714172})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2593829035758972})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.23709595203399658})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2672230005264282})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25883254408836365})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.24201378226280212})
store['active_learning_steps'][95]['training']['best_epoch']=12
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9759, 'crossentropy': 0.233535107421875}
store['active_learning_steps'][95]['eval_training']={}
store['active_learning_steps'][95]['eval_training']['epochs']=[]
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6912211179733276})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4139423966407776})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3303837180137634})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27728572487831116})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25747451186180115})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23089739680290222})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.21820813417434692})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24079656600952148})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2364988625049591})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.21483489871025085})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.22033226490020752})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2217225432395935})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2093317210674286})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.20386114716529846})
store['active_learning_steps'][95]['eval_training']['best_epoch']=14
store['active_learning_steps'][95]['acquisition']={'indices': [36985, 31345, 44275, 59838, 26174, 3222, 5370, 33684, 43771, 41081], 'labels': [-1, 3, -1, -1, -1, -1, 3, -1, -1, -1], 'scores': [0.6617574691772461, 0.6646630167961121, 0.3829209804534912, 0.39470672607421875, 0.6334185004234314, 0.5011645555496216, 0.6381378769874573, 0.4365708827972412, 0.38918566703796387, 0.5476875305175781]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0900731086730957})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5597261786460876})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3586951196193695})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3447785973548889})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3230966329574585})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29725751280784607})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2647720277309418})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2880714535713196})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25266069173812866})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29476088285446167})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29646700620651245})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2780464291572571})
store['active_learning_steps'][96]['training']['best_epoch']=9
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9727, 'crossentropy': 0.24208466796875}
store['active_learning_steps'][96]['eval_training']={}
store['active_learning_steps'][96]['eval_training']['epochs']=[]
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6820976734161377})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4477810859680176})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37852293252944946})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3342142701148987})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3107677102088928})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27390676736831665})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24794334173202515})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25657975673675537})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2553495168685913})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23519334197044373})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2719140946865082})
store['active_learning_steps'][96]['eval_training']['best_epoch']=10
store['active_learning_steps'][96]['acquisition']={'indices': [48130, 5112, 7496, 40882, 43588, 49364, 17835, 14326, 8310, 45954], 'labels': [-1, -1, -1, -1, 8, -1, -1, -1, -1, -1], 'scores': [0.3927879333496094, 0.4552966356277466, 0.35033273696899414, 0.4721742868423462, 0.6192346811294556, 0.37456250190734863, 0.5315958261489868, 0.27357208728790283, 0.21930992603302002, 0.5111078023910522]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.130955457687378})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5914894342422485})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.47066715359687805})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3285030722618103})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29983705282211304})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26702362298965454})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29944366216659546})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2569730281829834})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2706647515296936})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2847522497177124})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.248207688331604})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2675333619117737})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25307729840278625})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2400662750005722})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2686522603034973})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2807356119155884})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28348371386528015})
store['active_learning_steps'][97]['training']['best_epoch']=14
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9769, 'crossentropy': 0.236222900390625}
store['active_learning_steps'][97]['eval_training']={}
store['active_learning_steps'][97]['eval_training']['epochs']=[]
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.652917742729187})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4466775059700012})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.35284435749053955})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.269756555557251})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2642512023448944})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.20834390819072723})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.21189525723457336})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.21514907479286194})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.19908422231674194})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23172929883003235})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.22523707151412964})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.21245144307613373})
store['active_learning_steps'][97]['eval_training']['best_epoch']=9
store['active_learning_steps'][97]['acquisition']={'indices': [6862, 10390, 34741, 54905, 57605, 38345, 12143, 6462, 47396, 29827], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.6139674186706543, 0.40400564670562744, 0.6820328831672668, 0.569496214389801, 0.5225546360015869, 0.4844159483909607, 0.5146872997283936, 0.5412657856941223, 0.5110088586807251, 0.38516759872436523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.4175281524658203})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6290097832679749})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4794270396232605})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3840472400188446})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3139147162437439})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2762219309806824})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.27214527130126953})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.26480528712272644})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26989877223968506})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2660714387893677})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29205772280693054})
store['active_learning_steps'][98]['training']['best_epoch']=8
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.973, 'crossentropy': 0.2389990478515625}
store['active_learning_steps'][98]['eval_training']={}
store['active_learning_steps'][98]['eval_training']['epochs']=[]
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6647365093231201})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4691130220890045})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37487345933914185})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31214603781700134})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30772167444229126})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2603508532047272})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2348870038986206})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26771867275238037})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.22265563905239105})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2339557707309723})
store['active_learning_steps'][98]['eval_training']['best_epoch']=9
store['active_learning_steps'][98]['acquisition']={'indices': [32664, 52726, 32573, 34133, 4935, 12748, 14337, 26516, 37736, 20912], 'labels': [-1, 2, 8, -1, 2, -1, -1, -1, -1, -1], 'scores': [0.45325183868408203, 0.5021160244941711, 0.5118913054466248, 0.5324316024780273, 0.4866490364074707, 0.47026383876800537, 0.524372935295105, 0.4634271264076233, 0.3369952440261841, 0.49661195278167725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.2367169857025146})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.5261759757995605})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3756644129753113})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.3475520610809326})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28866446018218994})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2812458276748657})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26428863406181335})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.24130992591381073})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27414894104003906})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28456631302833557})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27834242582321167})
store['active_learning_steps'][99]['training']['best_epoch']=8
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.974, 'crossentropy': 0.2471299560546875}
store['active_learning_steps'][99]['eval_training']={}
store['active_learning_steps'][99]['eval_training']['epochs']=[]
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6588057279586792})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4206407070159912})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3627692461013794})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2981314957141876})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30842363834381104})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2716001272201538})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2778252363204956})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2502046227455139})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.24527901411056519})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.23917627334594727})
store['active_learning_steps'][99]['eval_training']['best_epoch']=10
store['active_learning_steps'][99]['acquisition']={'indices': [23736, 48912, 51561, 49425, 22546, 40513, 50646, 47949, 45700, 343], 'labels': [-1, 2, -1, -1, -1, -1, -1, 5, -1, -1], 'scores': [0.5141509771347046, 0.5779399871826172, 0.2870100736618042, 0.2640498876571655, 0.5889995694160461, 0.23855304718017578, 0.303027868270874, 0.5789393186569214, 0.3742638826370239, 0.5941349267959595]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0715547800064087})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.5521454811096191})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.37261608242988586})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3726428747177124})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2868794798851013})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27316272258758545})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27933037281036377})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25095027685165405})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2733915448188782})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26987123489379883})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24580693244934082})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2604483664035797})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2632485032081604})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27107512950897217})
store['active_learning_steps'][100]['training']['best_epoch']=11
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9713, 'crossentropy': 0.250141943359375}
store['active_learning_steps'][100]['eval_training']={}
store['active_learning_steps'][100]['eval_training']['epochs']=[]
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7509603500366211})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5322315096855164})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3453980088233948})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3176174759864807})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2833064794540405})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32727402448654175})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.239052414894104})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24082370102405548})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.22527776658535004})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23964142799377441})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23130130767822266})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2125181257724762})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2058924436569214})
store['active_learning_steps'][100]['eval_training']['best_epoch']=13
store['active_learning_steps'][100]['acquisition']={'indices': [33549, 5555, 52314, 21526, 39679, 33763, 42265, 35371, 36526, 6332], 'labels': [6, -1, -1, -1, -1, -1, 7, -1, 9, -1], 'scores': [0.41986751556396484, 0.33990514278411865, 0.5103058815002441, 0.5689948797225952, 0.47380948066711426, 0.3918760418891907, 0.30685341358184814, 0.5139254331588745, 0.5404024720191956, 0.4972766637802124]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.184601068496704})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6200045347213745})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37425220012664795})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31478965282440186})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.29274529218673706})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2549617290496826})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2587490677833557})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.23050138354301453})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2505056858062744})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2707059979438782})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25473934412002563})
store['active_learning_steps'][101]['training']['best_epoch']=8
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9755, 'crossentropy': 0.2434131591796875}
store['active_learning_steps'][101]['eval_training']={}
store['active_learning_steps'][101]['eval_training']['epochs']=[]
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6412519812583923})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.47144556045532227})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31512778997421265})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3022623360157013})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25145167112350464})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27509447932243347})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2591657042503357})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.26042440533638})
store['active_learning_steps'][101]['eval_training']['best_epoch']=5
store['active_learning_steps'][101]['acquisition']={'indices': [15334, 6509, 1671, 51426, 46029, 54739, 7126, 27455, 29602, 16701], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5309847593307495, 0.45011723041534424, 0.32165849208831787, 0.4358144998550415, 0.31948143243789673, 0.45082783699035645, 0.45098286867141724, 0.5336987972259521, 0.36677324771881104, 0.469931423664093]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.111839771270752})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6312930583953857})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.43113625049591064})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.35023191571235657})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28819721937179565})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28290387988090515})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3107954263687134})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29966893792152405})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2514688968658447})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25922030210494995})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2673082947731018})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2871936559677124})
store['active_learning_steps'][102]['training']['best_epoch']=9
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.9754, 'crossentropy': 0.2470921142578125}
store['active_learning_steps'][102]['eval_training']={}
store['active_learning_steps'][102]['eval_training']['epochs']=[]
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.746474027633667})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.48300063610076904})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3693911135196686})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3770233988761902})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3182675540447235})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2912294864654541})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27014148235321045})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26242420077323914})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25600600242614746})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26786044239997864})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26398831605911255})
store['active_learning_steps'][102]['eval_training']['best_epoch']=9
store['active_learning_steps'][102]['acquisition']={'indices': [16541, 2276, 49116, 47036, 12000, 26571, 4822, 39743, 42761, 31939], 'labels': [-1, 4, -1, 2, 7, -1, 4, -1, -1, 9], 'scores': [0.4924849271774292, 0.43588951230049133, 0.40071988105773926, 0.4511587917804718, 0.4504729211330414, 0.40735721588134766, 0.6241761445999146, 0.3603883981704712, 0.5268746614456177, 0.4356774687767029]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1392732858657837})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.5980167388916016})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.40560850501060486})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30418622493743896})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2747538685798645})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2778438329696655})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2868664562702179})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26605087518692017})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2604443430900574})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23543232679367065})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2663523256778717})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23613682389259338})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26286107301712036})
store['active_learning_steps'][103]['training']['best_epoch']=10
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.2422151123046875}
