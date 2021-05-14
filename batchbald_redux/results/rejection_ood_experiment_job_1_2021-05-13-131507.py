store = {}
store['timestamp']=1620908107
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=1']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=1
store['worker_id']=1
store['num_workers']=20
store['config']={'seed': 1235, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 1000, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.161111831665039})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.453094959259033})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.623962163925171})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.633950710296631})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7097, 'crossentropy': 1.93384453125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0863163471221924})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.076101303100586})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.0973293781280518})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [34999, 27120, 8349, 51516, 42721, 51498, 26743, 48255, 44, 13710], 'labels': [0, 2, 0, -1, 9, 5, -1, -1, -1, -1], 'scores': [0.8603826761245728, 1.0067381858825684, 0.6161460876464844, 0.5889767408370972, 0.7833563089370728, 0.6486831307411194, 0.6089903116226196, 0.627392590045929, 0.6627812385559082, 0.48242783546447754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.0786261558532715})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.7252612113952637})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.6195268630981445})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.917588233947754})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6528, 'crossentropy': 1.9532498046875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.1848477125167847})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.2190364599227905})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1074855327606201})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [17991, 25783, 32161, 5743, 51703, 25495, 14288, 42676, 45109, 56891], 'labels': [-1, 0, 8, 8, 4, 8, 7, 4, 8, 8], 'scores': [0.510491132736206, 0.8251909613609314, 0.7050743103027344, 0.932780385017395, 0.6566668748855591, 0.9545438289642334, 0.5751376152038574, 0.656089186668396, 0.8114084601402283, 0.8328122496604919]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.9987373352050781})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.0658376216888428})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.577971935272217})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.2589259147644043})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6658, 'crossentropy': 1.820435546875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1766951084136963})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.1473073959350586})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.124474048614502})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [13103, 24573, 39150, 2784, 54596, 59601, 17369, 55880, 52516, 33433], 'labels': [-1, 3, -1, 1, 8, -1, 2, -1, 6, -1], 'scores': [0.39132869243621826, 0.7493552565574646, 0.476993203163147, 0.48105645179748535, 0.5683426856994629, 0.440926194190979, 0.6659258008003235, 0.4495890140533447, 0.5844777822494507, 0.6952105760574341]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.5892984867095947})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.7134387493133545})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.7440195083618164})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 2.1072025299072266})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7546, 'crossentropy': 1.46789931640625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.0375220775604248})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0252764225006104})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 0.9541138410568237})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [3061, 20564, 58441, 21532, 37493, 15870, 16628, 58811, 54212, 26348], 'labels': [4, 5, 2, 5, 8, 6, 9, 2, 7, 2], 'scores': [0.49762070178985596, 0.619951069355011, 0.6089057922363281, 0.7061445713043213, 0.25949060916900635, 0.6244805455207825, 0.5490940809249878, 0.5709910988807678, 0.7018042206764221, 0.5293444991111755]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.331965684890747})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.538475513458252})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.809403896331787})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.8297572135925293})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7814, 'crossentropy': 1.22378212890625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 0.9938956499099731})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 0.8981723785400391})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 0.8460879325866699})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [21685, 49503, 2172, 16350, 21712, 47081, 14043, 38512, 57509, 7949], 'labels': [3, 5, 5, 9, 6, 5, 2, 5, 2, -1], 'scores': [0.6350576877593994, 0.4909147620201111, 0.6414289474487305, 0.6153799295425415, 0.3827853202819824, 0.6229724884033203, 0.4871535301208496, 0.7648051977157593, 0.5402548909187317, 0.49286556243896484]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.3026076555252075})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.3121769428253174})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.4303650856018066})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.4748990535736084})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7902, 'crossentropy': 1.11059140625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 0.9880409836769104})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.8736912608146667})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.8414047956466675})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [35249, 2278, 17127, 17212, 42115, 35619, 41792, 25050, 17063, 32977], 'labels': [3, 0, 3, 2, 2, 8, 9, 4, 3, 6], 'scores': [0.2816773056983948, 0.4808802604675293, 0.6693229079246521, 0.42270833253860474, 0.5147849321365356, 0.34797412157058716, 0.5116100311279297, 0.585703432559967, 0.29260462522506714, 0.4415777325630188]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0299694538116455})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.1356041431427002})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0788910388946533})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.090383529663086})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8423, 'crossentropy': 0.88772783203125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8356130123138428})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7847699522972107})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8026876449584961})
store['active_learning_steps'][6]['eval_training']['best_epoch']=2
store['active_learning_steps'][6]['acquisition']={'indices': [44013, 49140, 45334, 39954, 49992, 45026, 40708, 57295, 26022, 12278], 'labels': [4, 5, 5, 4, 5, 8, 8, 9, 8, 7], 'scores': [0.4854394793510437, 0.5240360498428345, 0.2976808547973633, 0.4998316168785095, 0.4731772541999817, 0.5178335905075073, 0.49752277135849, 0.5470645427703857, 0.37920212745666504, 0.4549877643585205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9987542033195496})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.9460598230361938})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9767571091651917})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0472197532653809})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0851590633392334})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8724, 'crossentropy': 0.802757275390625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7239229679107666})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6793744564056396})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6140626072883606})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.5997575521469116})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [46115, 3254, 7168, 12681, 56472, 11904, 18772, 12337, 53997, 33976], 'labels': [2, 8, 8, 1, 7, 8, 6, 0, 8, 9], 'scores': [0.44052380323410034, 0.3779487907886505, 0.6869331002235413, 0.5374631285667419, 0.7192410826683044, 0.651064395904541, 0.7798866033554077, 0.6106313467025757, 0.5058351755142212, 0.635686457157135]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.874311089515686})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8810235857963562})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9775053262710571})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9350341558456421})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8673, 'crossentropy': 0.79823212890625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.7886394262313843})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.75393146276474})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7353549003601074})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [30499, 36591, 55869, 2040, 12937, 35326, 20167, 5702, 8704, 148], 'labels': [5, 1, 3, 1, 5, 5, 3, 3, 1, 7], 'scores': [0.3567413091659546, 0.24309289455413818, 0.29749417304992676, 0.4253038167953491, 0.47624707221984863, 0.24395650625228882, 0.3892248868942261, 0.44255322217941284, 0.38438189029693604, 0.2875140905380249]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.789895236492157})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8024902939796448})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8058983683586121})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7426822185516357})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.9036627411842346})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8494138717651367})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8921878337860107})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9117, 'crossentropy': 0.654252587890625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.681262195110321})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.557612419128418})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.4946717619895935})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.48843151330947876})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.49109339714050293})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4535089433193207})
store['active_learning_steps'][9]['eval_training']['best_epoch']=6
store['active_learning_steps'][9]['acquisition']={'indices': [9030, 49200, 8756, 26736, 48878, 44877, 28257, 37160, 48630, 39671], 'labels': [-1, 0, 3, -1, -1, -1, -1, 5, 6, 5], 'scores': [0.5511800050735474, 0.7725762128829956, 0.5695902109146118, 0.48572105169296265, 0.4383535385131836, 0.41078007221221924, 0.4240518808364868, 0.5464985370635986, 0.3324660062789917, 0.47510695457458496]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7680838108062744})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6488769054412842})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6861543655395508})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7545214295387268})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6774502396583557})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9131, 'crossentropy': 0.557401171875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6647671461105347})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5503731966018677})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4704096019268036})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4809654951095581})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [35804, 28250, 28306, 50590, 605, 54989, 4285, 43042, 54482, 4066], 'labels': [9, -1, 8, -1, -1, -1, -1, 8, -1, 1], 'scores': [0.42902064323425293, 0.3971675634384155, 0.5653884410858154, 0.4097479581832886, 0.42881953716278076, 0.4555175304412842, 0.4514005184173584, 0.6526522040367126, 0.36762338876724243, 0.7313947677612305]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8603181838989258})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7080873847007751})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7330000400543213})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7297532558441162})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8093235492706299})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8991, 'crossentropy': 0.636302392578125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6880055069923401})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.5807234048843384})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5569990873336792})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5319783091545105})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [6879, 42167, 57028, 46402, 42711, 11126, 59581, 19810, 23629, 57267], 'labels': [4, 4, -1, 4, 4, 4, 8, 4, 5, 9], 'scores': [0.5834828615188599, 0.6273333430290222, 0.4159320592880249, 0.498901903629303, 0.5555065870285034, 0.6311149597167969, 0.4803647994995117, 0.5637729167938232, 0.6167317032814026, 0.5551345348358154]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7722128629684448})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6227768659591675})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6391295194625854})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6562058925628662})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7721825242042542})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9145, 'crossentropy': 0.540312158203125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7090933322906494})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5819060802459717})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5445423126220703})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.49691301584243774})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [18962, 42622, 25748, 14697, 10778, 47749, 54039, 38832, 23603, 36783], 'labels': [7, -1, 7, 8, -1, 3, 9, 8, 7, 0], 'scores': [0.5597820281982422, 0.322792649269104, 0.5187345743179321, 0.38455355167388916, 0.40381836891174316, 0.33440983295440674, 0.4619014859199524, 0.49784159660339355, 0.5085020661354065, 0.6782296895980835]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8531209230422974})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7301117181777954})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7361247539520264})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6468528509140015})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6424777507781982})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7146958112716675})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6940518617630005})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7601443529129028})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9263, 'crossentropy': 0.558973486328125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7036622762680054})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4928022623062134})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4874500632286072})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4282166063785553})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.42307162284851074})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.43595680594444275})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3992614150047302})
store['active_learning_steps'][13]['eval_training']['best_epoch']=7
store['active_learning_steps'][13]['acquisition']={'indices': [30164, 32193, 6636, 32730, 8879, 5194, 9559, 11737, 48735, 32453], 'labels': [4, 3, 5, 3, 3, 0, -1, -1, -1, 8], 'scores': [0.7464827299118042, 0.570109486579895, 0.6568391919136047, 0.7644665241241455, 0.633783221244812, 0.7073014974594116, 0.23434865474700928, 0.42338383197784424, 0.6755272150039673, 0.590424656867981]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8054150342941284})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5868468284606934})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5677398443222046})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6423699855804443})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6680046319961548})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5866849422454834})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9331, 'crossentropy': 0.47313701171875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6342790126800537})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4450983703136444})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4461953639984131})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4161508083343506})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4076777994632721})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [21564, 5851, 29839, 36544, 44999, 40259, 17713, 20864, 31958, 39025], 'labels': [-1, 7, 2, -1, -1, 8, -1, -1, -1, 9], 'scores': [0.4713047742843628, 0.4688042402267456, 0.5321998000144958, 0.34670013189315796, 0.47867846488952637, 0.5800052881240845, 0.4559208154678345, 0.46175622940063477, 0.7361392974853516, 0.43218010663986206]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7543144226074219})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6022578477859497})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5604793429374695})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5918604135513306})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5748341083526611})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.594077467918396})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9304, 'crossentropy': 0.49239384765625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6404850482940674})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4799049496650696})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4498567581176758})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.42352020740509033})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.45239269733428955})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [10635, 37962, 29528, 19501, 43941, 31768, 27896, 54633, 13305, 56146], 'labels': [-1, 8, -1, 3, 0, -1, -1, -1, -1, -1], 'scores': [0.35615670680999756, 0.49305441975593567, 0.3618725538253784, 0.49056196212768555, 0.5315377712249756, 0.46408963203430176, 0.4357333183288574, 0.43042922019958496, 0.3940945863723755, 0.39906561374664307]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9140771627426147})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5839563608169556})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5361266136169434})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5474637746810913})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.656627893447876})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.608512818813324})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9245, 'crossentropy': 0.480197314453125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6599361896514893})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4961847960948944})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4523412585258484})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.45729953050613403})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4387209415435791})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [29094, 28199, 21668, 41242, 5315, 17121, 13034, 4611, 8185, 39810], 'labels': [3, 3, 2, -1, 3, 8, -1, -1, 1, -1], 'scores': [0.6318321228027344, 0.520555317401886, 0.40087783336639404, 0.32646632194519043, 0.5981391668319702, 0.3398873805999756, 0.35796821117401123, 0.6149675846099854, 0.4648744463920593, 0.33360111713409424]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7970150709152222})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5190258026123047})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5530338883399963})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5237398743629456})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5772771835327148})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9319, 'crossentropy': 0.495040185546875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7010091543197632})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5087234377861023})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5100499391555786})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4505615234375})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [41370, 29458, 27703, 44350, 38321, 31301, 15938, 13207, 35843, 26358], 'labels': [5, 3, 6, 3, 3, 5, -1, 6, 8, 3], 'scores': [0.42472344636917114, 0.49145519733428955, 0.5023581981658936, 0.6298501491546631, 0.5344579219818115, 0.6510071754455566, 0.4507255554199219, 0.5307464599609375, 0.3674825429916382, 0.4562699794769287]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7891126871109009})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5170433521270752})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5834692120552063})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.508927583694458})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5100486278533936})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5304641723632812})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5070900321006775})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5592994689941406})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5036113262176514})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5519953966140747})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5374677181243896})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5286186933517456})
store['active_learning_steps'][18]['training']['best_epoch']=9
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.948, 'crossentropy': 0.442811962890625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6410990357398987})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4962998330593109})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4243330657482147})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.37806111574172974})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.34730610251426697})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.32268211245536804})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.29705289006233215})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.30058377981185913})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.29173874855041504})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.302640825510025})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.30562031269073486})
store['active_learning_steps'][18]['eval_training']['best_epoch']=9
store['active_learning_steps'][18]['acquisition']={'indices': [16217, 93, 9899, 13899, 41323, 14722, 41377, 55609, 15751, 15648], 'labels': [-1, -1, -1, -1, 6, 0, 9, -1, 2, -1], 'scores': [0.5156360268592834, 0.5425284504890442, 0.581626832485199, 0.5274240374565125, 0.7767341732978821, 0.6512097716331482, 0.5652438998222351, 0.5688254833221436, 0.8810790181159973, 0.49917513132095337]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9267737865447998})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5402177572250366})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5576698780059814})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5215443968772888})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5218859910964966})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5626877546310425})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5933297872543335})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9376, 'crossentropy': 0.4761021484375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6291675567626953})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.46861112117767334})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.43550676107406616})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.41107407212257385})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.41347283124923706})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.39474740624427795})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [16045, 39320, 30872, 2118, 46697, 18233, 19927, 15242, 31040, 7867], 'labels': [0, 6, 2, 7, -1, -1, 6, -1, 6, 6], 'scores': [0.6025384664535522, 0.4004715085029602, 0.6508486866950989, 0.7298696637153625, 0.44506359100341797, 0.4180572032928467, 0.5639149844646454, 0.29570484161376953, 0.44520145654678345, 0.4221601188182831]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8245407342910767})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5101934671401978})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4937356114387512})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47153615951538086})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.49947839975357056})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.475428968667984})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5238745808601379})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9452, 'crossentropy': 0.439605419921875}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5600849986076355})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4766325056552887})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4352900981903076})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3745638132095337})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.373995840549469})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3666248619556427})
store['active_learning_steps'][20]['eval_training']['best_epoch']=6
store['active_learning_steps'][20]['acquisition']={'indices': [40458, 50908, 32702, 55505, 40899, 10482, 19505, 8702, 46920, 21040], 'labels': [-1, 9, 5, -1, -1, 8, 2, -1, -1, 9], 'scores': [0.2961794137954712, 0.508907675743103, 0.5503723621368408, 0.4384843111038208, 0.38101518154144287, 0.34122323989868164, 0.7439388036727905, 0.32285356521606445, 0.46143388748168945, 0.7806369066238403]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.850017786026001})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5078330039978027})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5171131491661072})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.43609750270843506})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4490772485733032})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4605363607406616})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.46271657943725586})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9471, 'crossentropy': 0.40056240234375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6041827201843262})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4808163344860077})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3956393003463745})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3504400849342346})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.33199524879455566})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.34041839838027954})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [10756, 30692, 35688, 12353, 14367, 657, 4315, 13752, 32499, 31074], 'labels': [3, 3, 3, -1, 3, -1, 9, 9, 4, -1], 'scores': [0.6004219055175781, 0.4884355664253235, 0.5534058213233948, 0.42453891038894653, 0.6540607213973999, 0.519768476486206, 0.6399584412574768, 0.631558895111084, 0.4374566078186035, 0.3707519769668579]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8697865605354309})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.502362847328186})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38858887553215027})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.40570828318595886})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4031188488006592})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4016292691230774})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9521, 'crossentropy': 0.37804970703125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6539881825447083})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5157038569450378})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.40923333168029785})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3869520425796509})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3744281530380249})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [45631, 20109, 7720, 57972, 6251, 7328, 39877, 52169, 15779, 24123], 'labels': [-1, 5, -1, 4, 3, -1, 7, 2, 0, -1], 'scores': [0.46145594120025635, 0.4414560794830322, 0.3168773651123047, 0.6918007135391235, 0.44994276762008667, 0.37402796745300293, 0.5154019594192505, 0.5734222531318665, 0.5724852681159973, 0.47777092456817627]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.93416428565979})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5347045063972473})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47528067231178284})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4446457624435425})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4783249497413635})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44243282079696655})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5120704770088196})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4807910621166229})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5317685008049011})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9498, 'crossentropy': 0.4017037841796875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6181432008743286})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4146983325481415})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.35905611515045166})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3971564769744873})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3253074884414673})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3307332396507263})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.31046968698501587})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3143763542175293})
store['active_learning_steps'][23]['eval_training']['best_epoch']=7
store['active_learning_steps'][23]['acquisition']={'indices': [25158, 52812, 59406, 41281, 55054, 36482, 42485, 44532, 59187, 30660], 'labels': [-1, -1, -1, -1, 3, -1, -1, -1, -1, 9], 'scores': [0.42668503522872925, 0.4595451354980469, 0.6500104069709778, 0.49239635467529297, 0.5467252731323242, 0.6182621717453003, 0.5050076246261597, 0.6371628046035767, 0.627819836139679, 0.43725425004959106]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9300976991653442})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4704360365867615})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.45201265811920166})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.44267451763153076})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.42440423369407654})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4383116066455841})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.45994675159454346})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4513559639453888})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9473, 'crossentropy': 0.416044775390625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5986412763595581})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4338552951812744})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4055982232093811})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3233603835105896})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3229382336139679})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.31018394231796265})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3388749361038208})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [32276, 25534, 14250, 58640, 35168, 53953, 20037, 29494, 34294, 27265], 'labels': [3, -1, -1, -1, -1, 8, 8, -1, 4, -1], 'scores': [0.6553351879119873, 0.44414353370666504, 0.43183910846710205, 0.417117714881897, 0.3984314203262329, 0.44916582107543945, 0.6664878129959106, 0.5843433737754822, 0.42629581689834595, 0.6463561058044434]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0199227333068848})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5166023969650269})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4480191767215729})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4571867287158966})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4543014168739319})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.46820908784866333})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9478, 'crossentropy': 0.40741669921875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6717755794525146})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.48549360036849976})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.44551926851272583})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3806668221950531})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3788314759731293})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [43, 42561, 20959, 52131, 35956, 228, 43576, 49064, 15592, 16210], 'labels': [-1, -1, 2, 5, 9, 3, -1, 8, 9, 5], 'scores': [0.3181535005569458, 0.349764347076416, 0.47248584032058716, 0.45400696992874146, 0.5077337026596069, 0.5785022974014282, 0.43521201610565186, 0.642337441444397, 0.5798893570899963, 0.4785456657409668]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8455121517181396})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5289444327354431})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39169764518737793})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37665581703186035})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4420333504676819})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40608662366867065})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4337432384490967})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9491, 'crossentropy': 0.3745028564453125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6292574405670166})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.43956246972084045})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.37387579679489136})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.36264926195144653})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3466879725456238})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.33048805594444275})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [33664, 33388, 57276, 50046, 10744, 25308, 52324, 15185, 37048, 55219], 'labels': [8, 8, 8, 7, 7, 7, -1, 2, 9, -1], 'scores': [0.39868152141571045, 0.4134928584098816, 0.5381501913070679, 0.6195959448814392, 0.5866971015930176, 0.46752041578292847, 0.5430408716201782, 0.6693345904350281, 0.6349813938140869, 0.461880087852478]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8310889601707458})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4722411632537842})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3794512450695038})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3710520267486572})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.39996641874313354})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3901558518409729})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4028772711753845})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9546, 'crossentropy': 0.354415771484375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.590964674949646})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4363614320755005})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40356314182281494})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3542925715446472})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3566989600658417})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33083879947662354})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [3095, 20355, 37383, 54259, 42519, 26635, 49202, 6272, 31155, 47068], 'labels': [9, -1, 3, -1, -1, 2, 5, 9, -1, -1], 'scores': [0.4207194149494171, 0.41549575328826904, 0.6003422737121582, 0.41456735134124756, 0.48549479246139526, 0.5571011304855347, 0.7216190099716187, 0.5519687533378601, 0.37966132164001465, 0.3855605125427246]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.021356463432312})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5206080675125122})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4122518301010132})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3922995924949646})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3836419880390167})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3978375196456909})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38173896074295044})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37776273488998413})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39965111017227173})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38983410596847534})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4152528643608093})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9522, 'crossentropy': 0.373834326171875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6328529119491577})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4336066246032715})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3822842240333557})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34066835045814514})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.33985990285873413})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.29261407256126404})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.297367662191391})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.28510046005249023})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.294361412525177})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2684819996356964})
store['active_learning_steps'][28]['eval_training']['best_epoch']=10
store['active_learning_steps'][28]['acquisition']={'indices': [2895, 24209, 18716, 34408, 38892, 16597, 9575, 36226, 25167, 11351], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.551954060792923, 0.5610989332199097, 0.5527260303497314, 0.48663437366485596, 0.7055872678756714, 0.6180160641670227, 0.6054556965827942, 0.6531772613525391, 0.5665701031684875, 0.7049335837364197]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0622978210449219})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.505477786064148})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4217824339866638})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3700161278247833})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.39032644033432007})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39046400785446167})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3851342797279358})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9579, 'crossentropy': 0.341715185546875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6453908085823059})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4651169776916504})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3839721083641052})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.34538137912750244})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.37000101804733276})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3264477849006653})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [11278, 31102, 30139, 56494, 57289, 15743, 15932, 37952, 10800, 28719], 'labels': [-1, 4, 6, 9, -1, 3, 7, 8, 8, 8], 'scores': [0.35368502140045166, 0.3949531018733978, 0.4287986755371094, 0.4447122812271118, 0.3623164892196655, 0.5642175674438477, 0.6430989503860474, 0.38757479190826416, 0.4258267283439636, 0.5834160447120667]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.19996976852417})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5398509502410889})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4204559028148651})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.406050443649292})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.44896188378334045})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40954017639160156})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38030385971069336})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42541420459747314})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.44224852323532104})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4171862006187439})
store['active_learning_steps'][30]['training']['best_epoch']=7
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9567, 'crossentropy': 0.373043115234375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6770472526550293})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4601704478263855})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3931090235710144})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.34357884526252747})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3109743595123291})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.33055588603019714})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.2785375714302063})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.29101699590682983})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2970011830329895})
store['active_learning_steps'][30]['eval_training']['best_epoch']=7
store['active_learning_steps'][30]['acquisition']={'indices': [23014, 7091, 19537, 26850, 19791, 30250, 32596, 52916, 25315, 25844], 'labels': [-1, -1, -1, 2, -1, -1, 8, 1, 5, 4], 'scores': [0.4744352102279663, 0.5056247115135193, 0.5595112442970276, 0.6792432069778442, 0.5799992084503174, 0.3857206106185913, 0.581287682056427, 0.6055814027786255, 0.7460858821868896, 0.6423734724521637]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.031761884689331})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4880470931529999})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32422155141830444})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32974910736083984})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30742397904396057})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3579108715057373})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3393914997577667})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3360949456691742})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9636, 'crossentropy': 0.305933349609375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5735443830490112})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.42725199460983276})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3646004796028137})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3269858956336975})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32383155822753906})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30656740069389343})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28544241189956665})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [34569, 46868, 13709, 57134, 40370, 51642, 1256, 28658, 19752, 50728], 'labels': [-1, -1, 6, -1, -1, -1, 9, 5, 5, 3], 'scores': [0.3043214678764343, 0.4536912441253662, 0.5918306112289429, 0.4999045133590698, 0.3486696481704712, 0.2403789758682251, 0.31409287452697754, 0.5102512538433075, 0.4843634366989136, 0.6894745826721191]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.1763265132904053})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5076981782913208})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3649860620498657})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3389248251914978})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.340302050113678})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3172414302825928})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3162641227245331})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3242374658584595})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34147658944129944})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3365147113800049})
store['active_learning_steps'][32]['training']['best_epoch']=7
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9618, 'crossentropy': 0.3144943115234375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5913602709770203})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.40730589628219604})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.37902793288230896})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3436375856399536})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.33764833211898804})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31686490774154663})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2604858875274658})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2745599150657654})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.24515503644943237})
store['active_learning_steps'][32]['eval_training']['best_epoch']=9
store['active_learning_steps'][32]['acquisition']={'indices': [29418, 49002, 4165, 47297, 24643, 37838, 24688, 17361, 52800, 44298], 'labels': [4, 1, 2, 8, -1, 2, 1, -1, 9, 2], 'scores': [0.6721988916397095, 0.40501147508621216, 0.8276326060295105, 0.6630358695983887, 0.4910162687301636, 0.4100457429885864, 0.5816504955291748, 0.526874303817749, 0.5069774985313416, 0.5458182096481323]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.026519775390625})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4464245140552521})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3532894551753998})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3429487943649292})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34033477306365967})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37557053565979004})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3188853859901428})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3779279589653015})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35877910256385803})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37848976254463196})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9629, 'crossentropy': 0.3142826171875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5989569425582886})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.41509100794792175})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.35841435194015503})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3083275556564331})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.2946920394897461})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2882577180862427})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2844606041908264})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2794272303581238})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2602921426296234})
store['active_learning_steps'][33]['eval_training']['best_epoch']=9
store['active_learning_steps'][33]['acquisition']={'indices': [36000, 39864, 46794, 52130, 31774, 32880, 16456, 39687, 4530, 20355], 'labels': [9, 8, 8, 0, -1, 0, -1, -1, 7, -1], 'scores': [0.4480111598968506, 0.36195969581604004, 0.5007211267948151, 0.3991727828979492, 0.3926123380661011, 0.6471959948539734, 0.5399529933929443, 0.4238017797470093, 0.4550328254699707, 0.4471955895423889]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0959560871124268})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.48840582370758057})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.410099059343338})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36614108085632324})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3411242961883545})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3462255001068115})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3783515691757202})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.344129741191864})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9568, 'crossentropy': 0.3181405517578125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6188836097717285})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.44236862659454346})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3686015009880066})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3277701735496521})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32388341426849365})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2795075476169586})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.29286521673202515})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [42274, 13069, 27765, 459, 52955, 29377, 12999, 5904, 28525, 10624], 'labels': [5, 4, 4, -1, -1, 1, 9, 5, 2, -1], 'scores': [0.6810816526412964, 0.3956468105316162, 0.5767795443534851, 0.5532262325286865, 0.25151026248931885, 0.3302990794181824, 0.5014010071754456, 0.6354928612709045, 0.43675899505615234, 0.38214677572250366]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9887676239013672})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5012070536613464})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34150636196136475})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3388417065143585})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30547669529914856})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30632007122039795})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30491235852241516})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34565407037734985})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3429405689239502})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34017252922058105})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.276033740234375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.631610631942749})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.42380160093307495})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3794083297252655})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3273313045501709})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.2827567458152771})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2970812916755676})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2792278528213501})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.25312596559524536})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2571874260902405})
store['active_learning_steps'][35]['eval_training']['best_epoch']=8
store['active_learning_steps'][35]['acquisition']={'indices': [16469, 45982, 31677, 59335, 7924, 8552, 108, 35482, 49890, 23664], 'labels': [-1, 4, 0, 4, 8, 2, 0, 4, 5, 4], 'scores': [0.43670201301574707, 0.42997249960899353, 0.44734424352645874, 0.5986515283584595, 0.6544103622436523, 0.5882589221000671, 0.48046696186065674, 0.48888611793518066, 0.7989185452461243, 0.2890353798866272]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.8524558544158936})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45617252588272095})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3510735034942627})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33518311381340027})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.333859920501709})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35092899203300476})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3367231488227844})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2948020100593567})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30718711018562317})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3297441601753235})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32149097323417664})
store['active_learning_steps'][36]['training']['best_epoch']=8
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9673, 'crossentropy': 0.2754015625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6379985213279724})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4092409014701843})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33087050914764404})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.31081223487854004})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2663364112377167})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2681906521320343})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2455378621816635})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.25270748138427734})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.23370327055454254})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.22998398542404175})
store['active_learning_steps'][36]['eval_training']['best_epoch']=10
store['active_learning_steps'][36]['acquisition']={'indices': [42913, 39951, 8246, 41779, 55148, 27795, 13969, 56756, 39314, 36295], 'labels': [-1, -1, -1, 7, -1, 3, 3, -1, -1, -1], 'scores': [0.44142675399780273, 0.5934127569198608, 0.41864538192749023, 0.3158408999443054, 0.5219250321388245, 0.5060427188873291, 0.5959252715110779, 0.6831517815589905, 0.6775634288787842, 0.4698547124862671]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.1057732105255127})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4799915552139282})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.368452250957489})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3792060315608978})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3438435196876526})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33059871196746826})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33722957968711853})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3382070064544678})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3558414578437805})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9669, 'crossentropy': 0.2981087646484375}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6663634777069092})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.461298406124115})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.40095657110214233})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3283855617046356})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.31723713874816895})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2848728895187378})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.250509113073349})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.28431329131126404})
store['active_learning_steps'][37]['eval_training']['best_epoch']=7
store['active_learning_steps'][37]['acquisition']={'indices': [38980, 8865, 52661, 54513, 11195, 5325, 55419, 8439, 2761, 1392], 'labels': [6, 3, 3, -1, -1, -1, -1, -1, 8, -1], 'scores': [0.47134751081466675, 0.5301532745361328, 0.6215775609016418, 0.4755592346191406, 0.5187025666236877, 0.4574003219604492, 0.5580355525016785, 0.602428674697876, 0.6826613545417786, 0.42757856845855713]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.0091569423675537})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.47963154315948486})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34798523783683777})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2765585482120514})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2806640863418579})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3066004812717438})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28107380867004395})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.280227978515625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6466078162193298})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.44794249534606934})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.40283286571502686})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35342228412628174})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3231896162033081})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33469486236572266})
store['active_learning_steps'][38]['eval_training']['best_epoch']=5
store['active_learning_steps'][38]['acquisition']={'indices': [41790, 53658, 31512, 46623, 24062, 12297, 14394, 9508, 52694, 57061], 'labels': [-1, 2, 2, 4, 9, 9, 3, -1, 2, 0], 'scores': [0.3692131042480469, 0.3144640326499939, 0.3760756254196167, 0.5082018971443176, 0.5066146850585938, 0.49941378831863403, 0.5808669328689575, 0.38455289602279663, 0.5355270504951477, 0.4387233257293701]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.2474956512451172})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5551073551177979})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36367613077163696})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3074343204498291})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34350866079330444})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3072397708892822})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3462359309196472})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3017709255218506})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32558614015579224})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34433653950691223})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.37127065658569336})
store['active_learning_steps'][39]['training']['best_epoch']=8
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.2664062744140625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5992602109909058})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39861467480659485})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35466933250427246})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3247714340686798})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.2808613181114197})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2711651027202606})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.295401930809021})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26501381397247314})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23165325820446014})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.22423520684242249})
store['active_learning_steps'][39]['eval_training']['best_epoch']=10
store['active_learning_steps'][39]['acquisition']={'indices': [4611, 11768, 50051, 33556, 8883, 46906, 22344, 1321, 45991, 7638], 'labels': [-1, -1, -1, -1, 2, -1, -1, -1, -1, 8], 'scores': [0.6762694120407104, 0.6043654680252075, 0.6369476318359375, 0.37200987339019775, 0.49964773654937744, 0.5680592656135559, 0.6267637014389038, 0.6108959317207336, 0.3524043560028076, 0.5857718586921692]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1555588245391846})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.527263879776001})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38593611121177673})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3190614879131317})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34239476919174194})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31366512179374695})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3044256269931793})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32286950945854187})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3186179995536804})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34941917657852173})
store['active_learning_steps'][40]['training']['best_epoch']=7
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9664, 'crossentropy': 0.2746181640625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6418606042861938})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.41489458084106445})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3449171185493469})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31040722131729126})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2829313278198242})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27846965193748474})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25685787200927734})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2571142911911011})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23786404728889465})
store['active_learning_steps'][40]['eval_training']['best_epoch']=9
store['active_learning_steps'][40]['acquisition']={'indices': [36389, 597, 28518, 48945, 7528, 30448, 39660, 36593, 45439, 35304], 'labels': [-1, -1, 4, -1, 2, -1, -1, -1, 2, 4], 'scores': [0.45285797119140625, 0.3210242986679077, 0.6408136487007141, 0.5300582647323608, 0.39474377036094666, 0.5831078290939331, 0.5069709420204163, 0.41483378410339355, 0.325350284576416, 0.6322512626647949]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.0151751041412354})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4882768392562866})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3697829842567444})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3750263452529907})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31108325719833374})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34729087352752686})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3222612738609314})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32564252614974976})
store['active_learning_steps'][41]['training']['best_epoch']=5
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9674, 'crossentropy': 0.2911376708984375}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6530610918998718})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.43535614013671875})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3693500757217407})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33040064573287964})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.30845391750335693})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3079374432563782})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.2839297652244568})
store['active_learning_steps'][41]['eval_training']['best_epoch']=7
store['active_learning_steps'][41]['acquisition']={'indices': [43652, 9754, 5013, 39687, 36744, 7678, 41751, 20169, 17133, 9687], 'labels': [-1, -1, 2, -1, 1, 3, -1, 4, -1, 0], 'scores': [0.343941330909729, 0.3146934509277344, 0.6267468333244324, 0.46521782875061035, 0.5494858622550964, 0.5753432512283325, 0.37677502632141113, 0.7381967306137085, 0.4503130316734314, 0.5250255465507507]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0765514373779297})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5088266134262085})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3430454730987549})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30886319279670715})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32076287269592285})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32604730129241943})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.301417738199234})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3221864700317383})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2797524929046631})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3248330354690552})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3536991775035858})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34139102697372437})
store['active_learning_steps'][42]['training']['best_epoch']=9
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9675, 'crossentropy': 0.2758960205078125}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6664667129516602})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.43993204832077026})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.34947967529296875})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3399866223335266})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29003405570983887})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.27175039052963257})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.28243139386177063})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.263124942779541})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.257124662399292})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.24691587686538696})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25769299268722534})
store['active_learning_steps'][42]['eval_training']['best_epoch']=10
store['active_learning_steps'][42]['acquisition']={'indices': [25299, 47647, 1089, 33163, 10845, 51939, 8719, 39076, 15822, 46272], 'labels': [-1, -1, -1, -1, -1, -1, 8, -1, -1, -1], 'scores': [0.5740245580673218, 0.5973620414733887, 0.6069455742835999, 0.5287379026412964, 0.5293347835540771, 0.4982030987739563, 0.5230578184127808, 0.5690097808837891, 0.42380690574645996, 0.39047133922576904]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1409934759140015})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5273129940032959})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3755455017089844})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3212262988090515})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31348592042922974})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29771846532821655})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31763410568237305})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3279733657836914})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3505591154098511})
store['active_learning_steps'][43]['training']['best_epoch']=6
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9647, 'crossentropy': 0.284568994140625}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6211420297622681})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.45092397928237915})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3762359619140625})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.318095326423645})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.2804374098777771})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2824519872665405})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.28688687086105347})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.27423322200775146})
store['active_learning_steps'][43]['eval_training']['best_epoch']=8
store['active_learning_steps'][43]['acquisition']={'indices': [14805, 12905, 36840, 22632, 11578, 58071, 30642, 36646, 33849, 45732], 'labels': [6, 6, -1, 1, -1, -1, -1, -1, -1, -1], 'scores': [0.5691403150558472, 0.7260665893554688, 0.32805049419403076, 0.4458659291267395, 0.4573988914489746, 0.2864469289779663, 0.37774837017059326, 0.35425865650177, 0.42720890045166016, 0.3563119173049927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1778531074523926})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5181214809417725})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41044461727142334})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3538386821746826})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3634943962097168})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3387295603752136})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35393327474594116})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33448725938796997})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3652368187904358})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34544843435287476})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3698711097240448})
store['active_learning_steps'][44]['training']['best_epoch']=8
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9692, 'crossentropy': 0.28973759765625}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6502151489257812})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.43224936723709106})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38072991371154785})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.2951796352863312})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.28244566917419434})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.26978829503059387})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.27936315536499023})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2682303190231323})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2660176753997803})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.25934210419654846})
store['active_learning_steps'][44]['eval_training']['best_epoch']=10
store['active_learning_steps'][44]['acquisition']={'indices': [11616, 17849, 39846, 4073, 20967, 31754, 54628, 17728, 27956, 24521], 'labels': [7, 7, -1, -1, 2, 6, 4, 6, -1, -1], 'scores': [0.3787667751312256, 0.6186129450798035, 0.4067649841308594, 0.6055601835250854, 0.6265543699264526, 0.5223995447158813, 0.6475297212600708, 0.5437569618225098, 0.6082479953765869, 0.631231963634491]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.163072943687439})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5331869125366211})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4641302824020386})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37338393926620483})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3788347840309143})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3458938002586365})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36783844232559204})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34561651945114136})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35942891240119934})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35047289729118347})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33850744366645813})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38914135098457336})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3907427191734314})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32793503999710083})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39431995153427124})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36965787410736084})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4196174144744873})
store['active_learning_steps'][45]['training']['best_epoch']=14
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9648, 'crossentropy': 0.3353132080078125}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6850850582122803})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.429435670375824})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4095398783683777})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3248354196548462})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3140454888343811})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2980421185493469})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.28981760144233704})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.24618685245513916})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2407173216342926})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2460961490869522})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.26760339736938477})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2520196735858917})
store['active_learning_steps'][45]['eval_training']['best_epoch']=9
store['active_learning_steps'][45]['acquisition']={'indices': [47729, 53627, 31581, 39208, 9538, 4164, 10259, 25092, 28742, 34999], 'labels': [-1, -1, -1, 5, -1, 7, 0, 0, -1, -1], 'scores': [0.5329300761222839, 0.44305145740509033, 0.48011767864227295, 0.6999125480651855, 0.382798433303833, 0.6850077509880066, 0.4696311354637146, 0.45404624938964844, 0.6377063393592834, 0.4242638349533081]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.1139171123504639})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.47501373291015625})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35100626945495605})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29927802085876465})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31410980224609375})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3102354109287262})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31010621786117554})
store['active_learning_steps'][46]['training']['best_epoch']=4
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9619, 'crossentropy': 0.2988880126953125}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.683794379234314})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5032660961151123})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.38522762060165405})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.351557195186615})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.360282301902771})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.35713881254196167})
store['active_learning_steps'][46]['eval_training']['best_epoch']=4
store['active_learning_steps'][46]['acquisition']={'indices': [8206, 58986, 37809, 47221, 56255, 40135, 18487, 29814, 48393, 952], 'labels': [-1, -1, -1, -1, -1, 4, 4, -1, -1, -1], 'scores': [0.4082466959953308, 0.3236740827560425, 0.37245142459869385, 0.3863832950592041, 0.43138301372528076, 0.3928184509277344, 0.3799542188644409, 0.41968637704849243, 0.38449978828430176, 0.36607861518859863]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0902206897735596})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5280184745788574})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.39614707231521606})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34233033657073975})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32549357414245605})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2991331219673157})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3091745972633362})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3454228639602661})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32015472650527954})
store['active_learning_steps'][47]['training']['best_epoch']=6
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9667, 'crossentropy': 0.28174560546875}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.639443039894104})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4177258610725403})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3425513505935669})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.335038959980011})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3234908878803253})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30360734462738037})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2881944179534912})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3003244400024414})
store['active_learning_steps'][47]['eval_training']['best_epoch']=7
store['active_learning_steps'][47]['acquisition']={'indices': [36109, 49571, 19440, 21315, 36126, 57736, 59830, 59314, 58392, 48774], 'labels': [9, 7, -1, 8, 5, 8, 7, 9, -1, -1], 'scores': [0.5412636399269104, 0.5879052877426147, 0.3160274624824524, 0.5411279201507568, 0.5786386728286743, 0.38015228509902954, 0.6015077829360962, 0.5903277397155762, 0.434726357460022, 0.27094221115112305]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0748956203460693})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4963514804840088})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35022908449172974})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28202399611473083})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3188076913356781})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2962326109409332})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30017656087875366})
store['active_learning_steps'][48]['training']['best_epoch']=4
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.27610361328125}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6583421230316162})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.43178075551986694})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.37447571754455566})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35256636142730713})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.31483423709869385})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.31121161580085754})
store['active_learning_steps'][48]['eval_training']['best_epoch']=6
store['active_learning_steps'][48]['acquisition']={'indices': [31011, 15544, 28374, 52499, 39028, 14664, 56756, 19359, 52192, 50937], 'labels': [-1, -1, 3, -1, -1, 8, -1, -1, -1, -1], 'scores': [0.2104358673095703, 0.4297538995742798, 0.4175885319709778, 0.3542667627334595, 0.44172024726867676, 0.36236441135406494, 0.3768116235733032, 0.4192548990249634, 0.44338035583496094, 0.3337380886077881]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0767605304718018})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.46699219942092896})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.41494613885879517})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3372820317745209})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.31822657585144043})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32652825117111206})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.303263783454895})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3508867025375366})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33758413791656494})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3341776132583618})
store['active_learning_steps'][49]['training']['best_epoch']=7
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.25856923828125}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6288065910339355})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4403778612613678})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.38295257091522217})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3158267140388489})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.29599833488464355})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.29590511322021484})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.24367448687553406})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26800698041915894})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.28067001700401306})
store['active_learning_steps'][49]['eval_training']['best_epoch']=7
store['active_learning_steps'][49]['acquisition']={'indices': [34910, 43309, 23733, 13195, 17020, 5936, 50661, 23689, 9267, 6044], 'labels': [-1, -1, -1, -1, -1, 4, -1, -1, -1, 2], 'scores': [0.31378674507141113, 0.3901517391204834, 0.3804851770401001, 0.5928195118904114, 0.4252934455871582, 0.4678584337234497, 0.3508298397064209, 0.42741191387176514, 0.36699843406677246, 0.5861346125602722]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.13449227809906})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5202021598815918})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3608490824699402})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31819191575050354})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31689533591270447})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29802072048187256})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3075815439224243})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2968657612800598})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30929362773895264})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3352452516555786})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32129037380218506})
store['active_learning_steps'][50]['training']['best_epoch']=8
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9698, 'crossentropy': 0.27111640625}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.608995795249939})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41456717252731323})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3638229966163635})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3232082724571228})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.27513936161994934})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2674604058265686})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2728073000907898})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.25635191798210144})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.25095927715301514})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.23356913030147552})
store['active_learning_steps'][50]['eval_training']['best_epoch']=10
store['active_learning_steps'][50]['acquisition']={'indices': [50803, 32941, 9716, 52024, 46504, 28156, 5207, 27552, 32918, 14633], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 2, -1], 'scores': [0.4885392189025879, 0.5384185314178467, 0.42680442333221436, 0.4754596948623657, 0.393995463848114, 0.44429004192352295, 0.518560528755188, 0.48129284381866455, 0.5738312005996704, 0.4201161861419678]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.288932204246521})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5725457668304443})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3489168882369995})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38488703966140747})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3201519846916199})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31979086995124817})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3504232168197632})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3387734889984131})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31194621324539185})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3071996569633484})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3342326283454895})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3352653384208679})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27818599343299866})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3196946382522583})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33422237634658813})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3341081142425537})
store['active_learning_steps'][51]['training']['best_epoch']=13
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.97, 'crossentropy': 0.288371923828125}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5414621829986572})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.39836400747299194})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.31001415848731995})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.278022825717926})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2871871590614319})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.27299270033836365})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2502910792827606})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2762213349342346})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.22004401683807373})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.21800586581230164})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2075464129447937})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.21123135089874268})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.21983005106449127})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2081741988658905})
store['active_learning_steps'][51]['eval_training']['best_epoch']=11
store['active_learning_steps'][51]['acquisition']={'indices': [16756, 38660, 7406, 914, 15738, 53802, 22561, 30344, 43060, 8198], 'labels': [7, -1, 1, -1, -1, 5, 6, 2, -1, 7], 'scores': [0.7273687124252319, 0.4684702157974243, 0.5201665163040161, 0.5485440492630005, 0.6458123326301575, 0.5410065948963165, 0.709433913230896, 0.36981379985809326, 0.4042072296142578, 0.47856536507606506]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.2298760414123535})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5747445821762085})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3829127550125122})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3293290138244629})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3039713501930237})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31415319442749023})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27419018745422363})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.314730167388916})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2943647801876068})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32728874683380127})
store['active_learning_steps'][52]['training']['best_epoch']=7
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.2548506591796875}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6840173602104187})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.44724345207214355})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3539370596408844})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33136773109436035})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3135491907596588})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2648717164993286})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29478126764297485})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25113481283187866})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.25626620650291443})
store['active_learning_steps'][52]['eval_training']['best_epoch']=8
store['active_learning_steps'][52]['acquisition']={'indices': [15647, 29537, 8543, 35269, 8228, 9728, 27238, 8350, 57026, 27914], 'labels': [-1, -1, -1, -1, 3, -1, -1, -1, -1, -1], 'scores': [0.35729682445526123, 0.3844594955444336, 0.3640167713165283, 0.6206151843070984, 0.5556321144104004, 0.37009450793266296, 0.4649266004562378, 0.5039561986923218, 0.389975368976593, 0.48464012145996094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.109061598777771})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5125792026519775})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36334532499313354})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3458858132362366})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29043716192245483})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2754065692424774})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3214280605316162})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.316836416721344})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3247705101966858})
store['active_learning_steps'][53]['training']['best_epoch']=6
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9704, 'crossentropy': 0.2628697265625}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6405009627342224})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45876479148864746})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39099735021591187})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3293910026550293})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2914060354232788})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2833554148674011})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2732040584087372})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2859341502189636})
store['active_learning_steps'][53]['eval_training']['best_epoch']=7
store['active_learning_steps'][53]['acquisition']={'indices': [29936, 21601, 340, 19774, 16606, 24929, 54931, 27790, 10053, 9567], 'labels': [-1, 1, 7, -1, -1, -1, -1, -1, -1, 8], 'scores': [0.47546422481536865, 0.5117934942245483, 0.5131312608718872, 0.31589066982269287, 0.4639090299606323, 0.3389526605606079, 0.4613065719604492, 0.33661937713623047, 0.354608952999115, 0.526697039604187]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 1.046622395515442})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4629877805709839})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3253970742225647})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3108958601951599})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28839486837387085})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2818986773490906})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30252009630203247})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3403327465057373})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2909170389175415})
store['active_learning_steps'][54]['training']['best_epoch']=6
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.969, 'crossentropy': 0.24426416015625}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6167469024658203})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38694241642951965})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3253779411315918})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3069865107536316})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29967421293258667})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2786523401737213})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2503120005130768})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23852986097335815})
store['active_learning_steps'][54]['eval_training']['best_epoch']=8
store['active_learning_steps'][54]['acquisition']={'indices': [31366, 54215, 13388, 22683, 34608, 47475, 59159, 57018, 41426, 17365], 'labels': [1, -1, 3, -1, 9, 5, -1, 9, 4, 0], 'scores': [0.411889910697937, 0.34747380018234253, 0.4690571427345276, 0.3288313150405884, 0.5318959355354309, 0.49542444944381714, 0.3963735103607178, 0.5176079869270325, 0.5952404737472534, 0.5856246948242188]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.2465462684631348})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5080996155738831})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35158878564834595})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3148930072784424})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2830544412136078})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29515719413757324})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2807389497756958})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3134617805480957})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3025853633880615})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27022531628608704})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31034034490585327})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33831754326820374})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3062518239021301})
store['active_learning_steps'][55]['training']['best_epoch']=10
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9713, 'crossentropy': 0.2666110595703125}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6498693227767944})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.37952226400375366})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3448624908924103})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27135220170021057})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27214330434799194})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.25469711422920227})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2590258717536926})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.23957978188991547})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2288743555545807})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.22282692790031433})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2167959362268448})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.22310584783554077})
store['active_learning_steps'][55]['eval_training']['best_epoch']=11
store['active_learning_steps'][55]['acquisition']={'indices': [59701, 21150, 12689, 29361, 40345, 3356, 48561, 17708, 46297, 45056], 'labels': [5, -1, -1, 5, -1, -1, -1, -1, -1, 8], 'scores': [0.45766061544418335, 0.4322021007537842, 0.5335256457328796, 0.5648210048675537, 0.5726274251937866, 0.4464881420135498, 0.4194127321243286, 0.3699462413787842, 0.34658920764923096, 0.7192406058311462]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.043548822402954})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4959300756454468})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34292978048324585})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3222823739051819})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30631256103515625})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3075158894062042})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29317158460617065})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28748685121536255})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2985767424106598})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3032238483428955})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2801935076713562})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29614073038101196})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2917633652687073})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31856828927993774})
store['active_learning_steps'][56]['training']['best_epoch']=11
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9701, 'crossentropy': 0.2658590576171875}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6461750268936157})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.40984126925468445})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.37579190731048584})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3052370548248291})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2644980549812317})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2655947804450989})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2401619553565979})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2304961383342743})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.209687739610672})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.22549378871917725})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2187330424785614})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2102959156036377})
store['active_learning_steps'][56]['eval_training']['best_epoch']=9
store['active_learning_steps'][56]['acquisition']={'indices': [45692, 25800, 55493, 18920, 12171, 44078, 56624, 37160, 54598, 15694], 'labels': [8, 1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4825758934020996, 0.39488330483436584, 0.4560530185699463, 0.47105205059051514, 0.498923659324646, 0.5093849897384644, 0.42648935317993164, 0.45179325342178345, 0.4149000644683838, 0.5234545469284058]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.1690328121185303})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5800796151161194})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3981333076953888})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2878786325454712})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29807421565055847})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.299946665763855})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.313234806060791})
store['active_learning_steps'][57]['training']['best_epoch']=4
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9673, 'crossentropy': 0.2980635498046875}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7259992361068726})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4979989528656006})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.402851939201355})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39100635051727295})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3644217252731323})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.29383665323257446})
store['active_learning_steps'][57]['eval_training']['best_epoch']=6
store['active_learning_steps'][57]['acquisition']={'indices': [8213, 15408, 15929, 20002, 55739, 22320, 45048, 21377, 5842, 9126], 'labels': [-1, -1, -1, 7, 5, 8, 4, 9, 1, 6], 'scores': [0.2550475597381592, 0.2762117385864258, 0.3281148672103882, 0.48459112644195557, 0.4250582456588745, 0.4700341820716858, 0.4698811173439026, 0.3924156427383423, 0.49450570344924927, 0.40422093868255615]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.2297203540802002})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5636409521102905})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3501829504966736})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35396212339401245})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29724785685539246})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2841930389404297})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3144455850124359})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25262224674224854})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3144426941871643})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29296913743019104})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2690160274505615})
store['active_learning_steps'][58]['training']['best_epoch']=8
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.266774560546875}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7521790266036987})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4581145644187927})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.37757670879364014})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3394683599472046})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2939869463443756})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2783837914466858})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24255511164665222})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25414690375328064})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24297139048576355})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.21982182562351227})
store['active_learning_steps'][58]['eval_training']['best_epoch']=10
store['active_learning_steps'][58]['acquisition']={'indices': [56163, 23983, 846, 36642, 53960, 57469, 6902, 37072, 52605, 1033], 'labels': [-1, -1, 6, 5, -1, -1, -1, -1, -1, 2], 'scores': [0.6563577055931091, 0.4200718402862549, 0.4792470335960388, 0.3869219422340393, 0.3863084316253662, 0.6393239498138428, 0.42560499906539917, 0.3743598461151123, 0.4708031415939331, 0.4276161193847656]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 1.1153874397277832})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.526273787021637})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3280878961086273})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31817302107810974})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3261873722076416})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28353989124298096})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.291387140750885})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28009232878685})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2766069173812866})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27925848960876465})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27513882517814636})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27709051966667175})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2531123757362366})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28789061307907104})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3027518689632416})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30422425270080566})
store['active_learning_steps'][59]['training']['best_epoch']=13
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9766, 'crossentropy': 0.2434947265625}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6934806108474731})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.41446125507354736})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3294955790042877})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.33982211351394653})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2509501874446869})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.2774728238582611})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25490742921829224})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.24040371179580688})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2241368591785431})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2406119853258133})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.22663725912570953})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2078833281993866})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.21376147866249084})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.21247316896915436})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.21383418142795563})
store['active_learning_steps'][59]['eval_training']['best_epoch']=12
store['active_learning_steps'][59]['acquisition']={'indices': [16493, 44292, 26472, 38967, 17386, 50412, 54422, 50461, 40643, 40027], 'labels': [-1, -1, -1, -1, -1, -1, -1, 7, -1, -1], 'scores': [0.38975322246551514, 0.5603162050247192, 0.7759349942207336, 0.48334139585494995, 0.6077278852462769, 0.4767998456954956, 0.3673628568649292, 0.7150377631187439, 0.5663957595825195, 0.4671297073364258]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.0625255107879639})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5605657696723938})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4140821695327759})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32436299324035645})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29796361923217773})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2783597707748413})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34543749690055847})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3184387683868408})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2790084779262543})
store['active_learning_steps'][60]['training']['best_epoch']=6
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9658, 'crossentropy': 0.2913116455078125}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6582551002502441})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4649222791194916})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36812907457351685})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3221818506717682})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3117057681083679})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30820798873901367})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2958548665046692})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28273123502731323})
store['active_learning_steps'][60]['eval_training']['best_epoch']=8
store['active_learning_steps'][60]['acquisition']={'indices': [10256, 58760, 47479, 21056, 42584, 55778, 13831, 41738, 5938, 3694], 'labels': [-1, -1, 0, -1, -1, -1, 3, 9, -1, -1], 'scores': [0.45704591274261475, 0.4184969663619995, 0.5016390681266785, 0.5013904571533203, 0.387969970703125, 0.6845706701278687, 0.690619707107544, 0.6277625560760498, 0.46708905696868896, 0.41212427616119385]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.231858253479004})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5702991485595703})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3899019956588745})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33532214164733887})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32217490673065186})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29468727111816406})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27877581119537354})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2864137291908264})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28185662627220154})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3246081471443176})
store['active_learning_steps'][61]['training']['best_epoch']=7
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9696, 'crossentropy': 0.2802315185546875}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6293613910675049})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.40408286452293396})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3500208258628845})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3044218420982361})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2931225895881653})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2786696255207062})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2902517318725586})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26243335008621216})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23842956125736237})
store['active_learning_steps'][61]['eval_training']['best_epoch']=9
store['active_learning_steps'][61]['acquisition']={'indices': [7134, 7337, 15416, 16152, 59294, 50661, 19837, 29978, 37368, 49487], 'labels': [-1, -1, -1, -1, 8, -1, -1, -1, -1, 8], 'scores': [0.5461599826812744, 0.41567742824554443, 0.4036135673522949, 0.41794353723526, 0.6059871912002563, 0.4281405210494995, 0.5670441389083862, 0.43743419647216797, 0.5356099605560303, 0.34290003776550293]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.1673319339752197})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5055344104766846})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38754481077194214})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2948007881641388})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26262083649635315})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28258076310157776})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28568029403686523})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2771304249763489})
store['active_learning_steps'][62]['training']['best_epoch']=5
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.258795654296875}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6170011758804321})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.41755378246307373})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36259663105010986})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3083330988883972})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3424025774002075})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2778280973434448})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27811649441719055})
store['active_learning_steps'][62]['eval_training']['best_epoch']=6
store['active_learning_steps'][62]['acquisition']={'indices': [13834, 54560, 45381, 4369, 44985, 14977, 36704, 50517, 37469, 23958], 'labels': [-1, -1, -1, -1, -1, -1, 2, -1, 2, -1], 'scores': [0.4178042411804199, 0.3348926305770874, 0.3776082396507263, 0.4819990396499634, 0.5145491361618042, 0.3319387435913086, 0.2852597236633301, 0.49645864963531494, 0.5209421515464783, 0.4929289221763611]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.231536865234375})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.521129310131073})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34182918071746826})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3183927536010742})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27108877897262573})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29256579279899597})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28837597370147705})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2867307662963867})
store['active_learning_steps'][63]['training']['best_epoch']=5
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9728, 'crossentropy': 0.2613847412109375}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7048727869987488})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44931280612945557})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40088585019111633})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3455524742603302})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36030417680740356})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3027228116989136})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3349730372428894})
store['active_learning_steps'][63]['eval_training']['best_epoch']=6
store['active_learning_steps'][63]['acquisition']={'indices': [39347, 5868, 10021, 44171, 26472, 23886, 36008, 54981, 55788, 47927], 'labels': [-1, -1, 8, -1, -1, 1, 8, 2, -1, -1], 'scores': [0.36818772554397583, 0.27203476428985596, 0.34904563426971436, 0.29209017753601074, 0.4414840340614319, 0.6046814918518066, 0.3333846926689148, 0.4890267848968506, 0.40255653858184814, 0.5361754894256592]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.1086193323135376})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5004147291183472})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3775985836982727})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30904483795166016})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2746243476867676})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28390124440193176})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2865734398365021})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.259579598903656})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25655415654182434})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28026390075683594})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24276262521743774})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25670963525772095})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2662696838378906})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3104183077812195})
store['active_learning_steps'][64]['training']['best_epoch']=11
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9728, 'crossentropy': 0.253147900390625}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6493290662765503})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44957512617111206})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32659387588500977})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30657222867012024})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2984161376953125})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.25877645611763})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2656567394733429})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.23084238171577454})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23431891202926636})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.22087246179580688})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.21837428212165833})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.22315575182437897})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2156633883714676})
store['active_learning_steps'][64]['eval_training']['best_epoch']=13
store['active_learning_steps'][64]['acquisition']={'indices': [51863, 39685, 37237, 29773, 38223, 7483, 3850, 36981, 31349, 56561], 'labels': [9, -1, -1, -1, -1, -1, -1, -1, 3, -1], 'scores': [0.7450676560401917, 0.3474999666213989, 0.405228853225708, 0.4019315242767334, 0.6460939049720764, 0.40667033195495605, 0.46261656284332275, 0.4865812063217163, 0.5319570302963257, 0.46599966287612915]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.246152639389038})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5503768920898438})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.42289382219314575})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3074900209903717})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30992308259010315})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3042411208152771})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29639479517936707})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29154667258262634})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32495296001434326})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2993263602256775})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32460594177246094})
store['active_learning_steps'][65]['training']['best_epoch']=8
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9693, 'crossentropy': 0.2754215576171875}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6216660141944885})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4027443826198578})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.34961745142936707})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2984696924686432})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2917666435241699})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2387230098247528})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2822203040122986})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23740984499454498})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2598041892051697})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2349046766757965})
store['active_learning_steps'][65]['eval_training']['best_epoch']=10
store['active_learning_steps'][65]['acquisition']={'indices': [36355, 10012, 30297, 50263, 34962, 26008, 7452, 50115, 19110, 3390], 'labels': [-1, 8, -1, -1, -1, -1, 6, -1, -1, -1], 'scores': [0.4428565502166748, 0.49882668256759644, 0.45822417736053467, 0.3282310962677002, 0.5305383205413818, 0.5479943752288818, 0.3804464340209961, 0.560827374458313, 0.49874448776245117, 0.55399489402771]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.27528977394104})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5928175449371338})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.36647284030914307})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3072112798690796})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2608269453048706})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2607545852661133})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27036768198013306})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27911052107810974})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2506101727485657})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26915332674980164})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2767462134361267})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27981096506118774})
store['active_learning_steps'][66]['training']['best_epoch']=9
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9731, 'crossentropy': 0.2286619384765625}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6927316188812256})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4109571576118469})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35454827547073364})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2993968427181244})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2815679907798767})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2576706111431122})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2374066561460495})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.21561244130134583})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.24358835816383362})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.20687806606292725})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.19892780482769012})
store['active_learning_steps'][66]['eval_training']['best_epoch']=11
store['active_learning_steps'][66]['acquisition']={'indices': [31635, 36013, 42843, 23518, 8707, 35453, 28914, 56608, 29093, 9191], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4506984353065491, 0.5595382452011108, 0.5842084884643555, 0.521261990070343, 0.4519966244697571, 0.5600274205207825, 0.3637073040008545, 0.4022824764251709, 0.6382256150245667, 0.43771183490753174]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.086171269416809})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5664972066879272})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3571251630783081})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32274743914604187})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2700873613357544})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27271753549575806})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2742760479450226})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2694878578186035})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26055487990379333})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2799679934978485})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2855404019355774})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.27764028310775757})
store['active_learning_steps'][67]['training']['best_epoch']=9
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9693, 'crossentropy': 0.2690274169921875}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6648378372192383})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.41022437810897827})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3419187664985657})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31194353103637695})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3124969005584717})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2640816569328308})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.24880489706993103})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.23977945744991302})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24820271134376526})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24068470299243927})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2132529318332672})
store['active_learning_steps'][67]['eval_training']['best_epoch']=11
store['active_learning_steps'][67]['acquisition']={'indices': [32350, 31446, 29360, 10984, 11470, 48192, 46473, 52670, 30222, 59747], 'labels': [-1, -1, 8, 3, -1, -1, -1, -1, -1, 5], 'scores': [0.48198825120925903, 0.3623344898223877, 0.5462923049926758, 0.4718577265739441, 0.5417965054512024, 0.4878758192062378, 0.38308095932006836, 0.38447511196136475, 0.4569742679595947, 0.5247810482978821]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1653954982757568})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.5518271923065186})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.38557204604148865})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3248652517795563})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32104626297950745})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25684234499931335})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2672308683395386})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26452431082725525})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2952835261821747})
store['active_learning_steps'][68]['training']['best_epoch']=6
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9725, 'crossentropy': 0.2607293212890625}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6577984690666199})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.39133042097091675})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35036325454711914})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33761367201805115})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2838360369205475})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3058320879936218})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2558749318122864})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27329176664352417})
store['active_learning_steps'][68]['eval_training']['best_epoch']=7
store['active_learning_steps'][68]['acquisition']={'indices': [25514, 26900, 43123, 51236, 33451, 55696, 20911, 34133, 47153, 27621], 'labels': [-1, 6, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4352412819862366, 0.49835342168807983, 0.3857302665710449, 0.5748847126960754, 0.5048823356628418, 0.31879329681396484, 0.39626824855804443, 0.526077389717102, 0.36608994007110596, 0.3224477767944336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.210822343826294})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6141687631607056})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3866203725337982})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2948446273803711})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29248684644699097})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2973949909210205})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29608094692230225})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29122915863990784})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30546072125434875})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28404951095581055})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2944941520690918})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2981310486793518})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.306060791015625})
store['active_learning_steps'][69]['training']['best_epoch']=10
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9706, 'crossentropy': 0.285858056640625}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6823697090148926})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.395610511302948})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3342926502227783})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2854255139827728})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26177504658699036})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27523159980773926})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27724742889404297})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2585671544075012})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24151328206062317})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.22206619381904602})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2328571379184723})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26274725794792175})
store['active_learning_steps'][69]['eval_training']['best_epoch']=10
store['active_learning_steps'][69]['acquisition']={'indices': [9628, 15446, 50253, 21610, 49010, 47363, 49354, 54391, 562, 3839], 'labels': [-1, -1, -1, -1, 9, -1, 0, -1, -1, -1], 'scores': [0.4578186273574829, 0.5863491892814636, 0.36812686920166016, 0.4778794050216675, 0.4710126519203186, 0.5150699615478516, 0.4162833094596863, 0.4147709608078003, 0.5000299215316772, 0.5985755920410156]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.110141396522522})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5542236566543579})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38681063055992126})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.31808340549468994})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29341545701026917})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2889920473098755})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32141679525375366})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2683366537094116})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26574036478996277})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.269829660654068})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30455976724624634})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30051183700561523})
store['active_learning_steps'][70]['training']['best_epoch']=9
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9734, 'crossentropy': 0.2483494873046875}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6762750148773193})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4392601251602173})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3566593825817108})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32461297512054443})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32988232374191284})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2731592059135437})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2560611665248871})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27180537581443787})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2564926743507385})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2475656270980835})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2206910252571106})
store['active_learning_steps'][70]['eval_training']['best_epoch']=11
store['active_learning_steps'][70]['acquisition']={'indices': [51826, 10962, 47527, 6591, 11044, 48735, 45695, 27112, 14680, 1434], 'labels': [-1, -1, -1, -1, 4, -1, -1, -1, -1, -1], 'scores': [0.6829397678375244, 0.44817304611206055, 0.3964484930038452, 0.5266432762145996, 0.4812403917312622, 0.7110376954078674, 0.50129234790802, 0.30778729915618896, 0.2920438051223755, 0.5886908769607544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 1.1651735305786133})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5053964853286743})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3866937458515167})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30276942253112793})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25457727909088135})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.26384711265563965})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24917122721672058})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25509583950042725})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2632511258125305})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23548239469528198})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2596629858016968})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2843705415725708})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2598932385444641})
store['active_learning_steps'][71]['training']['best_epoch']=10
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9733, 'crossentropy': 0.2545674072265625}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6784436106681824})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.43818342685699463})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.34736794233322144})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.29251301288604736})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2866755723953247})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2325441837310791})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.258287250995636})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2610975205898285})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.23497618734836578})
store['active_learning_steps'][71]['eval_training']['best_epoch']=6
store['active_learning_steps'][71]['acquisition']={'indices': [14002, 51490, 38479, 16150, 29321, 23001, 10477, 36926, 51006, 3290], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 4], 'scores': [0.49373626708984375, 0.5100860595703125, 0.5430752038955688, 0.4661659002304077, 0.3364819288253784, 0.5210769176483154, 0.589562177658081, 0.49994659423828125, 0.4220871925354004, 0.5341043472290039]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.206403374671936})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.46125033497810364})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3993380069732666})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30712032318115234})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2576068341732025})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26729393005371094})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2547570466995239})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2835119664669037})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27682894468307495})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2664267122745514})
store['active_learning_steps'][72]['training']['best_epoch']=7
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.2404648681640625}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6912071704864502})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.45581650733947754})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35259145498275757})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.32646995782852173})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31367576122283936})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27139437198638916})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2744341790676117})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25956955552101135})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2300606071949005})
store['active_learning_steps'][72]['eval_training']['best_epoch']=9
store['active_learning_steps'][72]['acquisition']={'indices': [9376, 25418, 6366, 59919, 24460, 10552, 8264, 21000, 39642, 26978], 'labels': [-1, 8, -1, 1, -1, -1, -1, -1, -1, -1], 'scores': [0.39185822010040283, 0.5907979607582092, 0.42436373233795166, 0.5017654299736023, 0.5379172563552856, 0.2681763172149658, 0.4323502779006958, 0.41614532470703125, 0.4468107223510742, 0.48494625091552734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.1067109107971191})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.48168590664863586})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35592398047447205})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28783535957336426})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2687135934829712})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2587915062904358})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2628941833972931})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2518754005432129})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25362151861190796})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25236696004867554})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2736305594444275})
store['active_learning_steps'][73]['training']['best_epoch']=8
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9756, 'crossentropy': 0.2363070068359375}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7084625959396362})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.42639070749282837})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3560216426849365})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33797377347946167})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27388888597488403})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3012440800666809})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.24954970180988312})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26939815282821655})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23956042528152466})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.22848477959632874})
store['active_learning_steps'][73]['eval_training']['best_epoch']=10
store['active_learning_steps'][73]['acquisition']={'indices': [37818, 44364, 33614, 4533, 7784, 16853, 59043, 45426, 40319, 25897], 'labels': [-1, 2, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.33308619260787964, 0.5492818355560303, 0.44991421699523926, 0.41446763277053833, 0.5440323352813721, 0.4783363938331604, 0.29095780849456787, 0.5408053398132324, 0.5590935945510864, 0.6091005802154541]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0522325038909912})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5514868497848511})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35530734062194824})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3370981216430664})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26653969287872314})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2676118016242981})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.299677312374115})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2599380314350128})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2662302851676941})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2677069306373596})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25977376103401184})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32104384899139404})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2857125699520111})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3190254867076874})
store['active_learning_steps'][74]['training']['best_epoch']=11
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9731, 'crossentropy': 0.26605361328125}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7024632692337036})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.456673800945282})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.31496214866638184})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30082958936691284})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28166627883911133})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2394544780254364})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24173426628112793})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24422287940979004})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2577500343322754})
store['active_learning_steps'][74]['eval_training']['best_epoch']=6
store['active_learning_steps'][74]['acquisition']={'indices': [7759, 29875, 56414, 19108, 27427, 47645, 25892, 49624, 8854, 13455], 'labels': [-1, -1, -1, -1, -1, -1, -1, 6, -1, -1], 'scores': [0.6577082276344299, 0.4681817293167114, 0.6611754894256592, 0.40686023235321045, 0.4585336446762085, 0.527895450592041, 0.6670788526535034, 0.6691854596138, 0.45896679162979126, 0.59549480676651]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.2714622020721436})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5939465165138245})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3604361414909363})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3219815492630005})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28753286600112915})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2601262331008911})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2643614411354065})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26242390275001526})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2588326632976532})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2844727039337158})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2643562853336334})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25330469012260437})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28689044713974})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3006572723388672})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30249106884002686})
store['active_learning_steps'][75]['training']['best_epoch']=12
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9711, 'crossentropy': 0.262848388671875}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.679354190826416})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3953131437301636})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.34411048889160156})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28300732374191284})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23865443468093872})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.22836732864379883})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2277998924255371})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26134568452835083})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2286202609539032})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.21451780200004578})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.196958988904953})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2050580084323883})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.21543975174427032})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.19891925156116486})
store['active_learning_steps'][75]['eval_training']['best_epoch']=11
store['active_learning_steps'][75]['acquisition']={'indices': [3058, 58529, 16939, 53813, 37908, 44344, 26472, 42920, 51040, 58390], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.6110022068023682, 0.44218015670776367, 0.4094698429107666, 0.49596309661865234, 0.4323766231536865, 0.4385896921157837, 0.7272305488586426, 0.8204325437545776, 0.5414878129959106, 0.5170871019363403]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.3298105001449585})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5973017811775208})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3742355704307556})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31272998452186584})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30064427852630615})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27489978075027466})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2855905294418335})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2494518756866455})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28352591395378113})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27036482095718384})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2898326516151428})
store['active_learning_steps'][76]['training']['best_epoch']=8
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9697, 'crossentropy': 0.26381484375}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6645328998565674})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4407133162021637})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3922138214111328})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3333682119846344})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27180707454681396})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25716885924339294})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2681438624858856})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2629740834236145})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25211888551712036})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24193421006202698})
store['active_learning_steps'][76]['eval_training']['best_epoch']=10
store['active_learning_steps'][76]['acquisition']={'indices': [38060, 57718, 52942, 53910, 43544, 36671, 4964, 54647, 48010, 34909], 'labels': [-1, 7, -1, 2, 9, -1, 7, 9, 7, -1], 'scores': [0.4366738796234131, 0.6136288642883301, 0.5444381833076477, 0.405703604221344, 0.5047758221626282, 0.3286792039871216, 0.5913536548614502, 0.4232620596885681, 0.5226597785949707, 0.4143490791320801]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.234392762184143})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5608363151550293})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40649962425231934})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32074904441833496})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30702435970306396})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29359379410743713})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27931395173072815})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2949627637863159})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27332112193107605})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.300991415977478})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2706157863140106})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27925723791122437})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2998390793800354})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28683021664619446})
store['active_learning_steps'][77]['training']['best_epoch']=11
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.261333935546875}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7020829916000366})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4516751170158386})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.36102497577667236})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28882527351379395})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3056821823120117})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.279035747051239})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2617040276527405})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27665868401527405})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26421940326690674})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2303173542022705})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.22605478763580322})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24394072592258453})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26000291109085083})
store['active_learning_steps'][77]['eval_training']['best_epoch']=11
store['active_learning_steps'][77]['acquisition']={'indices': [13506, 19136, 21611, 29593, 47886, 19245, 55383, 30723, 15080, 20795], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4700208306312561, 0.5312808752059937, 0.2996253967285156, 0.3711695671081543, 0.4812544584274292, 0.5291917324066162, 0.4819587469100952, 0.6193810701370239, 0.5235645771026611, 0.4667009711265564]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.2232304811477661})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.6018285751342773})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3903976082801819})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31381988525390625})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.28246957063674927})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2742077708244324})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2602142095565796})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2772204279899597})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25397390127182007})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2425214946269989})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24637579917907715})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28422999382019043})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28731459379196167})
store['active_learning_steps'][78]['training']['best_epoch']=10
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9748, 'crossentropy': 0.2312691162109375}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6608721613883972})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.42326104640960693})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3328646421432495})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28882813453674316})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2597867250442505})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.245616614818573})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24830208718776703})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.23015975952148438})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.21912342309951782})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.21903884410858154})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.20532506704330444})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.20417079329490662})
store['active_learning_steps'][78]['eval_training']['best_epoch']=12
store['active_learning_steps'][78]['acquisition']={'indices': [868, 3694, 23043, 914, 53089, 52971, 13342, 13350, 33628, 5488], 'labels': [-1, -1, -1, -1, -1, 2, -1, 4, -1, -1], 'scores': [0.4412562847137451, 0.4394029974937439, 0.3249574899673462, 0.5522551536560059, 0.3529934883117676, 0.6602107286453247, 0.48014676570892334, 0.5417028665542603, 0.5063285827636719, 0.3927062749862671]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.2394365072250366})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.575607419013977})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4035019278526306})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3022635579109192})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28508180379867554})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2716265320777893})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27992022037506104})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31477290391921997})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26209181547164917})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2859651446342468})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27570223808288574})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2619709372520447})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28361836075782776})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26552754640579224})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2973088026046753})
store['active_learning_steps'][79]['training']['best_epoch']=12
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9735, 'crossentropy': 0.2609041748046875}
store['active_learning_steps'][79]['eval_training']={}
store['active_learning_steps'][79]['eval_training']['epochs']=[]
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7599647045135498})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.41137808561325073})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3655523657798767})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32181277871131897})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.26034078001976013})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2557092010974884})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24205747246742249})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25138211250305176})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.22082100808620453})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.21375876665115356})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.21362021565437317})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.20718275010585785})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.21655240654945374})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2070235013961792})
store['active_learning_steps'][79]['eval_training']['best_epoch']=14
store['active_learning_steps'][79]['acquisition']={'indices': [54065, 47909, 56410, 47590, 45965, 13195, 21537, 33560, 17655, 47831], 'labels': [-1, -1, -1, 2, -1, -1, -1, -1, -1, -1], 'scores': [0.6180675029754639, 0.39055854082107544, 0.750496506690979, 0.5489860475063324, 0.5667258501052856, 0.5788880586624146, 0.6497355699539185, 0.58818519115448, 0.5318827629089355, 0.46479254961013794]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.1372737884521484})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5109459161758423})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33524444699287415})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31022509932518005})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2863399386405945})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2863624095916748})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2806492745876312})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2572275400161743})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2658439874649048})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2767810523509979})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2708907425403595})
store['active_learning_steps'][80]['training']['best_epoch']=8
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9731, 'crossentropy': 0.239939013671875}
store['active_learning_steps'][80]['eval_training']={}
store['active_learning_steps'][80]['eval_training']['epochs']=[]
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6441385746002197})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41617846488952637})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3561539947986603})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.325946569442749})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2857029438018799})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27279824018478394})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2598438560962677})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24875271320343018})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.242862731218338})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.22388949990272522})
store['active_learning_steps'][80]['eval_training']['best_epoch']=10
store['active_learning_steps'][80]['acquisition']={'indices': [45723, 44475, 54140, 9758, 39814, 27714, 42337, 51234, 4276, 14757], 'labels': [-1, -1, -1, -1, -1, -1, 5, 5, 3, -1], 'scores': [0.23506653308868408, 0.37800776958465576, 0.39982283115386963, 0.45488494634628296, 0.30614030361175537, 0.3725101947784424, 0.6866359710693359, 0.3892444372177124, 0.3649105429649353, 0.49709558486938477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.1176886558532715})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5387134552001953})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35923516750335693})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31354182958602905})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2981688976287842})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2686612010002136})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2754672169685364})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2892085909843445})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2863345742225647})
store['active_learning_steps'][81]['training']['best_epoch']=6
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9724, 'crossentropy': 0.2551157958984375}
store['active_learning_steps'][81]['eval_training']={}
store['active_learning_steps'][81]['eval_training']['epochs']=[]
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6604621410369873})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.45519137382507324})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.38123804330825806})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3704128861427307})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.318847119808197})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27060651779174805})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2844712734222412})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2450939416885376})
store['active_learning_steps'][81]['eval_training']['best_epoch']=8
store['active_learning_steps'][81]['acquisition']={'indices': [44914, 36509, 4909, 42646, 1799, 24478, 57956, 6220, 2064, 2751], 'labels': [-1, -1, 8, -1, -1, -1, 2, -1, 7, -1], 'scores': [0.22121655941009521, 0.3759208917617798, 0.37520676851272583, 0.3465101718902588, 0.3115878105163574, 0.36649060249328613, 0.46125489473342896, 0.3875066041946411, 0.4117750823497772, 0.36381590366363525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1977226734161377})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5646153092384338})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3759598433971405})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33080941438674927})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.299720823764801})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2757623493671417})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.262610524892807})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26273325085639954})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3001604676246643})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3116278648376465})
store['active_learning_steps'][82]['training']['best_epoch']=7
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.25268466796875}
store['active_learning_steps'][82]['eval_training']={}
store['active_learning_steps'][82]['eval_training']['epochs']=[]
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7319573163986206})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.48522108793258667})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36956948041915894})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2846195101737976})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2775954008102417})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30594098567962646})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2696796655654907})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2650420069694519})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25082629919052124})
store['active_learning_steps'][82]['eval_training']['best_epoch']=9
store['active_learning_steps'][82]['acquisition']={'indices': [20522, 33933, 13023, 23736, 31404, 51266, 1033, 45424, 26240, 192], 'labels': [-1, -1, -1, -1, 3, -1, -1, 4, 5, -1], 'scores': [0.40260565280914307, 0.43513941764831543, 0.3696213960647583, 0.46945738792419434, 0.476310670375824, 0.43114471435546875, 0.226837158203125, 0.7382318377494812, 0.3800486922264099, 0.4399659037590027]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.1446536779403687})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4993916153907776})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3807922601699829})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27297642827033997})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2851017117500305})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2837694585323334})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.271403431892395})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27410006523132324})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2724018394947052})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27957695722579956})
store['active_learning_steps'][83]['training']['best_epoch']=7
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9689, 'crossentropy': 0.2462584228515625}
store['active_learning_steps'][83]['eval_training']={}
store['active_learning_steps'][83]['eval_training']['epochs']=[]
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6605494022369385})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4625876545906067})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34611546993255615})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30626577138900757})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3018662929534912})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27810025215148926})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2849576771259308})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.24623289704322815})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26682156324386597})
store['active_learning_steps'][83]['eval_training']['best_epoch']=8
store['active_learning_steps'][83]['acquisition']={'indices': [52673, 39074, 54770, 13013, 57442, 28076, 49947, 53777, 46547, 48863], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4218429923057556, 0.5474791526794434, 0.5529852509498596, 0.4202078580856323, 0.3198779821395874, 0.5767741799354553, 0.41831910610198975, 0.5034803152084351, 0.5225551128387451, 0.5385733246803284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.088699460029602})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5486270189285278})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3912885785102844})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3040931224822998})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28122037649154663})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2886631190776825})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26643049716949463})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23398026823997498})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.302456259727478})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2521436810493469})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2687969207763672})
store['active_learning_steps'][84]['training']['best_epoch']=8
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9712, 'crossentropy': 0.2461482666015625}
store['active_learning_steps'][84]['eval_training']={}
store['active_learning_steps'][84]['eval_training']['epochs']=[]
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6711509227752686})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4376988410949707})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3343185484409332})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3178692162036896})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25629550218582153})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.25573715567588806})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2285771369934082})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26737329363822937})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2540472745895386})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.24032661318778992})
store['active_learning_steps'][84]['eval_training']['best_epoch']=7
store['active_learning_steps'][84]['acquisition']={'indices': [27778, 12855, 25476, 4302, 30157, 27716, 14588, 4834, 32583, 56212], 'labels': [-1, -1, -1, -1, -1, 7, 3, 8, -1, -1], 'scores': [0.31906068325042725, 0.4793124198913574, 0.38263142108917236, 0.4408486485481262, 0.5409184694290161, 0.5318418145179749, 0.5113599896430969, 0.5344786643981934, 0.7394444346427917, 0.40348124504089355]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.2053422927856445})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5768427848815918})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4178851842880249})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3329229950904846})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2908921539783478})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2829151451587677})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2845260202884674})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2650705575942993})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32032471895217896})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28281134366989136})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2642355263233185})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2946542501449585})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30381834506988525})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31295180320739746})
store['active_learning_steps'][85]['training']['best_epoch']=11
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9734, 'crossentropy': 0.259187646484375}
store['active_learning_steps'][85]['eval_training']={}
store['active_learning_steps'][85]['eval_training']['epochs']=[]
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6231586933135986})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3825376331806183})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3025266230106354})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33467668294906616})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.28145503997802734})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.257184773683548})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23754793405532837})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24312922358512878})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.21392787992954254})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23759464919567108})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2163594365119934})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.21394383907318115})
store['active_learning_steps'][85]['eval_training']['best_epoch']=9
store['active_learning_steps'][85]['acquisition']={'indices': [15696, 55612, 7308, 11482, 48436, 26852, 32323, 14609, 16961, 31571], 'labels': [-1, -1, 8, 8, -1, 8, 5, -1, 0, -1], 'scores': [0.48046422004699707, 0.7007749080657959, 0.5602333545684814, 0.8238672018051147, 0.3323880434036255, 0.5555621385574341, 0.5132566392421722, 0.39660555124282837, 0.44757574796676636, 0.45341503620147705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.516789197921753})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6833752393722534})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3982830345630646})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3579775094985962})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26959463953971863})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2694428563117981})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30271416902542114})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2750571668148041})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29616162180900574})
store['active_learning_steps'][86]['training']['best_epoch']=6
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9688, 'crossentropy': 0.28118984375}
store['active_learning_steps'][86]['eval_training']={}
store['active_learning_steps'][86]['eval_training']['epochs']=[]
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6373228430747986})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.46587562561035156})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39353740215301514})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3097435534000397})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3300124704837799})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3037731647491455})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30190733075141907})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27249327301979065})
store['active_learning_steps'][86]['eval_training']['best_epoch']=8
store['active_learning_steps'][86]['acquisition']={'indices': [13424, 16047, 22124, 15079, 20789, 59049, 18848, 20312, 32522, 2606], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4532359838485718, 0.4311579465866089, 0.4419684410095215, 0.42518484592437744, 0.34053802490234375, 0.4176332950592041, 0.33817076683044434, 0.4995102286338806, 0.5001018047332764, 0.34644007682800293]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2099664211273193})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.49410152435302734})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.35504692792892456})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28771525621414185})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2840602397918701})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2482282817363739})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24791038036346436})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2539004683494568})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23891018331050873})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2476024180650711})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.24989594519138336})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2534545958042145})
store['active_learning_steps'][87]['training']['best_epoch']=9
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9768, 'crossentropy': 0.2286063720703125}
store['active_learning_steps'][87]['eval_training']={}
store['active_learning_steps'][87]['eval_training']['epochs']=[]
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6274915337562561})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4265263080596924})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3206636607646942})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.283866286277771})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.269321084022522})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2635391354560852})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2650075852870941})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.22726169228553772})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.20307588577270508})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.23493692278862})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.20739251375198364})
store['active_learning_steps'][87]['eval_training']['best_epoch']=9
store['active_learning_steps'][87]['acquisition']={'indices': [9982, 27101, 9825, 35168, 47410, 53873, 59031, 46046, 23540, 52145], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.3907431960105896, 0.3966430425643921, 0.47797679901123047, 0.5708009600639343, 0.5362598299980164, 0.3205142021179199, 0.35079801082611084, 0.5203598737716675, 0.4722977876663208, 0.33134984970092773]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.2000420093536377})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5922272801399231})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.40350058674812317})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3163585662841797})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30740097165107727})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28879356384277344})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.299913227558136})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.28675055503845215})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2800571918487549})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29457053542137146})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3109999895095825})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2672290802001953})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3087475597858429})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28902149200439453})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27751559019088745})
store['active_learning_steps'][88]['training']['best_epoch']=12
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9728, 'crossentropy': 0.27209365234375}
store['active_learning_steps'][88]['eval_training']={}
store['active_learning_steps'][88]['eval_training']['epochs']=[]
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6922063827514648})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.43960076570510864})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3285110592842102})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3004559278488159})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2939434349536896})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26268231868743896})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27010875940322876})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.268386572599411})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2383919209241867})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2512715458869934})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.22490380704402924})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2138361930847168})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24183300137519836})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2339484840631485})
store['active_learning_steps'][88]['eval_training']['best_epoch']=12
store['active_learning_steps'][88]['acquisition']={'indices': [49423, 50018, 10239, 10506, 43005, 44847, 14446, 19194, 45946, 42988], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.7236201167106628, 0.611109733581543, 0.6249727010726929, 0.5730032920837402, 0.5385587215423584, 0.479475736618042, 0.8133640885353088, 0.5903059840202332, 0.35072624683380127, 0.48576974868774414]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1669318675994873})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5808289051055908})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3800196647644043})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28999581933021545})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27692896127700806})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2497435212135315})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2397284209728241})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2320879101753235})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27954867482185364})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2521556615829468})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2498752921819687})
store['active_learning_steps'][89]['training']['best_epoch']=8
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.222508154296875}
store['active_learning_steps'][89]['eval_training']={}
store['active_learning_steps'][89]['eval_training']['epochs']=[]
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6754330992698669})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46137166023254395})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3568934202194214})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2956218719482422})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2962878346443176})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24937447905540466})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25232720375061035})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24400296807289124})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24820971488952637})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23145791888237})
store['active_learning_steps'][89]['eval_training']['best_epoch']=10
store['active_learning_steps'][89]['acquisition']={'indices': [19189, 50618, 52778, 32488, 58952, 3719, 5548, 29270, 21923, 25848], 'labels': [-1, 6, -1, -1, -1, 2, 8, -1, -1, -1], 'scores': [0.3826472759246826, 0.47390490770339966, 0.479372501373291, 0.4728584289550781, 0.3610485792160034, 0.4634231925010681, 0.3029705286026001, 0.25283944606781006, 0.4238358736038208, 0.4469258785247803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.1879459619522095})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.6091253161430359})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4239538013935089})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.406556099653244})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30630266666412354})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28385239839553833})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.28148454427719116})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28933078050613403})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3080073595046997})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29514050483703613})
store['active_learning_steps'][90]['training']['best_epoch']=7
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9706, 'crossentropy': 0.26596865234375}
store['active_learning_steps'][90]['eval_training']={}
store['active_learning_steps'][90]['eval_training']['epochs']=[]
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.684810996055603})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4828871190547943})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37251362204551697})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36580485105514526})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2787889838218689})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27806299924850464})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26372748613357544})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2710675001144409})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.22617167234420776})
store['active_learning_steps'][90]['eval_training']['best_epoch']=9
store['active_learning_steps'][90]['acquisition']={'indices': [34835, 15746, 12690, 23492, 1525, 6097, 18081, 1143, 32639, 53777], 'labels': [-1, -1, -1, -1, -1, -1, -1, 2, -1, -1], 'scores': [0.5418628454208374, 0.4824451804161072, 0.5658161044120789, 0.4550092816352844, 0.5339093208312988, 0.49429595470428467, 0.5906825661659241, 0.5384921431541443, 0.5197790265083313, 0.4823032021522522]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.3430678844451904})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.6507185697555542})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.39136821031570435})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34360218048095703})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28125232458114624})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2609714865684509})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24879798293113708})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2836484909057617})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2680080831050873})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2763550281524658})
store['active_learning_steps'][91]['training']['best_epoch']=7
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9735, 'crossentropy': 0.244268359375}
store['active_learning_steps'][91]['eval_training']={}
store['active_learning_steps'][91]['eval_training']['epochs']=[]
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7055186033248901})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4439847469329834})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.366729736328125})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2959187924861908})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3528556227684021})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25254085659980774})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25299978256225586})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.22177110612392426})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25921502709388733})
store['active_learning_steps'][91]['eval_training']['best_epoch']=8
store['active_learning_steps'][91]['acquisition']={'indices': [9180, 17386, 49971, 30932, 14666, 6911, 39667, 47870, 51426, 18521], 'labels': [3, -1, -1, 0, -1, -1, -1, 9, -1, -1], 'scores': [0.48407790064811707, 0.4547417163848877, 0.6059708595275879, 0.4898545742034912, 0.45088887214660645, 0.3036755919456482, 0.400272011756897, 0.4874728322029114, 0.45898693799972534, 0.4126628637313843]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.2706828117370605})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.6314077973365784})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3987167477607727})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.348746657371521})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30902135372161865})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29558098316192627})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.282156765460968})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2570178508758545})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2689976096153259})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2860429286956787})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2537934184074402})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.276422381401062})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3161972165107727})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26960939168930054})
store['active_learning_steps'][92]['training']['best_epoch']=11
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9736, 'crossentropy': 0.2589040771484375}
store['active_learning_steps'][92]['eval_training']={}
store['active_learning_steps'][92]['eval_training']['epochs']=[]
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7207369804382324})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.48810094594955444})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36447256803512573})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33931732177734375})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2660960555076599})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30871421098709106})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2991645038127899})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2752741277217865})
store['active_learning_steps'][92]['eval_training']['best_epoch']=5
store['active_learning_steps'][92]['acquisition']={'indices': [33941, 45631, 37468, 30883, 46270, 6386, 37696, 58060, 31556, 8785], 'labels': [-1, -1, -1, 3, -1, -1, 2, -1, -1, -1], 'scores': [0.3842955231666565, 0.630752682685852, 0.5234013795852661, 0.7137657999992371, 0.44225919246673584, 0.5079755783081055, 0.5073465704917908, 0.5097039937973022, 0.39939284324645996, 0.5478143692016602]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.3752880096435547})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.6001728773117065})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4025990962982178})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32511353492736816})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2805604934692383})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2952585220336914})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26265108585357666})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.25865378975868225})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.25423663854599})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29187920689582825})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26121535897254944})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.285923570394516})
store['active_learning_steps'][93]['training']['best_epoch']=9
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.2469704345703125}
store['active_learning_steps'][93]['eval_training']={}
store['active_learning_steps'][93]['eval_training']['epochs']=[]
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6781637668609619})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3916933536529541})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3372901976108551})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.299607515335083})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2853384017944336})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2493496984243393})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25812941789627075})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2399570345878601})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.22376209497451782})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2194329798221588})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.21557548642158508})
store['active_learning_steps'][93]['eval_training']['best_epoch']=11
store['active_learning_steps'][93]['acquisition']={'indices': [36507, 17787, 45979, 9390, 35952, 393, 12316, 51750, 16021, 16647], 'labels': [-1, -1, -1, 9, -1, -1, -1, -1, -1, -1], 'scores': [0.5696563720703125, 0.6220437288284302, 0.35248804092407227, 0.4715500473976135, 0.5787372589111328, 0.7283995747566223, 0.5152978897094727, 0.42971158027648926, 0.48855137825012207, 0.4369301199913025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.2513234615325928})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5608208775520325})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3730405569076538})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30845147371292114})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24271230399608612})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24682000279426575})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24892815947532654})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2524263262748718})
store['active_learning_steps'][94]['training']['best_epoch']=5
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9734, 'crossentropy': 0.2451341796875}
store['active_learning_steps'][94]['eval_training']={}
store['active_learning_steps'][94]['eval_training']['epochs']=[]
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7424901127815247})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4294126033782959})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43703585863113403})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3498505651950836})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32004064321517944})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.28491103649139404})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2647985816001892})
store['active_learning_steps'][94]['eval_training']['best_epoch']=7
store['active_learning_steps'][94]['acquisition']={'indices': [56521, 18081, 46373, 46252, 49977, 901, 52893, 53375, 34722, 20354], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.384432315826416, 0.587916910648346, 0.42627406120300293, 0.46281325817108154, 0.5054926872253418, 0.44031286239624023, 0.4064507484436035, 0.5136845111846924, 0.534461498260498, 0.37944716215133667]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.364534854888916})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6084945797920227})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.4139445722103119})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.31759071350097656})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.278869092464447})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26021215319633484})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.25855952501296997})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2935923635959625})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.24357476830482483})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2539128363132477})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.26601332426071167})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2676597535610199})
store['active_learning_steps'][95]['training']['best_epoch']=9
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9771, 'crossentropy': 0.23520751953125}
store['active_learning_steps'][95]['eval_training']={}
store['active_learning_steps'][95]['eval_training']['epochs']=[]
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6412304639816284})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.43892428278923035})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3533846437931061})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30479884147644043})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25473541021347046})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2570273280143738})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24889859557151794})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24532678723335266})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2568511366844177})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23287729918956757})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.20614366233348846})
store['active_learning_steps'][95]['eval_training']['best_epoch']=11
store['active_learning_steps'][95]['acquisition']={'indices': [11572, 26403, 9432, 54436, 2359, 21876, 13376, 27952, 121, 53844], 'labels': [5, -1, -1, 3, 3, -1, 3, 5, -1, 5], 'scores': [0.5498450994491577, 0.45705699920654297, 0.5207008123397827, 0.41509437561035156, 0.6296996474266052, 0.3604707717895508, 0.5609921216964722, 0.48818492889404297, 0.39990234375, 0.7480115294456482]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.278322458267212})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.591101884841919})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.41622525453567505})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36069995164871216})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30611103773117065})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2729524075984955})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30980202555656433})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2918957769870758})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2798200845718384})
store['active_learning_steps'][96]['training']['best_epoch']=6
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9691, 'crossentropy': 0.28224453125}
store['active_learning_steps'][96]['eval_training']={}
store['active_learning_steps'][96]['eval_training']['epochs']=[]
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6367204189300537})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.43344682455062866})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3534221649169922})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3239169120788574})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2958916425704956})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3046538233757019})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26014167070388794})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28402745723724365})
store['active_learning_steps'][96]['eval_training']['best_epoch']=7
store['active_learning_steps'][96]['acquisition']={'indices': [50782, 48807, 40752, 33262, 53211, 26579, 41772, 14868, 8668, 31313], 'labels': [5, -1, 3, -1, -1, 7, 5, -1, 5, -1], 'scores': [0.3790828287601471, 0.33209121227264404, 0.5778211355209351, 0.24491393566131592, 0.5040758848190308, 0.3032420873641968, 0.568317711353302, 0.26042842864990234, 0.683168888092041, 0.35500216484069824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.3685003519058228})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7186623811721802})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.43733352422714233})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3198162913322449})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3247012495994568})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3114382028579712})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29909032583236694})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.287786602973938})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2713562846183777})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3005519509315491})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2697031497955322})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.29962071776390076})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2776032090187073})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2924234867095947})
store['active_learning_steps'][97]['training']['best_epoch']=11
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9727, 'crossentropy': 0.2628864013671875}
store['active_learning_steps'][97]['eval_training']={}
store['active_learning_steps'][97]['eval_training']['epochs']=[]
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.629554808139801})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4513741135597229})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.383092999458313})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3066262900829315})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3176722824573517})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2815980315208435})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26929694414138794})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23085004091262817})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2374429702758789})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23084783554077148})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23792707920074463})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25962191820144653})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.21697762608528137})
store['active_learning_steps'][97]['eval_training']['best_epoch']=13
store['active_learning_steps'][97]['acquisition']={'indices': [1254, 22356, 39449, 49616, 31646, 100, 21880, 45016, 29018, 3836], 'labels': [-1, -1, 7, 7, -1, -1, 2, -1, -1, -1], 'scores': [0.45152783393859863, 0.4949793219566345, 0.3494970500469208, 0.540937602519989, 0.3944690227508545, 0.37346482276916504, 0.5038402080535889, 0.3905261754989624, 0.5755899548530579, 0.3143131732940674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.1535377502441406})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5058534145355225})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.35178089141845703})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3051193952560425})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24458569288253784})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2745399475097656})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23733831942081451})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24020421504974365})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.22387543320655823})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.2584195137023926})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24701274931430817})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.24456435441970825})
store['active_learning_steps'][98]['training']['best_epoch']=9
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9752, 'crossentropy': 0.2221586669921875}
store['active_learning_steps'][98]['eval_training']={}
store['active_learning_steps'][98]['eval_training']['epochs']=[]
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6412458419799805})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.43340301513671875})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37231117486953735})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30247050523757935})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27013495564460754})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23694023489952087})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2626741826534271})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23880800604820251})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24610550701618195})
store['active_learning_steps'][98]['eval_training']['best_epoch']=6
store['active_learning_steps'][98]['acquisition']={'indices': [56542, 7752, 32896, 33900, 40208, 35503, 17231, 56249, 46167, 21806], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.2568243741989136, 0.3276815414428711, 0.43498939275741577, 0.29711198806762695, 0.4152108430862427, 0.4284200668334961, 0.3673628568649292, 0.6373014450073242, 0.319050669670105, 0.501218318939209]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9832024574279785})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4757469892501831})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3511383533477783})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28106945753097534})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24927407503128052})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.23600460588932037})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.26070940494537354})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24456006288528442})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2512758672237396})
store['active_learning_steps'][99]['training']['best_epoch']=6
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.2512654052734375}
store['active_learning_steps'][99]['eval_training']={}
store['active_learning_steps'][99]['eval_training']['epochs']=[]
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7459481954574585})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4602707624435425})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3776213526725769})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2925664782524109})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28065598011016846})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2666056752204895})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2630225419998169})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2502826750278473})
store['active_learning_steps'][99]['eval_training']['best_epoch']=8
store['active_learning_steps'][99]['acquisition']={'indices': [31451, 14654, 9474, 10213, 55788, 14312, 19566, 40575, 12950, 55934], 'labels': [-1, -1, -1, -1, -1, 1, -1, -1, 2, -1], 'scores': [0.21898269653320312, 0.4111587405204773, 0.3393881320953369, 0.4304589033126831, 0.4052013158798218, 0.32680046558380127, 0.3776777982711792, 0.33204877376556396, 0.4573330879211426, 0.24107825756072998]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.2393412590026855})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5580712556838989})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3504255712032318})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.326927125453949})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2810530364513397})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2580782175064087})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2533040940761566})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24606701731681824})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.26232045888900757})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26758670806884766})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2840152382850647})
store['active_learning_steps'][100]['training']['best_epoch']=8
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.976, 'crossentropy': 0.21694169921875}
store['active_learning_steps'][100]['eval_training']={}
store['active_learning_steps'][100]['eval_training']['epochs']=[]
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6605488061904907})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4186022877693176})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.343253493309021})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3142958879470825})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3244462013244629})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25877636671066284})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24952921271324158})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24068626761436462})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2838982343673706})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26043272018432617})
store['active_learning_steps'][100]['eval_training']['best_epoch']=8
store['active_learning_steps'][100]['acquisition']={'indices': [16971, 47090, 21433, 24957, 13533, 16766, 14330, 44330, 33301, 2196], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.43578100204467773, 0.5803049802780151, 0.37579822540283203, 0.6085197925567627, 0.4097411632537842, 0.42881107330322266, 0.49036240577697754, 0.3929041624069214, 0.5744812488555908, 0.5451287031173706]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1857073307037354})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5556304454803467})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34667110443115234})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2824428677558899})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2696290612220764})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.25053077936172485})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2553783655166626})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24792127311229706})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.23043908178806305})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.2574459910392761})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24387633800506592})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24997825920581818})
store['active_learning_steps'][101]['training']['best_epoch']=9
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9748, 'crossentropy': 0.23926787109375}
store['active_learning_steps'][101]['eval_training']={}
store['active_learning_steps'][101]['eval_training']['epochs']=[]
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.738019585609436})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.39076897501945496})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3580842614173889})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30726832151412964})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27992236614227295})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2896128296852112})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2644912004470825})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2628207206726074})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2446340024471283})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.22685864567756653})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24625280499458313})
store['active_learning_steps'][101]['eval_training']['best_epoch']=10
store['active_learning_steps'][101]['acquisition']={'indices': [12432, 57506, 18554, 39220, 9482, 16286, 56086, 736, 24303, 48726], 'labels': [-1, 2, -1, -1, -1, 0, -1, -1, -1, 8], 'scores': [0.42655301094055176, 0.4665013551712036, 0.35132551193237305, 0.4639582633972168, 0.41564154624938965, 0.6039157509803772, 0.5429048538208008, 0.44240009784698486, 0.4615563154220581, 0.48038291931152344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.1483879089355469})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5907133221626282})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.38539648056030273})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30490195751190186})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2750507891178131})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.25624677538871765})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26529210805892944})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.24440352618694305})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24890539050102234})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.24159732460975647})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.247493177652359})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2673904299736023})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.26515406370162964})
store['active_learning_steps'][102]['training']['best_epoch']=10
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.9734, 'crossentropy': 0.231596826171875}
store['active_learning_steps'][102]['eval_training']={}
store['active_learning_steps'][102]['eval_training']['epochs']=[]
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6172059774398804})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4373135566711426})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.329680860042572})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30525678396224976})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28304460644721985})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2709828317165375})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.246645987033844})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25107109546661377})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23291203379631042})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24718716740608215})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2347668707370758})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2148551642894745})
store['active_learning_steps'][102]['eval_training']['best_epoch']=12
store['active_learning_steps'][102]['acquisition']={'indices': [4036, 4897, 48673, 5773, 29956, 24317, 1733, 21348, 50170, 2557], 'labels': [-1, -1, -1, 0, -1, -1, -1, -1, -1, -1], 'scores': [0.5880271792411804, 0.5163223743438721, 0.2548485994338989, 0.5017552971839905, 0.4607725143432617, 0.4675377607345581, 0.4597572088241577, 0.5061821937561035, 0.5157458782196045, 0.48777520656585693]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.2531712055206299})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5465433597564697})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3986973166465759})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3081682622432709})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2911985516548157})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27414846420288086})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2345457673072815})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9794921875, 'crossentropy': 0.2441154420375824})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.24714943766593933})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23088262975215912})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.221294105052948})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.22520776093006134})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.22322848439216614})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9794921875, 'crossentropy': 0.24118560552597046})
store['active_learning_steps'][103]['training']['best_epoch']=11
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9758, 'crossentropy': 0.22759560546875}
store['active_learning_steps'][103]['eval_training']={}
store['active_learning_steps'][103]['eval_training']['epochs']=[]
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.711467981338501})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4185059666633606})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38078904151916504})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28845441341400146})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2941058874130249})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24313633143901825})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.23534688353538513})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.20981091260910034})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23690898716449738})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.21865123510360718})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.21484768390655518})
store['active_learning_steps'][103]['eval_training']['best_epoch']=8
store['active_learning_steps'][103]['acquisition']={'indices': [34614, 1887, 4016, 42342, 5324, 36844, 46698, 49125, 25662, 5891], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 4, -1], 'scores': [0.5222336053848267, 0.5767484307289124, 0.3952697515487671, 0.43199074268341064, 0.3988701105117798, 0.40815305709838867, 0.5047889947891235, 0.5705205202102661, 0.4043859839439392, 0.390649676322937]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0177628993988037})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.46397101879119873})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.35525673627853394})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2798179090023041})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2523413896560669})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.25128817558288574})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30802592635154724})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2629181444644928})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2794973850250244})
store['active_learning_steps'][104]['training']['best_epoch']=6
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9728, 'crossentropy': 0.23876328125}
store['active_learning_steps'][104]['eval_training']={}
store['active_learning_steps'][104]['eval_training']['epochs']=[]
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7007433176040649})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4377717971801758})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3549002707004547})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3165488541126251})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.301029771566391})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2982494831085205})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25481027364730835})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24062854051589966})
store['active_learning_steps'][104]['eval_training']['best_epoch']=8
store['active_learning_steps'][104]['acquisition']={'indices': [4369, 32350, 53449, 13754, 35798, 8409, 8670, 48374, 5555, 44843], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4535456895828247, 0.5635251402854919, 0.42187273502349854, 0.4674108028411865, 0.44545435905456543, 0.5426710844039917, 0.36011582612991333, 0.42734283208847046, 0.37224483489990234, 0.4187270402908325]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.1587331295013428})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.515403151512146})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3600476086139679})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29257965087890625})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2805512547492981})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23338353633880615})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.24321885406970978})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24237965047359467})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.23271706700325012})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.23692604899406433})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2436058074235916})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.23436591029167175})
store['active_learning_steps'][105]['training']['best_epoch']=9
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.9745, 'crossentropy': 0.223614892578125}
store['active_learning_steps'][105]['eval_training']={}
store['active_learning_steps'][105]['eval_training']['epochs']=[]
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5803258419036865})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.43442678451538086})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.327173113822937})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28041452169418335})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2838248610496521})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2786523103713989})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26773226261138916})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.22783306241035461})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26340389251708984})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.227875754237175})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2483135163784027})
store['active_learning_steps'][105]['eval_training']['best_epoch']=8
store['active_learning_steps'][105]['acquisition']={'indices': [43632, 43097, 59342, 29379, 29422, 34763, 30663, 16418, 43368, 2290], 'labels': [-1, 8, -1, 9, -1, -1, -1, -1, -1, -1], 'scores': [0.5471974611282349, 0.3636576533317566, 0.5207828283309937, 0.474669873714447, 0.5131407380104065, 0.4917173385620117, 0.5090537071228027, 0.38596630096435547, 0.534072995185852, 0.47898685932159424]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.2282049655914307})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5860691666603088})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3852839171886444})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.30494093894958496})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3111131489276886})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2573908567428589})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.26482582092285156})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.20459815859794617})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2508499026298523})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23088204860687256})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.982421875, 'crossentropy': 0.19807176291942596})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2458111047744751})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.27166643738746643})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.24025565385818481})
store['active_learning_steps'][106]['training']['best_epoch']=11
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9752, 'crossentropy': 0.222158740234375}
store['active_learning_steps'][106]['eval_training']={}
store['active_learning_steps'][106]['eval_training']['epochs']=[]
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6478983163833618})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.376769483089447})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.329522967338562})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3062988817691803})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26519161462783813})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2659706175327301})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2463758885860443})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23230504989624023})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.22238823771476746})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.22298385202884674})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2070925533771515})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24749574065208435})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.22131124138832092})
store['active_learning_steps'][106]['eval_training']['best_epoch']=11
store['active_learning_steps'][106]['acquisition']={'indices': [25910, 29934, 12734, 38998, 15413, 10317, 19252, 20487, 39440, 49651], 'labels': [1, -1, -1, -1, -1, -1, 4, -1, -1, -1], 'scores': [0.379474401473999, 0.45968329906463623, 0.4375566244125366, 0.3363224267959595, 0.23501574993133545, 0.4326026439666748, 0.43386340141296387, 0.3686748743057251, 0.4951361417770386, 0.5812342762947083]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1655933856964111})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5970538854598999})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3974820375442505})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3239187002182007})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27615445852279663})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2812429666519165})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29449597001075745})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.27657705545425415})
store['active_learning_steps'][107]['training']['best_epoch']=5
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.2809542724609375}
store['active_learning_steps'][107]['eval_training']={}
store['active_learning_steps'][107]['eval_training']['epochs']=[]
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6729534864425659})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4999741315841675})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38054898381233215})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37820494174957275})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34472590684890747})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3265652656555176})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31848859786987305})
store['active_learning_steps'][107]['eval_training']['best_epoch']=7
store['active_learning_steps'][107]['acquisition']={'indices': [54321, 41802, 5554, 11749, 34678, 22438, 38308, 31252, 20758, 5103], 'labels': [9, 2, 6, 8, 8, 8, -1, 5, 8, 2], 'scores': [0.4024631381034851, 0.4182926416397095, 0.33577701449394226, 0.3106796145439148, 0.43333977460861206, 0.3879740238189697, 0.4079819917678833, 0.5738122463226318, 0.2844846844673157, 0.48223912715911865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0876684188842773})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.5371013283729553})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.37536874413490295})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2931082248687744})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.28831225633621216})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2645761966705322})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.247606098651886})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24696394801139832})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23127701878547668})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24215443432331085})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29289180040359497})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24133765697479248})
store['active_learning_steps'][108]['training']['best_epoch']=9
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9753, 'crossentropy': 0.2248632080078125}
store['active_learning_steps'][108]['eval_training']={}
store['active_learning_steps'][108]['eval_training']['epochs']=[]
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.654202938079834})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4174675941467285})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3302394449710846})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2925204634666443})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28998255729675293})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27508682012557983})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2630236744880676})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2508874237537384})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.22829082608222961})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2308284044265747})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.21094821393489838})
store['active_learning_steps'][108]['eval_training']['best_epoch']=11
store['active_learning_steps'][108]['acquisition']={'indices': [3281, 8790, 52145, 15843, 23421, 53872, 24086, 38217, 9242, 19537], 'labels': [8, 3, 6, 6, -1, 8, -1, -1, -1, -1], 'scores': [0.39737802743911743, 0.5248559713363647, 0.5019212365150452, 0.4347478151321411, 0.5109294652938843, 0.6504142880439758, 0.29829728603363037, 0.5004243850708008, 0.40565645694732666, 0.4787304401397705]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.2830777168273926})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5871166586875916})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.425018310546875})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.34540799260139465})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27527928352355957})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.23707173764705658})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2629832625389099})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.22701141238212585})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23798689246177673})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27047544717788696})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.22339028120040894})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.24246567487716675})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25367599725723267})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.2529546022415161})
store['active_learning_steps'][109]['training']['best_epoch']=11
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.9754, 'crossentropy': 0.240862646484375}
store['active_learning_steps'][109]['eval_training']={}
store['active_learning_steps'][109]['eval_training']['epochs']=[]
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.641228437423706})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4403015375137329})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.32986295223236084})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.31881266832351685})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2810894548892975})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25274595618247986})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2333465814590454})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2528972923755646})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2364949733018875})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.22322025895118713})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.20481449365615845})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.20680466294288635})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.20899049937725067})
store['active_learning_steps'][109]['eval_training']['best_epoch']=11
store['active_learning_steps'][109]['acquisition']={'indices': [25347, 57311, 2515, 46348, 9239, 12263, 47927, 57491, 56292, 28902], 'labels': [-1, 5, -1, -1, -1, -1, -1, -1, 9, -1], 'scores': [0.43228209018707275, 0.5915148854255676, 0.627060055732727, 0.3136434555053711, 0.4213641881942749, 0.4667741060256958, 0.605492115020752, 0.45718252658843994, 0.7287135124206543, 0.5386101007461548]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.2951204776763916})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.6015406847000122})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.43660902976989746})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.32926326990127563})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2841112017631531})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29499536752700806})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.23481148481369019})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.2367877960205078})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.25150027871131897})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.22430652379989624})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2305418998003006})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.24952295422554016})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2340223491191864})
store['active_learning_steps'][110]['training']['best_epoch']=10
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9718, 'crossentropy': 0.258455810546875}
store['active_learning_steps'][110]['eval_training']={}
store['active_learning_steps'][110]['eval_training']['epochs']=[]
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6485475301742554})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40079939365386963})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3222038447856903})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3173392713069916})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2472396343946457})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2550784647464752})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2625543773174286})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23144453763961792})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2579187750816345})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.257035493850708})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24550941586494446})
store['active_learning_steps'][110]['eval_training']['best_epoch']=8
store['active_learning_steps'][110]['acquisition']={'indices': [57741, 41156, 46734, 30082, 25909, 9534, 24486, 59153, 54213, 46604], 'labels': [-1, 0, 4, -1, 9, 6, -1, -1, -1, 0], 'scores': [0.4066658616065979, 0.4650203287601471, 0.6140847206115723, 0.37064439058303833, 0.5028938055038452, 0.3478255867958069, 0.2375349998474121, 0.38414162397384644, 0.47743624448776245, 0.6638888418674469]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0895938873291016})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5873784422874451})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34852588176727295})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31448158621788025})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.28805142641067505})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2558435797691345})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.23633381724357605})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.22564783692359924})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23679715394973755})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.21230481564998627})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.22233140468597412})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.98046875, 'crossentropy': 0.22177107632160187})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.22347623109817505})
store['active_learning_steps'][111]['training']['best_epoch']=10
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9762, 'crossentropy': 0.2217552001953125}
