store = {}
store['timestamp']=1620908108
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=5']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=5
store['worker_id']=5
store['num_workers']=20
store['config']={'seed': 1241, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 1000, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.452007293701172})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.3993334770202637})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6762375831604004})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.818283796310425})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.9607927799224854})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.666, 'crossentropy': 2.191916015625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2205485105514526})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1762893199920654})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.222346305847168})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1739280223846436})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [52173, 59865, 53131, 8200, 49011, 24809, 10677, 47346, 5166, 59492], 'labels': [-1, 8, 8, 3, 0, 0, 3, 0, 2, 5], 'scores': [0.3966888189315796, 0.8200141787528992, 0.8457699418067932, 0.7410485148429871, 0.7556518912315369, 0.7260433435440063, 0.5431689023971558, 0.7595557570457458, 0.8933097124099731, 0.6243311166763306]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.9578659534454346})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.318990707397461})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.4966201782226562})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.5768468379974365})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7369, 'crossentropy': 1.70206640625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0649995803833008})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.0406643152236938})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.0099895000457764})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [28197, 12273, 56684, 24708, 39713, 2817, 30463, 19737, 50468, 10810], 'labels': [9, 7, 9, 5, -1, 0, 4, 2, -1, -1], 'scores': [0.7556648254394531, 0.5852262377738953, 0.7166674137115479, 0.7507905960083008, 0.7102199196815491, 0.7155500054359436, 0.5698519945144653, 0.6343415677547455, 0.597007155418396, 0.5465797185897827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.9246175289154053})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.29795503616333})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.2056877613067627})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.5033059120178223})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7199, 'crossentropy': 1.706933203125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1523103713989258})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.096071720123291})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.061418056488037})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [55661, 42047, 1722, 15954, 15929, 20733, 45214, 33046, 53291, 33596], 'labels': [5, 5, 3, 7, 1, 6, 4, 5, 7, -1], 'scores': [0.7046331167221069, 0.6818288564682007, 0.5697534084320068, 0.6928880214691162, 0.4222760796546936, 0.7240177392959595, 0.6157000064849854, 0.5377835631370544, 0.520688533782959, 0.4787130355834961]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.0421576499938965})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.3400765657424927})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2917752265930176})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.4375214576721191})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.8418, 'crossentropy': 0.947080078125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7522977590560913})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.6678627133369446})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7255362868309021})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [13195, 45056, 39149, 49114, 33472, 13340, 52944, 16922, 32444, 40481], 'labels': [-1, 8, 8, 8, 9, 4, 8, 3, 3, 3], 'scores': [0.42000842094421387, 0.6085075736045837, 0.38906657695770264, 0.4923964738845825, 0.680344820022583, 0.5389885902404785, 0.5964961051940918, 0.5459064245223999, 0.6118277311325073, 0.5701746344566345]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0955531597137451})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.0855917930603027})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.2789981365203857})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.3057657480239868})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.2543981075286865})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8411, 'crossentropy': 1.03034599609375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7897689342498779})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.6635842323303223})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.6342916488647461})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.6418009996414185})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [26765, 16650, 20183, 29085, 17972, 22480, 45338, 8892, 19078, 14896], 'labels': [-1, 2, 4, 2, 9, 4, 6, 8, -1, 8], 'scores': [0.38964879512786865, 0.7037580609321594, 0.6366633772850037, 0.5542970895767212, 0.5782940983772278, 0.5671443343162537, 0.4720759391784668, 0.48955678939819336, 0.5744028091430664, 0.7862323522567749]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9705512523651123})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0455961227416992})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0462141036987305})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.184483289718628})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8469, 'crossentropy': 0.82151962890625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8121926784515381})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.7531554102897644})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.745754599571228})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [32229, 35664, 48145, 12361, 33360, 31063, 30398, 23844, 43801, 17482], 'labels': [1, 6, 6, 2, 9, 2, 3, 1, 1, 2], 'scores': [0.36012136936187744, 0.3536924123764038, 0.37937790155410767, 0.49543458223342896, 0.5167129039764404, 0.5563072562217712, 0.3760296106338501, 0.46561765670776367, 0.2966744303703308, 0.4860086441040039]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.971436619758606})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0793426036834717})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.1879427433013916})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1414144039154053})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8491, 'crossentropy': 0.818978271484375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.7893707752227783})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.7680127024650574})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7276453375816345})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [4761, 39096, 26529, 13065, 59361, 28958, 7990, 16053, 5247, 38067], 'labels': [8, 9, -1, 8, 8, 2, 6, 9, 2, 8], 'scores': [0.4672936201095581, 0.5569537878036499, 0.39739298820495605, 0.4506876468658447, 0.4224206209182739, 0.5392796397209167, 0.6607414484024048, 0.500352144241333, 0.5680332183837891, 0.4607667326927185]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.871263861656189})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9735085964202881})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9952007532119751})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9351592063903809})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.855, 'crossentropy': 0.82349482421875}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.7950133085250854})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.7409754991531372})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7050936818122864})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [36268, 6944, 38796, 38448, 53758, 47219, 56171, 9433, 18302, 20122], 'labels': [5, 2, 6, 6, 3, 6, 6, 7, 6, 6], 'scores': [0.6268941760063171, 0.6590718030929565, 0.5042710304260254, 0.3687772750854492, 0.4540848731994629, 0.381208598613739, 0.458745539188385, 0.4524127244949341, 0.5382028818130493, 0.4012998938560486]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9386029243469238})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7539913654327393})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8591214418411255})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.81342613697052})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.9219415783882141})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8876, 'crossentropy': 0.689958984375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6931173801422119})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.56306391954422})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5342835187911987})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.5522180795669556})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [28512, 53598, 11148, 26940, 27512, 13262, 42121, 5898, 21007, 43110], 'labels': [5, 5, 4, 6, -1, -1, 5, 9, 3, 8], 'scores': [0.5539219379425049, 0.27567702531814575, 0.3949550986289978, 0.5243077874183655, 0.3456084728240967, 0.460176944732666, 0.5780091285705566, 0.4046177268028259, 0.542779266834259, 0.4375423192977905]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6990278959274292})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6429681777954102})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7034075856208801})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6881400346755981})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7531031966209412})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9094, 'crossentropy': 0.5702435546875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6973463296890259})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5886341333389282})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5158446431159973})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.47303852438926697})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [9994, 36091, 45212, 8893, 48006, 47028, 27402, 59275, 11625, 21355], 'labels': [0, -1, 5, 3, 6, 4, -1, 3, 8, 0], 'scores': [0.6942332983016968, 0.42628729343414307, 0.4844626784324646, 0.36989033222198486, 0.4338458180427551, 0.4567684531211853, 0.33803999423980713, 0.39360782504081726, 0.5720288157463074, 0.7127059102058411]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7426959276199341})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.566178560256958})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5767184495925903})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.607934296131134})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6036164164543152})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9145, 'crossentropy': 0.550033154296875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6949974298477173})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5330324172973633})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4772781729698181})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4544377326965332})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [26577, 3070, 40846, 57882, 21023, 24479, 38267, 40409, 40654, 47409], 'labels': [2, 1, 4, 0, -1, 8, 8, 2, 5, 2], 'scores': [0.47984635829925537, 0.5037775635719299, 0.4727909564971924, 0.6788415908813477, 0.3291579484939575, 0.6490292549133301, 0.34594494104385376, 0.47846531867980957, 0.5179203152656555, 0.5791847705841064]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8192381858825684})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6103509664535522})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6549719572067261})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7253885269165039})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6702210903167725})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9097, 'crossentropy': 0.562568701171875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6992942094802856})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5932079553604126})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5017071962356567})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4823143780231476})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [55227, 57070, 25156, 40076, 12848, 37750, 38464, 2588, 59286, 50390], 'labels': [-1, 8, 2, 2, 8, 5, -1, 6, 8, 0], 'scores': [0.4367680549621582, 0.34943318367004395, 0.4191042184829712, 0.29521727561950684, 0.28833508491516113, 0.533536434173584, 0.32443487644195557, 0.35307013988494873, 0.5358775854110718, 0.30500900745391846]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8121302127838135})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6124159097671509})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.613306999206543})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6504002809524536})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7036425471305847})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9107, 'crossentropy': 0.574476611328125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6982818841934204})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5454579591751099})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.48628824949264526})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5151816010475159})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [47597, 13024, 15795, 30451, 55503, 20792, 43420, 30125, 25714, 56076], 'labels': [8, 7, -1, 8, 0, 9, 6, 5, 0, 7], 'scores': [0.4934116005897522, 0.29566824436187744, 0.4084925651550293, 0.3850959539413452, 0.48531073331832886, 0.63941890001297, 0.36809241771698, 0.4827547073364258, 0.4350419044494629, 0.5376729965209961]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8039976954460144})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5799992084503174})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.551003098487854})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6415128707885742})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5991350412368774})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6108666658401489})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9219, 'crossentropy': 0.5183404296875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6160994172096252})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.47189125418663025})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.43203675746917725})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.45027077198028564})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4079826772212982})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [54779, 49531, 23951, 19101, 18757, 19549, 30144, 45171, 1187, 15482], 'labels': [-1, 7, -1, 3, -1, 3, 9, -1, -1, -1], 'scores': [0.4981178045272827, 0.531432032585144, 0.5088802576065063, 0.5857372283935547, 0.49875378608703613, 0.5179473757743835, 0.5904131531715393, 0.5846951007843018, 0.4970647096633911, 0.45896434783935547]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.8774387240409851})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5350080132484436})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5762250423431396})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6050767302513123})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5578669309616089})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9204, 'crossentropy': 0.52108740234375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7032473087310791})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.5550494194030762})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.485212504863739})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4514015316963196})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [8552, 43126, 24860, 31939, 51227, 43385, 52664, 47741, 677, 3970], 'labels': [2, 3, 9, 9, 5, 9, 3, 5, 4, -1], 'scores': [0.4579024314880371, 0.5265646576881409, 0.5559442043304443, 0.40125250816345215, 0.5092504024505615, 0.34159356355667114, 0.5522007346153259, 0.4959743022918701, 0.40225911140441895, 0.3272210359573364]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8299314975738525})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5475223660469055})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.555069088935852})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6978470087051392})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.570467472076416})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.927, 'crossentropy': 0.48910693359375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7067044973373413})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.500076949596405})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5000993609428406})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5193578004837036})
store['active_learning_steps'][15]['eval_training']['best_epoch']=2
store['active_learning_steps'][15]['acquisition']={'indices': [26706, 52998, 21836, 57234, 10274, 12181, 31347, 54437, 2696, 46576], 'labels': [5, 7, 5, 5, 8, 5, 3, 8, 9, 5], 'scores': [0.477819561958313, 0.3391129970550537, 0.4304500222206116, 0.544284999370575, 0.5347147583961487, 0.484444797039032, 0.43492060899734497, 0.4369692802429199, 0.4268020987510681, 0.45022767782211304]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8532387018203735})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.506109356880188})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4949946403503418})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4973337650299072})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5220775008201599})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.620237410068512})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9343, 'crossentropy': 0.43917392578125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6122643947601318})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4627458453178406})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.41693252325057983})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3740105628967285})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3735419511795044})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [588, 20265, 42746, 56300, 40318, 54909, 31373, 15010, 54, 1531], 'labels': [2, 2, 2, 9, -1, 8, 2, 3, 9, 2], 'scores': [0.5361311435699463, 0.4676225185394287, 0.6073483824729919, 0.6224649548530579, 0.26491260528564453, 0.4893127679824829, 0.30629047751426697, 0.4325840473175049, 0.4618338346481323, 0.5415493845939636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.9259566068649292})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.518997311592102})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.48431307077407837})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5153795480728149})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.538345217704773})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5125008821487427})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9412, 'crossentropy': 0.4144373046875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6412708759307861})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.48391246795654297})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.41554558277130127})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.3875361680984497})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.36315950751304626})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [24175, 51194, 59726, 24904, 5370, 16524, 1608, 54711, 39546, 28246], 'labels': [1, 9, 5, -1, 3, -1, 7, 0, 1, -1], 'scores': [0.4281808137893677, 0.4705709218978882, 0.5496350526809692, 0.31866908073425293, 0.4703950881958008, 0.32654595375061035, 0.4431993365287781, 0.5271649360656738, 0.4559169411659241, 0.34642982482910156]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.770936131477356})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.45817166566848755})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.44482100009918213})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5156862735748291})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.48491621017456055})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5586510300636292})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9327, 'crossentropy': 0.437108349609375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5863839387893677})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4743828773498535})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4489292502403259})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4230685532093048})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.3851921558380127})
store['active_learning_steps'][18]['eval_training']['best_epoch']=5
store['active_learning_steps'][18]['acquisition']={'indices': [49569, 18322, 14247, 13709, 27309, 40190, 23718, 42020, 19190, 43745], 'labels': [1, 7, -1, 6, -1, -1, 2, 9, 9, 8], 'scores': [0.5463651418685913, 0.49305081367492676, 0.36803877353668213, 0.5094473958015442, 0.261020302772522, 0.3269484043121338, 0.43955063819885254, 0.5767601728439331, 0.4968685507774353, 0.42602628469467163]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.967357873916626})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5001348257064819})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.42244571447372437})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.45098036527633667})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.41745394468307495})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.48469534516334534})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.46397480368614197})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.48088058829307556})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9427, 'crossentropy': 0.39756865234375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5760656595230103})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4328788220882416})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4058496356010437})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3391442894935608})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.31673890352249146})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3335583806037903})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.30508941411972046})
store['active_learning_steps'][19]['eval_training']['best_epoch']=7
store['active_learning_steps'][19]['acquisition']={'indices': [57820, 17698, 52123, 50908, 21466, 38586, 51040, 31090, 27620, 52717], 'labels': [3, 9, 9, 9, 3, -1, -1, 4, -1, -1], 'scores': [0.44609278440475464, 0.4880179762840271, 0.5708496570587158, 0.55804842710495, 0.382076621055603, 0.4364175796508789, 0.4220690131187439, 0.5737722516059875, 0.3983997106552124, 0.36343055963516235]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9585603475570679})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.504356861114502})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.47857075929641724})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49533534049987793})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.46452921628952026})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5008081197738647})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5411005020141602})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.47182828187942505})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9426, 'crossentropy': 0.418732080078125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6092285513877869})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4472033977508545})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.383463978767395})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.356949120759964})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3395591378211975})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3318706750869751})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3132750391960144})
store['active_learning_steps'][20]['eval_training']['best_epoch']=7
store['active_learning_steps'][20]['acquisition']={'indices': [16972, 15412, 55790, 39942, 27514, 56244, 45121, 46446, 44091, 57221], 'labels': [-1, 3, 8, 9, 4, 4, -1, -1, 4, -1], 'scores': [0.4225124716758728, 0.512654185295105, 0.5422018766403198, 0.40026751160621643, 0.6553701758384705, 0.7112976312637329, 0.5425838828086853, 0.4997652769088745, 0.5685545802116394, 0.7222170233726501]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9333704710006714})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4672199487686157})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.42909228801727295})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4739788770675659})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.44072556495666504})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.46342355012893677})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9434, 'crossentropy': 0.402542578125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6521604061126709})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.48338577151298523})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4140244126319885})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.41911450028419495})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3770049214363098})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [55447, 50898, 59418, 26132, 58628, 28181, 14514, 45026, 56025, 458], 'labels': [-1, 2, 0, 4, -1, -1, -1, 8, -1, -1], 'scores': [0.4956824779510498, 0.45751893520355225, 0.7450615763664246, 0.44312429428100586, 0.3810533881187439, 0.3559190034866333, 0.3889372944831848, 0.5446264147758484, 0.3487107753753662, 0.2960525155067444]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.9006147980690002})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.46155139803886414})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4181584119796753})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4105647802352905})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4264132082462311})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4214550852775574})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4906914234161377})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9459, 'crossentropy': 0.3783626953125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6416279077529907})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4467228651046753})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.366171270608902})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.3770630955696106})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.33732473850250244})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3003461956977844})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [45975, 53560, 38219, 29320, 24151, 5288, 19590, 4799, 29800, 12345], 'labels': [0, -1, 6, 1, -1, -1, 5, 7, 3, 3], 'scores': [0.3973236083984375, 0.3156003952026367, 0.4821646809577942, 0.6531748175621033, 0.36622536182403564, 0.34747761487960815, 0.560745894908905, 0.31580913066864014, 0.3782939314842224, 0.6310205459594727]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8533614873886108})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5256028175354004})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4371572434902191})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4396785497665405})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.43581897020339966})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4453137516975403})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48337289690971375})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48547035455703735})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9487, 'crossentropy': 0.38084697265625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6884593963623047})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.43529629707336426})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.39161768555641174})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3430056869983673})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3394695520401001})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3109654486179352})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.2911912202835083})
store['active_learning_steps'][23]['eval_training']['best_epoch']=7
store['active_learning_steps'][23]['acquisition']={'indices': [44350, 38920, 47274, 43856, 8458, 59475, 13034, 16146, 13647, 23302], 'labels': [3, 7, 8, 5, 4, -1, -1, 2, 3, -1], 'scores': [0.5873141288757324, 0.7328891158103943, 0.38632678985595703, 0.2713339924812317, 0.6257717609405518, 0.4816914200782776, 0.31230759620666504, 0.38132065534591675, 0.589566707611084, 0.3565800189971924]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9510790109634399})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4650479555130005})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4032354950904846})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5061088800430298})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.40616729855537415})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4970760941505432})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.945, 'crossentropy': 0.37566005859375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6950049996376038})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4491908550262451})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.41933608055114746})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.3998264670372009})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.3807646632194519})
store['active_learning_steps'][24]['eval_training']['best_epoch']=5
store['active_learning_steps'][24]['acquisition']={'indices': [3671, 52987, 3283, 3273, 30006, 32326, 19507, 15743, 47086, 16022], 'labels': [-1, -1, 7, 8, -1, -1, -1, 3, -1, 8], 'scores': [0.37759244441986084, 0.32975703477859497, 0.27505040168762207, 0.46913594007492065, 0.306615948677063, 0.2626294493675232, 0.2723473310470581, 0.3684523105621338, 0.3881957530975342, 0.4882410764694214]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9236640334129333})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5201243758201599})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.40695735812187195})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.45453959703445435})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3991219997406006})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.42974746227264404})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4073074162006378})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3888698220252991})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.401494562625885})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.42384859919548035})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39219191670417786})
store['active_learning_steps'][25]['training']['best_epoch']=8
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9543, 'crossentropy': 0.354202001953125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5882322788238525})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4758007526397705})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.344330370426178})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3371274769306183})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3381761610507965})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3028879761695862})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3169027864933014})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.2941129803657532})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.27988213300704956})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.2856411039829254})
store['active_learning_steps'][25]['eval_training']['best_epoch']=9
store['active_learning_steps'][25]['acquisition']={'indices': [14799, 22547, 32708, 59928, 40646, 55310, 8074, 43402, 24689, 8820], 'labels': [5, -1, -1, -1, 8, 1, -1, 5, -1, -1], 'scores': [0.4335479736328125, 0.43576180934906006, 0.5777056217193604, 0.48443377017974854, 0.791795551776886, 0.5032650232315063, 0.42634499073028564, 0.41834503412246704, 0.4487183094024658, 0.4018874168395996]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9437428712844849})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5256026983261108})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.43471759557724})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4318210482597351})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4390256404876709})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.46238163113594055})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47622472047805786})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9508, 'crossentropy': 0.371098876953125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5826812982559204})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.409930944442749})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.410441517829895})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.37600845098495483})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3577083647251129})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.33466216921806335})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [57664, 3960, 59938, 36138, 47424, 30139, 57916, 46086, 35559, 14501], 'labels': [-1, 6, -1, -1, -1, 6, -1, 5, -1, 4], 'scores': [0.4890401363372803, 0.45656293630599976, 0.4904850721359253, 0.33684319257736206, 0.43835198879241943, 0.5872131586074829, 0.4112309217453003, 0.6472700238227844, 0.3450288772583008, 0.23620516061782837]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8350894451141357})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4632275104522705})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.43487244844436646})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.439761221408844})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3487078547477722})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.40912002325057983})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.40457648038864136})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44501668214797974})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.95, 'crossentropy': 0.3496767578125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6389281749725342})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4646161198616028})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.372226744890213})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.35260260105133057})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.330112487077713})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.32098209857940674})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.29574596881866455})
store['active_learning_steps'][27]['eval_training']['best_epoch']=7
store['active_learning_steps'][27]['acquisition']={'indices': [44609, 28274, 51241, 46853, 47728, 39294, 8940, 14168, 33162, 30408], 'labels': [3, -1, 2, 3, -1, 7, 6, 5, 8, 1], 'scores': [0.49338844418525696, 0.2319435477256775, 0.3541635572910309, 0.4760971665382385, 0.36122703552246094, 0.3924107253551483, 0.4908129572868347, 0.4090013802051544, 0.5386534929275513, 0.3464618921279907]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8575491905212402})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4653678238391876})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.36206889152526855})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3908061385154724})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36295580863952637})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3844512701034546})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9481, 'crossentropy': 0.3590923828125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6226980090141296})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4455852210521698})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3959119915962219})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.34874892234802246})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.33505406975746155})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [6574, 22989, 12874, 33121, 25645, 47674, 55432, 28231, 49011, 38404], 'labels': [-1, 3, 3, -1, 3, -1, 3, 5, -1, -1], 'scores': [0.5480879545211792, 0.31212180852890015, 0.5719404816627502, 0.35006213188171387, 0.44351595640182495, 0.3184032440185547, 0.46172034740448, 0.4348621368408203, 0.3211137056350708, 0.33622944355010986]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8795009851455688})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4698549211025238})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.410794734954834})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3766152262687683})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3969659209251404})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4272954761981964})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3985700011253357})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9484, 'crossentropy': 0.34857392578125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5798209309577942})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4340723752975464})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.38746893405914307})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.31775766611099243})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.34008073806762695})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.31978851556777954})
store['active_learning_steps'][29]['eval_training']['best_epoch']=4
store['active_learning_steps'][29]['acquisition']={'indices': [24256, 42169, 29795, 46614, 56464, 6070, 48160, 30141, 45152, 52106], 'labels': [8, 7, -1, -1, 9, -1, -1, 0, -1, -1], 'scores': [0.40265876054763794, 0.2824475169181824, 0.42968106269836426, 0.27392083406448364, 0.3464498519897461, 0.352813720703125, 0.4855642318725586, 0.3447350263595581, 0.32287758588790894, 0.27138853073120117]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.8177847862243652})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.43854814767837524})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3367127776145935})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33361124992370605})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.32971271872520447})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3188167214393616})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.32571882009506226})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.32979321479797363})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3392723798751831})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9576, 'crossentropy': 0.3073560546875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.695441722869873})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4756931662559509})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.38186711072921753})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.32817786931991577})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.31090620160102844})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.29979419708251953})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.2877887487411499})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.28728294372558594})
store['active_learning_steps'][30]['eval_training']['best_epoch']=8
store['active_learning_steps'][30]['acquisition']={'indices': [15321, 7221, 36182, 36478, 51799, 36267, 28746, 12836, 12900, 59935], 'labels': [-1, -1, -1, -1, -1, -1, -1, 3, 9, -1], 'scores': [0.4905681610107422, 0.2776743173599243, 0.3938731551170349, 0.5654215812683105, 0.4596238136291504, 0.43032026290893555, 0.5560868978500366, 0.638899028301239, 0.4054022431373596, 0.39703071117401123]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9515357613563538})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45709317922592163})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.38958677649497986})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3965302109718323})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4253254532814026})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37326839566230774})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3841659724712372})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36790844798088074})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4320639669895172})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.336024671792984})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40391844511032104})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3924804925918579})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3820524513721466})
store['active_learning_steps'][31]['training']['best_epoch']=10
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9597, 'crossentropy': 0.329766064453125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6304140090942383})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.39473944902420044})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3446391820907593})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.28170540928840637})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30358070135116577})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2828183174133301})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.2583318054676056})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.278988242149353})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.26754868030548096})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2464563250541687})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2614474296569824})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.23585620522499084})
store['active_learning_steps'][31]['eval_training']['best_epoch']=12
store['active_learning_steps'][31]['acquisition']={'indices': [3512, 54099, 16955, 12305, 34520, 21134, 53116, 36141, 11096, 45443], 'labels': [-1, -1, -1, 9, 6, 4, 0, 1, 9, 5], 'scores': [0.5914353132247925, 0.5334104895591736, 0.455080509185791, 0.7078939080238342, 0.39754854142665863, 0.5553092956542969, 0.5752803087234497, 0.6796088814735413, 0.31335189938545227, 0.3960416913032532]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9492380023002625})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4511040449142456})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3888506293296814})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36048686504364014})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35651081800460815})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38101911544799805})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34945303201675415})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3392312228679657})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4150805175304413})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4057098627090454})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3831554651260376})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9571, 'crossentropy': 0.3112336669921875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6768102645874023})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3959290385246277})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.33405035734176636})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.30129119753837585})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2783965766429901})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.28511732816696167})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2630338966846466})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.27148276567459106})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2590109705924988})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.26486045122146606})
store['active_learning_steps'][32]['eval_training']['best_epoch']=9
store['active_learning_steps'][32]['acquisition']={'indices': [27241, 20995, 53820, 44440, 41822, 27455, 59386, 52770, 56254, 5504], 'labels': [8, -1, -1, -1, -1, -1, 4, 9, -1, -1], 'scores': [0.43756911158561707, 0.5617669224739075, 0.5615514516830444, 0.251021146774292, 0.5237028002738953, 0.6816869974136353, 0.5056881904602051, 0.4831728935241699, 0.5616110563278198, 0.5157950520515442]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.860316276550293})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4569311738014221})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4303942918777466})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.40845781564712524})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3805540204048157})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39053553342819214})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4097723662853241})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3975743055343628})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9553, 'crossentropy': 0.337776953125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6126413345336914})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4403474032878876})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.35359930992126465})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.32890719175338745})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3174698054790497})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3101714253425598})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.2812850773334503})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [34745, 22677, 23749, 45063, 14549, 6311, 1250, 37974, 57718, 42001], 'labels': [2, 4, -1, -1, -1, 1, -1, 2, 7, 2], 'scores': [0.6028409004211426, 0.5008964240550995, 0.3441648483276367, 0.5381553173065186, 0.37663722038269043, 0.44357430934906006, 0.44481778144836426, 0.5049637854099274, 0.49477922916412354, 0.7015438675880432]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.0583630800247192})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5064019560813904})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37202024459838867})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33501535654067993})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36455821990966797})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34329289197921753})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3553639352321625})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9555, 'crossentropy': 0.3386402587890625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6411633491516113})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4387781620025635})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3697984516620636})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3488898277282715})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.35332393646240234})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3214764893054962})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [10778, 28194, 7673, 2302, 41965, 32108, 24684, 25262, 17552, 39206], 'labels': [-1, -1, -1, 8, 2, 4, 9, 8, -1, -1], 'scores': [0.33358144760131836, 0.31223607063293457, 0.3055098056793213, 0.3210207223892212, 0.5680005550384521, 0.33738744258880615, 0.35032224655151367, 0.5567507147789001, 0.35123515129089355, 0.25071489810943604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9799913167953491})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.471871554851532})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3993990421295166})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3608252704143524})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34167730808258057})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32382500171661377})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4003300368785858})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39256203174591064})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3678869903087616})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.955, 'crossentropy': 0.3222849365234375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5930944085121155})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4284741282463074})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.38310471177101135})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3469007909297943})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3070858120918274})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2862226366996765})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.2865302562713623})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2682875990867615})
store['active_learning_steps'][35]['eval_training']['best_epoch']=8
store['active_learning_steps'][35]['acquisition']={'indices': [46724, 4564, 892, 24512, 1925, 42672, 40154, 12089, 20976, 49192], 'labels': [7, -1, 6, 3, -1, 7, -1, 3, 5, -1], 'scores': [0.5224419236183167, 0.4175748825073242, 0.49288296699523926, 0.40339869260787964, 0.30895692110061646, 0.42112472653388977, 0.4408160448074341, 0.3883971571922302, 0.4725121259689331, 0.5048010945320129]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8841316103935242})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4955381751060486})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4038510322570801})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33178138732910156})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3560441732406616})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3179996609687805})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3520383834838867})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3725712299346924})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3209037780761719})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9615, 'crossentropy': 0.2822539306640625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6669288277626038})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.43641647696495056})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.39021870493888855})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.33247441053390503})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.34087061882019043})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29229432344436646})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.30301451683044434})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.29319924116134644})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [13021, 13752, 35675, 1521, 17518, 21390, 55208, 55496, 41770, 46134], 'labels': [5, 9, 7, -1, 0, 3, 5, 9, -1, -1], 'scores': [0.419769823551178, 0.5642477869987488, 0.4267900586128235, 0.4743422269821167, 0.3770299553871155, 0.5012028217315674, 0.6037236452102661, 0.7027337551116943, 0.44095754623413086, 0.4922272562980652]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.036325216293335})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5370943546295166})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.37646564841270447})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.347027063369751})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3577779531478882})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3589100241661072})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35547947883605957})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9576, 'crossentropy': 0.3198134521484375}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6606918573379517})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4708194136619568})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3741505742073059})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3659331202507019})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31639760732650757})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.29970335960388184})
store['active_learning_steps'][37]['eval_training']['best_epoch']=6
store['active_learning_steps'][37]['acquisition']={'indices': [16085, 37508, 21058, 56200, 54933, 22562, 8745, 52354, 49624, 55415], 'labels': [-1, -1, 5, 5, 6, 6, -1, -1, 6, -1], 'scores': [0.4722093939781189, 0.35157716274261475, 0.34130585193634033, 0.4297981560230255, 0.4284156560897827, 0.5460588335990906, 0.3958752155303955, 0.3158527612686157, 0.5886415243148804, 0.44395363330841064]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9365910887718201})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5496512651443481})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3973267078399658})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3109823167324066})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32358258962631226})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33077454566955566})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31719568371772766})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9589, 'crossentropy': 0.3161713134765625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6665321588516235})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4233378767967224})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3855127990245819})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3442333936691284})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.34637555480003357})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3142549991607666})
store['active_learning_steps'][38]['eval_training']['best_epoch']=6
store['active_learning_steps'][38]['acquisition']={'indices': [57246, 39457, 47779, 12890, 12493, 15936, 53019, 16843, 28218, 18598], 'labels': [-1, 0, -1, -1, 8, -1, 2, -1, -1, 9], 'scores': [0.43744587898254395, 0.5433992147445679, 0.283073365688324, 0.34086644649505615, 0.5121247172355652, 0.28736329078674316, 0.4331700801849365, 0.3456399440765381, 0.5000997185707092, 0.5828148722648621]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.0721524953842163})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5372375249862671})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.41982460021972656})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3508422076702118})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30574294924736023})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3376726508140564})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3704761266708374})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3576831817626953})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9624, 'crossentropy': 0.299772412109375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5733419060707092})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.42074641585350037})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3323831558227539})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.32474327087402344})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31532949209213257})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.30763447284698486})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3110290467739105})
store['active_learning_steps'][39]['eval_training']['best_epoch']=6
store['active_learning_steps'][39]['acquisition']={'indices': [57276, 11891, 20037, 9924, 50827, 10746, 44570, 4043, 8867, 37147], 'labels': [-1, 9, 8, 8, 1, 9, 7, -1, 8, 7], 'scores': [0.3711754083633423, 0.33756065368652344, 0.3526427745819092, 0.4281817674636841, 0.5167829990386963, 0.5100328326225281, 0.590460479259491, 0.4261993169784546, 0.5674166679382324, 0.528597354888916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.9021115303039551})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5059717893600464})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4123082756996155})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.33732348680496216})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33060288429260254})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36810022592544556})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3642078638076782})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32159164547920227})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36861947178840637})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40503060817718506})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38540488481521606})
store['active_learning_steps'][40]['training']['best_epoch']=8
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.958, 'crossentropy': 0.3155794189453125}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6739732027053833})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4202495813369751})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.38967180252075195})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3168443441390991})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3113399147987366})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3164769411087036})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.2734237611293793})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.26430803537368774})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2573390007019043})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.24643641710281372})
store['active_learning_steps'][40]['eval_training']['best_epoch']=10
store['active_learning_steps'][40]['acquisition']={'indices': [552, 16021, 17278, 31571, 8002, 31252, 42360, 44225, 7307, 52808], 'labels': [-1, -1, 7, -1, -1, 5, -1, -1, -1, 8], 'scores': [0.58845055103302, 0.5947821736335754, 0.456537127494812, 0.46212923526763916, 0.5322796702384949, 0.6654306650161743, 0.25892001390457153, 0.4493255019187927, 0.38393843173980713, 0.42621296644210815]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0216002464294434})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.505691647529602})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.37650156021118164})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3578624725341797})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3599061071872711})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3248447775840759})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33832189440727234})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31756138801574707})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34858939051628113})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3450498580932617})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39273273944854736})
store['active_learning_steps'][41]['training']['best_epoch']=8
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.959, 'crossentropy': 0.3112416015625}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6644483804702759})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4181559681892395})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.34380829334259033})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3364635109901428})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.28527411818504333})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3059523105621338})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.28235578536987305})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2751616835594177})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2660526931285858})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.24420122802257538})
store['active_learning_steps'][41]['eval_training']['best_epoch']=10
store['active_learning_steps'][41]['acquisition']={'indices': [53472, 24172, 48020, 5873, 18324, 6487, 25543, 11963, 49626, 48471], 'labels': [-1, -1, -1, -1, 0, -1, -1, -1, -1, -1], 'scores': [0.3732197880744934, 0.7330254316329956, 0.4761749505996704, 0.49531328678131104, 0.6152617335319519, 0.49873656034469604, 0.41642773151397705, 0.43833446502685547, 0.4825392961502075, 0.3784291744232178]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0670320987701416})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49497053027153015})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3707190752029419})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34001314640045166})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36351606249809265})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.335247278213501})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37410759925842285})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3473210632801056})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3457602262496948})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.96, 'crossentropy': 0.303978662109375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6397359371185303})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.43934375047683716})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.40109390020370483})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3419702351093292})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3243056535720825})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3147966265678406})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31398218870162964})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.27706801891326904})
store['active_learning_steps'][42]['eval_training']['best_epoch']=8
store['active_learning_steps'][42]['acquisition']={'indices': [19968, 31576, 914, 56978, 37293, 39880, 57246, 30151, 22497, 15779], 'labels': [-1, 7, -1, 8, 3, -1, -1, 4, 7, 0], 'scores': [0.39078855514526367, 0.4912561774253845, 0.6091639995574951, 0.5135666131973267, 0.4658659100532532, 0.5380774736404419, 0.4930509328842163, 0.345880925655365, 0.6223670244216919, 0.5255067944526672]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.154845952987671})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5808773040771484})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40059614181518555})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34912317991256714})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3212992250919342})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3432682752609253})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3339020013809204})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36989742517471313})
store['active_learning_steps'][43]['training']['best_epoch']=5
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9622, 'crossentropy': 0.3185361083984375}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6467887759208679})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4631217122077942})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3911347985267639})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3572784662246704})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.32110780477523804})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30047717690467834})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.28256505727767944})
store['active_learning_steps'][43]['eval_training']['best_epoch']=7
store['active_learning_steps'][43]['acquisition']={'indices': [13998, 31014, 49541, 47403, 49537, 57728, 27164, 26763, 17589, 41378], 'labels': [9, -1, 9, 9, 2, 9, 9, -1, 6, -1], 'scores': [0.5582969188690186, 0.3345775604248047, 0.5068286657333374, 0.35077714920043945, 0.6077359914779663, 0.6258307695388794, 0.5229133367538452, 0.3775184154510498, 0.33496755361557007, 0.4535191059112549]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0833497047424316})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5319111347198486})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3809701204299927})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3165455460548401})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3306578993797302})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3319441080093384})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33741283416748047})
store['active_learning_steps'][44]['training']['best_epoch']=4
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9598, 'crossentropy': 0.31363359375}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6551127433776855})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.45901694893836975})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.39465513825416565})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3474934697151184})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.39788004755973816})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3246222138404846})
store['active_learning_steps'][44]['eval_training']['best_epoch']=6
store['active_learning_steps'][44]['acquisition']={'indices': [49410, 1120, 50336, 37405, 7695, 55131, 49890, 40477, 54832, 56297], 'labels': [3, 8, -1, -1, 2, -1, 5, -1, 0, -1], 'scores': [0.27137917280197144, 0.39745664596557617, 0.36703431606292725, 0.31237512826919556, 0.44993776082992554, 0.35879331827163696, 0.5346751809120178, 0.42597854137420654, 0.35479456186294556, 0.305273175239563]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0482417345046997})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5619409084320068})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.406459242105484})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33464694023132324})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3463796377182007})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33968913555145264})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34085288643836975})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9586, 'crossentropy': 0.3092614990234375}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6073986887931824})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.46604427695274353})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.39138656854629517})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.352583646774292})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.37300699949264526})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36946314573287964})
store['active_learning_steps'][45]['eval_training']['best_epoch']=4
store['active_learning_steps'][45]['acquisition']={'indices': [24587, 26879, 44123, 34800, 37062, 18596, 31059, 3160, 27863, 37823], 'labels': [8, -1, 8, 5, 9, 4, -1, -1, -1, -1], 'scores': [0.47331976890563965, 0.4270620346069336, 0.5549598336219788, 0.5708624720573425, 0.4014430046081543, 0.3472525477409363, 0.24006545543670654, 0.38199692964553833, 0.3582754135131836, 0.3872531056404114]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.0224683284759521})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5487062931060791})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4294856786727905})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32272791862487793})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3376197814941406})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3149314522743225})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3203766345977783})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31604450941085815})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30835336446762085})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3697241544723511})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34169691801071167})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3089965283870697})
store['active_learning_steps'][46]['training']['best_epoch']=9
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9658, 'crossentropy': 0.2706623779296875}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.671850860118866})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.42573875188827515})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.35950613021850586})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.30862218141555786})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2608183026313782})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29291248321533203})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2819567322731018})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.26312243938446045})
store['active_learning_steps'][46]['eval_training']['best_epoch']=5
store['active_learning_steps'][46]['acquisition']={'indices': [7768, 7852, 27880, 39487, 20175, 34937, 32645, 29962, 21848, 22815], 'labels': [8, -1, 2, 2, -1, -1, -1, -1, -1, -1], 'scores': [0.5051378607749939, 0.43528664112091064, 0.5361741185188293, 0.6995182633399963, 0.3121150732040405, 0.3916928172111511, 0.4927845001220703, 0.3694307804107666, 0.34662163257598877, 0.37915635108947754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.1756559610366821})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5957331657409668})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.44517531991004944})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.394253134727478})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36858412623405457})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3647695779800415})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3464103639125824})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37216177582740784})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3805222809314728})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33966976404190063})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3723159730434418})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3477601408958435})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.355163037776947})
store['active_learning_steps'][47]['training']['best_epoch']=10
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9627, 'crossentropy': 0.287559521484375}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6275172233581543})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4453115463256836})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3707829713821411})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.35204440355300903})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.2934255599975586})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3139398694038391})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.26910799741744995})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.25347238779067993})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.2828996777534485})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2754881978034973})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.2749940752983093})
store['active_learning_steps'][47]['eval_training']['best_epoch']=8
store['active_learning_steps'][47]['acquisition']={'indices': [41785, 45919, 40398, 58309, 19837, 25654, 5244, 4311, 9576, 26516], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.44046735763549805, 0.543948233127594, 0.605492353439331, 0.39614778757095337, 0.7203907370567322, 0.530760645866394, 0.5305306911468506, 0.41822850704193115, 0.4947364330291748, 0.5285471677780151]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.267824649810791})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5989918112754822})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3917752504348755})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3253563344478607})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.31553179025650024})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2804532051086426})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3196151852607727})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.360598623752594})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3316752314567566})
store['active_learning_steps'][48]['training']['best_epoch']=6
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9661, 'crossentropy': 0.275898583984375}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6020398139953613})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.46201956272125244})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38166868686676025})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3209007978439331})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3083561062812805})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.303350567817688})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.28230342268943787})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30925437808036804})
store['active_learning_steps'][48]['eval_training']['best_epoch']=7
store['active_learning_steps'][48]['acquisition']={'indices': [42658, 10992, 27409, 8262, 2862, 45019, 1986, 14162, 27781, 24521], 'labels': [0, -1, -1, 0, 6, 8, -1, -1, 2, -1], 'scores': [0.34028100967407227, 0.4482157230377197, 0.41106104850769043, 0.3807023763656616, 0.4843705892562866, 0.5292478799819946, 0.3418436050415039, 0.2007988691329956, 0.30426399409770966, 0.4207512140274048]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.1425352096557617})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6061214208602905})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4349159598350525})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3537828028202057})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3756028413772583})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34685018658638})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3262302875518799})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32700473070144653})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.363325834274292})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3510781526565552})
store['active_learning_steps'][49]['training']['best_epoch']=7
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9628, 'crossentropy': 0.2947642822265625}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6093647480010986})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.43432119488716125})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.405650794506073})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2940431833267212})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.30415746569633484})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3166460692882538})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2658543586730957})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2701793611049652})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.297899067401886})
store['active_learning_steps'][49]['eval_training']['best_epoch']=7
store['active_learning_steps'][49]['acquisition']={'indices': [41094, 6450, 22205, 20830, 17898, 18256, 16362, 9355, 9118, 7036], 'labels': [-1, -1, 5, 9, -1, -1, -1, -1, 9, 4], 'scores': [0.44795286655426025, 0.34317827224731445, 0.4235433340072632, 0.7504960894584656, 0.4536670446395874, 0.5653263330459595, 0.45314693450927734, 0.19503390789031982, 0.8316290378570557, 0.5469650626182556]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0687518119812012})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5383691787719727})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4137899577617645})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30270496010780334})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32044196128845215})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2854011058807373})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30616340041160583})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2963908612728119})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33951446413993835})
store['active_learning_steps'][50]['training']['best_epoch']=6
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9655, 'crossentropy': 0.2737966552734375}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5580120086669922})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.39182567596435547})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3571532666683197})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.31153738498687744})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3141535222530365})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29916220903396606})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2868501543998718})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26822513341903687})
store['active_learning_steps'][50]['eval_training']['best_epoch']=8
store['active_learning_steps'][50]['acquisition']={'indices': [45557, 47448, 15191, 25850, 10012, 23089, 56739, 31635, 53865, 48070], 'labels': [-1, -1, 0, -1, 8, 2, 2, -1, -1, 2], 'scores': [0.26254183053970337, 0.3883323669433594, 0.5733656287193298, 0.3838435411453247, 0.5638112425804138, 0.41522151231765747, 0.538778156042099, 0.4697491526603699, 0.38930177688598633, 0.32124775648117065]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.9924298524856567})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.45946869254112244})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39461660385131836})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3278709650039673})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2942627966403961})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.307628333568573})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3021846413612366})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3103650212287903})
store['active_learning_steps'][51]['training']['best_epoch']=5
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9653, 'crossentropy': 0.2797809326171875}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6740293502807617})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.46164098381996155})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3858795464038849})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3491157293319702})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3297204375267029})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3201780915260315})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31172001361846924})
store['active_learning_steps'][51]['eval_training']['best_epoch']=7
store['active_learning_steps'][51]['acquisition']={'indices': [26635, 23751, 8519, 9963, 16554, 6179, 11599, 20101, 37770, 12928], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.38386428356170654, 0.37460434436798096, 0.35218966007232666, 0.3766833543777466, 0.38487231731414795, 0.41867637634277344, 0.43244409561157227, 0.2847694158554077, 0.3982919454574585, 0.29847919940948486]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9882209897041321})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4943036437034607})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3213834762573242})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3086150288581848})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3056598901748657})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29394596815109253})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3023015856742859})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3207533359527588})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2607225179672241})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3066263198852539})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3260449767112732})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.318881630897522})
store['active_learning_steps'][52]['training']['best_epoch']=9
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9654, 'crossentropy': 0.257783251953125}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.601874828338623})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4400675594806671})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.32524967193603516})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3162282109260559})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2851595878601074})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.29392045736312866})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.26036661863327026})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26109033823013306})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.24368175864219666})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.24690666794776917})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24558866024017334})
store['active_learning_steps'][52]['eval_training']['best_epoch']=9
store['active_learning_steps'][52]['acquisition']={'indices': [29123, 50409, 11271, 29673, 22103, 44520, 38827, 48836, 32328, 11708], 'labels': [-1, -1, -1, -1, 3, -1, -1, -1, -1, -1], 'scores': [0.3351198434829712, 0.38924455642700195, 0.5559340715408325, 0.4187023639678955, 0.47297173738479614, 0.42014074325561523, 0.5386958122253418, 0.3565319776535034, 0.41581225395202637, 0.5380610227584839]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9932695627212524})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5412689447402954})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3864557445049286})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3740777373313904})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3343706727027893})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30869418382644653})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32062482833862305})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3444949984550476})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31846100091934204})
store['active_learning_steps'][53]['training']['best_epoch']=6
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9604, 'crossentropy': 0.292884814453125}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6153625249862671})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4098055362701416})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.37816739082336426})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.325452983379364})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3414042592048645})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2831836938858032})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.24343669414520264})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2651892304420471})
store['active_learning_steps'][53]['eval_training']['best_epoch']=7
store['active_learning_steps'][53]['acquisition']={'indices': [6935, 49947, 50391, 54350, 59385, 51986, 3804, 38275, 20614, 3895], 'labels': [0, -1, 9, 2, 9, 2, 7, 2, 8, -1], 'scores': [0.2644446790218353, 0.29129862785339355, 0.29139018058776855, 0.44541606307029724, 0.41802746057510376, 0.545028030872345, 0.17946785688400269, 0.4591883420944214, 0.5459613800048828, 0.4045846462249756]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.079815149307251})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.46492356061935425})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4226028323173523})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.41934794187545776})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30843695998191833})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.31912049651145935})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3114641010761261})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3228719234466553})
store['active_learning_steps'][54]['training']['best_epoch']=5
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.961, 'crossentropy': 0.2850350830078125}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6515870690345764})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.46563607454299927})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3724840581417084})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.36690378189086914})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.30023193359375})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.33067506551742554})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.29134875535964966})
store['active_learning_steps'][54]['eval_training']['best_epoch']=7
store['active_learning_steps'][54]['acquisition']={'indices': [45680, 5440, 5422, 13986, 20169, 19188, 36818, 52790, 36625, 12188], 'labels': [-1, -1, 7, -1, 4, 1, 7, -1, 1, -1], 'scores': [0.33437633514404297, 0.35363173484802246, 0.3252262473106384, 0.39991748332977295, 0.3911776542663574, 0.6633822917938232, 0.5126466155052185, 0.33078789710998535, 0.2288946509361267, 0.4311925172805786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0737268924713135})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5741386413574219})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.42982688546180725})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.37346118688583374})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35793060064315796})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35425400733947754})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3333836495876312})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35431671142578125})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3558327257633209})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3455410599708557})
store['active_learning_steps'][55]['training']['best_epoch']=7
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9608, 'crossentropy': 0.2877288818359375}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6493158340454102})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.443448007106781})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3748260736465454})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3059999942779541})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.30659934878349304})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2920406758785248})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.27308809757232666})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.2918700575828552})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.26998162269592285})
store['active_learning_steps'][55]['eval_training']['best_epoch']=9
store['active_learning_steps'][55]['acquisition']={'indices': [36515, 3959, 33763, 20959, 53649, 10268, 56773, 27458, 8983, 10732], 'labels': [3, -1, -1, -1, -1, 1, 9, 2, -1, -1], 'scores': [0.5871810913085938, 0.3864927887916565, 0.5671203136444092, 0.4269939661026001, 0.3019707202911377, 0.44846880435943604, 0.380449116230011, 0.7033814191818237, 0.38521599769592285, 0.3242911100387573]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.9629608392715454})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.509258508682251})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.39870327711105347})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3744996190071106})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.34349727630615234})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34020769596099854})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.29344063997268677})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.31176894903182983})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29242995381355286})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3197900652885437})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3694669008255005})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3547726273536682})
store['active_learning_steps'][56]['training']['best_epoch']=9
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.966, 'crossentropy': 0.2528891845703125}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6699010729789734})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4254736304283142})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3667981028556824})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.34475499391555786})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.28582465648651123})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2992323338985443})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2658887505531311})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.25667160749435425})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24351239204406738})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2554503083229065})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2681323289871216})
store['active_learning_steps'][56]['eval_training']['best_epoch']=9
store['active_learning_steps'][56]['acquisition']={'indices': [16647, 35381, 23710, 50736, 58641, 31731, 43543, 47110, 10665, 34707], 'labels': [-1, -1, 9, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.31916356086730957, 0.31880056858062744, 0.4997446537017822, 0.6005786061286926, 0.4889165163040161, 0.29136228561401367, 0.6064503192901611, 0.4701780676841736, 0.4111820459365845, 0.4907163977622986]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9598915576934814})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5251554846763611})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4093610644340515})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3595975935459137})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.32176634669303894})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28695517778396606})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.331516295671463})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33287864923477173})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33678603172302246})
store['active_learning_steps'][57]['training']['best_epoch']=6
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9621, 'crossentropy': 0.2855333984375}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6043082475662231})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3725372552871704})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3595484495162964})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.33081772923469543})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2732411026954651})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.30913984775543213})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.30977410078048706})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.291697233915329})
store['active_learning_steps'][57]['eval_training']['best_epoch']=5
store['active_learning_steps'][57]['acquisition']={'indices': [11711, 29055, 27532, 35371, 24325, 52358, 2151, 53357, 59818, 45502], 'labels': [2, 0, -1, -1, -1, 2, -1, -1, -1, 1], 'scores': [0.7464092373847961, 0.5948594808578491, 0.6088424921035767, 0.5810314416885376, 0.4697718620300293, 0.6721566915512085, 0.4657236337661743, 0.5259130001068115, 0.32809770107269287, 0.4906774163246155]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.1462061405181885})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.569894015789032})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4247698485851288})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3755314350128174})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3172864615917206})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.33572113513946533})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3114688992500305})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.343202143907547})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.34627339243888855})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35601240396499634})
store['active_learning_steps'][58]['training']['best_epoch']=7
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9629, 'crossentropy': 0.2762057861328125}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6198304295539856})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4202064871788025})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3743167221546173})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3578035235404968})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2751355767250061})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.2780610918998718})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.27142688632011414})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2535094916820526})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.30105575919151306})
store['active_learning_steps'][58]['eval_training']['best_epoch']=8
store['active_learning_steps'][58]['acquisition']={'indices': [30517, 32209, 50371, 40655, 10768, 15429, 42437, 38230, 7287, 35419], 'labels': [-1, -1, 7, -1, 4, -1, -1, 9, -1, -1], 'scores': [0.37463968992233276, 0.3845983147621155, 0.5300494432449341, 0.39616256952285767, 0.5476669669151306, 0.4440659284591675, 0.40563684701919556, 0.3441809415817261, 0.30946874618530273, 0.46724653244018555]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.0191367864608765})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5615719556808472})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4475071430206299})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3407704830169678})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.290441632270813})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3365197777748108})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.300430566072464})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2976846694946289})
store['active_learning_steps'][59]['training']['best_epoch']=5
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9586, 'crossentropy': 0.2936350830078125}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6650247573852539})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4343854784965515})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3869763910770416})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.30772876739501953})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3254222273826599})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3213132917881012})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3128175139427185})
store['active_learning_steps'][59]['eval_training']['best_epoch']=4
store['active_learning_steps'][59]['acquisition']={'indices': [14062, 5684, 30658, 6900, 17883, 54739, 18440, 5667, 52647, 6322], 'labels': [8, 6, 4, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5135338306427002, 0.49755680561065674, 0.3745328187942505, 0.3380582332611084, 0.26392531394958496, 0.3465295433998108, 0.49792027473449707, 0.45520055294036865, 0.29169267416000366, 0.30156147480010986]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0091736316680908})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5800346732139587})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.34538811445236206})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3025617301464081})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.29653066396713257})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2969193756580353})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3023678660392761})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2900346517562866})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27058255672454834})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.29120317101478577})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3090974986553192})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32147058844566345})
store['active_learning_steps'][60]['training']['best_epoch']=9
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9681, 'crossentropy': 0.250491650390625}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6845839619636536})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.43437516689300537})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3540479838848114})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3052990734577179})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2809484899044037})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.26906707882881165})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2539152503013611})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.2545982599258423})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.24383226037025452})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.23284289240837097})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.23747064173221588})
store['active_learning_steps'][60]['eval_training']['best_epoch']=10
store['active_learning_steps'][60]['acquisition']={'indices': [635, 38588, 36228, 41828, 41453, 28190, 46523, 22169, 31896, 15402], 'labels': [5, -1, -1, -1, 3, -1, -1, 2, -1, -1], 'scores': [0.4804549217224121, 0.3860940933227539, 0.43767261505126953, 0.614737868309021, 0.5549087524414062, 0.4047497510910034, 0.3047757148742676, 0.40686237812042236, 0.4327046871185303, 0.40639734268188477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.070467233657837})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5325428247451782})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3892357647418976})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3618496358394623})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30884990096092224})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2978942394256592})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31838881969451904})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2956308126449585})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27704834938049316})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3283478617668152})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3012405037879944})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32031774520874023})
store['active_learning_steps'][61]['training']['best_epoch']=9
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9661, 'crossentropy': 0.261587646484375}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5883130431175232})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4140721559524536})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3428501486778259})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.2794283926486969})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.28153738379478455})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.24354562163352966})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.255987286567688})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25186529755592346})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2316230684518814})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23486778140068054})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2340506911277771})
store['active_learning_steps'][61]['eval_training']['best_epoch']=9
store['active_learning_steps'][61]['acquisition']={'indices': [51459, 1248, 15985, 40463, 42341, 15668, 42331, 37967, 33035, 53799], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.3485618829727173, 0.5786556005477905, 0.48665928840637207, 0.5289535522460938, 0.5605694055557251, 0.4346461296081543, 0.5246479511260986, 0.3175831437110901, 0.45459508895874023, 0.5583686828613281]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0239078998565674})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5867944955825806})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4038039743900299})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32872825860977173})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3253660202026367})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3595830798149109})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34949520230293274})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31163591146469116})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.300184965133667})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31593239307403564})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30663901567459106})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3384265899658203})
store['active_learning_steps'][62]['training']['best_epoch']=9
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9686, 'crossentropy': 0.266555322265625}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6282032132148743})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3715935945510864})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.30804163217544556})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3244362473487854})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26014384627342224})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2612575888633728})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.23770755529403687})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2399194836616516})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2374669313430786})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.24464966356754303})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.21781043708324432})
store['active_learning_steps'][62]['eval_training']['best_epoch']=11
store['active_learning_steps'][62]['acquisition']={'indices': [5443, 40414, 49744, 47124, 33371, 26150, 53759, 21896, 55043, 26266], 'labels': [-1, -1, 8, -1, 3, 5, -1, 8, -1, -1], 'scores': [0.6409619450569153, 0.3435540795326233, 0.5611428022384644, 0.33243924379348755, 0.5030892789363861, 0.5774437785148621, 0.3640683889389038, 0.3911324739456177, 0.5671230554580688, 0.41107773780822754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.096585988998413})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.46686965227127075})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3695189356803894})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3150107264518738})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27563148736953735})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2975752353668213})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2945670485496521})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30401456356048584})
store['active_learning_steps'][63]['training']['best_epoch']=5
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9651, 'crossentropy': 0.2744869140625}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6009947061538696})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.42177653312683105})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3818199634552002})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3387436866760254})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.31500405073165894})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2794116139411926})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2628113925457001})
store['active_learning_steps'][63]['eval_training']['best_epoch']=7
store['active_learning_steps'][63]['acquisition']={'indices': [31845, 18144, 28914, 19205, 19362, 29923, 36293, 1832, 56614, 8459], 'labels': [8, -1, -1, -1, 8, -1, -1, -1, -1, 5], 'scores': [0.6181196570396423, 0.3039515018463135, 0.40837371349334717, 0.366502046585083, 0.5592527985572815, 0.44320130348205566, 0.32651257514953613, 0.40024232864379883, 0.3786890506744385, 0.46460390090942383]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0814566612243652})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5752801895141602})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4089727997779846})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.36406460404396057})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3093259334564209})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33191561698913574})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3223813772201538})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3070967197418213})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3188377320766449})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3246166706085205})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3148936927318573})
store['active_learning_steps'][64]['training']['best_epoch']=8
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9655, 'crossentropy': 0.2824544189453125}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7062381505966187})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.461743026971817})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3675026297569275})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.35153043270111084})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2876891791820526})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.28512412309646606})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2700972259044647})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.27287551760673523})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24994432926177979})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2967134416103363})
store['active_learning_steps'][64]['eval_training']['best_epoch']=9
store['active_learning_steps'][64]['acquisition']={'indices': [35949, 30913, 28499, 41002, 52169, 50926, 52659, 19866, 20890, 14722], 'labels': [-1, -1, -1, 7, 2, 5, -1, 3, -1, 0], 'scores': [0.6137241721153259, 0.4499175548553467, 0.5405458211898804, 0.4191961884498596, 0.6133295893669128, 0.22088181972503662, 0.4221614599227905, 0.4957602620124817, 0.3003751039505005, 0.7240109443664551]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9206198453903198})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4548508822917938})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3110750913619995})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28758084774017334})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.292514443397522})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2873873710632324})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2650132477283478})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.261059045791626})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3057946562767029})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23941746354103088})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2724531888961792})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2643088102340698})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29395776987075806})
store['active_learning_steps'][65]['training']['best_epoch']=10
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9667, 'crossentropy': 0.244681591796875}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.62470543384552})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3823974132537842})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30312979221343994})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3140948414802551})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.26885002851486206})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23400291800498962})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24603639543056488})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2544547915458679})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.21671685576438904})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.21886757016181946})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.21838685870170593})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.20690587162971497})
store['active_learning_steps'][65]['eval_training']['best_epoch']=12
store['active_learning_steps'][65]['acquisition']={'indices': [9516, 49749, 13156, 54767, 38374, 2860, 24073, 49903, 18071, 41535], 'labels': [3, -1, 2, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5729035437107086, 0.42499208450317383, 0.7070457339286804, 0.27076876163482666, 0.3499784469604492, 0.38581860065460205, 0.35350537300109863, 0.3161393404006958, 0.3823906183242798, 0.29504215717315674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9747913479804993})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4998743534088135})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3967575132846832})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3207988739013672})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27529096603393555})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32379209995269775})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28706592321395874})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31163978576660156})
store['active_learning_steps'][66]['training']['best_epoch']=5
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9604, 'crossentropy': 0.2849791259765625}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7475017309188843})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.42485368251800537})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3775526285171509})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3510027229785919})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.359877347946167})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3096155524253845})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3038787841796875})
store['active_learning_steps'][66]['eval_training']['best_epoch']=7
store['active_learning_steps'][66]['acquisition']={'indices': [48380, 36008, 50621, 45068, 44506, 1523, 28547, 34058, 45605, 19895], 'labels': [6, 8, -1, -1, -1, -1, -1, 3, -1, -1], 'scores': [0.3992096781730652, 0.4647715091705322, 0.2670825719833374, 0.3508439064025879, 0.33331799507141113, 0.3288379907608032, 0.35580992698669434, 0.4278841018676758, 0.28886842727661133, 0.3429903984069824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.158452033996582})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.573070228099823})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4097704291343689})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3380126357078552})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33029189705848694})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30108147859573364})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32323509454727173})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3027803301811218})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2820802628993988})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31883561611175537})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30975762009620667})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2942945659160614})
store['active_learning_steps'][67]['training']['best_epoch']=9
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9641, 'crossentropy': 0.269923486328125}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5976496934890747})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.40051913261413574})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.34039726853370667})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3138611912727356})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3061491549015045})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2853989005088806})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.24427646398544312})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.2583448886871338})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.25920727849006653})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.24472881853580475})
store['active_learning_steps'][67]['eval_training']['best_epoch']=7
store['active_learning_steps'][67]['acquisition']={'indices': [12558, 9464, 43524, 55689, 9871, 26565, 4594, 18428, 5103, 12598], 'labels': [7, 5, -1, -1, -1, -1, -1, -1, 2, -1], 'scores': [0.44139060378074646, 0.42378437519073486, 0.5059370398521423, 0.3064965009689331, 0.3157185912132263, 0.33554792404174805, 0.4229278564453125, 0.3796113133430481, 0.5409539341926575, 0.3244568109512329]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.182554006576538})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5151804089546204})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3855578899383545})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31001168489456177})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29400789737701416})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28640860319137573})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27476513385772705})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2973805367946625})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3303998112678528})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27585530281066895})
store['active_learning_steps'][68]['training']['best_epoch']=7
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.963, 'crossentropy': 0.28464140625}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6835232973098755})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46608394384384155})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.34755101799964905})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3255128264427185})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30152636766433716})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2891530990600586})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2841328978538513})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27834242582321167})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2628963589668274})
store['active_learning_steps'][68]['eval_training']['best_epoch']=9
store['active_learning_steps'][68]['acquisition']={'indices': [31317, 26170, 48681, 9147, 52170, 26852, 49910, 59690, 9555, 1168], 'labels': [-1, -1, 2, 4, -1, -1, 6, -1, -1, -1], 'scores': [0.37674468755722046, 0.503943681716919, 0.47450071573257446, 0.4270740747451782, 0.579047441482544, 0.3968921899795532, 0.6945611834526062, 0.3864225149154663, 0.37957799434661865, 0.3517613410949707]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1548686027526855})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.531129002571106})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35886240005493164})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32429587841033936})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30688315629959106})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2960740923881531})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2698970139026642})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2822967767715454})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31827202439308167})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2805384397506714})
store['active_learning_steps'][69]['training']['best_epoch']=7
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9714, 'crossentropy': 0.24629736328125}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6347990036010742})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4166509807109833})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.356455534696579})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.341438889503479})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30648261308670044})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3119148313999176})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28609931468963623})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.284612238407135})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2612370550632477})
store['active_learning_steps'][69]['eval_training']['best_epoch']=9
store['active_learning_steps'][69]['acquisition']={'indices': [18086, 35401, 42774, 40414, 44029, 21613, 4105, 30924, 36363, 14152], 'labels': [-1, 3, 4, -1, -1, -1, -1, -1, 6, 7], 'scores': [0.37686729431152344, 0.6288713812828064, 0.5219959020614624, 0.5369027853012085, 0.42808210849761963, 0.30494165420532227, 0.48165619373321533, 0.4244440793991089, 0.4721522331237793, 0.7104242444038391]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.107926368713379})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5235927104949951})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38208699226379395})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30799078941345215})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2792910933494568})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27887415885925293})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2561517655849457})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28578758239746094})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25925540924072266})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31236955523490906})
store['active_learning_steps'][70]['training']['best_epoch']=7
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9685, 'crossentropy': 0.24080126953125}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6171690225601196})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.44814568758010864})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3522006571292877})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.308133602142334})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2892419695854187})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2670325040817261})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25452837347984314})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24140669405460358})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2241341471672058})
store['active_learning_steps'][70]['eval_training']['best_epoch']=9
store['active_learning_steps'][70]['acquisition']={'indices': [32156, 51846, 45190, 56514, 54545, 18679, 25947, 35216, 58979, 14611], 'labels': [-1, -1, -1, 2, -1, -1, 8, -1, -1, -1], 'scores': [0.3258727788925171, 0.3686254024505615, 0.49798381328582764, 0.5249829292297363, 0.32726871967315674, 0.4096219539642334, 0.2739374041557312, 0.28278446197509766, 0.3870443105697632, 0.2938758134841919]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1627495288848877})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.560999870300293})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36919528245925903})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.294472336769104})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27707639336586})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26480841636657715})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2825857996940613})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2591027319431305})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28300780057907104})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2720368206501007})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2933620512485504})
store['active_learning_steps'][71]['training']['best_epoch']=8
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.969, 'crossentropy': 0.2504522216796875}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6320127844810486})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41326025128364563})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3870375454425812})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3029378056526184})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28010356426239014})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2784695029258728})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2966008186340332})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2651071846485138})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25955069065093994})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.23419684171676636})
store['active_learning_steps'][71]['eval_training']['best_epoch']=10
store['active_learning_steps'][71]['acquisition']={'indices': [8204, 47651, 6222, 21067, 29231, 15705, 17354, 28593, 52178, 54977], 'labels': [-1, 3, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5158146619796753, 0.5606697201728821, 0.4061245322227478, 0.2855181097984314, 0.33348381519317627, 0.5307554006576538, 0.49248266220092773, 0.5953993797302246, 0.4547387361526489, 0.34613507986068726]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.194009780883789})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5535929203033447})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33994826674461365})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33441054821014404})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28895509243011475})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2781626284122467})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27473312616348267})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2791594862937927})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27242088317871094})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2914052903652191})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2791058123111725})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26467615365982056})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2819484770298004})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2978205680847168})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28666946291923523})
store['active_learning_steps'][72]['training']['best_epoch']=12
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9671, 'crossentropy': 0.2490508056640625}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6197280883789062})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.38097167015075684})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.32221701741218567})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30139315128326416})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27054494619369507})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.27248096466064453})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.24739056825637817})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.25259512662887573})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.23440584540367126})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.23779866099357605})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.24038726091384888})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.23538655042648315})
store['active_learning_steps'][72]['eval_training']['best_epoch']=9
store['active_learning_steps'][72]['acquisition']={'indices': [31800, 27710, 52210, 17865, 21173, 33984, 58812, 32043, 25468, 29495], 'labels': [-1, -1, -1, -1, -1, -1, 3, -1, -1, -1], 'scores': [0.4169934391975403, 0.2709963321685791, 0.535903811454773, 0.5549701452255249, 0.46657419204711914, 0.5242067575454712, 0.5090335011482239, 0.41813963651657104, 0.5081667900085449, 0.4314742088317871]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0348834991455078})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5116586089134216})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35459697246551514})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3030042350292206})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.299128919839859})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28527575731277466})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28584519028663635})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2839045226573944})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3050517737865448})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2731814682483673})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2952437996864319})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27271878719329834})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27818459272384644})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27250248193740845})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3119868040084839})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30846190452575684})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31450018286705017})
store['active_learning_steps'][73]['training']['best_epoch']=14
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.967, 'crossentropy': 0.264432275390625}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6688706874847412})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4556543827056885})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3593527376651764})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3198728561401367})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.298074334859848})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.24845841526985168})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26846230030059814})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24964174628257751})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.24218817055225372})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.22394418716430664})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.24737954139709473})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.24137869477272034})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2150244116783142})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2288680076599121})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.20500637590885162})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.20843711495399475})
store['active_learning_steps'][73]['eval_training']['best_epoch']=15
store['active_learning_steps'][73]['acquisition']={'indices': [33150, 17924, 13253, 29193, 50425, 51720, 6011, 27200, 55920, 18193], 'labels': [8, -1, -1, -1, -1, 8, -1, -1, -1, -1], 'scores': [0.643436074256897, 0.4985560178756714, 0.6355751156806946, 0.4982173442840576, 0.5549867153167725, 0.6058304905891418, 0.6034210920333862, 0.5287945866584778, 0.505748987197876, 0.6386899352073669]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0970141887664795})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5375430583953857})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3961932063102722})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32482051849365234})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29419994354248047})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28460073471069336})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27596983313560486})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2767673134803772})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2584553360939026})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2654993534088135})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27601146697998047})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25355178117752075})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3309212327003479})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30691641569137573})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3033181130886078})
store['active_learning_steps'][74]['training']['best_epoch']=12
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.968, 'crossentropy': 0.258920263671875}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6651520729064941})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.43546998500823975})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.335713654756546})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3399670720100403})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.2936321496963501})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2553020119667053})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25157299637794495})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.23313817381858826})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.24887344241142273})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.25399017333984375})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2152731716632843})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.22254371643066406})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2328311800956726})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.23059460520744324})
store['active_learning_steps'][74]['eval_training']['best_epoch']=11
store['active_learning_steps'][74]['acquisition']={'indices': [17869, 59735, 26805, 20072, 36107, 34923, 22728, 47643, 58588, 58057], 'labels': [-1, -1, -1, 3, -1, -1, -1, 3, -1, -1], 'scores': [0.5098813772201538, 0.4741109609603882, 0.5144204497337341, 0.5250346660614014, 0.5400612950325012, 0.5649023056030273, 0.6890867948532104, 0.46599945425987244, 0.4845132827758789, 0.610500693321228]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.106605887413025})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6080607175827026})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38460689783096313})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.352680504322052})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34607362747192383})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27424418926239014})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2757203280925751})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2682686150074005})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29904282093048096})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.297351211309433})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29997918009757996})
store['active_learning_steps'][75]['training']['best_epoch']=8
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9681, 'crossentropy': 0.2579892822265625}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6671555042266846})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.40677446126937866})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.33127570152282715})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3078170418739319})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29224735498428345})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.28730547428131104})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2598262429237366})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2517782747745514})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.262241005897522})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2411808967590332})
store['active_learning_steps'][75]['eval_training']['best_epoch']=10
store['active_learning_steps'][75]['acquisition']={'indices': [9436, 14337, 6320, 9940, 47555, 48687, 38408, 39891, 53693, 1135], 'labels': [4, 7, 0, 4, 0, 5, 5, 4, 4, 5], 'scores': [0.5440528988838196, 0.38997912406921387, 0.45947563648223877, 0.6253581047058105, 0.25683820247650146, 0.44683459401130676, 0.5084632039070129, 0.5701996088027954, 0.6847874522209167, 0.47712957859039307]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9686330556869507})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4958849549293518})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4118371307849884})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3009772300720215})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2575059235095978})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.252288281917572})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26304417848587036})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23909005522727966})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24291741847991943})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2587842345237732})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26638880372047424})
store['active_learning_steps'][76]['training']['best_epoch']=8
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9716, 'crossentropy': 0.2389666015625}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6384291648864746})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40416011214256287})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.37197887897491455})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2989429235458374})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2656886875629425})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26674485206604004})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25786730647087097})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25650203227996826})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25344884395599365})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2255835086107254})
store['active_learning_steps'][76]['eval_training']['best_epoch']=10
store['active_learning_steps'][76]['acquisition']={'indices': [35103, 48735, 55683, 21231, 34284, 41551, 38750, 32684, 1737, 49082], 'labels': [8, -1, 8, 8, -1, -1, -1, -1, -1, 3], 'scores': [0.3001658320426941, 0.5217534303665161, 0.5376132726669312, 0.304287314414978, 0.32896125316619873, 0.3752172589302063, 0.3881375789642334, 0.4391758441925049, 0.4035661220550537, 0.39781612157821655]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.1544145345687866})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6095645427703857})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39090466499328613})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36469775438308716})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2954059839248657})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30256974697113037})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26659291982650757})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30944257974624634})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29133275151252747})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2672000527381897})
store['active_learning_steps'][77]['training']['best_epoch']=7
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.969, 'crossentropy': 0.2565890625}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6433614492416382})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4246826767921448})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33420267701148987})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29387426376342773})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27652424573898315})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2667872905731201})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27538079023361206})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2534515857696533})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23341907560825348})
store['active_learning_steps'][77]['eval_training']['best_epoch']=9
store['active_learning_steps'][77]['acquisition']={'indices': [17601, 59350, 18890, 57985, 28578, 50572, 50201, 40373, 36696, 56530], 'labels': [-1, -1, -1, 4, -1, 1, -1, -1, -1, -1], 'scores': [0.3554278612136841, 0.47313392162323, 0.24292361736297607, 0.7295501828193665, 0.4812333583831787, 0.4955987334251404, 0.2802478075027466, 0.3777039051055908, 0.33758413791656494, 0.24706757068634033]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.2015841007232666})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5596656799316406})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41719377040863037})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37719568610191345})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29247450828552246})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25766754150390625})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27039217948913574})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.262536883354187})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2796521782875061})
store['active_learning_steps'][78]['training']['best_epoch']=6
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9668, 'crossentropy': 0.2546450927734375}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7341943979263306})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.438391774892807})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3553599715232849})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34913575649261475})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31549108028411865})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26670193672180176})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26831528544425964})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.25071048736572266})
store['active_learning_steps'][78]['eval_training']['best_epoch']=8
store['active_learning_steps'][78]['acquisition']={'indices': [51395, 9963, 1284, 42629, 22058, 6211, 46069, 54586, 19969, 25173], 'labels': [-1, -1, -1, -1, -1, 2, -1, 9, -1, -1], 'scores': [0.3172779083251953, 0.5781019926071167, 0.45012032985687256, 0.43016982078552246, 0.47656679153442383, 0.4391191601753235, 0.35467207431793213, 0.42026233673095703, 0.3240373134613037, 0.4732487201690674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0782833099365234})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5676240921020508})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.387814998626709})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3395293354988098})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3017996549606323})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2868962585926056})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30034497380256653})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2843165099620819})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27735239267349243})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.285744309425354})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2880425751209259})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3076992630958557})
store['active_learning_steps'][79]['training']['best_epoch']=9
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.2466068603515625}
store['active_learning_steps'][79]['eval_training']={}
store['active_learning_steps'][79]['eval_training']['epochs']=[]
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.691277265548706})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4400044083595276})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33377689123153687})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.33329805731773376})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.27326101064682007})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2558196783065796})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2803232669830322})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2476915717124939})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.23494172096252441})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2505602240562439})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24005290865898132})
store['active_learning_steps'][79]['eval_training']['best_epoch']=9
store['active_learning_steps'][79]['acquisition']={'indices': [30289, 32413, 34908, 40012, 58616, 12509, 40953, 25914, 17831, 147], 'labels': [-1, 1, 5, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4273572564125061, 0.4828759431838989, 0.6690106093883514, 0.5632107257843018, 0.4628635048866272, 0.39294642210006714, 0.540578305721283, 0.543769121170044, 0.38614940643310547, 0.5687109231948853]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.1275041103363037})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48082223534584045})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3608291745185852})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33349478244781494})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.336581826210022})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2673513889312744})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2930418848991394})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2892857789993286})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3104558289051056})
store['active_learning_steps'][80]['training']['best_epoch']=6
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9635, 'crossentropy': 0.27016279296875}
store['active_learning_steps'][80]['eval_training']={}
store['active_learning_steps'][80]['eval_training']['epochs']=[]
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6543377041816711})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4319537878036499})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3910987377166748})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32650187611579895})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.321043998003006})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28964728116989136})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3037458062171936})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2960326373577118})
store['active_learning_steps'][80]['eval_training']['best_epoch']=6
store['active_learning_steps'][80]['acquisition']={'indices': [21481, 4822, 26282, 56914, 47454, 49067, 51601, 14058, 24826, 58157], 'labels': [-1, 4, -1, 0, -1, 2, -1, -1, 8, -1], 'scores': [0.396356463432312, 0.4531223773956299, 0.410306453704834, 0.5083906650543213, 0.33649468421936035, 0.34049272537231445, 0.21251773834228516, 0.4477485418319702, 0.33414316177368164, 0.4732469320297241]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0867061614990234})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4782842993736267})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39919018745422363})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3341415524482727})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2957633137702942})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26692861318588257})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2691907584667206})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2691810429096222})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27037274837493896})
store['active_learning_steps'][81]['training']['best_epoch']=6
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9697, 'crossentropy': 0.2569855224609375}
store['active_learning_steps'][81]['eval_training']={}
store['active_learning_steps'][81]['eval_training']['epochs']=[]
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6472454071044922})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4578746259212494})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34718140959739685})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34399843215942383})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2881740927696228})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2680250406265259})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30193233489990234})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2560899257659912})
store['active_learning_steps'][81]['eval_training']['best_epoch']=8
store['active_learning_steps'][81]['acquisition']={'indices': [37720, 55042, 30978, 46231, 56472, 58772, 1784, 230, 18367, 6844], 'labels': [8, -1, -1, 8, 7, -1, 6, -1, -1, -1], 'scores': [0.4854797124862671, 0.26699888706207275, 0.30464309453964233, 0.30866074562072754, 0.3409769833087921, 0.3432159423828125, 0.35731926560401917, 0.32826709747314453, 0.27500706911087036, 0.4714428186416626]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.1559175252914429})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5504920482635498})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4028396010398865})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2815522253513336})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26585251092910767})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.255770742893219})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2894042730331421})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27937719225883484})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27405136823654175})
store['active_learning_steps'][82]['training']['best_epoch']=6
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9707, 'crossentropy': 0.24964404296875}
store['active_learning_steps'][82]['eval_training']={}
store['active_learning_steps'][82]['eval_training']['epochs']=[]
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7555445432662964})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4760921895503998})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37755024433135986})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3193104863166809})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2886502742767334})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27355653047561646})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25037556886672974})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2775912582874298})
store['active_learning_steps'][82]['eval_training']['best_epoch']=7
store['active_learning_steps'][82]['acquisition']={'indices': [24131, 14220, 34344, 56539, 28946, 33182, 58694, 49487, 51041, 26389], 'labels': [-1, -1, -1, -1, -1, -1, -1, 8, -1, 0], 'scores': [0.39813733100891113, 0.35900044441223145, 0.407551646232605, 0.4381234645843506, 0.4384075403213501, 0.3872349262237549, 0.4217606782913208, 0.5366165041923523, 0.3325989246368408, 0.5003130435943604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1829816102981567})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5726662874221802})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37461695075035095})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.287115216255188})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27341192960739136})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25446128845214844})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.25262922048568726})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2590962052345276})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27618280053138733})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23312562704086304})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26341432332992554})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24401618540287018})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.2588731646537781})
store['active_learning_steps'][83]['training']['best_epoch']=10
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9716, 'crossentropy': 0.2412478515625}
store['active_learning_steps'][83]['eval_training']={}
store['active_learning_steps'][83]['eval_training']['epochs']=[]
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5786603689193726})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3545641303062439})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32198086380958557})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2597000300884247})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2427373230457306})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24462924897670746})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2320849895477295})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2278943657875061})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.217172771692276})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23175066709518433})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.21428659558296204})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.21513968706130981})
store['active_learning_steps'][83]['eval_training']['best_epoch']=11
store['active_learning_steps'][83]['acquisition']={'indices': [3803, 28988, 51231, 38701, 13780, 34725, 56220, 30702, 50023, 26966], 'labels': [-1, 7, -1, -1, -1, -1, 7, -1, -1, -1], 'scores': [0.420910120010376, 0.4881662130355835, 0.45967578887939453, 0.5167346000671387, 0.27543389797210693, 0.35268139839172363, 0.37446755170822144, 0.31685173511505127, 0.34312140941619873, 0.49156129360198975]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1411142349243164})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6669164896011353})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4110594689846039})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3435005843639374})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3319544196128845})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3098818063735962})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27841636538505554})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31125879287719727})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3062741756439209})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2674115300178528})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31648290157318115})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.280398964881897})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31365758180618286})
store['active_learning_steps'][84]['training']['best_epoch']=10
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.264155712890625}
store['active_learning_steps'][84]['eval_training']={}
store['active_learning_steps'][84]['eval_training']['epochs']=[]
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6402318477630615})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.38785260915756226})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33943721652030945})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3130751848220825})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27013176679611206})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3003041744232178})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2429245412349701})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2802616357803345})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24037927389144897})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25872448086738586})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26180416345596313})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.22554424405097961})
store['active_learning_steps'][84]['eval_training']['best_epoch']=12
store['active_learning_steps'][84]['acquisition']={'indices': [6269, 32402, 45048, 12377, 32453, 9426, 9290, 39320, 14355, 59336], 'labels': [3, -1, 4, 3, -1, -1, 9, 6, 2, -1], 'scores': [0.4634096026420593, 0.5935474634170532, 0.5130332708358765, 0.4851933717727661, 0.36733150482177734, 0.46132051944732666, 0.4242132902145386, 0.4030539393424988, 0.36887288093566895, 0.41517674922943115]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.2603750228881836})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5372713804244995})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.376875102519989})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3203420639038086})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31363171339035034})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28284507989883423})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2727507948875427})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2543267607688904})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24254260957241058})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23756350576877594})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2381269931793213})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2389635145664215})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24991878867149353})
store['active_learning_steps'][85]['training']['best_epoch']=10
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9713, 'crossentropy': 0.23577568359375}
store['active_learning_steps'][85]['eval_training']={}
store['active_learning_steps'][85]['eval_training']['epochs']=[]
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7072511315345764})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4413050711154938})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.34838616847991943})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3138478398323059})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26934194564819336})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27414393424987793})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.249827578663826})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24973884224891663})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23825326561927795})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2574329376220703})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2446126639842987})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2374354898929596})
store['active_learning_steps'][85]['eval_training']['best_epoch']=12
store['active_learning_steps'][85]['acquisition']={'indices': [20211, 30008, 44236, 2090, 38641, 27079, 8688, 21636, 4427, 36761], 'labels': [4, -1, -1, -1, -1, -1, 6, -1, -1, -1], 'scores': [0.4409734606742859, 0.41000187397003174, 0.39708375930786133, 0.5729589462280273, 0.48342180252075195, 0.4577469825744629, 0.46060043573379517, 0.2869380712509155, 0.3510175943374634, 0.42638325691223145]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.2627450227737427})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5598900318145752})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3997524380683899})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31162112951278687})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3066626489162445})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26209041476249695})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2911687195301056})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2927662432193756})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2618356943130493})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2662026882171631})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27408379316329956})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.29354122281074524})
store['active_learning_steps'][86]['training']['best_epoch']=9
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.971, 'crossentropy': 0.24321474609375}
store['active_learning_steps'][86]['eval_training']={}
store['active_learning_steps'][86]['eval_training']['epochs']=[]
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7078239917755127})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4180167317390442})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35966068506240845})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3063954710960388})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2760869264602661})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25733810663223267})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24740572273731232})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.22595325112342834})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2296050786972046})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.22467561066150665})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.21366184949874878})
store['active_learning_steps'][86]['eval_training']['best_epoch']=11
store['active_learning_steps'][86]['acquisition']={'indices': [39561, 38321, 8919, 14588, 8641, 52879, 20536, 29212, 51948, 44591], 'labels': [2, -1, -1, 3, 9, -1, -1, 7, -1, -1], 'scores': [0.5336800813674927, 0.49290168285369873, 0.4513004422187805, 0.5247835516929626, 0.5479947328567505, 0.3826695680618286, 0.3051375150680542, 0.4332619905471802, 0.44567203521728516, 0.5285650491714478]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.042062520980835})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5464670658111572})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3754085302352905})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31625986099243164})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31004539132118225})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26177364587783813})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29084938764572144})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2510908544063568})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2822890281677246})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27919137477874756})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.27456581592559814})
store['active_learning_steps'][87]['training']['best_epoch']=8
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9714, 'crossentropy': 0.2515926513671875}
store['active_learning_steps'][87]['eval_training']={}
store['active_learning_steps'][87]['eval_training']['epochs']=[]
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6601386070251465})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.39262187480926514})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34797531366348267})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3033062517642975})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27736014127731323})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24285659193992615})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2589707374572754})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2531717121601105})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23035070300102234})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24128836393356323})
store['active_learning_steps'][87]['eval_training']['best_epoch']=9
store['active_learning_steps'][87]['acquisition']={'indices': [17670, 7072, 34189, 14329, 40803, 9180, 28794, 558, 29723, 31527], 'labels': [-1, -1, -1, 0, -1, 3, -1, -1, 5, -1], 'scores': [0.34432995319366455, 0.44783616065979004, 0.44195520877838135, 0.5867425203323364, 0.49987077713012695, 0.6180861592292786, 0.4975042939186096, 0.5813621878623962, 0.2914014458656311, 0.2910560369491577]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.175227165222168})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.6698399782180786})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4179156422615051})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3306015729904175})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30041205883026123})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28315362334251404})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23762765526771545})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2860136032104492})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2673681676387787})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.271503210067749})
store['active_learning_steps'][88]['training']['best_epoch']=7
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9725, 'crossentropy': 0.232049658203125}
store['active_learning_steps'][88]['eval_training']={}
store['active_learning_steps'][88]['eval_training']['epochs']=[]
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5852107405662537})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4046149253845215})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3455507755279541})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3062073588371277})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2895594537258148})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25321465730667114})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24382248520851135})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2835373878479004})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2517735958099365})
store['active_learning_steps'][88]['eval_training']['best_epoch']=7
store['active_learning_steps'][88]['acquisition']={'indices': [38698, 50517, 49294, 25058, 18130, 47567, 20011, 46858, 42782, 29387], 'labels': [5, -1, -1, -1, 8, -1, -1, -1, 7, -1], 'scores': [0.5812804102897644, 0.48057734966278076, 0.5354243516921997, 0.44826173782348633, 0.39758920669555664, 0.4004318118095398, 0.4138360023498535, 0.4550849199295044, 0.5362803339958191, 0.41770321130752563]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.2439322471618652})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6718838810920715})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40896838903427124})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3400678336620331})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28026941418647766})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2619438171386719})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25332316756248474})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2756692171096802})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2673209309577942})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.26214396953582764})
store['active_learning_steps'][89]['training']['best_epoch']=7
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.968, 'crossentropy': 0.2592846435546875}
