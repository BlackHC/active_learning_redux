store = {}
store['timestamp']=1620908040
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=3']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=3
store['worker_id']=3
store['num_workers']=20
store['config']={'seed': 1238, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 1000, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.0615382194519043})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.4197230339050293})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.558882713317871})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9552721977233887})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7052, 'crossentropy': 1.8186998046875}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0878674983978271})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.0167542695999146})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0307573080062866})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [54954, 9306, 31843, 32116, 49137, 6885, 36473, 54007, 58080, 33979], 'labels': [8, 9, -1, 8, 3, 1, 8, 4, 3, 8], 'scores': [0.7340605854988098, 0.7410205006599426, 0.4171743392944336, 0.5799230337142944, 0.8503836989402771, 0.6017518639564514, 0.6492919921875, 0.5603106021881104, 0.6560338139533997, 0.7232935428619385]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.093514919281006})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.198695659637451})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.3609330654144287})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 2.2777411937713623})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7313, 'crossentropy': 1.749530078125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.0474281311035156})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.043764352798462})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.016741156578064})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [23763, 40874, 5854, 10045, 27257, 46668, 21402, 42678, 36821, 26341], 'labels': [5, 6, -1, 0, -1, -1, 1, 3, 6, -1], 'scores': [0.6427984237670898, 0.8079805970191956, 0.5331230163574219, 0.615796685218811, 0.5466604232788086, 0.8101773262023926, 0.45977938175201416, 1.1035905480384827, 0.8496386408805847, 0.6141282320022583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.7357538938522339})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.940577745437622})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.1685171127319336})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 2.1556267738342285})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.735, 'crossentropy': 1.542375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0655159950256348})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 0.999644935131073})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.9510773420333862})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [3872, 26848, 54785, 53170, 18716, 46631, 20712, 57882, 30011, 34605], 'labels': [8, -1, -1, 8, 6, 8, 8, 0, 3, -1], 'scores': [0.6957403421401978, 0.4424762725830078, 0.414456844329834, 0.7320769429206848, 0.6365687251091003, 0.510783314704895, 0.5196129083633423, 0.6500017046928406, 0.5720750093460083, 0.48670172691345215]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.645790696144104})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.751578450202942})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.0201046466827393})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.055171489715576})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7621, 'crossentropy': 1.39772333984375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.0648438930511475})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.9984689354896545})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9975458383560181})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [19058, 1370, 21530, 24726, 28360, 7965, 14825, 14667, 50618, 55268], 'labels': [1, 9, 5, 6, 5, 4, 3, 9, 6, 8], 'scores': [0.4887627959251404, 0.3974685072898865, 0.5724754929542542, 0.7219258546829224, 0.6417549252510071, 0.6187639236450195, 0.6796628832817078, 0.5909128189086914, 0.4628645181655884, 0.5968442559242249]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.3323856592178345})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.4326171875})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.7245032787322998})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.9752893447875977})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7787, 'crossentropy': 1.22618681640625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9678672552108765})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 0.9209060668945312})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 0.947359561920166})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [36693, 22358, 54943, 17651, 54286, 45181, 13557, 38720, 53658, 6011], 'labels': [2, 2, 0, 5, 2, 8, -1, 2, 2, 5], 'scores': [0.6194742321968079, 0.5213137865066528, 0.5309661626815796, 0.5545486211776733, 0.5908742547035217, 0.7212720513343811, 0.31100165843963623, 0.5911039710044861, 0.35816413164138794, 0.6078048348426819]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.2702431678771973})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.5190114974975586})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.7077182531356812})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 2.041566848754883})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7944, 'crossentropy': 1.06124482421875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9151960611343384})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.8766992092132568})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 0.8474401235580444})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [49634, 56515, 49094, 17121, 33357, 40905, 51241, 40984, 20784, 43430], 'labels': [8, -1, 5, 8, 3, 5, 2, 9, 5, -1], 'scores': [0.3006083369255066, 0.22829580307006836, 0.39410048723220825, 0.38407009840011597, 0.5117343664169312, 0.7120408415794373, 0.4817734360694885, 0.5176917314529419, 0.6980337500572205, 0.21447443962097168]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.3481652736663818})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.3868343830108643})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.7317171096801758})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.6799192428588867})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7912, 'crossentropy': 1.137856640625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 0.9898424744606018})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 0.9435662031173706})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 0.9140831232070923})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [13816, 53023, 59735, 56167, 34678, 34508, 41556, 40837, 1269, 22889], 'labels': [0, 7, 3, 7, 8, 0, 0, 7, -1, 6], 'scores': [0.5266344547271729, 0.4001598358154297, 0.28410470485687256, 0.46270477771759033, 0.5388104915618896, 0.4911404848098755, 0.5554521083831787, 0.5235042572021484, 0.3192709684371948, 0.323117733001709]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.1828199625015259})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.4752256870269775})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.5917503833770752})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.786898136138916})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8023, 'crossentropy': 1.067987109375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 0.9729918837547302})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 0.9035413265228271})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 0.85113525390625})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [14520, 31899, 58277, 24388, 9046, 50026, 8837, 8772, 42802, 50770], 'labels': [4, 7, -1, -1, 4, 0, 9, 1, 9, 3], 'scores': [0.6423230767250061, 0.4436570405960083, 0.31025099754333496, 0.3049588203430176, 0.5025326013565063, 0.3382232189178467, 0.5404329299926758, 0.600239634513855, 0.5863972306251526, 0.34185367822647095]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.098346471786499})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.2309606075286865})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.382016897201538})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.5819690227508545})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8287, 'crossentropy': 0.96557197265625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9293442368507385})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8233484029769897})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.8482219576835632})
store['active_learning_steps'][8]['eval_training']['best_epoch']=2
store['active_learning_steps'][8]['acquisition']={'indices': [36157, 50981, 160, 36839, 918, 25640, 19557, 27000, 57240, 24646], 'labels': [7, 4, 8, 5, 7, 9, 8, 5, 5, 8], 'scores': [0.5165252685546875, 0.4972505569458008, 0.419384241104126, 0.5151891708374023, 0.4311659336090088, 0.5630631446838379, 0.4425050616264343, 0.5011447668075562, 0.43220382928848267, 0.33509761095046997]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8940545320510864})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.9018011093139648})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9016207456588745})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.989437460899353})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.859, 'crossentropy': 0.811584716796875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8696892857551575})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7786352038383484})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7440264225006104})
store['active_learning_steps'][9]['eval_training']['best_epoch']=3
store['active_learning_steps'][9]['acquisition']={'indices': [31428, 53483, 22648, 20176, 43248, 30183, 19566, 14100, 32757, 8876], 'labels': [3, -1, 9, 4, 9, 3, -1, 5, 5, 5], 'scores': [0.3002443313598633, 0.19997727870941162, 0.4562144875526428, 0.36320924758911133, 0.4276617765426636, 0.38831865787506104, 0.4218684434890747, 0.47415924072265625, 0.36710619926452637, 0.4140623211860657]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8665964007377625})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.778113603591919})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8486825227737427})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8618273735046387})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8306956887245178})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8846, 'crossentropy': 0.674351513671875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7519304752349854})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6189427375793457})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.5643907785415649})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.581484317779541})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [51785, 2546, 57407, 41965, 54754, 21661, 52685, 39724, 13396, 32672], 'labels': [-1, 4, -1, 2, -1, -1, -1, 9, 8, 9], 'scores': [0.448097825050354, 0.4111521244049072, 0.40342044830322266, 0.5359598994255066, 0.4744873046875, 0.3620356321334839, 0.49689507484436035, 0.4449964761734009, 0.2948383092880249, 0.34990406036376953]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8242381811141968})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.8395290374755859})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7993224859237671})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8436330556869507})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9136441946029663})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8477554321289062})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.8898, 'crossentropy': 0.764747802734375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.719241738319397})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5890085697174072})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.545198917388916})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5225954055786133})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.5182862877845764})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [19466, 44607, 1149, 20091, 16676, 46582, 17338, 3383, 7610, 49038], 'labels': [2, -1, 4, 5, 3, -1, -1, -1, -1, 5], 'scores': [0.61794114112854, 0.5006051063537598, 0.5676504373550415, 0.5633536279201508, 0.6815226078033447, 0.5843203067779541, 0.43185532093048096, 0.496371865272522, 0.4218834638595581, 0.2589190602302551]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.902338981628418})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7615628242492676})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8091733455657959})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8490659594535828})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7802388668060303})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8949, 'crossentropy': 0.679885498046875}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.7305821180343628})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6007598638534546})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5516380071640015})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.5907168388366699})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [25654, 59415, 5646, 50651, 33676, 32325, 32766, 21985, 44446, 52744], 'labels': [-1, -1, -1, -1, -1, -1, 8, -1, 1, 7], 'scores': [0.45397889614105225, 0.33816587924957275, 0.40242475271224976, 0.22473692893981934, 0.5562649965286255, 0.49045318365097046, 0.4134918451309204, 0.5435682535171509, 0.4969816207885742, 0.46626144647598267]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8099958896636963})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7792967557907104})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7902750968933105})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8905273675918579})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8996899127960205})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8843, 'crossentropy': 0.663370703125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7128837704658508})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5924468636512756})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6103078722953796})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5629090070724487})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [16035, 47889, 17540, 16102, 44903, 7294, 25783, 51986, 34883, 425], 'labels': [9, 5, 1, 6, 3, 6, 0, 2, 8, 3], 'scores': [0.4859120845794678, 0.5265495777130127, 0.47968119382858276, 0.4263761043548584, 0.3760082721710205, 0.4860461354255676, 0.3653237819671631, 0.3862428069114685, 0.32104772329330444, 0.3524819612503052]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8859171867370605})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6908433437347412})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7502127885818481})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7068067789077759})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7448821067810059})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.8905, 'crossentropy': 0.6624908203125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7420226335525513})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6299153566360474})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5474255681037903})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5683678388595581})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [7600, 55064, 29390, 5740, 12424, 27840, 21471, 4650, 23943, 33397], 'labels': [3, 9, 9, 9, 2, 3, -1, -1, -1, -1], 'scores': [0.34726637601852417, 0.5088241696357727, 0.645606517791748, 0.5781687498092651, 0.65346360206604, 0.40275460481643677, 0.3338193893432617, 0.3903161287307739, 0.29279589653015137, 0.38810086250305176]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8252651691436768})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6629491448402405})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6949288845062256})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.668583869934082})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.735350489616394})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9047, 'crossentropy': 0.632683251953125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7153096199035645})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5718619227409363})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5471097230911255})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5112060308456421})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [23912, 52358, 50279, 30917, 52866, 10573, 12536, 45602, 20382, 52795], 'labels': [5, 2, 5, -1, 7, 7, 3, 5, 2, -1], 'scores': [0.6134560704231262, 0.6997799873352051, 0.5599278211593628, 0.4290503263473511, 0.5424187183380127, 0.6012680530548096, 0.38956356048583984, 0.49272477626800537, 0.4707992672920227, 0.3762843608856201]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8246280550956726})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6141096353530884})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6061370372772217})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6131765842437744})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6125837564468384})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7192078828811646})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9177, 'crossentropy': 0.5596890625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.649945080280304})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.49012550711631775})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4724203944206238})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4396938979625702})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.44958943128585815})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [50144, 9538, 58874, 11378, 9410, 12308, 39194, 46615, 34665, 22772], 'labels': [9, 7, 3, 4, 4, 8, 0, -1, 9, 9], 'scores': [0.48383116722106934, 0.6756409406661987, 0.56791090965271, 0.47886621952056885, 0.42771124839782715, 0.4017261862754822, 0.20141267776489258, 0.4017658233642578, 0.3584171533584595, 0.4293075203895569]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8649634718894958})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6821644306182861})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6356971263885498})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7096279263496399})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6984392404556274})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6594458222389221})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9135, 'crossentropy': 0.59612001953125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6646479368209839})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.514641284942627})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4549747109413147})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4696164131164551})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.438218355178833})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [57191, 30443, 13018, 50453, 45822, 36196, 29004, 22033, 44157, 58429], 'labels': [2, 2, 8, -1, 3, -1, 2, 5, 3, 2], 'scores': [0.6076316237449646, 0.5304062366485596, 0.5592612624168396, 0.4020345211029053, 0.4478692412376404, 0.4505981206893921, 0.42658984661102295, 0.5865055322647095, 0.5205514430999756, 0.47347140312194824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9287368655204773})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7120549082756042})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.603569507598877})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.582455039024353})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6526430249214172})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6432058811187744})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6722855567932129})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9216, 'crossentropy': 0.55593056640625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6438759565353394})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.48014065623283386})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4300593137741089})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.43280938267707825})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.463066965341568})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4279964864253998})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [30974, 39355, 41293, 32774, 13481, 28512, 31184, 32994, 45409, 24088], 'labels': [-1, 8, 4, 8, -1, 5, 9, 6, -1, -1], 'scores': [0.27984511852264404, 0.7422664761543274, 0.6539099216461182, 0.523352324962616, 0.4090992212295532, 0.6698891520500183, 0.5299694538116455, 0.4499221444129944, 0.6067502498626709, 0.39159512519836426]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.9440487623214722})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5980945825576782})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5809805393218994})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5520467162132263})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5516336560249329})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5849286317825317})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5794740915298462})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6595813035964966})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9349, 'crossentropy': 0.457610205078125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6410166025161743})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.45582401752471924})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.42094770073890686})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4115840792655945})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.398730993270874})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.40810829401016235})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.35194289684295654})
store['active_learning_steps'][19]['eval_training']['best_epoch']=7
store['active_learning_steps'][19]['acquisition']={'indices': [15926, 31717, 38524, 53522, 6292, 55265, 3625, 10086, 52737, 21174], 'labels': [-1, 4, 4, 2, -1, -1, -1, 7, -1, 2], 'scores': [0.2709064483642578, 0.4828566312789917, 0.6637516021728516, 0.6865306496620178, 0.4219210147857666, 0.49697422981262207, 0.32595181465148926, 0.4133073091506958, 0.4396165609359741, 0.48146259784698486]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8620256185531616})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5526659488677979})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5057960748672485})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5049138069152832})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5076829195022583})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.623700737953186})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5691182017326355})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9391, 'crossentropy': 0.44913916015625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6638714671134949})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.49315279722213745})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.42660844326019287})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.38728493452072144})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.34705960750579834})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.36456790566444397})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [44255, 42310, 59361, 17935, 34406, 34565, 36603, 45491, 1019, 35332], 'labels': [6, 2, 8, -1, 4, 8, -1, 5, 7, 9], 'scores': [0.5931130051612854, 0.31680601835250854, 0.6636537313461304, 0.39855456352233887, 0.5203213691711426, 0.4418415427207947, 0.2734560966491699, 0.542118489742279, 0.5776644349098206, 0.3732234835624695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8539896607398987})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6228131055831909})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4902620315551758})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.48467516899108887})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5054683685302734})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5004628896713257})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4926011562347412})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9407, 'crossentropy': 0.4388330078125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6538627743721008})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4852662682533264})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.403850257396698})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.39915931224823})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.38488340377807617})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.37824273109436035})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [54051, 10982, 50802, 46530, 30669, 50024, 21023, 14631, 34829, 24943], 'labels': [5, 1, 2, 4, -1, 0, -1, 1, 5, 3], 'scores': [0.3953106999397278, 0.6168387532234192, 0.43190330266952515, 0.6582173109054565, 0.34186840057373047, 0.6342595815658569, 0.44797277450561523, 0.6426249742507935, 0.7539001107215881, 0.6829575896263123]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9042811393737793})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5398735404014587})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48847442865371704})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5016132593154907})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.529016375541687})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.530350923538208})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9372, 'crossentropy': 0.443452392578125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6655746698379517})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5341238379478455})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43828099966049194})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4192078113555908})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.41318729519844055})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [4135, 29259, 54950, 45026, 49064, 1674, 1458, 33246, 19945, 5129], 'labels': [-1, 8, 8, 8, 8, 9, -1, -1, 5, 2], 'scores': [0.2846485376358032, 0.5006753206253052, 0.5709584951400757, 0.6379965543746948, 0.634151816368103, 0.47041743993759155, 0.33287274837493896, 0.3018975257873535, 0.756536066532135, 0.5648717284202576]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0300726890563965})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5898724794387817})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4616926908493042})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.45038795471191406})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5136513710021973})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5094950199127197})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5473921298980713})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9452, 'crossentropy': 0.4304341796875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6916133165359497})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4885372519493103})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4517558813095093})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.39266741275787354})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.38163286447525024})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35493531823158264})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [1512, 32747, 17465, 41624, 35389, 41453, 39533, 47910, 31989, 26389], 'labels': [0, 8, 1, 3, 1, 3, 1, 1, -1, 0], 'scores': [0.6300010085105896, 0.49261903762817383, 0.573364794254303, 0.3812446594238281, 0.549617350101471, 0.6317289471626282, 0.41736292839050293, 0.7437873482704163, 0.48286867141723633, 0.5712614059448242]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8440403342247009})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5063311457633972})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.47849324345588684})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.442524790763855})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5079887509346008})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4886263906955719})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.47575250267982483})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9466, 'crossentropy': 0.422446435546875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6399599313735962})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5095306634902954})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.42178401350975037})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42593443393707275})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3644944429397583})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3648102283477783})
store['active_learning_steps'][24]['eval_training']['best_epoch']=5
store['active_learning_steps'][24]['acquisition']={'indices': [23471, 43516, 4972, 26866, 24626, 5553, 1944, 131, 5307, 26733], 'labels': [6, -1, -1, 3, -1, -1, -1, -1, 2, 2], 'scores': [0.6641804873943329, 0.5287277102470398, 0.48671257495880127, 0.5483364462852478, 0.6490134000778198, 0.5199308395385742, 0.6446356177330017, 0.4654277563095093, 0.5043267607688904, 0.6855604648590088]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9898414015769958})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5110717415809631})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44989874958992004})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.45506471395492554})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44340425729751587})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4498730003833771})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5075980424880981})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4461074471473694})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9498, 'crossentropy': 0.393166943359375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6508573293685913})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4716067612171173})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4067787230014801})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3994789719581604})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3516092002391815})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.35594111680984497})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3348630666732788})
store['active_learning_steps'][25]['eval_training']['best_epoch']=7
store['active_learning_steps'][25]['acquisition']={'indices': [32067, 32974, 14697, 7478, 53463, 37758, 53556, 39501, 5574, 53322], 'labels': [-1, 1, 8, 9, -1, 0, 8, -1, 8, -1], 'scores': [0.41297924518585205, 0.4418019652366638, 0.6136321425437927, 0.4783017635345459, 0.4894874095916748, 0.5781464576721191, 0.6554463505744934, 0.3642849922180176, 0.5120865106582642, 0.545177698135376]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0115156173706055})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5331774950027466})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4173441529273987})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4194510579109192})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44007033109664917})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.46733030676841736})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9441, 'crossentropy': 0.413776123046875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6426109075546265})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.48935312032699585})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.43980172276496887})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.40279829502105713})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.38653719425201416})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [3015, 28102, 48732, 41485, 51462, 18696, 23104, 21764, 42632, 53091], 'labels': [0, 0, -1, 0, -1, -1, 0, -1, 0, -1], 'scores': [0.26694148778915405, 0.7090452909469604, 0.39175164699554443, 0.5348938703536987, 0.4856971502304077, 0.4699193835258484, 0.713437557220459, 0.3352389335632324, 0.5126023292541504, 0.42792564630508423]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8990782499313354})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4990760087966919})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46641117334365845})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4193325638771057})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4488164782524109})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4803094267845154})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4360467791557312})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9436, 'crossentropy': 0.43887666015625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.654009222984314})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47104179859161377})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3939819931983948})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3648723363876343})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34790730476379395})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33367955684661865})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [3992, 10038, 1058, 50431, 21692, 17236, 13270, 59303, 2980, 12689], 'labels': [-1, 9, 2, 3, 2, -1, -1, 8, 7, -1], 'scores': [0.38041675090789795, 0.6464253067970276, 0.5327020883560181, 0.6799939274787903, 0.32229509949684143, 0.3768686056137085, 0.4083036184310913, 0.5858544111251831, 0.4760269522666931, 0.5229103565216064]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0295937061309814})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5403533577919006})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.46897703409194946})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43766874074935913})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.47566676139831543})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.443798691034317})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.47186195850372314})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.946, 'crossentropy': 0.41376708984375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6894549131393433})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.480865478515625})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.40725600719451904})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3839128017425537})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36981597542762756})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36256206035614014})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [34539, 12758, 10772, 38315, 49200, 1573, 45658, 6352, 20280, 38586], 'labels': [-1, 6, 9, 0, 0, 2, 3, -1, 7, 7], 'scores': [0.36027467250823975, 0.3752514123916626, 0.33121609687805176, 0.547505259513855, 0.7889410257339478, 0.5428881645202637, 0.5942832827568054, 0.42071717977523804, 0.5689775347709656, 0.42123550176620483]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8977876901626587})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4932311773300171})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.40811043977737427})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4248031675815582})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4162260890007019})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42319604754447937})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9433, 'crossentropy': 0.41108466796875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7033013105392456})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.49463701248168945})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.42842650413513184})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4432382583618164})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.40037521719932556})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [13156, 49228, 843, 17257, 13127, 46610, 12812, 1598, 34942, 50972], 'labels': [2, 3, 3, 3, 3, 5, 3, -1, 9, -1], 'scores': [0.6338316798210144, 0.39375197887420654, 0.4758577346801758, 0.5763022899627686, 0.3233265280723572, 0.3862900733947754, 0.3738987445831299, 0.4450610876083374, 0.5316164493560791, 0.3624298572540283]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1084473133087158})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5590240955352783})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5334208607673645})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44259005784988403})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4468502700328827})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.45228493213653564})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4428774416446686})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9403, 'crossentropy': 0.42505986328125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6924511790275574})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5109065175056458})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4479385018348694})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.40606898069381714})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4057519733905792})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.40283241868019104})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [51942, 26186, 52067, 29903, 13145, 12568, 13365, 8024, 33121, 35276], 'labels': [9, -1, 8, 0, 5, -1, 8, 2, 5, 5], 'scores': [0.4911869168281555, 0.2845379114151001, 0.3017178773880005, 0.4687085747718811, 0.5164213180541992, 0.4292869567871094, 0.5384643077850342, 0.6026625633239746, 0.5468223094940186, 0.7284868955612183]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0870238542556763})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5331017971038818})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.45000168681144714})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.47707033157348633})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3972664773464203})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40835273265838623})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39887750148773193})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4012501835823059})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9576, 'crossentropy': 0.37002412109375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6267597079277039})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.43913841247558594})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39814263582229614})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37017953395843506})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31549549102783203})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3499985933303833})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31650757789611816})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [53640, 6738, 42971, 33354, 24145, 57821, 6375, 31311, 42514, 57720], 'labels': [8, -1, -1, -1, 3, -1, -1, -1, -1, 0], 'scores': [0.5137280225753784, 0.341269314289093, 0.3253885507583618, 0.42922019958496094, 0.6726836562156677, 0.41625845432281494, 0.3142671585083008, 0.4039947986602783, 0.3978172540664673, 0.5514975786209106]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9764468669891357})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5649901628494263})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4015970826148987})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42790108919143677})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4159092307090759})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47625821828842163})
store['active_learning_steps'][32]['training']['best_epoch']=3
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9502, 'crossentropy': 0.387984765625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6880234479904175})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.49155300855636597})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44730687141418457})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3943614363670349})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4224816560745239})
store['active_learning_steps'][32]['eval_training']['best_epoch']=4
store['active_learning_steps'][32]['acquisition']={'indices': [22938, 58972, 46886, 11446, 50386, 18030, 42599, 23628, 36902, 52838], 'labels': [-1, -1, -1, -1, 9, -1, -1, 6, -1, 4], 'scores': [0.4073648452758789, 0.4438587427139282, 0.3596848249435425, 0.5987240076065063, 0.34542810916900635, 0.38450300693511963, 0.2835448980331421, 0.5119222402572632, 0.5384401082992554, 0.5474638342857361]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.029902458190918})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5516647100448608})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.43905413150787354})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3801017999649048})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39024075865745544})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.38315218687057495})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4048553705215454})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9539, 'crossentropy': 0.348704638671875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.651652455329895})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.47475558519363403})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.41439133882522583})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.41242921352386475})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37355005741119385})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.35367685556411743})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [25384, 5086, 57930, 35993, 42884, 552, 11954, 11482, 13863, 32639], 'labels': [5, 3, -1, -1, -1, -1, -1, 8, -1, -1], 'scores': [0.3832471966743469, 0.5246228277683258, 0.3205680847167969, 0.39607107639312744, 0.42884916067123413, 0.4302588701248169, 0.3619323968887329, 0.3976868987083435, 0.36377835273742676, 0.42077934741973877]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9940177202224731})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.46769455075263977})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4352574050426483})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39163777232170105})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38154974579811096})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39538848400115967})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.41868284344673157})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4509347975254059})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9562, 'crossentropy': 0.3518546875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6249017119407654})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.45009303092956543})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.38494348526000977})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.36085647344589233})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3179854452610016})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30300000309944153})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31426799297332764})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [6220, 45713, 23844, 11600, 14067, 42740, 3153, 42793, 26405, 39151], 'labels': [4, -1, -1, 2, -1, -1, -1, 4, 9, 4], 'scores': [0.5722865462303162, 0.25237441062927246, 0.3426942229270935, 0.6726762652397156, 0.32189011573791504, 0.3763432502746582, 0.26514172554016113, 0.6630069613456726, 0.5272234678268433, 0.5922022461891174]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9008236527442932})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4885246157646179})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3793843686580658})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3611389398574829})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3578886389732361})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4102957546710968})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36574146151542664})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38750776648521423})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9536, 'crossentropy': 0.3418986572265625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6465401649475098})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3852919638156891})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3505713939666748})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.35404306650161743})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3236772418022156})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31669461727142334})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34962546825408936})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [17728, 17645, 52550, 22906, 40398, 50623, 37679, 11017, 37460, 49021], 'labels': [6, -1, -1, -1, -1, -1, -1, -1, 8, 2], 'scores': [0.3827403485774994, 0.36891019344329834, 0.6469676494598389, 0.5662252902984619, 0.6098979711532593, 0.3606986999511719, 0.5735956430435181, 0.5636756420135498, 0.5744824409484863, 0.44546371698379517]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.064321756362915})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5687025785446167})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4080837368965149})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3989579677581787})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37225908041000366})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3996008336544037})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4000927805900574})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3979949653148651})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9547, 'crossentropy': 0.3514243408203125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7510768175125122})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5039913654327393})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4116475582122803})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34142011404037476})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34878772497177124})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3190648555755615})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35161206126213074})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [24172, 13995, 3172, 2372, 40767, 14786, 30056, 20072, 49062, 10213], 'labels': [-1, -1, -1, -1, -1, -1, -1, 3, 5, -1], 'scores': [0.5390667915344238, 0.6309047341346741, 0.3534128665924072, 0.36429762840270996, 0.5663747191429138, 0.3605363368988037, 0.42289066314697266, 0.6177803874015808, 0.27404484152793884, 0.5011167526245117]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0073819160461426})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5632874965667725})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4252246618270874})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4134933650493622})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39857661724090576})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35902905464172363})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35417959094047546})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.41713255643844604})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4152129590511322})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40954774618148804})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9584, 'crossentropy': 0.3526525146484375}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6702349781990051})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3951108455657959})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3555988669395447})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34757524728775024})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32330530881881714})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2997886538505554})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2780364453792572})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2720332741737366})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27296653389930725})
store['active_learning_steps'][37]['eval_training']['best_epoch']=8
store['active_learning_steps'][37]['acquisition']={'indices': [27503, 27744, 33684, 27754, 56258, 3432, 44144, 54558, 12206, 36902], 'labels': [2, -1, -1, -1, -1, -1, -1, 7, 7, 7], 'scores': [0.5488871037960052, 0.3834265470504761, 0.43640464544296265, 0.49610984325408936, 0.4187036156654358, 0.37834084033966064, 0.49595022201538086, 0.5208089053630829, 0.44849681854248047, 0.44947534799575806]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0249443054199219})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5091884136199951})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.362571656703949})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3855200409889221})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38774436712265015})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3614192306995392})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.344622939825058})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3665607273578644})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3709868788719177})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.41588693857192993})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9588, 'crossentropy': 0.3224280029296875}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6150670647621155})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4066610038280487})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37753185629844666})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3355066776275635})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3193969130516052})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.29536521434783936})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.28697970509529114})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28864848613739014})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.27189698815345764})
store['active_learning_steps'][38]['eval_training']['best_epoch']=9
store['active_learning_steps'][38]['acquisition']={'indices': [581, 38107, 24052, 25716, 6780, 2508, 6683, 40117, 41707, 28198], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.554388165473938, 0.5420655012130737, 0.5877547860145569, 0.6791344881057739, 0.7544783353805542, 0.6825464963912964, 0.4445725679397583, 0.5352158546447754, 0.4786047339439392, 0.5350417494773865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0526490211486816})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5146382451057434})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4199073314666748})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3811342716217041})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3587545156478882})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.40064358711242676})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3556540608406067})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40207141637802124})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41428714990615845})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36155056953430176})
store['active_learning_steps'][39]['training']['best_epoch']=7
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9594, 'crossentropy': 0.331541943359375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6744860410690308})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4515472650527954})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.40667596459388733})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3641747534275055})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.314521849155426})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3353493809700012})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2900233864784241})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31496462225914})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30025631189346313})
store['active_learning_steps'][39]['eval_training']['best_epoch']=7
store['active_learning_steps'][39]['acquisition']={'indices': [58172, 52042, 37700, 15753, 18619, 30350, 28654, 46167, 35912, 41903], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.8370571732521057, 0.5501455068588257, 0.48188555240631104, 0.5984063148498535, 0.3899344205856323, 0.4527064561843872, 0.39323723316192627, 0.3909803032875061, 0.4053705334663391, 0.2978569269180298]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.980594277381897})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.46697747707366943})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.42545437812805176})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4038713276386261})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35563719272613525})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.370221883058548})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.38895100355148315})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3702549934387207})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9594, 'crossentropy': 0.32397587890625}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6736264228820801})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4512024223804474})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3413125276565552})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.375221312046051})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3182918429374695})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.30003923177719116})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29694056510925293})
store['active_learning_steps'][40]['eval_training']['best_epoch']=7
store['active_learning_steps'][40]['acquisition']={'indices': [17320, 25847, 18673, 19194, 16574, 35926, 13134, 22162, 55973, 868], 'labels': [-1, 1, -1, -1, -1, 4, 3, -1, -1, -1], 'scores': [0.5348749160766602, 0.37721681594848633, 0.6075994968414307, 0.3149198293685913, 0.49755334854125977, 0.4017869234085083, 0.37798988819122314, 0.6741312742233276, 0.5014978647232056, 0.3622499704360962]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9523937702178955})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4890786409378052})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4076678156852722})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39059463143348694})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4332375228404999})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.43946152925491333})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4124060869216919})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9509, 'crossentropy': 0.3757876708984375}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6735203266143799})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.48975810408592224})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37187469005584717})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38544130325317383})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.38375967741012573})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3452000617980957})
store['active_learning_steps'][41]['eval_training']['best_epoch']=6
store['active_learning_steps'][41]['acquisition']={'indices': [6879, 38246, 27155, 819, 26406, 45304, 51144, 59986, 53048, 52175], 'labels': [4, 7, -1, -1, -1, 9, 5, 6, -1, 1], 'scores': [0.3132936358451843, 0.3730487823486328, 0.24325668811798096, 0.3803083896636963, 0.30066680908203125, 0.3337273597717285, 0.40357905626296997, 0.5470015406608582, 0.406497597694397, 0.2808179259300232]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0652520656585693})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5464358329772949})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4413796067237854})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39217713475227356})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3870003819465637})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3650219440460205})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35938042402267456})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3695420026779175})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.41851508617401123})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3748403489589691})
store['active_learning_steps'][42]['training']['best_epoch']=7
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9615, 'crossentropy': 0.31633310546875}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6423095464706421})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4336540400981903})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3841606378555298})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34865185618400574})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30418699979782104})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3073952794075012})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3180355727672577})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2849895656108856})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.28401798009872437})
store['active_learning_steps'][42]['eval_training']['best_epoch']=9
store['active_learning_steps'][42]['acquisition']={'indices': [45640, 24967, 7091, 42920, 36143, 475, 58728, 59188, 9591, 403], 'labels': [-1, 9, -1, -1, -1, -1, -1, -1, 8, -1], 'scores': [0.5823194980621338, 0.5440245866775513, 0.44826358556747437, 0.5360400676727295, 0.5385273694992065, 0.5372322201728821, 0.4775170087814331, 0.6139630079269409, 0.43616944551467896, 0.6756112575531006]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0534942150115967})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.545654296875})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4278014302253723})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42653635144233704})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4176101088523865})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4124976396560669})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40316158533096313})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40943264961242676})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39609983563423157})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.41037794947624207})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4547649621963501})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42310893535614014})
store['active_learning_steps'][43]['training']['best_epoch']=9
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9614, 'crossentropy': 0.3433390625}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.665168285369873})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4236513078212738})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3792271316051483})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31718504428863525})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2887778878211975})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.308063268661499})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2740229070186615})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.28123509883880615})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27060890197753906})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.27883458137512207})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2767030596733093})
store['active_learning_steps'][43]['eval_training']['best_epoch']=9
store['active_learning_steps'][43]['acquisition']={'indices': [46938, 49348, 31911, 40525, 3203, 29249, 11536, 17478, 46434, 4036], 'labels': [-1, 5, -1, -1, -1, 3, 9, 4, -1, -1], 'scores': [0.4540354013442993, 0.6705596148967743, 0.4671725034713745, 0.45393455028533936, 0.46716392040252686, 0.5949177742004395, 0.42303338646888733, 0.4773479700088501, 0.6202772855758667, 0.8369683027267456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.035644769668579})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49329817295074463})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4108264446258545})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.39598435163497925})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.364419549703598})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4119061529636383})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.36818060278892517})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3474796414375305})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.390655517578125})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.4125555753707886})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.38454359769821167})
store['active_learning_steps'][44]['training']['best_epoch']=8
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9602, 'crossentropy': 0.325363525390625}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6680464744567871})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40798449516296387})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.37490254640579224})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30966636538505554})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32103049755096436})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32171595096588135})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3154137134552002})
store['active_learning_steps'][44]['eval_training']['best_epoch']=4
store['active_learning_steps'][44]['acquisition']={'indices': [54025, 26213, 44855, 55042, 21700, 26775, 35807, 4282, 4848, 36064], 'labels': [-1, -1, -1, -1, 7, -1, -1, -1, -1, -1], 'scores': [0.5048298835754395, 0.3435615301132202, 0.48341822624206543, 0.38020801544189453, 0.579812228679657, 0.510489284992218, 0.5004329681396484, 0.4855271577835083, 0.43580329418182373, 0.4541962742805481]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9589169025421143})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5100115537643433})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3976430892944336})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3638809025287628})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33907270431518555})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38925373554229736})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34576547145843506})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3577576279640198})
store['active_learning_steps'][45]['training']['best_epoch']=5
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9592, 'crossentropy': 0.3244412109375}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6251362562179565})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.44057708978652954})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4187392592430115})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38481605052948})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.31736642122268677})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32087236642837524})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31626248359680176})
store['active_learning_steps'][45]['eval_training']['best_epoch']=7
store['active_learning_steps'][45]['acquisition']={'indices': [26392, 5678, 17382, 25500, 59399, 46709, 49970, 52464, 9117, 652], 'labels': [6, 5, 6, -1, 8, 3, -1, -1, -1, 5], 'scores': [0.46064549684524536, 0.4631054401397705, 0.5729398131370544, 0.3269606828689575, 0.44531381130218506, 0.5403742790222168, 0.4180023670196533, 0.3707866668701172, 0.43614768981933594, 0.5655954778194427]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.9944648742675781})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4650712311267853})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35285159945487976})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36153358221054077})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32771041989326477})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3485393524169922})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3210776448249817})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3634595274925232})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30700916051864624})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35048913955688477})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32313472032546997})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37669265270233154})
store['active_learning_steps'][46]['training']['best_epoch']=9
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9673, 'crossentropy': 0.2915423828125}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.636850893497467})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4227186143398285})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35820627212524414})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32686465978622437})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2845185697078705})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2697693705558777})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24976380169391632})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2431841939687729})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24182020127773285})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27217134833335876})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.23892703652381897})
store['active_learning_steps'][46]['eval_training']['best_epoch']=11
store['active_learning_steps'][46]['acquisition']={'indices': [120, 56014, 228, 42504, 55496, 17857, 30111, 23366, 46941, 32468], 'labels': [-1, 5, 3, 8, 9, 4, 8, 9, 5, -1], 'scores': [0.6309183835983276, 0.6811407208442688, 0.6975229382514954, 0.7947288155555725, 0.5148671865463257, 0.2812226712703705, 0.5349359512329102, 0.47394198179244995, 0.5229086577892303, 0.4880356788635254]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0453221797943115})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4772226810455322})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3826868534088135})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36248207092285156})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3482239246368408})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3521638512611389})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3964710235595703})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3574336767196655})
store['active_learning_steps'][47]['training']['best_epoch']=5
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9576, 'crossentropy': 0.319064306640625}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6418737173080444})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4258273243904114})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4222522974014282})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36621803045272827})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3723224699497223})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3540698289871216})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3403659462928772})
store['active_learning_steps'][47]['eval_training']['best_epoch']=7
store['active_learning_steps'][47]['acquisition']={'indices': [9129, 15956, 12905, 23099, 40943, 20363, 51364, 27640, 14309, 30878], 'labels': [9, 8, 6, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4335101842880249, 0.43808650970458984, 0.7008033394813538, 0.4823133945465088, 0.42082762718200684, 0.5309810042381287, 0.3785139322280884, 0.5051785707473755, 0.5775734186172485, 0.3988678455352783]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.0963906049728394})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.538410484790802})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.40454012155532837})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3916754722595215})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36444926261901855})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3550979197025299})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33117538690567017})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3334101140499115})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3693280816078186})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.359940767288208})
store['active_learning_steps'][48]['training']['best_epoch']=7
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9635, 'crossentropy': 0.3032295166015625}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7089644074440002})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43773940205574036})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3826907277107239})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33684617280960083})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3213752806186676})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32297372817993164})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2680498957633972})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2639716863632202})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26621052622795105})
store['active_learning_steps'][48]['eval_training']['best_epoch']=8
store['active_learning_steps'][48]['acquisition']={'indices': [45292, 54922, 36109, 25613, 30032, 26825, 3084, 57274, 969, 3060], 'labels': [-1, -1, 9, -1, -1, -1, -1, -1, -1, 7], 'scores': [0.5263449549674988, 0.44278013706207275, 0.5763448476791382, 0.49810224771499634, 0.5157524347305298, 0.5221818685531616, 0.4930551052093506, 0.523614227771759, 0.5542461276054382, 0.43929898738861084]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0300389528274536})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.553210973739624})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3901282846927643})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35161036252975464})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3168250322341919})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3677605986595154})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36605527997016907})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3413863778114319})
store['active_learning_steps'][49]['training']['best_epoch']=5
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.962, 'crossentropy': 0.291643701171875}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6828100681304932})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4306384325027466})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.40263503789901733})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37787169218063354})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.32280194759368896})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31773287057876587})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2926541566848755})
store['active_learning_steps'][49]['eval_training']['best_epoch']=7
store['active_learning_steps'][49]['acquisition']={'indices': [26072, 5884, 18247, 5265, 52886, 13905, 42708, 33331, 36417, 9582], 'labels': [1, -1, 0, 4, 7, 7, -1, -1, 6, -1], 'scores': [0.5924810767173767, 0.4178708791732788, 0.3095579147338867, 0.6558120548725128, 0.5664327144622803, 0.4356718063354492, 0.40466463565826416, 0.41396284103393555, 0.5534895658493042, 0.4204118251800537]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.056788682937622})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.44162213802337646})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.40725409984588623})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32713782787323})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.375246524810791})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32492244243621826})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3284687399864197})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3345588445663452})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3434183597564697})
store['active_learning_steps'][50]['training']['best_epoch']=6
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9666, 'crossentropy': 0.284561865234375}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6920838356018066})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.42696523666381836})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34232962131500244})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30641987919807434})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3148149847984314})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.29455995559692383})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2939760088920593})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26424431800842285})
store['active_learning_steps'][50]['eval_training']['best_epoch']=8
store['active_learning_steps'][50]['acquisition']={'indices': [54076, 46079, 21208, 8207, 59054, 49784, 46274, 20312, 24645, 49781], 'labels': [-1, -1, -1, 4, -1, -1, 7, -1, -1, -1], 'scores': [0.388735294342041, 0.4338066577911377, 0.48844289779663086, 0.8184250593185425, 0.3357285261154175, 0.4656566381454468, 0.5183139741420746, 0.55122971534729, 0.36097514629364014, 0.23357665538787842]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0793901681900024})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5674819946289062})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39021944999694824})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3255229890346527})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35137850046157837})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35288387537002563})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3246532380580902})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38280510902404785})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.321025013923645})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32268986105918884})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.35707318782806396})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3238370418548584})
store['active_learning_steps'][51]['training']['best_epoch']=9
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9625, 'crossentropy': 0.309277099609375}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6694169044494629})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4506567120552063})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37293457984924316})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32359641790390015})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3026810884475708})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2794898748397827})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2700367569923401})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28451281785964966})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.282345712184906})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2553773820400238})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2775915563106537})
store['active_learning_steps'][51]['eval_training']['best_epoch']=10
store['active_learning_steps'][51]['acquisition']={'indices': [14175, 47242, 641, 11404, 37503, 10389, 52912, 9164, 21066, 59492], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 0, -1], 'scores': [0.48777830600738525, 0.47217869758605957, 0.3229556083679199, 0.4757812023162842, 0.4469543695449829, 0.439693808555603, 0.38856709003448486, 0.5011148452758789, 0.6075087785720825, 0.589353084564209]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9936753511428833})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4972933530807495})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3627774715423584})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32133087515830994})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36156779527664185})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.35191887617111206})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3255434036254883})
store['active_learning_steps'][52]['training']['best_epoch']=4
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9626, 'crossentropy': 0.2975837646484375}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6366300582885742})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4599873423576355})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3910956382751465})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36705076694488525})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.36947178840637207})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3272545337677002})
store['active_learning_steps'][52]['eval_training']['best_epoch']=6
store['active_learning_steps'][52]['acquisition']={'indices': [6516, 43008, 59290, 1254, 8532, 24620, 50471, 42526, 39208, 54911], 'labels': [-1, -1, -1, -1, 6, 9, 4, 3, 5, -1], 'scores': [0.2764430642127991, 0.3722633123397827, 0.3342859745025635, 0.43880796432495117, 0.3810085654258728, 0.4914565682411194, 0.34415626525878906, 0.4415203332901001, 0.6503463387489319, 0.3011065721511841]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9760763645172119})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.462130606174469})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4095042943954468})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33812588453292847})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3592899441719055})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3264337480068207})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34647494554519653})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3385414481163025})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3514839708805084})
store['active_learning_steps'][53]['training']['best_epoch']=6
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9627, 'crossentropy': 0.287558642578125}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.648373007774353})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41937723755836487})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3690096139907837})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32595038414001465})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28795772790908813})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2902276813983917})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29909855127334595})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.25070834159851074})
store['active_learning_steps'][53]['eval_training']['best_epoch']=8
store['active_learning_steps'][53]['acquisition']={'indices': [36744, 26114, 10205, 48382, 41286, 52086, 2612, 43138, 12036, 17958], 'labels': [1, 6, 1, 8, -1, 5, -1, -1, 4, 9], 'scores': [0.6365166306495667, 0.418928325176239, 0.30562323331832886, 0.5383424162864685, 0.4113349914550781, 0.6102020740509033, 0.3849290609359741, 0.41256439685821533, 0.3253173232078552, 0.45225632190704346]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.0897393226623535})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4764299988746643})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40201953053474426})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34358513355255127})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34569668769836426})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32351571321487427})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32295340299606323})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.328574538230896})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3306174576282501})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3774060010910034})
store['active_learning_steps'][54]['training']['best_epoch']=7
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9665, 'crossentropy': 0.2857458740234375}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6056702733039856})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.45378434658050537})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3489574193954468})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3552699089050293})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2842763066291809})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27489492297172546})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2577263414859772})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2653326392173767})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26659297943115234})
store['active_learning_steps'][54]['eval_training']['best_epoch']=7
store['active_learning_steps'][54]['acquisition']={'indices': [57251, 27150, 44877, 41578, 57939, 15579, 14410, 56586, 30041, 5188], 'labels': [5, 2, -1, 8, 2, 5, -1, 5, 3, 5], 'scores': [0.4556393623352051, 0.4328039288520813, 0.3811589479446411, 0.5145676136016846, 0.46438080072402954, 0.29174286127090454, 0.5659358501434326, 0.37592917680740356, 0.46544671058654785, 0.47652667760849]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9811226725578308})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5332213640213013})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36564165353775024})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3389858603477478})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29656219482421875})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3322749733924866})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3176165819168091})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31495267152786255})
store['active_learning_steps'][55]['training']['best_epoch']=5
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9673, 'crossentropy': 0.268209619140625}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6515860557556152})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4651563763618469})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40099895000457764})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3315672278404236})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31082770228385925})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31535792350769043})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29743438959121704})
store['active_learning_steps'][55]['eval_training']['best_epoch']=7
store['active_learning_steps'][55]['acquisition']={'indices': [11144, 7006, 23762, 37311, 10331, 43363, 59481, 49822, 55339, 10584], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.40322136878967285, 0.3781201243400574, 0.5685823559761047, 0.5174649953842163, 0.5513266921043396, 0.559840977191925, 0.5690262317657471, 0.5185747146606445, 0.6110661625862122, 0.340657114982605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0740764141082764})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.49499183893203735})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41300755739212036})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3646852374076843})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33543866872787476})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35371536016464233})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36448535323143005})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3444143533706665})
store['active_learning_steps'][56]['training']['best_epoch']=5
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9643, 'crossentropy': 0.291031591796875}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6692920327186584})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4846787750720978})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3875502943992615})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35139137506484985})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3307698369026184})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35800325870513916})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3156009614467621})
store['active_learning_steps'][56]['eval_training']['best_epoch']=7
store['active_learning_steps'][56]['acquisition']={'indices': [38142, 32776, 55264, 48340, 27966, 5835, 27842, 53979, 42925, 4646], 'labels': [8, 4, 8, -1, 9, 4, -1, 8, -1, 2], 'scores': [0.5736586451530457, 0.6991006135940552, 0.5583839416503906, 0.36459052562713623, 0.40617597103118896, 0.3300532102584839, 0.2655942440032959, 0.49097687005996704, 0.39584922790527344, 0.45346206426620483]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0463147163391113})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.48893722891807556})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37260305881500244})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3681338131427765})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3529016673564911})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3140548765659332})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34067052602767944})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3138071894645691})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3593429923057556})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.367251455783844})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3318224549293518})
store['active_learning_steps'][57]['training']['best_epoch']=8
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9678, 'crossentropy': 0.2790767822265625}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6207470893859863})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3713884651660919})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33935248851776123})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2920176088809967})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28962984681129456})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27623337507247925})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.275718629360199})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2571008503437042})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2524701654911041})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2505180835723877})
store['active_learning_steps'][57]['eval_training']['best_epoch']=10
store['active_learning_steps'][57]['acquisition']={'indices': [31571, 27357, 47729, 19961, 35034, 57414, 51881, 45915, 8715, 23474], 'labels': [-1, -1, -1, -1, -1, -1, -1, 4, -1, -1], 'scores': [0.39407217502593994, 0.4495795965194702, 0.5336371660232544, 0.4631854295730591, 0.31417953968048096, 0.4671670198440552, 0.44456911087036133, 0.724230945110321, 0.4829704761505127, 0.6011291742324829]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0653005838394165})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5565662384033203})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4157227873802185})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3486770987510681})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.370779812335968})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34009337425231934})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36018872261047363})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35236823558807373})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37627455592155457})
store['active_learning_steps'][58]['training']['best_epoch']=6
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9636, 'crossentropy': 0.298060986328125}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6095510125160217})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4178459644317627})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.34891724586486816})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3211349844932556})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.297511488199234})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2713005244731903})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2770523428916931})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28182029724121094})
store['active_learning_steps'][58]['eval_training']['best_epoch']=6
store['active_learning_steps'][58]['acquisition']={'indices': [23210, 11322, 956, 48475, 1875, 51557, 51231, 45749, 8954, 7891], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 7, 8], 'scores': [0.3889286518096924, 0.40424883365631104, 0.4398202896118164, 0.3469862937927246, 0.4723736047744751, 0.5237268209457397, 0.5450626015663147, 0.6485830545425415, 0.5362675786018372, 0.5441419184207916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1513779163360596})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5858874917030334})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4373610317707062})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3936067223548889})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31932783126831055})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.352108895778656})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3435082733631134})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3649820387363434})
store['active_learning_steps'][59]['training']['best_epoch']=5
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9632, 'crossentropy': 0.2886886474609375}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7204886674880981})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4870864152908325})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4087187647819519})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.39026495814323425})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3364136219024658})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3045647144317627})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3184126913547516})
store['active_learning_steps'][59]['eval_training']['best_epoch']=6
store['active_learning_steps'][59]['acquisition']={'indices': [42335, 1179, 56048, 56970, 3084, 9151, 35878, 31121, 46728, 44781], 'labels': [6, -1, -1, 4, -1, -1, 9, -1, 4, -1], 'scores': [0.4447029232978821, 0.40171241760253906, 0.37740135192871094, 0.2838844060897827, 0.32317376136779785, 0.5072616338729858, 0.38945621252059937, 0.45868241786956787, 0.3632664680480957, 0.5249230861663818]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1549148559570312})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4624129831790924})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4163684844970703})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36336299777030945})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3167635202407837})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31196555495262146})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29050126671791077})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.298963338136673})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28820499777793884})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2721177935600281})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31188511848449707})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.304695188999176})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3196154236793518})
store['active_learning_steps'][60]['training']['best_epoch']=10
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9691, 'crossentropy': 0.2758645751953125}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.626212477684021})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.38062673807144165})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31412333250045776})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.302513062953949})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2642187178134918})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26551979780197144})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24454060196876526})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.276182621717453})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23265162110328674})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23841777443885803})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2139045149087906})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.21901270747184753})
store['active_learning_steps'][60]['eval_training']['best_epoch']=11
store['active_learning_steps'][60]['acquisition']={'indices': [18279, 53811, 9588, 41243, 34189, 21874, 45446, 58603, 956, 14481], 'labels': [-1, -1, 7, -1, -1, -1, 7, -1, -1, -1], 'scores': [0.621772050857544, 0.5892840623855591, 0.6328800618648529, 0.3164548873901367, 0.5215362906455994, 0.4192965626716614, 0.5842745304107666, 0.4593414068222046, 0.6080000400543213, 0.47595709562301636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1116780042648315})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5278231501579285})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43319112062454224})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3507828712463379})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3577118515968323})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2948535084724426})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3262327313423157})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30835580825805664})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.360925555229187})
store['active_learning_steps'][61]['training']['best_epoch']=6
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9674, 'crossentropy': 0.2706869384765625}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6806367635726929})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40917253494262695})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.32760369777679443})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2908991575241089})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2884935140609741})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2786705195903778})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3094305992126465})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2826996445655823})
store['active_learning_steps'][61]['eval_training']['best_epoch']=6
store['active_learning_steps'][61]['acquisition']={'indices': [34754, 5727, 22470, 27825, 52223, 8745, 26938, 35976, 36161, 21965], 'labels': [-1, -1, -1, -1, -1, -1, -1, 5, -1, -1], 'scores': [0.5645525455474854, 0.5034784078598022, 0.3980422616004944, 0.385936975479126, 0.5069311857223511, 0.6146005988121033, 0.4772146940231323, 0.6094111800193787, 0.357629656791687, 0.34785157442092896]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0362679958343506})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6079175472259521})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.39623984694480896})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33479028940200806})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3221599757671356})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.326307475566864})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3478595018386841})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.366400808095932})
store['active_learning_steps'][62]['training']['best_epoch']=5
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9669, 'crossentropy': 0.2798012451171875}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6844768524169922})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4967787265777588})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3767048120498657})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35285666584968567})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32521986961364746})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3017365634441376})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3065412640571594})
store['active_learning_steps'][62]['eval_training']['best_epoch']=6
store['active_learning_steps'][62]['acquisition']={'indices': [29511, 4432, 56838, 39355, 57486, 35609, 45081, 34327, 48295, 52092], 'labels': [-1, -1, 5, -1, -1, -1, -1, -1, -1, 7], 'scores': [0.5685087442398071, 0.5684198141098022, 0.40972697734832764, 0.5004878044128418, 0.3340461254119873, 0.5071601271629333, 0.29382026195526123, 0.3932288885116577, 0.29885315895080566, 0.39818841218948364]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.3177647590637207})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5438477993011475})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.42507404088974})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32633766531944275})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3395519256591797})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3284912109375})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31393104791641235})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34398216009140015})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30104589462280273})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.296062707901001})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35608333349227905})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3374941349029541})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3470466136932373})
store['active_learning_steps'][63]['training']['best_epoch']=10
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9672, 'crossentropy': 0.2705439453125}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6400766372680664})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4361501932144165})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3522658944129944})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3313913345336914})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3129468858242035})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2791854441165924})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2621610760688782})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25696438550949097})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24559761583805084})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2440580129623413})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25018173456192017})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24876397848129272})
store['active_learning_steps'][63]['eval_training']['best_epoch']=10
store['active_learning_steps'][63]['acquisition']={'indices': [44032, 58588, 23731, 25219, 33331, 36506, 36994, 13085, 32275, 5182], 'labels': [-1, -1, -1, -1, -1, -1, -1, 6, -1, -1], 'scores': [0.5444790720939636, 0.3151581287384033, 0.5520143508911133, 0.5650177001953125, 0.6669189929962158, 0.6226847171783447, 0.408221960067749, 0.6628166437149048, 0.6555179357528687, 0.4774724245071411]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0976483821868896})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5334030389785767})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.41599732637405396})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3143691122531891})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3602283298969269})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33572450280189514})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3119787871837616})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3226288855075836})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3364855945110321})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35083574056625366})
store['active_learning_steps'][64]['training']['best_epoch']=7
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9677, 'crossentropy': 0.2720808837890625}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6566726565361023})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4494019150733948})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3485124111175537})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3226948082447052})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.28941085934638977})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3004049062728882})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28781604766845703})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26999250054359436})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2555128335952759})
store['active_learning_steps'][64]['eval_training']['best_epoch']=9
store['active_learning_steps'][64]['acquisition']={'indices': [10557, 43547, 13969, 53910, 20709, 42438, 9804, 24805, 31115, 50461], 'labels': [6, 2, 3, 2, 8, 9, -1, 2, 9, 7], 'scores': [0.44709599018096924, 0.3797706961631775, 0.5900086760520935, 0.41971075534820557, 0.6108595728874207, 0.48462653160095215, 0.48109543323516846, 0.5256671905517578, 0.3868620991706848, 0.36934149265289307]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.1685583591461182})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5221027135848999})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3774879574775696})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32618507742881775})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3215690553188324})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3040585517883301})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3152504563331604})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3088368773460388})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3276294767856598})
store['active_learning_steps'][65]['training']['best_epoch']=6
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9672, 'crossentropy': 0.273753564453125}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.606997013092041})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.46828746795654297})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36914536356925964})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33631134033203125})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2835178077220917})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3306317925453186})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2744637727737427})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27201616764068604})
store['active_learning_steps'][65]['eval_training']['best_epoch']=8
store['active_learning_steps'][65]['acquisition']={'indices': [15733, 42995, 35971, 2385, 41007, 47870, 1160, 16549, 12950, 24680], 'labels': [-1, 4, 0, -1, -1, 9, 4, 3, 2, -1], 'scores': [0.29244565963745117, 0.4474942088127136, 0.6221209764480591, 0.29633402824401855, 0.4264969825744629, 0.4600539207458496, 0.41478073596954346, 0.5603427886962891, 0.5488038063049316, 0.4158848524093628]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.288025140762329})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5709466338157654})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.42060303688049316})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3699498772621155})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30930715799331665})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3344634473323822})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32963138818740845})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3297419548034668})
store['active_learning_steps'][66]['training']['best_epoch']=5
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9623, 'crossentropy': 0.2863170166015625}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7277137041091919})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.45586711168289185})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3364362418651581})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3318779766559601})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3209874629974365})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3080056607723236})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.28814390301704407})
store['active_learning_steps'][66]['eval_training']['best_epoch']=7
store['active_learning_steps'][66]['acquisition']={'indices': [16889, 11167, 57281, 52391, 2148, 34002, 24460, 8234, 23059, 49541], 'labels': [-1, 4, -1, -1, 6, -1, -1, -1, 1, 9], 'scores': [0.3158796429634094, 0.4374728202819824, 0.4812780022621155, 0.20416808128356934, 0.5129344463348389, 0.34994006156921387, 0.3162219524383545, 0.34051698446273804, 0.484244167804718, 0.47852301597595215]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.1287977695465088})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5594916343688965})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3976966142654419})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3358921408653259})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31129521131515503})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3037087023258209})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30703169107437134})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32122093439102173})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3444151282310486})
store['active_learning_steps'][67]['training']['best_epoch']=6
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9688, 'crossentropy': 0.26629873046875}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.671983003616333})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4461994171142578})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3493005931377411})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3206765651702881})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3073955476284027})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30781811475753784})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2744769752025604})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2642417252063751})
store['active_learning_steps'][67]['eval_training']['best_epoch']=8
store['active_learning_steps'][67]['acquisition']={'indices': [59336, 53211, 50201, 35476, 4800, 49525, 42475, 14572, 59934, 24767], 'labels': [-1, -1, -1, -1, 6, 8, -1, 4, 0, 4], 'scores': [0.46890318393707275, 0.42806708812713623, 0.38938403129577637, 0.25934040546417236, 0.39608803391456604, 0.5484748482704163, 0.3244129419326782, 0.5545024275779724, 0.41068583726882935, 0.38772064447402954]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.2359063625335693})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5777192115783691})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45546215772628784})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3527047634124756})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33183276653289795})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3171052932739258})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3158520460128784})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29200583696365356})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30281567573547363})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.305666983127594})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31470996141433716})
store['active_learning_steps'][68]['training']['best_epoch']=8
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9695, 'crossentropy': 0.2619129638671875}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6345359086990356})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4261159300804138})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.35422444343566895})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3192019462585449})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28166720271110535})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.312205970287323})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29636603593826294})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3005073666572571})
store['active_learning_steps'][68]['eval_training']['best_epoch']=5
store['active_learning_steps'][68]['acquisition']={'indices': [15832, 21760, 11195, 20849, 49517, 53325, 40688, 45056, 29845, 696], 'labels': [-1, -1, -1, -1, 6, -1, -1, 8, -1, 2], 'scores': [0.5187888145446777, 0.43980491161346436, 0.5760462880134583, 0.4797990322113037, 0.8365924954414368, 0.5119667053222656, 0.4288542866706848, 0.4347708225250244, 0.5027270317077637, 0.431575745344162]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0210702419281006})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5095978379249573})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34464144706726074})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30634570121765137})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30858898162841797})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2899426221847534})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2905582785606384})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.302562415599823})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2848150134086609})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.298151433467865})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2920040488243103})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3088960349559784})
store['active_learning_steps'][69]['training']['best_epoch']=9
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9695, 'crossentropy': 0.267268505859375}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6146277189254761})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4188023805618286})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3223954439163208})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30521655082702637})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.256244033575058})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.24416357278823853})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.237076997756958})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2426406890153885})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23390606045722961})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24044117331504822})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24317052960395813})
store['active_learning_steps'][69]['eval_training']['best_epoch']=9
store['active_learning_steps'][69]['acquisition']={'indices': [52411, 13566, 44694, 3933, 33459, 39031, 6842, 53261, 23451, 15214], 'labels': [-1, -1, 4, -1, -1, 2, -1, -1, -1, -1], 'scores': [0.5290294885635376, 0.507408618927002, 0.3532620668411255, 0.6412838697433472, 0.6032903790473938, 0.4818301200866699, 0.5590193867683411, 0.4292181730270386, 0.7069771885871887, 0.6263447999954224]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1039211750030518})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5516173839569092})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4019349217414856})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.34693142771720886})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32444196939468384})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3222270607948303})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.294535756111145})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32003578543663025})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27502956986427307})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29943162202835083})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3085251450538635})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3014407157897949})
store['active_learning_steps'][70]['training']['best_epoch']=9
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.26822548828125}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6531782150268555})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4376433491706848})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3497985005378723})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33155322074890137})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33574217557907104})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30178672075271606})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28517717123031616})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2641088366508484})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2543802261352539})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27150624990463257})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2624722719192505})
store['active_learning_steps'][70]['eval_training']['best_epoch']=9
store['active_learning_steps'][70]['acquisition']={'indices': [49910, 16420, 37128, 29485, 24250, 43233, 16162, 29109, 14772, 12005], 'labels': [6, -1, -1, -1, 5, -1, -1, -1, -1, -1], 'scores': [0.43115901947021484, 0.5872698426246643, 0.43298840522766113, 0.5165802240371704, 0.454184889793396, 0.39822161197662354, 0.6249372363090515, 0.6262853741645813, 0.375341534614563, 0.6658051013946533]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9987565279006958})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.543328583240509})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3861275315284729})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2890649437904358})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2840774357318878})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30687952041625977})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28503865003585815})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28066954016685486})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29965466260910034})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3104143738746643})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3374398946762085})
store['active_learning_steps'][71]['training']['best_epoch']=8
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9678, 'crossentropy': 0.2548646484375}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6654382944107056})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.451548308134079})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36699897050857544})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3135836720466614})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3364643454551697})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30783864855766296})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2951641082763672})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29725468158721924})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2613948881626129})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2559327185153961})
store['active_learning_steps'][71]['eval_training']['best_epoch']=10
store['active_learning_steps'][71]['acquisition']={'indices': [4446, 27492, 21598, 24443, 5408, 62, 34291, 14341, 22717, 35638], 'labels': [-1, -1, 2, -1, 3, -1, 1, 9, 3, 2], 'scores': [0.5215039253234863, 0.4710267186164856, 0.5546088814735413, 0.3262217044830322, 0.47727859020233154, 0.46598517894744873, 0.3614346385002136, 0.4761335849761963, 0.46349215507507324, 0.44461965560913086]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9819152355194092})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.466342031955719})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33567166328430176})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3282718062400818})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3063010573387146})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.292483389377594})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29023435711860657})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27111127972602844})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.262507826089859})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3033634424209595})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3053378760814667})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3153124749660492})
store['active_learning_steps'][72]['training']['best_epoch']=9
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9689, 'crossentropy': 0.25969990234375}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6895771026611328})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43195170164108276})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.34465861320495605})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2915371358394623})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2581946551799774})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2532229721546173})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2541888952255249})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.23222053050994873})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.20098209381103516})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.21561980247497559})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23285982012748718})
store['active_learning_steps'][72]['eval_training']['best_epoch']=9
store['active_learning_steps'][72]['acquisition']={'indices': [10987, 12441, 50195, 39964, 51453, 21884, 56575, 44071, 28670, 33669], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 7, -1], 'scores': [0.45388221740722656, 0.32491159439086914, 0.5325500965118408, 0.6354575753211975, 0.39866816997528076, 0.5948065519332886, 0.4289711117744446, 0.6265110373497009, 0.5094103813171387, 0.5873481035232544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.2587783336639404})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6059587597846985})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4056328535079956})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32992449402809143})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.299664169549942})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29522448778152466})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31012076139450073})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32168543338775635})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31344369053840637})
store['active_learning_steps'][73]['training']['best_epoch']=6
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.97, 'crossentropy': 0.2570930419921875}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6831563115119934})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4171677231788635})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36040839552879333})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3271443843841553})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2630123496055603})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2564530372619629})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2683525085449219})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26333945989608765})
store['active_learning_steps'][73]['eval_training']['best_epoch']=6
store['active_learning_steps'][73]['acquisition']={'indices': [59336, 1950, 7768, 23328, 6315, 39256, 38378, 4611, 23736, 5910], 'labels': [-1, 9, 8, -1, 7, -1, 5, -1, -1, -1], 'scores': [0.48785096406936646, 0.37400418519973755, 0.43669044971466064, 0.2187669277191162, 0.38106489181518555, 0.46602535247802734, 0.4640936851501465, 0.5058794021606445, 0.4523810148239136, 0.3965543508529663]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.9667423367500305})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5044220089912415})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3448522686958313})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28708070516586304})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30792176723480225})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26387977600097656})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2868340015411377})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2942567467689514})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29236167669296265})
store['active_learning_steps'][74]['training']['best_epoch']=6
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9713, 'crossentropy': 0.237473583984375}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7142773270606995})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4415445327758789})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3493305444717407})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3271833062171936})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28304827213287354})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2926785349845886})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2812689542770386})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.277766615152359})
store['active_learning_steps'][74]['eval_training']['best_epoch']=8
store['active_learning_steps'][74]['acquisition']={'indices': [55547, 55782, 24052, 8104, 40025, 11737, 52812, 32387, 7964, 17865], 'labels': [-1, -1, 4, 5, -1, 2, -1, 4, -1, -1], 'scores': [0.4610280990600586, 0.4911057949066162, 0.30434858798980713, 0.46834656596183777, 0.37163496017456055, 0.4128345251083374, 0.31816941499710083, 0.5461893081665039, 0.4575839042663574, 0.4116098880767822]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.2545523643493652})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5363072156906128})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3883950114250183})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34031933546066284})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3049267530441284})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34860992431640625})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3379128575325012})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3278481960296631})
store['active_learning_steps'][75]['training']['best_epoch']=5
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9676, 'crossentropy': 0.2759666748046875}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.665860652923584})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.45635876059532166})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.35951656103134155})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3078869879245758})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34145066142082214})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.29208818078041077})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3182776868343353})
store['active_learning_steps'][75]['eval_training']['best_epoch']=6
store['active_learning_steps'][75]['acquisition']={'indices': [5124, 39214, 3010, 55618, 30942, 8963, 24800, 53106, 14232, 40195], 'labels': [-1, -1, 7, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.6020921468734741, 0.4163018465042114, 0.2598898410797119, 0.41696596145629883, 0.2864576578140259, 0.23480260372161865, 0.41074419021606445, 0.3142831325531006, 0.4359300136566162, 0.3349796533584595]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.089796781539917})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5300180315971375})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3758528232574463})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29018574953079224})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26569193601608276})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2885327935218811})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2641976475715637})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2577860355377197})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25564152002334595})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24557313323020935})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2730149030685425})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2550179660320282})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25886014103889465})
store['active_learning_steps'][76]['training']['best_epoch']=10
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.973, 'crossentropy': 0.2431071533203125}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6848851442337036})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43960094451904297})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3506135940551758})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32964104413986206})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29170987010002136})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2676195502281189})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25301891565322876})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.22316309809684753})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2266489416360855})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2069636583328247})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2548094391822815})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.21462935209274292})
store['active_learning_steps'][76]['eval_training']['best_epoch']=10
store['active_learning_steps'][76]['acquisition']={'indices': [11468, 42884, 52089, 52926, 39789, 57322, 19369, 58895, 51231, 49218], 'labels': [-1, -1, 7, -1, -1, -1, 0, -1, -1, -1], 'scores': [0.38389861583709717, 0.7468878030776978, 0.6905750036239624, 0.566929042339325, 0.387612521648407, 0.6239908337593079, 0.4866442382335663, 0.3189454674720764, 0.5890716314315796, 0.5585069060325623]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.3355358839035034})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6195133328437805})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3927549123764038})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3338022232055664})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29838865995407104})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29777950048446655})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30456113815307617})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3048357367515564})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29530972242355347})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29733285307884216})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29637840390205383})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3061276078224182})
store['active_learning_steps'][77]['training']['best_epoch']=9
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9716, 'crossentropy': 0.2530510009765625}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6916345357894897})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4135048985481262})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35951849818229675})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2678908109664917})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.26889461278915405})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2645215690135956})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2574061155319214})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.23169627785682678})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.249431774020195})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2275271713733673})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.22307218611240387})
store['active_learning_steps'][77]['eval_training']['best_epoch']=11
store['active_learning_steps'][77]['acquisition']={'indices': [1852, 53137, 5800, 52957, 48310, 51057, 728, 1082, 8949, 44266], 'labels': [-1, -1, 8, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.45256316661834717, 0.49159669876098633, 0.3900054097175598, 0.3999890089035034, 0.4439491033554077, 0.3780862092971802, 0.42656296491622925, 0.388485848903656, 0.5121417045593262, 0.6189588308334351]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.06497323513031})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5877653360366821})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37716466188430786})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34687483310699463})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3240715265274048})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3089393377304077})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31850728392601013})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2946905195713043})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3133202791213989})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2990897297859192})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31420108675956726})
store['active_learning_steps'][78]['training']['best_epoch']=8
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9694, 'crossentropy': 0.2576248779296875}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6626308560371399})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.43165311217308044})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3414766788482666})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3153303265571594})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2923956513404846})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28938546776771545})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2912427484989166})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.25116586685180664})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2931744158267975})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.24656975269317627})
store['active_learning_steps'][78]['eval_training']['best_epoch']=10
store['active_learning_steps'][78]['acquisition']={'indices': [54813, 14004, 56561, 5666, 635, 20662, 47264, 52666, 57368, 6335], 'labels': [-1, -1, -1, -1, 5, -1, 9, 7, -1, -1], 'scores': [0.4493575096130371, 0.32843196392059326, 0.5151756405830383, 0.3914680480957031, 0.467820405960083, 0.4418303966522217, 0.4289964437484741, 0.34577175974845886, 0.2915467619895935, 0.4925270080566406]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1606976985931396})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6008951663970947})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36087271571159363})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29519879817962646})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3061044216156006})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28029972314834595})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2817395031452179})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2838223874568939})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28826218843460083})
store['active_learning_steps'][79]['training']['best_epoch']=6
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9712, 'crossentropy': 0.2411003173828125}
store['active_learning_steps'][79]['eval_training']={}
store['active_learning_steps'][79]['eval_training']['epochs']=[]
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6833416819572449})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3705480694770813})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3264724016189575})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2883075177669525})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2871946692466736})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.29791736602783203})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2665124237537384})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.26210951805114746})
store['active_learning_steps'][79]['eval_training']['best_epoch']=8
store['active_learning_steps'][79]['acquisition']={'indices': [26405, 45919, 22169, 3916, 12630, 34661, 55561, 54770, 24665, 34311], 'labels': [-1, -1, 2, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5870152711868286, 0.5112504363059998, 0.4412298798561096, 0.5330591201782227, 0.44626009464263916, 0.34859395027160645, 0.5348280072212219, 0.5467912554740906, 0.410158634185791, 0.36084628105163574]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9336515665054321})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5171822309494019})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3761444389820099})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3068782091140747})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2904653549194336})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.323189914226532})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2716636657714844})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3008371591567993})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26314425468444824})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29880473017692566})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.296644389629364})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.287622332572937})
store['active_learning_steps'][80]['training']['best_epoch']=9
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9728, 'crossentropy': 0.2372468017578125}
store['active_learning_steps'][80]['eval_training']={}
store['active_learning_steps'][80]['eval_training']['epochs']=[]
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6370995044708252})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.44900181889533997})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3266376256942749})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3019051253795624})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2712351679801941})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.28880828619003296})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2714868187904358})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25419706106185913})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.24565225839614868})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23128578066825867})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2196645587682724})
store['active_learning_steps'][80]['eval_training']['best_epoch']=11
store['active_learning_steps'][80]['acquisition']={'indices': [26110, 35641, 22040, 24934, 17039, 36152, 27877, 14658, 42826, 32227], 'labels': [-1, -1, -1, -1, -1, 7, 5, -1, 9, -1], 'scores': [0.35019826889038086, 0.41314172744750977, 0.5177115201950073, 0.4483078718185425, 0.5941809415817261, 0.48872387409210205, 0.6446915864944458, 0.5175234079360962, 0.39577239751815796, 0.35504019260406494]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.1176153421401978})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5733922719955444})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4061713218688965})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2952975630760193})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30219632387161255})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30852794647216797})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3079218864440918})
store['active_learning_steps'][81]['training']['best_epoch']=4
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9646, 'crossentropy': 0.3014820556640625}
store['active_learning_steps'][81]['eval_training']={}
store['active_learning_steps'][81]['eval_training']['epochs']=[]
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6233878135681152})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4381963312625885})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4196268916130066})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4065837860107422})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35840028524398804})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.31564491987228394})
store['active_learning_steps'][81]['eval_training']['best_epoch']=6
store['active_learning_steps'][81]['acquisition']={'indices': [27514, 38158, 50916, 5343, 58728, 22927, 21526, 3415, 13428, 30642], 'labels': [4, 8, 4, -1, -1, -1, -1, 3, 9, -1], 'scores': [0.32009392976760864, 0.24897277355194092, 0.46288055181503296, 0.272543728351593, 0.30803847312927246, 0.280523419380188, 0.4194570779800415, 0.4271904230117798, 0.4204009175300598, 0.2140423059463501]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.2107335329055786})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6266202926635742})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4449416995048523})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3817812204360962})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.302868127822876})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2816128134727478})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.283111572265625})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28283458948135376})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2872045934200287})
store['active_learning_steps'][82]['training']['best_epoch']=6
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9696, 'crossentropy': 0.260226611328125}
store['active_learning_steps'][82]['eval_training']={}
store['active_learning_steps'][82]['eval_training']['epochs']=[]
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.677820086479187})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.42959704995155334})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37765246629714966})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3117470145225525})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32665377855300903})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2784425616264343})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31031209230422974})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3103722929954529})
store['active_learning_steps'][82]['eval_training']['best_epoch']=6
store['active_learning_steps'][82]['acquisition']={'indices': [48288, 22898, 30176, 55278, 3691, 12066, 4935, 11727, 52169, 51242], 'labels': [-1, -1, -1, 0, 0, 8, 2, -1, 2, -1], 'scores': [0.45819950103759766, 0.3809250593185425, 0.3620108366012573, 0.565532922744751, 0.35854554176330566, 0.426405131816864, 0.2646369934082031, 0.5370488166809082, 0.41643619537353516, 0.5098695755004883]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.1056935787200928})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5968667268753052})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.410514771938324})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37243080139160156})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30880045890808105})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34236347675323486})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32019418478012085})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3257656991481781})
store['active_learning_steps'][83]['training']['best_epoch']=5
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.969, 'crossentropy': 0.273262353515625}
store['active_learning_steps'][83]['eval_training']={}
store['active_learning_steps'][83]['eval_training']['epochs']=[]
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6757071018218994})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4963115453720093})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4147487282752991})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3980925679206848})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.369588166475296})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34580427408218384})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3735046684741974})
store['active_learning_steps'][83]['eval_training']['best_epoch']=6
store['active_learning_steps'][83]['acquisition']={'indices': [21786, 53537, 5896, 3692, 1642, 7829, 18486, 42953, 22098, 22799], 'labels': [-1, -1, 8, 7, 6, -1, -1, 4, -1, 9], 'scores': [0.4501509666442871, 0.26596057415008545, 0.5139482021331787, 0.4439169764518738, 0.46524548530578613, 0.4818268418312073, 0.31441307067871094, 0.31986165046691895, 0.5422118902206421, 0.4060821533203125]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.154062271118164})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5759663581848145})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4055038094520569})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3679755926132202})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3042106628417969})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3069714903831482})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32337474822998047})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2936827838420868})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30613481998443604})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2963889241218567})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30938178300857544})
store['active_learning_steps'][84]['training']['best_epoch']=8
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9704, 'crossentropy': 0.254579638671875}
store['active_learning_steps'][84]['eval_training']={}
store['active_learning_steps'][84]['eval_training']['epochs']=[]
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7463045120239258})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4026617407798767})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.327480673789978})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32833606004714966})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2711494565010071})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2614900767803192})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2665184736251831})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2582479417324066})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.24124836921691895})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.24744731187820435})
store['active_learning_steps'][84]['eval_training']['best_epoch']=9
store['active_learning_steps'][84]['acquisition']={'indices': [21134, 22284, 48681, 7409, 11328, 14096, 9858, 4724, 27016, 45746], 'labels': [4, -1, 2, -1, -1, 5, -1, -1, -1, 8], 'scores': [0.43951016664505005, 0.32100749015808105, 0.5789427757263184, 0.3824721574783325, 0.4321180582046509, 0.40371328592300415, 0.3374234437942505, 0.5098211765289307, 0.39766407012939453, 0.48164236545562744]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.2110013961791992})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6460246443748474})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4120604693889618})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3624285161495209})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31514406204223633})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3353648781776428})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2910516858100891})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3120570778846741})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33457088470458984})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3113124966621399})
store['active_learning_steps'][85]['training']['best_epoch']=7
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.264002490234375}
store['active_learning_steps'][85]['eval_training']={}
store['active_learning_steps'][85]['eval_training']['epochs']=[]
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7067363858222961})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48264631628990173})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3778396248817444})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3441923260688782})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3240765333175659})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2763091027736664})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.28762465715408325})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2854160666465759})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24424517154693604})
store['active_learning_steps'][85]['eval_training']['best_epoch']=9
store['active_learning_steps'][85]['acquisition']={'indices': [15216, 22604, 50342, 19917, 1488, 21544, 50137, 39321, 36581, 2184], 'labels': [3, -1, 8, -1, -1, -1, -1, -1, -1, 2], 'scores': [0.4749756455421448, 0.3176305294036865, 0.5491707921028137, 0.34425580501556396, 0.45914459228515625, 0.2896186113357544, 0.3055459260940552, 0.30002760887145996, 0.33823978900909424, 0.47462135553359985]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.191343903541565})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6217368841171265})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4000404477119446})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34599560499191284})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30595213174819946})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31458693742752075})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2823711037635803})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2860107123851776})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28578221797943115})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2857222259044647})
store['active_learning_steps'][86]['training']['best_epoch']=7
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9726, 'crossentropy': 0.2468789306640625}
store['active_learning_steps'][86]['eval_training']={}
store['active_learning_steps'][86]['eval_training']['epochs']=[]
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6916764974594116})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4486730694770813})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36926352977752686})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3007034361362457})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30946534872055054})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2763214409351349})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25360479950904846})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.257699191570282})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25453007221221924})
store['active_learning_steps'][86]['eval_training']['best_epoch']=7
store['active_learning_steps'][86]['acquisition']={'indices': [51242, 32679, 54590, 31919, 37957, 13646, 10288, 17947, 403, 56375], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.557827353477478, 0.3338075876235962, 0.2988177537918091, 0.5759439468383789, 0.4297320246696472, 0.6440413594245911, 0.6098880767822266, 0.437694787979126, 0.5254737734794617, 0.5354604721069336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.19102942943573})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5726135969161987})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4288308620452881})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35335877537727356})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3190195560455322})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2825365960597992})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.285413920879364})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3101734519004822})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2967856526374817})
store['active_learning_steps'][87]['training']['best_epoch']=6
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9693, 'crossentropy': 0.2668057861328125}
store['active_learning_steps'][87]['eval_training']={}
store['active_learning_steps'][87]['eval_training']['epochs']=[]
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.696133017539978})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.455671489238739})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4009573459625244})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.384012371301651})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.278542697429657})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30124354362487793})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2958499789237976})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2909899950027466})
store['active_learning_steps'][87]['eval_training']['best_epoch']=5
store['active_learning_steps'][87]['acquisition']={'indices': [33818, 30308, 15141, 30766, 482, 40378, 57367, 27637, 23519, 44803], 'labels': [-1, -1, -1, -1, -1, -1, 7, -1, -1, -1], 'scores': [0.5405805110931396, 0.5997896194458008, 0.4529285430908203, 0.39258527755737305, 0.48886799812316895, 0.5148720741271973, 0.3817315697669983, 0.6197628974914551, 0.3716745376586914, 0.624161958694458]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1277869939804077})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.541405439376831})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4154033362865448})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35369107127189636})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31599390506744385})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2892824411392212})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30428963899612427})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2970306873321533})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3314693570137024})
store['active_learning_steps'][88]['training']['best_epoch']=6
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9726, 'crossentropy': 0.249643603515625}
store['active_learning_steps'][88]['eval_training']={}
store['active_learning_steps'][88]['eval_training']['epochs']=[]
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7242051959037781})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4702405333518982})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.399382084608078})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3165661096572876})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30457577109336853})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29734474420547485})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2923564314842224})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2744913399219513})
store['active_learning_steps'][88]['eval_training']['best_epoch']=8
store['active_learning_steps'][88]['acquisition']={'indices': [37647, 48393, 33231, 56446, 39891, 46148, 26998, 30368, 33795, 9561], 'labels': [-1, -1, -1, -1, 4, -1, 3, -1, -1, -1], 'scores': [0.44369256496429443, 0.4410734176635742, 0.42093855142593384, 0.35811400413513184, 0.41109132766723633, 0.5095281600952148, 0.38819265365600586, 0.3985494375228882, 0.3937375545501709, 0.3772818446159363]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.120459794998169})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5867949724197388})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39926284551620483})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3694186210632324})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3013961911201477})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2751658856868744})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2657242715358734})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29724666476249695})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27415239810943604})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2908061444759369})
store['active_learning_steps'][89]['training']['best_epoch']=7
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9745, 'crossentropy': 0.23848251953125}
store['active_learning_steps'][89]['eval_training']={}
store['active_learning_steps'][89]['eval_training']['epochs']=[]
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.692058265209198})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.432803213596344})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.35194194316864014})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32140159606933594})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28614938259124756})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2889178991317749})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.24941924214363098})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2456163614988327})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2708854675292969})
store['active_learning_steps'][89]['eval_training']['best_epoch']=8
store['active_learning_steps'][89]['acquisition']={'indices': [55323, 35949, 4937, 33378, 867, 51872, 59095, 41882, 9528, 55995], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.39276933670043945, 0.4010441303253174, 0.5632793307304382, 0.3488442897796631, 0.4778745174407959, 0.48029816150665283, 0.2626841068267822, 0.39470934867858887, 0.4353083372116089, 0.35770249366760254]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.11552095413208})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5798102021217346})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.41792362928390503})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35987019538879395})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30836033821105957})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29608607292175293})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29133281111717224})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28801971673965454})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2985508441925049})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2726195156574249})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2947036325931549})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27695783972740173})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2972155213356018})
store['active_learning_steps'][90]['training']['best_epoch']=10
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.97, 'crossentropy': 0.2574779296875}
store['active_learning_steps'][90]['eval_training']={}
store['active_learning_steps'][90]['eval_training']['epochs']=[]
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6141680479049683})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.44825127720832825})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3937423527240753})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3032250702381134})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2763618528842926})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2621588110923767})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25846153497695923})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2391170859336853})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.23567470908164978})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2479511797428131})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.24628692865371704})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2424490749835968})
store['active_learning_steps'][90]['eval_training']['best_epoch']=9
store['active_learning_steps'][90]['acquisition']={'indices': [44746, 28536, 33451, 22272, 22636, 42041, 48397, 1033, 29530, 34540], 'labels': [9, 3, -1, 5, -1, -1, 5, 2, 4, -1], 'scores': [0.4648856818675995, 0.5702153444290161, 0.39355677366256714, 0.6686514616012573, 0.38314735889434814, 0.4642057418823242, 0.425811767578125, 0.7094495892524719, 0.40379971265792847, 0.36864209175109863]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1805243492126465})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5850147604942322})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4134067893028259})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36198943853378296})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3071129620075226})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2870819568634033})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.295582115650177})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2999853491783142})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2871737480163574})
store['active_learning_steps'][91]['training']['best_epoch']=6
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.2638451171875}
store['active_learning_steps'][91]['eval_training']={}
store['active_learning_steps'][91]['eval_training']['epochs']=[]
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6813746690750122})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4992496371269226})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40719056129455566})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3846786618232727})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3308030366897583})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.31881219148635864})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3074112832546234})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31670063734054565})
store['active_learning_steps'][91]['eval_training']['best_epoch']=7
store['active_learning_steps'][91]['acquisition']={'indices': [35025, 29928, 25022, 8214, 5760, 22098, 7003, 30069, 33798, 41999], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.36509668827056885, 0.5341637134552002, 0.4001758098602295, 0.2984405755996704, 0.5135788321495056, 0.546528160572052, 0.3289121389389038, 0.42377161979675293, 0.558324933052063, 0.5335394740104675]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1294971704483032})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.516700267791748})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3740677833557129})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3402256369590759})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28462207317352295})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2741174101829529})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2705835700035095})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2776155471801758})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27233850955963135})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25704625248908997})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27352356910705566})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25936180353164673})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29099440574645996})
store['active_learning_steps'][92]['training']['best_epoch']=10
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9768, 'crossentropy': 0.2159516845703125}
store['active_learning_steps'][92]['eval_training']={}
store['active_learning_steps'][92]['eval_training']['epochs']=[]
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8179528713226318})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4919710159301758})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38560956716537476})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33862629532814026})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3074859380722046})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2877332270145416})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2851009964942932})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.24009983241558075})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2614730894565582})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23147794604301453})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23747123777866364})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2589653730392456})
store['active_learning_steps'][92]['eval_training']['best_epoch']=10
store['active_learning_steps'][92]['acquisition']={'indices': [16537, 28339, 9923, 23791, 40780, 8715, 29287, 58227, 8506, 40218], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5791836977005005, 0.5413460731506348, 0.42520439624786377, 0.5554304122924805, 0.44133472442626953, 0.476285457611084, 0.553635835647583, 0.6393451690673828, 0.5573512315750122, 0.5823712944984436]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.2109789848327637})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5418322682380676})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3634871542453766})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.38375043869018555})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30472537875175476})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3017672002315521})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2938183546066284})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29225510358810425})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28312820196151733})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28655731678009033})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28127989172935486})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2637696862220764})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28623250126838684})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.276479572057724})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2880518436431885})
store['active_learning_steps'][93]['training']['best_epoch']=12
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9741, 'crossentropy': 0.2362104248046875}
store['active_learning_steps'][93]['eval_training']={}
store['active_learning_steps'][93]['eval_training']['epochs']=[]
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7206214666366577})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4230692684650421})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35287076234817505})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.29939156770706177})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2923087477684021})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.27498456835746765})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.26315274834632874})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2144969403743744})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.26022428274154663})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2197539210319519})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.21979176998138428})
store['active_learning_steps'][93]['eval_training']['best_epoch']=8
store['active_learning_steps'][93]['acquisition']={'indices': [41930, 19904, 41817, 57215, 45292, 24740, 47361, 10806, 52326, 38774], 'labels': [-1, 7, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.3584188222885132, 0.6230121850967407, 0.39501285552978516, 0.45053958892822266, 0.5342816114425659, 0.5484938025474548, 0.513656735420227, 0.5676913261413574, 0.5071101188659668, 0.419175386428833]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.326500415802002})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.6212990880012512})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4032226800918579})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34949564933776855})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29984530806541443})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31042274832725525})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2741079330444336})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2822507619857788})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29331356287002563})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29510876536369324})
store['active_learning_steps'][94]['training']['best_epoch']=7
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.235233740234375}
store['active_learning_steps'][94]['eval_training']={}
store['active_learning_steps'][94]['eval_training']['epochs']=[]
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6598814725875854})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.452181875705719})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3563562333583832})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35200339555740356})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27459636330604553})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28821974992752075})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26524585485458374})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25142815709114075})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2889598608016968})
store['active_learning_steps'][94]['eval_training']['best_epoch']=8
store['active_learning_steps'][94]['acquisition']={'indices': [57478, 35773, 5309, 54080, 15952, 41557, 25414, 26641, 17952, 45559], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5497936010360718, 0.3659243583679199, 0.3147423267364502, 0.5971289873123169, 0.5633348226547241, 0.6108648777008057, 0.510494589805603, 0.4529911279678345, 0.663070797920227, 0.6003701686859131]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.4063124656677246})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5609175562858582})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.4119007885456085})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2917456030845642})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2916008234024048})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29311662912368774})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24785923957824707})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28075557947158813})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2686081528663635})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2363920509815216})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2753356695175171})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2569887638092041})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2701369822025299})
store['active_learning_steps'][95]['training']['best_epoch']=10
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9768, 'crossentropy': 0.209585791015625}
store['active_learning_steps'][95]['eval_training']={}
store['active_learning_steps'][95]['eval_training']['epochs']=[]
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7220397591590881})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.44319063425064087})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32159844040870667})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3486612141132355})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26653003692626953})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2631669342517853})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2632075250148773})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24431630969047546})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2286812663078308})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.245793417096138})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.21678239107131958})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23416948318481445})
store['active_learning_steps'][95]['eval_training']['best_epoch']=11
store['active_learning_steps'][95]['acquisition']={'indices': [34920, 52456, 25457, 54560, 1153, 39936, 14238, 7784, 47609, 36595], 'labels': [-1, 2, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5547552108764648, 0.6020339727401733, 0.5598131418228149, 0.47869396209716797, 0.5806715488433838, 0.3481302261352539, 0.5246983766555786, 0.5215444564819336, 0.5080710649490356, 0.36109089851379395]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.1741013526916504})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5706976056098938})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.38053375482559204})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31228917837142944})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3141043782234192})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2618737816810608})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2681448757648468})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30573898553848267})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27300408482551575})
store['active_learning_steps'][96]['training']['best_epoch']=6
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9738, 'crossentropy': 0.239211376953125}
store['active_learning_steps'][96]['eval_training']={}
store['active_learning_steps'][96]['eval_training']['epochs']=[]
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6263842582702637})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4564405381679535})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3772253394126892})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3412206172943115})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32161736488342285})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29663342237472534})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27103397250175476})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27127039432525635})
store['active_learning_steps'][96]['eval_training']['best_epoch']=7
store['active_learning_steps'][96]['acquisition']={'indices': [25627, 10310, 43952, 5813, 7203, 21007, 23860, 31185, 16047, 50917], 'labels': [-1, -1, -1, -1, -1, -1, -1, 2, -1, -1], 'scores': [0.42575955390930176, 0.5603172779083252, 0.34159600734710693, 0.18686127662658691, 0.4644516706466675, 0.5587033033370972, 0.33753859996795654, 0.50413578748703, 0.3813058137893677, 0.21487081050872803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.2873865365982056})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.6222814321517944})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36130452156066895})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3306165635585785})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3182917535305023})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2749784588813782})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.277573823928833})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25352388620376587})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2978334426879883})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29030489921569824})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2427612543106079})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2636410593986511})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27131980657577515})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27021822333335876})
store['active_learning_steps'][97]['training']['best_epoch']=11
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9769, 'crossentropy': 0.2093481201171875}
store['active_learning_steps'][97]['eval_training']={}
store['active_learning_steps'][97]['eval_training']['epochs']=[]
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6952707171440125})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44675499200820923})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3674391210079193})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3005705177783966})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26662683486938477})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.28693798184394836})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25521689653396606})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2369432896375656})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.23435455560684204})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2209164798259735})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.21338118612766266})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.22006317973136902})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.18620732426643372})
store['active_learning_steps'][97]['eval_training']['best_epoch']=13
store['active_learning_steps'][97]['acquisition']={'indices': [51926, 40127, 54323, 37268, 17780, 1008, 40852, 1082, 40286, 11658], 'labels': [4, -1, -1, -1, -1, -1, 8, -1, -1, -1], 'scores': [0.3897244781255722, 0.4685477018356323, 0.5135213732719421, 0.47494375705718994, 0.5643852949142456, 0.45583879947662354, 0.5247495174407959, 0.5079425573348999, 0.28770411014556885, 0.4684717655181885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1267063617706299})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5447216033935547})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4239453375339508})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34775310754776})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29984575510025024})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2755105793476105})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2803618907928467})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27187758684158325})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28841662406921387})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29950660467147827})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2827162444591522})
store['active_learning_steps'][98]['training']['best_epoch']=8
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9769, 'crossentropy': 0.2318804931640625}
store['active_learning_steps'][98]['eval_training']={}
store['active_learning_steps'][98]['eval_training']['epochs']=[]
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6751270294189453})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4125860929489136})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34035545587539673})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.327303409576416})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2719283103942871})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30651313066482544})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.25635668635368347})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2567746639251709})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.269599050283432})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23878496885299683})
store['active_learning_steps'][98]['eval_training']['best_epoch']=10
store['active_learning_steps'][98]['acquisition']={'indices': [22442, 23027, 4379, 44317, 35384, 14844, 33966, 10044, 33083, 58094], 'labels': [2, -1, -1, -1, -1, -1, -1, 6, -1, 7], 'scores': [0.42918533086776733, 0.6708345413208008, 0.48224323987960815, 0.5030133724212646, 0.663083553314209, 0.3845701217651367, 0.4956003427505493, 0.5715535581111908, 0.3512386083602905, 0.5631334781646729]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.2523895502090454})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5804482698440552})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.41621071100234985})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.320795476436615})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3304629623889923})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3103470504283905})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2958451509475708})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3124977946281433})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2953520119190216})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2739335000514984})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2748330533504486})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27363157272338867})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30583226680755615})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2769773304462433})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2991572916507721})
store['active_learning_steps'][99]['training']['best_epoch']=12
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.974, 'crossentropy': 0.25073994140625}
store['active_learning_steps'][99]['eval_training']={}
store['active_learning_steps'][99]['eval_training']['epochs']=[]
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7546232342720032})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4656479060649872})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.32966339588165283})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31492912769317627})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2828611135482788})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28742313385009766})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2510148286819458})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27597683668136597})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2369147688150406})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2482776641845703})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.22787296772003174})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.21914848685264587})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24199527502059937})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.21411675214767456})
store['active_learning_steps'][99]['eval_training']['best_epoch']=14
store['active_learning_steps'][99]['acquisition']={'indices': [16606, 36550, 42161, 17855, 32823, 32932, 55196, 13376, 52044, 3895], 'labels': [-1, -1, 3, 6, -1, -1, 6, 3, -1, -1], 'scores': [0.6317483186721802, 0.5834372043609619, 0.5467817783355713, 0.7024242281913757, 0.4915348291397095, 0.4337249994277954, 0.7224658131599426, 0.6217811107635498, 0.6303094029426575, 0.4008256196975708]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.190441370010376})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5495160222053528})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38895946741104126})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3246675133705139})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28798091411590576})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3304894268512726})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27726250886917114})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27717024087905884})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25213122367858887})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25461822748184204})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2702597975730896})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28678491711616516})
store['active_learning_steps'][100]['training']['best_epoch']=9
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9729, 'crossentropy': 0.244062451171875}
