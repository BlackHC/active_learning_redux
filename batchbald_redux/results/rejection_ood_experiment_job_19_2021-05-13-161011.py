store = {}
store['timestamp']=1620918611
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=19']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=19
store['worker_id']=19
store['num_workers']=20
store['config']={'seed': 1262, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 1000, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.3199095726013184})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.636904239654541})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.044189214706421})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.9680259227752686})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.662, 'crossentropy': 2.1365548828125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2293310165405273})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2187228202819824})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.180020809173584})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [3778, 37973, 14596, 47587, 43679, 39611, 8469, 51730, 49509, 37592], 'labels': [0, 6, 2, 3, 6, 8, 0, 9, 8, 5], 'scores': [0.81461101770401, 0.8458417654037476, 0.5857087969779968, 0.9770788550376892, 0.7408660650253296, 0.8243671655654907, 0.773670494556427, 0.7745272517204285, 0.8140236735343933, 0.7314304113388062]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.6922049522399902})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.9858964681625366})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.2315573692321777})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.357468843460083})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7212, 'crossentropy': 1.6221568359375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0188184976577759})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.014093041419983})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.9556791186332703})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [13843, 26321, 47468, 12250, 53517, 16003, 50897, 57191, 31056, 2504], 'labels': [5, -1, 5, 8, 8, 3, 2, 2, 2, -1], 'scores': [0.5006543397903442, 0.30327463150024414, 0.6100045442581177, 0.6563917994499207, 0.7163160443305969, 0.655880331993103, 0.49776744842529297, 0.48815399408340454, 0.7993704676628113, 0.34636032581329346]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.4183425903320312})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.6624910831451416})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.8379366397857666})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.1557352542877197})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7656, 'crossentropy': 1.3298271484375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 0.8841955661773682})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 0.8325762748718262})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 0.8590915203094482})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [1537, 25480, 27883, 46376, 51590, 18130, 11148, 42629, 37689, 2032], 'labels': [4, 3, 2, 7, 9, 8, 4, 7, 3, 4], 'scores': [0.6796984672546387, 0.8167041540145874, 0.6047383546829224, 0.48020175099372864, 0.599241316318512, 0.5712761282920837, 0.6020410060882568, 0.436077743768692, 0.4354371428489685, 0.6493789553642273]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.221343994140625})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.356168270111084})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.364746332168579})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.5501030683517456})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.8181, 'crossentropy': 1.08232021484375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.883785605430603})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8206401467323303})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.7892047166824341})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [10992, 44013, 49057, 9542, 22145, 56710, 38425, 30932, 46242, 5216], 'labels': [0, 4, -1, 2, 6, -1, -1, 0, 3, -1], 'scores': [0.6232484579086304, 0.6438181400299072, 0.3860197067260742, 0.3734344244003296, 0.5376814603805542, 0.3466982841491699, 0.5224605798721313, 0.5472629070281982, 0.5095545053482056, 0.432344913482666]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.2387619018554688})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3708062171936035})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.3787037134170532})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.6151883602142334})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8012, 'crossentropy': 1.13149853515625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.874803364276886})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.8467443585395813})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.8292413353919983})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [5740, 26503, 43004, 18656, 18419, 5000, 58085, 32306, 29602, 24820], 'labels': [9, 3, 8, 1, 8, 7, 5, 1, -1, 5], 'scores': [0.8064008951187134, 0.5430695116519928, 0.47477471828460693, 0.5069609880447388, 0.5328764319419861, 0.6491792798042297, 0.6297382116317749, 0.38029348850250244, 0.2884082794189453, 0.4706760048866272]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0673909187316895})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.4512864351272583})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.4802327156066895})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.5289583206176758})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.835, 'crossentropy': 1.0072236328125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.8973163366317749})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.8500909209251404})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.7918825149536133})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [18782, 9036, 5833, 19843, 39668, 50233, 28182, 46139, 51988, 56571], 'labels': [5, 2, 1, 2, 8, 7, 8, 0, 7, 5], 'scores': [0.5338386297225952, 0.4736989736557007, 0.41348540782928467, 0.6184313893318176, 0.47548508644104004, 0.6346539258956909, 0.4274662137031555, 0.4111211895942688, 0.6762667894363403, 0.514797031879425]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9660754203796387})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0129268169403076})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9916197061538696})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0619322061538696})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8273, 'crossentropy': 0.91370234375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8288764953613281})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7449287176132202})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.6968972682952881})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [8849, 2284, 1059, 313, 10594, 8902, 21072, 56938, 9718, 2634], 'labels': [7, 9, 8, 9, 4, 9, 9, 5, 4, 7], 'scores': [0.4876863956451416, 0.5401979088783264, 0.42622900009155273, 0.2623254060745239, 0.45568525791168213, 0.401578426361084, 0.4339810609817505, 0.4745646119117737, 0.520715594291687, 0.5104711651802063]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9647113084793091})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9802566766738892})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0436149835586548})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.976555347442627})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.842, 'crossentropy': 0.8986013671875}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8929582834243774})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8129141330718994})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.7611162662506104})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [31710, 19309, 57880, 22974, 38817, 17756, 48776, 34881, 20183, 22034], 'labels': [8, 6, 9, 4, 5, 8, 6, 7, 4, 4], 'scores': [0.41121959686279297, 0.3135601282119751, 0.5585421323776245, 0.4838470220565796, 0.39625781774520874, 0.4480157494544983, 0.32030266523361206, 0.42762434482574463, 0.5373584032058716, 0.44201570749282837]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.929722249507904})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8638863563537598})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9707743525505066})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0366657972335815})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0784449577331543})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8878, 'crossentropy': 0.774747021484375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7211949825286865})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6424705386161804})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6054317951202393})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.5559580326080322})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [52971, 32381, 52747, 42805, 22779, 35629, 9952, 39835, 15797, 37007], 'labels': [2, 6, 3, 2, 5, -1, 8, 7, 6, -1], 'scores': [0.6850792169570923, 0.6130871772766113, 0.7502171993255615, 0.4218354821205139, 0.6073697805404663, 0.5261633396148682, 0.5130906105041504, 0.5962072610855103, 0.5701786279678345, 0.39999496936798096]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8014163970947266})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8368119597434998})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.754310131072998})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.892943263053894})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8987049460411072})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9603527784347534})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8912, 'crossentropy': 0.733180224609375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7433477640151978})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6085553169250488})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.5825536251068115})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5332558155059814})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5252364873886108})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [11607, 9476, 24110, 53940, 9258, 43717, 11735, 49131, 26452, 51575], 'labels': [1, -1, 8, 0, -1, -1, 1, 1, 6, -1], 'scores': [0.5786798596382141, 0.5034240484237671, 0.5525314807891846, 0.5258561372756958, 0.5161208510398865, 0.4800945520401001, 0.5974861979484558, 0.5169645547866821, 0.5037851333618164, 0.6419636011123657]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8497002720832825})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8139305114746094})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8620935678482056})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9005517363548279})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8718364238739014})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8891, 'crossentropy': 0.6812685546875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7279382944107056})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6062976121902466})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5587342977523804})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5641481280326843})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [11643, 49497, 57311, 21007, 19089, 581, 17707, 17948, 32481, 12615], 'labels': [5, 0, 5, 3, 5, 3, 9, 8, 2, 4], 'scores': [0.5161905288696289, 0.5630941390991211, 0.6347798705101013, 0.5051584243774414, 0.40843743085861206, 0.7415027022361755, 0.41337716579437256, 0.5499791502952576, 0.6344196200370789, 0.3893800377845764]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8380982279777527})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6706569790840149})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7123658061027527})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7099511623382568})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7242661714553833})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9111, 'crossentropy': 0.57347275390625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7260128259658813})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5551849603652954})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5437934398651123})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.46655625104904175})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [55011, 44712, 32276, 6604, 45031, 14286, 54928, 26994, 14264, 50756], 'labels': [2, 4, 3, 8, 3, 3, 5, 2, -1, -1], 'scores': [0.5377609729766846, 0.45964160561561584, 0.5423662066459656, 0.36362022161483765, 0.4774462580680847, 0.430364727973938, 0.42449671030044556, 0.5116013288497925, 0.41428112983703613, 0.4301002025604248]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7106528282165527})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5832291841506958})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.640962541103363})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7077096700668335})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6470280885696411})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.916, 'crossentropy': 0.545078125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6687599420547485})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5228719711303711})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.468658983707428})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.47591572999954224})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [46869, 26591, 19025, 29189, 25971, 17178, 4083, 38642, 17855, 17896], 'labels': [6, -1, 8, 8, 4, 8, 8, 6, 6, 4], 'scores': [0.3195849657058716, 0.31427979469299316, 0.3853950500488281, 0.5203777551651001, 0.49879491329193115, 0.38280290365219116, 0.5530672073364258, 0.4471836984157562, 0.48366743326187134, 0.6966782808303833]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7789425849914551})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6550357341766357})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6059725284576416})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.689401388168335})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.691105306148529})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6852125525474548})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9194, 'crossentropy': 0.5470466796875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6789854168891907})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.4864720404148102})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4915665090084076})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.46522748470306396})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.4340684413909912})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [11065, 20532, 57592, 35225, 33524, 3094, 29863, 5459, 459, 33150], 'labels': [-1, 7, 2, -1, -1, 8, -1, -1, -1, 8], 'scores': [0.4251096248626709, 0.48234713077545166, 0.5120717883110046, 0.4715917110443115, 0.5508471727371216, 0.6160625219345093, 0.5354702472686768, 0.4204944372177124, 0.6376008987426758, 0.6347994804382324]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7838104367256165})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6507313251495361})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6383717656135559})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6491705179214478})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6551996469497681})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6970275044441223})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9242, 'crossentropy': 0.5550439453125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6531228423118591})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5116279721260071})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4535623788833618})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4469020366668701})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.441074013710022})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [35010, 23100, 55120, 7281, 49125, 49863, 16011, 38824, 47920, 38920], 'labels': [3, 9, -1, 0, -1, 5, 5, 1, 5, 7], 'scores': [0.4680328369140625, 0.4935827851295471, 0.4437206983566284, 0.587816596031189, 0.5062395334243774, 0.48253095149993896, 0.6340362429618835, 0.433940052986145, 0.45863133668899536, 0.4872317910194397]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7912824749946594})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5988857746124268})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5753250122070312})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6168971061706543})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6725444793701172})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7646312713623047})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9162, 'crossentropy': 0.55036806640625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6748162508010864})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5269115567207336})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5074925422668457})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.4477797746658325})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.47022634744644165})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [52201, 21265, 46540, 58929, 5720, 47895, 39605, 55629, 3762, 2044], 'labels': [8, -1, -1, -1, 4, -1, -1, -1, 8, 6], 'scores': [0.45162057876586914, 0.405666708946228, 0.4025557041168213, 0.36634206771850586, 0.6195321083068848, 0.3243900537490845, 0.3435027599334717, 0.36488550901412964, 0.4298202395439148, 0.462854266166687]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7696253657341003})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5628082752227783})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5855610966682434})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5857759714126587})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5841763019561768})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.912, 'crossentropy': 0.5512310546875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6588884592056274})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5213299989700317})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.521550178527832})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.49090930819511414})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [21990, 23202, 53350, 39316, 14394, 37048, 138, 55669, 40732, 10424], 'labels': [1, 3, 0, 7, 3, 9, 5, 2, 0, 3], 'scores': [0.5355981588363647, 0.4111294746398926, 0.44096261262893677, 0.4356604814529419, 0.5441452264785767, 0.6093316078186035, 0.4100097417831421, 0.37363457679748535, 0.5601431727409363, 0.45866650342941284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8481929302215576})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5529541969299316})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5035183429718018})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5114516019821167})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5014055967330933})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5282949209213257})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.561691164970398})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5774638652801514})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9361, 'crossentropy': 0.5164521484375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6985775828361511})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4638303518295288})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4553849697113037})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.41389021277427673})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.41539108753204346})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3699566125869751})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3731248378753662})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [7552, 42963, 45469, 59303, 560, 42787, 10064, 3989, 13256, 48360], 'labels': [-1, 9, -1, 8, 7, 4, 8, -1, -1, 3], 'scores': [0.4956629276275635, 0.7002498507499695, 0.6410504579544067, 0.5332491397857666, 0.34154143929481506, 0.6721388697624207, 0.47540828585624695, 0.4244520664215088, 0.30997610092163086, 0.5412880778312683]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8729130029678345})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5828325748443604})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5279057621955872})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5567725896835327})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5183735489845276})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5618239045143127})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5509774684906006})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.616219162940979})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9379, 'crossentropy': 0.4740265625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6281248927116394})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4809170067310333})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4341898560523987})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3722681999206543})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.36612483859062195})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.36656010150909424})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3627636432647705})
store['active_learning_steps'][18]['eval_training']['best_epoch']=7
store['active_learning_steps'][18]['acquisition']={'indices': [54926, 24798, 29991, 24194, 45917, 7288, 20020, 3258, 49227, 59391], 'labels': [8, 4, 3, 9, 9, -1, -1, -1, 9, -1], 'scores': [0.43478137254714966, 0.21588294208049774, 0.6789236664772034, 0.521816074848175, 0.46829909086227417, 0.3628748655319214, 0.40597307682037354, 0.2900047302246094, 0.5466669201850891, 0.32000505924224854]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9075558185577393})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5605801343917847})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5390499830245972})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5609855651855469})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5200244188308716})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6021089553833008})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5795223712921143})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5707697868347168})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9318, 'crossentropy': 0.50085634765625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6323777437210083})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.469688355922699})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.40793099999427795})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.3959624767303467})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.37144413590431213})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4033539891242981})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.3835689127445221})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [25418, 50841, 34741, 28686, 36008, 52971, 53734, 48572, 28710, 3944], 'labels': [8, 4, -1, -1, -1, -1, 0, -1, -1, 5], 'scores': [0.495807409286499, 0.4938523769378662, 0.5433796644210815, 0.5620245337486267, 0.4198194146156311, 0.4517700672149658, 0.601226270198822, 0.4594258666038513, 0.43207597732543945, 0.6546621322631836]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8071243762969971})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5251281261444092})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5780056715011597})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6292561292648315})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.614250898361206})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9329, 'crossentropy': 0.4710265625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6731314063072205})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5441250801086426})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4976653456687927})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4688754677772522})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [55545, 33062, 22611, 28387, 57728, 54469, 24632, 45732, 8918, 3512], 'labels': [2, 7, 2, 1, 9, 8, 2, 3, 8, -1], 'scores': [0.39469200372695923, 0.45993876457214355, 0.3704017400741577, 0.27658283710479736, 0.48685622215270996, 0.40747296810150146, 0.4026132822036743, 0.5530219078063965, 0.2797468900680542, 0.18172669410705566]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8252456188201904})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5161158442497253})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5077539682388306})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.47154858708381653})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4698823094367981})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4703540802001953})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5236650705337524})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5432969927787781})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9411, 'crossentropy': 0.44966015625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6564010977745056})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.47664594650268555})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.39231568574905396})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3654015362262726})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3517746925354004})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3135465979576111})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.34729182720184326})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [59609, 1341, 29076, 1248, 2297, 4612, 44910, 1657, 15683, 6067], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4766000509262085, 0.5279210805892944, 0.3528188467025757, 0.376259446144104, 0.6212061047554016, 0.5132362842559814, 0.46992921829223633, 0.38962095975875854, 0.4465330243110657, 0.3737003803253174]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.051858901977539})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6210819482803345})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5738069415092468})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5494605302810669})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6378242373466492})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6845608353614807})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5379244685173035})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6291755437850952})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.611350417137146})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6301470994949341})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9393, 'crossentropy': 0.488175390625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6854872703552246})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.47541356086730957})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.40265074372291565})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.3916659355163574})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.374190092086792})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.37046074867248535})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3675926923751831})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3629934787750244})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.34556737542152405})
store['active_learning_steps'][22]['eval_training']['best_epoch']=9
store['active_learning_steps'][22]['acquisition']={'indices': [20226, 3425, 59361, 50342, 44758, 13077, 32172, 411, 13156, 35233], 'labels': [-1, 8, 8, 8, -1, 0, -1, -1, 2, -1], 'scores': [0.45988285541534424, 0.2669559717178345, 0.6433848142623901, 0.647442102432251, 0.31062400341033936, 0.45153939723968506, 0.42029476165771484, 0.5528945922851562, 0.547560065984726, 0.3048861026763916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9299880266189575})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.49047544598579407})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4798193573951721})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45657026767730713})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5051063299179077})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4467284083366394})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.49488580226898193})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5909091830253601})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.49056172370910645})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9475, 'crossentropy': 0.43163291015625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.603036105632782})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4272502064704895})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.37368541955947876})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.345559298992157})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.33475857973098755})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3596605658531189})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.34889286756515503})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.34520620107650757})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [40345, 3802, 31485, 39788, 57244, 50802, 21173, 22133, 42774, 18966], 'labels': [-1, -1, -1, -1, -1, -1, -1, 2, -1, 7], 'scores': [0.48523640632629395, 0.47184884548187256, 0.4292118549346924, 0.27356600761413574, 0.37304389476776123, 0.44030237197875977, 0.5163092017173767, 0.6226286888122559, 0.3577946424484253, 0.4520508050918579]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9523816108703613})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5762410163879395})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5109521746635437})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.45910024642944336})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.48454898595809937})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49874067306518555})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5273737907409668})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9398, 'crossentropy': 0.44158408203125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6936925649642944})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4979446828365326})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.38627761602401733})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.38276463747024536})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3762705326080322})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3621920645236969})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [54298, 27243, 50659, 2449, 48594, 44652, 42986, 49828, 50981, 54885], 'labels': [-1, 6, -1, 4, 6, -1, 1, -1, 4, 6], 'scores': [0.33244049549102783, 0.5451325178146362, 0.35596680641174316, 0.47330760955810547, 0.4590674638748169, 0.34779036045074463, 0.4144284129142761, 0.34694159030914307, 0.5400001406669617, 0.5125253200531006]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9371111392974854})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5318285226821899})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.47602537274360657})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5213634371757507})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.45482075214385986})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5064988732337952})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4909089207649231})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5847180485725403})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.939, 'crossentropy': 0.466116357421875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6134737133979797})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4823012053966522})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.377785325050354})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3715388774871826})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.37918728590011597})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3354259133338928})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.33968693017959595})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [13253, 57523, 36014, 50461, 8829, 50425, 9030, 6676, 459, 4738], 'labels': [-1, 3, 6, 7, -1, 6, -1, -1, -1, 0], 'scores': [0.49183720350265503, 0.6967099905014038, 0.4363178014755249, 0.6440677046775818, 0.6012647747993469, 0.6580196022987366, 0.5628721714019775, 0.5556123852729797, 0.7954881191253662, 0.5830416679382324]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8309128284454346})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5066866874694824})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.44585710763931274})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4187876582145691})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4501957297325134})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.46721524000167847})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.46023353934288025})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9388, 'crossentropy': 0.413908740234375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6168086528778076})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.46854257583618164})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.38650405406951904})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.39043331146240234})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3485802114009857})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.35221558809280396})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [866, 4874, 39759, 9583, 10169, 36907, 32130, 569, 25246, 20859], 'labels': [2, -1, -1, -1, -1, 4, -1, -1, 2, 8], 'scores': [0.4719846248626709, 0.3333204984664917, 0.386461079120636, 0.29109907150268555, 0.23445963859558105, 0.34602442383766174, 0.4279487729072571, 0.36926013231277466, 0.48310941457748413, 0.4435112476348877]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.885331928730011})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4913754463195801})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.42710381746292114})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4029075503349304})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4035256803035736})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41070330142974854})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4762018322944641})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9488, 'crossentropy': 0.3901415771484375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6629164218902588})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.47656095027923584})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.412036657333374})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3727973699569702})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34098345041275024})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.31881603598594666})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [15978, 34879, 31535, 35506, 19880, 775, 6862, 42508, 58384, 11536], 'labels': [-1, -1, -1, -1, -1, -1, -1, 3, 8, 9], 'scores': [0.3584989309310913, 0.3993086814880371, 0.43316709995269775, 0.38366472721099854, 0.38370561599731445, 0.3484857678413391, 0.41630733013153076, 0.5007548928260803, 0.3503485321998596, 0.4790306091308594]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8960343599319458})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.585891842842102})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.47183775901794434})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4919922947883606})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5093858242034912})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4625355005264282})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.499531090259552})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5719815492630005})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4421515464782715})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5236430168151855})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5171175003051758})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4980604648590088})
store['active_learning_steps'][28]['training']['best_epoch']=9
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9485, 'crossentropy': 0.43030107421875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6329023838043213})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4370449185371399})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.36951541900634766})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3264830708503723})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.306580126285553})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.30482035875320435})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.29521405696868896})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.27322715520858765})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.28528231382369995})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.26670074462890625})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.26422858238220215})
store['active_learning_steps'][28]['eval_training']['best_epoch']=11
store['active_learning_steps'][28]['acquisition']={'indices': [47265, 41674, 53570, 25356, 14540, 28321, 41369, 41199, 41453, 45718], 'labels': [-1, -1, -1, -1, 7, -1, 9, -1, 3, -1], 'scores': [0.5828655362129211, 0.5691880583763123, 0.6385065317153931, 0.5868338942527771, 0.6139094829559326, 0.5063501596450806, 0.7154592871665955, 0.613654613494873, 0.7186271548271179, 0.4998362064361572]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8570840358734131})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4683838486671448})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41419029235839844})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.411109983921051})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4148918688297272})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3821627199649811})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4161291718482971})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4212663173675537})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4224522113800049})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9539, 'crossentropy': 0.3615835693359375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.659851610660553})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.41088980436325073})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.38113126158714294})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3312259912490845})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.33075714111328125})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3331848382949829})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3049505352973938})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.30908411741256714})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [9481, 53333, 38546, 18612, 10844, 43570, 44423, 44830, 1674, 18194], 'labels': [9, -1, -1, -1, 0, -1, 9, -1, 9, -1], 'scores': [0.5617671310901642, 0.5762444734573364, 0.5049524307250977, 0.42735838890075684, 0.5593136548995972, 0.5844064950942993, 0.6308352947235107, 0.6101400852203369, 0.5920163989067078, 0.4797036647796631]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8262274265289307})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4849337339401245})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4280398488044739})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4093562364578247})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38870224356651306})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44635725021362305})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4167450964450836})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.46776407957077026})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9501, 'crossentropy': 0.3917244140625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6211434006690979})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4380021393299103})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3911546468734741})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.35401538014411926})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.35193702578544617})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.35553425550460815})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3052676320075989})
store['active_learning_steps'][30]['eval_training']['best_epoch']=7
store['active_learning_steps'][30]['acquisition']={'indices': [40247, 21564, 23245, 23814, 23721, 59749, 2369, 16565, 44533, 46035], 'labels': [-1, -1, -1, 2, 2, -1, -1, -1, -1, -1], 'scores': [0.3420475721359253, 0.3872905969619751, 0.4908616542816162, 0.6006351709365845, 0.5265453457832336, 0.5610600709915161, 0.6716698408126831, 0.46423089504241943, 0.391288161277771, 0.33634817600250244]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8873316049575806})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.49280333518981934})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.44072121381759644})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4275233745574951})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43268078565597534})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4318709373474121})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4367629289627075})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9412, 'crossentropy': 0.424558642578125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6945692300796509})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5189040303230286})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.41812294721603394})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.38263216614723206})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.39789262413978577})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.35201728343963623})
store['active_learning_steps'][31]['eval_training']['best_epoch']=6
store['active_learning_steps'][31]['acquisition']={'indices': [45286, 47319, 34403, 33001, 38378, 42695, 44071, 12455, 17741, 31963], 'labels': [-1, -1, -1, 5, 5, -1, -1, -1, -1, -1], 'scores': [0.5701676607131958, 0.482621431350708, 0.37345051765441895, 0.5358763933181763, 0.4371366500854492, 0.5071513652801514, 0.5478854179382324, 0.42359375953674316, 0.3597334623336792, 0.2160021960735321]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8624371290206909})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5714863538742065})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.39236050844192505})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.383012592792511})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4107680320739746})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38257551193237305})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.40057891607284546})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39657631516456604})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39515602588653564})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9535, 'crossentropy': 0.365219287109375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6239734888076782})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.40794461965560913})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.39442360401153564})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.33858513832092285})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.31340107321739197})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.30663228034973145})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.30064862966537476})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2950918674468994})
store['active_learning_steps'][32]['eval_training']['best_epoch']=8
store['active_learning_steps'][32]['acquisition']={'indices': [48010, 12426, 2765, 25168, 21026, 27832, 17205, 22682, 17456, 31988], 'labels': [7, -1, 0, -1, -1, -1, -1, -1, 8, 3], 'scores': [0.6347173452377319, 0.6081457734107971, 0.7338148355484009, 0.41199183464050293, 0.36794912815093994, 0.44881701469421387, 0.523138701915741, 0.48400962352752686, 0.5281416773796082, 0.6993021070957184]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8761564493179321})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5000345706939697})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39472055435180664})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42611587047576904})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41262638568878174})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41342318058013916})
store['active_learning_steps'][33]['training']['best_epoch']=3
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9468, 'crossentropy': 0.3968679443359375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.635621964931488})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.48520827293395996})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5072965621948242})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4278859496116638})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.39087820053100586})
store['active_learning_steps'][33]['eval_training']['best_epoch']=5
store['active_learning_steps'][33]['acquisition']={'indices': [14697, 1795, 53194, 47377, 33301, 31748, 26635, 8704, 13996, 49890], 'labels': [8, -1, 1, -1, -1, 3, 2, 1, 9, 5], 'scores': [0.37501853704452515, 0.4035072326660156, 0.4086502194404602, 0.2632536292076111, 0.44664764404296875, 0.542705237865448, 0.41683679819107056, 0.5361740589141846, 0.4529406428337097, 0.6462553143501282]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9638016223907471})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5362225770950317})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4102509617805481})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4369148015975952})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44149458408355713})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41431576013565063})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9483, 'crossentropy': 0.38878779296875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7103561162948608})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4473413825035095})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4490237236022949})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.39606571197509766})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3704828917980194})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [8765, 46032, 32266, 25295, 56566, 36478, 5638, 44736, 34520, 28231], 'labels': [3, 9, -1, 5, 5, -1, 2, 5, 6, 5], 'scores': [0.5791808366775513, 0.4071692228317261, 0.27969563007354736, 0.44103485345840454, 0.463492214679718, 0.3195641040802002, 0.4155985713005066, 0.552356481552124, 0.4097833037376404, 0.5785974264144897]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0146225690841675})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5642887949943542})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4200361371040344})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4048466682434082})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43611568212509155})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4548945724964142})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4593453109264374})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9519, 'crossentropy': 0.3601152587890625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6051665544509888})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4509054720401764})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3893545866012573})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3433457016944885})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.34586793184280396})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32876232266426086})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [42337, 13103, 9242, 3397, 8702, 25910, 9201, 57597, 17796, 53219], 'labels': [5, -1, -1, -1, 9, 1, -1, 2, -1, -1], 'scores': [0.6025370955467224, 0.48249971866607666, 0.5640769004821777, 0.5113164186477661, 0.7999700903892517, 0.46185004711151123, 0.5119935274124146, 0.5373202562332153, 0.532699704170227, 0.5131198763847351]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0008485317230225})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.507565975189209})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4271613359451294})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3719322681427002})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37750446796417236})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37589389085769653})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39141565561294556})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9567, 'crossentropy': 0.354551708984375}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6509168744087219})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.47172611951828003})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3881995677947998})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.36917978525161743})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3379356265068054})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3024308681488037})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [49790, 18143, 19642, 46679, 46379, 27351, 44385, 22199, 14650, 30427], 'labels': [-1, -1, -1, -1, 3, -1, -1, 2, 4, 1], 'scores': [0.47370827198028564, 0.46406662464141846, 0.4258013963699341, 0.37798941135406494, 0.5376937389373779, 0.3314249515533447, 0.6833111047744751, 0.4279751777648926, 0.5813952684402466, 0.42818063497543335]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9918465614318848})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4935253858566284})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4203014373779297})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4077056646347046})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3899271488189697})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4025591015815735})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3999412953853607})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3691454529762268})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39940160512924194})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4474613070487976})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41614866256713867})
store['active_learning_steps'][37]['training']['best_epoch']=8
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9579, 'crossentropy': 0.3381115966796875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6276720762252808})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3958420753479004})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.33672893047332764})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.34760522842407227})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3237963318824768})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.271642804145813})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2787051796913147})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.28307515382766724})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.2615816295146942})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28459879755973816})
store['active_learning_steps'][37]['eval_training']['best_epoch']=9
store['active_learning_steps'][37]['acquisition']={'indices': [29677, 49200, 12203, 23982, 55095, 36115, 3737, 7380, 21049, 14790], 'labels': [-1, 0, -1, -1, 0, -1, -1, 7, -1, 9], 'scores': [0.5355981588363647, 0.585768461227417, 0.5337436199188232, 0.5647826194763184, 0.5711599886417389, 0.5765763521194458, 0.47480154037475586, 0.80478435754776, 0.4969290494918823, 0.5798646211624146]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9473176002502441})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5073670148849487})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3964722752571106})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4167730212211609})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.36012721061706543})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4058278799057007})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41682302951812744})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40302175283432007})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.957, 'crossentropy': 0.328700146484375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5958889722824097})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4395076036453247})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.36505162715911865})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.35639312863349915})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3324766755104065})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33445268869400024})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3069573938846588})
store['active_learning_steps'][38]['eval_training']['best_epoch']=7
store['active_learning_steps'][38]['acquisition']={'indices': [35736, 11864, 7695, 19807, 51744, 50196, 58033, 31794, 36744, 45118], 'labels': [6, 5, -1, -1, -1, -1, -1, 2, 1, 5], 'scores': [0.35559511184692383, 0.49512362480163574, 0.34809160232543945, 0.41722571849823, 0.5323529243469238, 0.3472484350204468, 0.4288524389266968, 0.5870055556297302, 0.5923544764518738, 0.3800520598888397]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.0069103240966797})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5147309303283691})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3524198532104492})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3452959954738617})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35667091608047485})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3601863384246826})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35049644112586975})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9552, 'crossentropy': 0.325931298828125}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6404505372047424})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.44460219144821167})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.38478970527648926})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3753613829612732})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.35654765367507935})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.31565284729003906})
store['active_learning_steps'][39]['eval_training']['best_epoch']=6
store['active_learning_steps'][39]['acquisition']={'indices': [12651, 54909, 6347, 26865, 57496, 23065, 27774, 38673, 37363, 45344], 'labels': [9, 8, 3, 8, -1, -1, -1, -1, 8, 5], 'scores': [0.5615766644477844, 0.4175448417663574, 0.5800173878669739, 0.2872844934463501, 0.4058723449707031, 0.3255786895751953, 0.33701860904693604, 0.34936797618865967, 0.29299288988113403, 0.45466893911361694]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0583463907241821})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5286095142364502})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.44482412934303284})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4356471002101898})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.41033679246902466})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39286088943481445})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.46180036664009094})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4431072473526001})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47620201110839844})
store['active_learning_steps'][40]['training']['best_epoch']=6
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9552, 'crossentropy': 0.37091240234375}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5962979793548584})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4357140362262726})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.40337371826171875})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3767887055873871})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3284108638763428})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3126477301120758})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.30180269479751587})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.29169267416000366})
store['active_learning_steps'][40]['eval_training']['best_epoch']=8
store['active_learning_steps'][40]['acquisition']={'indices': [3765, 47101, 57507, 13031, 5704, 47140, 29467, 42920, 47387, 47656], 'labels': [2, -1, 0, 2, 9, 3, -1, -1, 8, -1], 'scores': [0.5351170897483826, 0.5146793127059937, 0.7862097024917603, 0.5291107296943665, 0.5362464785575867, 0.5406946539878845, 0.579961359500885, 0.3660060167312622, 0.5270240902900696, 0.567527174949646]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9804339408874512})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5299524068832397})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.42775434255599976})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3794785737991333})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34991705417633057})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35916492342948914})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34855830669403076})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3433866798877716})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39769503474235535})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3622933328151703})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36901313066482544})
store['active_learning_steps'][41]['training']['best_epoch']=8
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9608, 'crossentropy': 0.322719677734375}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6355575323104858})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4202025532722473})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.374794065952301})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3190460503101349})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3033447861671448})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.29334187507629395})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27705976366996765})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.26347023248672485})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2729211449623108})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2720526456832886})
store['active_learning_steps'][41]['eval_training']['best_epoch']=8
store['active_learning_steps'][41]['acquisition']={'indices': [33202, 51733, 24920, 4068, 59446, 42804, 41016, 46269, 3082, 40549], 'labels': [-1, -1, -1, -1, -1, -1, -1, 3, -1, -1], 'scores': [0.4675105810165405, 0.42008209228515625, 0.4967837333679199, 0.4622546434402466, 0.49440479278564453, 0.42690515518188477, 0.45024967193603516, 0.5084137320518494, 0.42649102210998535, 0.5179797410964966]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.066474437713623})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5373904705047607})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3835754990577698})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38464927673339844})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38374245166778564})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.37568899989128113})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3761707544326782})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.376442015171051})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3915766477584839})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9564, 'crossentropy': 0.3509724853515625}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6193411350250244})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4755145013332367})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3703018128871918})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3489052653312683})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.324920117855072})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3154221475124359})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30016234517097473})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2940124571323395})
store['active_learning_steps'][42]['eval_training']['best_epoch']=8
store['active_learning_steps'][42]['acquisition']={'indices': [40624, 670, 41744, 48510, 3367, 54377, 1801, 57642, 47420, 7710], 'labels': [-1, 3, -1, -1, 0, 3, -1, 0, -1, 0], 'scores': [0.6500677466392517, 0.6243404150009155, 0.3800917863845825, 0.4510244131088257, 0.6557844877243042, 0.42705416679382324, 0.7366895079612732, 0.6537233889102936, 0.3553140163421631, 0.3814719021320343]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0354827642440796})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5877500772476196})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41007697582244873})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3498002290725708})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3654816746711731})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3467167317867279})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3502696752548218})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36446046829223633})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.357110857963562})
store['active_learning_steps'][43]['training']['best_epoch']=6
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9575, 'crossentropy': 0.3279328125}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6085729598999023})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4243999123573303})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.369384229183197})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3460104167461395})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.31099334359169006})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31936195492744446})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.2901085913181305})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27991393208503723})
store['active_learning_steps'][43]['eval_training']['best_epoch']=8
store['active_learning_steps'][43]['acquisition']={'indices': [23402, 23782, 4111, 17213, 16749, 45963, 27564, 31177, 55354, 5315], 'labels': [-1, 7, 2, 1, 0, -1, -1, -1, -1, 3], 'scores': [0.6028412580490112, 0.34817326068878174, 0.6937096118927002, 0.4290392994880676, 0.4331352114677429, 0.2889368534088135, 0.4750959873199463, 0.43909966945648193, 0.38425707817077637, 0.5848557949066162]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0322130918502808})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5273404717445374})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39346951246261597})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41882413625717163})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3844342827796936})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37186458706855774})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34690243005752563})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3719937801361084})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4032418131828308})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34939634799957275})
store['active_learning_steps'][44]['training']['best_epoch']=7
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9572, 'crossentropy': 0.351760107421875}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6519222259521484})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4057193398475647})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3358054757118225})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3399239778518677})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34572166204452515})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2820556163787842})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3055882751941681})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27144336700439453})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2588600516319275})
store['active_learning_steps'][44]['eval_training']['best_epoch']=9
store['active_learning_steps'][44]['acquisition']={'indices': [31787, 40304, 2250, 8817, 24308, 24057, 4811, 54129, 12316, 19029], 'labels': [-1, 6, 5, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5187373161315918, 0.7414120435714722, 0.5412856340408325, 0.5115673542022705, 0.5477902889251709, 0.43935465812683105, 0.4100797176361084, 0.48571157455444336, 0.5842393636703491, 0.5414113998413086]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.965187668800354})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.511851966381073})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.43748682737350464})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3588225841522217})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35371220111846924})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34188735485076904})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3442060053348541})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35304152965545654})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3434523940086365})
store['active_learning_steps'][45]['training']['best_epoch']=6
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9618, 'crossentropy': 0.3062459716796875}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6239648461341858})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4181058704853058})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.33139246702194214})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.30542752146720886})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3228033781051636})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3074225187301636})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.28145116567611694})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25314652919769287})
store['active_learning_steps'][45]['eval_training']['best_epoch']=8
store['active_learning_steps'][45]['acquisition']={'indices': [5999, 34359, 19939, 56664, 16856, 20832, 11632, 13822, 19524, 59212], 'labels': [-1, -1, -1, 2, -1, 2, 2, -1, 2, -1], 'scores': [0.40011894702911377, 0.3921557664871216, 0.6178344488143921, 0.49684470891952515, 0.41175293922424316, 0.47213131189346313, 0.41130203008651733, 0.4554166793823242, 0.62079918384552, 0.48854148387908936]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9976904392242432})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5065622925758362})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3832993507385254})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33979058265686035})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3576611876487732})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33804816007614136})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34224915504455566})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32692646980285645})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36697274446487427})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3410705626010895})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32182660698890686})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3800080716609955})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3668789565563202})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32837989926338196})
store['active_learning_steps'][46]['training']['best_epoch']=11
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9632, 'crossentropy': 0.32874150390625}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6385500431060791})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4340723752975464})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.36137688159942627})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.30885133147239685})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2952044606208801})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.25681066513061523})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2583127021789551})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.24965617060661316})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2236056923866272})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.244989275932312})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2418595254421234})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2171010971069336})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24197036027908325})
store['active_learning_steps'][46]['eval_training']['best_epoch']=12
store['active_learning_steps'][46]['acquisition']={'indices': [7646, 40994, 9651, 23400, 11504, 57114, 52218, 30518, 15616, 9989], 'labels': [-1, -1, -1, 8, -1, -1, 8, 6, -1, -1], 'scores': [0.6997700333595276, 0.4380922317504883, 0.5163413286209106, 0.634632021188736, 0.4384680986404419, 0.5573924779891968, 0.5733765363693237, 0.4598241150379181, 0.46440452337265015, 0.37753868103027344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9738362431526184})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5060701370239258})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3823431432247162})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34178632497787476})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3428645133972168})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33761605620384216})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35383141040802})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3560241460800171})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29740744829177856})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.323594868183136})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35056138038635254})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.34299784898757935})
store['active_learning_steps'][47]['training']['best_epoch']=9
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9643, 'crossentropy': 0.311438818359375}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6648881435394287})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.41827982664108276})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3508996367454529})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31097841262817383})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.25757670402526855})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24123887717723846})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26003599166870117})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.262788325548172})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24483749270439148})
store['active_learning_steps'][47]['eval_training']['best_epoch']=6
store['active_learning_steps'][47]['acquisition']={'indices': [10479, 16245, 5466, 25694, 32942, 29731, 2302, 40920, 52487, 56411], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.6594442129135132, 0.6080323457717896, 0.5273324251174927, 0.43646538257598877, 0.5615922212600708, 0.6464362740516663, 0.46729493141174316, 0.4953908920288086, 0.6347060203552246, 0.5110728740692139]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9311607480049133})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4522538185119629})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3552558422088623})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3323078751564026})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2935712933540344})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31733572483062744})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2923903465270996})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3294954299926758})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33171191811561584})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3127976655960083})
store['active_learning_steps'][48]['training']['best_epoch']=7
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9626, 'crossentropy': 0.2949279052734375}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6482900381088257})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4470388889312744})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.34704282879829407})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.29408955574035645})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32175856828689575})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.28139007091522217})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2583773732185364})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24014948308467865})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25397956371307373})
store['active_learning_steps'][48]['eval_training']['best_epoch']=8
store['active_learning_steps'][48]['acquisition']={'indices': [31951, 36704, 1348, 16239, 26376, 15865, 5504, 54259, 18521, 18805], 'labels': [-1, 2, -1, -1, 1, -1, -1, -1, -1, -1], 'scores': [0.6374759078025818, 0.3385142683982849, 0.3126657009124756, 0.38039085268974304, 0.4608688950538635, 0.402429461479187, 0.49559974670410156, 0.472068190574646, 0.5323440432548523, 0.4431055784225464]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.086021900177002})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5362972021102905})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3601130247116089})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3841665983200073})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.330282986164093})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3078623414039612})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3270646929740906})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3562512993812561})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3354622721672058})
store['active_learning_steps'][49]['training']['best_epoch']=6
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9582, 'crossentropy': 0.3079284912109375}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.59365314245224})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.41568681597709656})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.38562923669815063})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3377021849155426})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.32723185420036316})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2911352515220642})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2857072949409485})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.26765143871307373})
store['active_learning_steps'][49]['eval_training']['best_epoch']=8
store['active_learning_steps'][49]['acquisition']={'indices': [31717, 7971, 254, 11992, 10119, 46857, 16485, 57573, 55245, 27763], 'labels': [4, -1, -1, 9, -1, -1, -1, -1, -1, -1], 'scores': [0.4266514182090759, 0.597449541091919, 0.4242684245109558, 0.49204546213150024, 0.4039956331253052, 0.43072497844696045, 0.4973337650299072, 0.34829676151275635, 0.4637596011161804, 0.3221362829208374]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0328575372695923})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5344724655151367})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.41672542691230774})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3769219219684601})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3671003580093384})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3677140474319458})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3841085433959961})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3665391206741333})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32949957251548767})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37366193532943726})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3619159460067749})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35487282276153564})
store['active_learning_steps'][50]['training']['best_epoch']=9
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9605, 'crossentropy': 0.3248334228515625}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6293169260025024})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.43056923151016235})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3846142590045929})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3457413911819458})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3199945092201233})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.25850021839141846})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2835731506347656})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2541370689868927})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25280436873435974})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.28567326068878174})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.26802074909210205})
store['active_learning_steps'][50]['eval_training']['best_epoch']=9
store['active_learning_steps'][50]['acquisition']={'indices': [5092, 59836, 6036, 14757, 41999, 49910, 43606, 51245, 6835, 42596], 'labels': [-1, 1, -1, -1, 0, -1, -1, -1, 7, -1], 'scores': [0.4329596161842346, 0.424268901348114, 0.5670992136001587, 0.8115487098693848, 0.4702543616294861, 0.23257875442504883, 0.5611579418182373, 0.50989830493927, 0.5115596055984497, 0.4642007350921631]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8867731690406799})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4717280864715576})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.39097440242767334})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3521804213523865})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35151392221450806})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30676883459091187})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2918466329574585})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3129272162914276})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2923301160335541})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3182598650455475})
store['active_learning_steps'][51]['training']['best_epoch']=7
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9609, 'crossentropy': 0.3050634765625}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6616103649139404})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4204309582710266})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3406216502189636})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.32850381731987})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3054756224155426})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.27853766083717346})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.29578641057014465})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.2639295756816864})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.23690836131572723})
store['active_learning_steps'][51]['eval_training']['best_epoch']=9
store['active_learning_steps'][51]['acquisition']={'indices': [12487, 8820, 5898, 47926, 10177, 40666, 36308, 7418, 10930, 26462], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.35303473472595215, 0.4067866802215576, 0.46635568141937256, 0.4074653387069702, 0.5859997272491455, 0.5526324510574341, 0.5696839094161987, 0.4252690076828003, 0.4445909261703491, 0.4489213228225708]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0458344221115112})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5146329998970032})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4146374762058258})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35054272413253784})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3412606120109558})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3116499185562134})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.30757588148117065})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33961552381515503})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39459455013275146})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3576104938983917})
store['active_learning_steps'][52]['training']['best_epoch']=7
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.962, 'crossentropy': 0.29737451171875}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6582605838775635})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.41969034075737})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.35000211000442505})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3621007800102234})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2980024218559265})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.27961182594299316})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2716635465621948})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.23966223001480103})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2553998827934265})
store['active_learning_steps'][52]['eval_training']['best_epoch']=8
store['active_learning_steps'][52]['acquisition']={'indices': [995, 4145, 30008, 55543, 11777, 49712, 24837, 34771, 5641, 28258], 'labels': [7, -1, -1, 1, 3, -1, -1, 0, -1, -1], 'scores': [0.30675366520881653, 0.25935983657836914, 0.40664827823638916, 0.30143237113952637, 0.47157877683639526, 0.37270069122314453, 0.38819199800491333, 0.48903346061706543, 0.40708041191101074, 0.36884641647338867]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0987403392791748})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.526471734046936})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.43754059076309204})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.34382641315460205})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3308256268501282})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.344252347946167})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34478333592414856})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35329627990722656})
store['active_learning_steps'][53]['training']['best_epoch']=5
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9558, 'crossentropy': 0.3499541259765625}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6161410808563232})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.44293832778930664})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38607877492904663})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36355745792388916})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33160316944122314})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3073931336402893})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.29179996252059937})
store['active_learning_steps'][53]['eval_training']['best_epoch']=7
store['active_learning_steps'][53]['acquisition']={'indices': [11708, 54602, 27936, 40208, 4153, 52173, 9135, 13998, 1276, 41478], 'labels': [3, -1, -1, -1, 2, 7, 2, 9, 5, 2], 'scores': [0.5722751021385193, 0.23853540420532227, 0.21198415756225586, 0.32987523078918457, 0.7400636076927185, 0.5923334956169128, 0.3564487099647522, 0.5965730547904968, 0.5295807123184204, 0.5583822131156921]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0412006378173828})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5147827863693237})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37602850794792175})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3641211688518524})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38062477111816406})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33929499983787537})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37022167444229126})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3463188409805298})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34779882431030273})
store['active_learning_steps'][54]['training']['best_epoch']=6
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9613, 'crossentropy': 0.310192529296875}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6710946559906006})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.45308172702789307})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3775215446949005})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.31674203276634216})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3146490454673767})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.29516953229904175})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3144005537033081})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28593164682388306})
store['active_learning_steps'][54]['eval_training']['best_epoch']=8
store['active_learning_steps'][54]['acquisition']={'indices': [33894, 55054, 15141, 3512, 23526, 22614, 31345, 1477, 36853, 10960], 'labels': [4, 3, 4, -1, 7, -1, 3, 4, 2, -1], 'scores': [0.39564016461372375, 0.4385857582092285, 0.5609471797943115, 0.43680715560913086, 0.42769384384155273, 0.4587053656578064, 0.661952793598175, 0.6020770072937012, 0.23010504245758057, 0.42596232891082764]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.993459939956665})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5112196803092957})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3711739182472229})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.34269359707832336})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.321002721786499})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3065743148326874})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28056401014328003})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33004051446914673})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3133653402328491})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32828888297080994})
store['active_learning_steps'][55]['training']['best_epoch']=7
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9641, 'crossentropy': 0.2952580078125}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.612675666809082})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4079173803329468})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.34228721261024475})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32159560918807983})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30011484026908875})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2804605960845947})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2834150195121765})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26061248779296875})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2415531873703003})
store['active_learning_steps'][55]['eval_training']['best_epoch']=9
store['active_learning_steps'][55]['acquisition']={'indices': [31961, 50196, 45954, 46809, 53169, 11446, 28229, 24630, 49340, 49825], 'labels': [-1, -1, 8, -1, -1, -1, -1, 5, -1, -1], 'scores': [0.4483304023742676, 0.3578575849533081, 0.2732585072517395, 0.23168760538101196, 0.5208238363265991, 0.49218833446502686, 0.42733216285705566, 0.4478219747543335, 0.2774404287338257, 0.4363134503364563]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9950039386749268})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5342357158660889})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3723376989364624})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33735719323158264})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.343299925327301})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.33997175097465515})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.313284695148468})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34976130723953247})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34998613595962524})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3432219624519348})
store['active_learning_steps'][56]['training']['best_epoch']=7
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9631, 'crossentropy': 0.3084300048828125}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6604966521263123})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4174741506576538})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34020039439201355})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31398963928222656})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2978994846343994})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29340270161628723})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2640407383441925})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2502910792827606})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26517361402511597})
store['active_learning_steps'][56]['eval_training']['best_epoch']=8
store['active_learning_steps'][56]['acquisition']={'indices': [34052, 38656, 24211, 49757, 7449, 25330, 21002, 36866, 16508, 58224], 'labels': [9, 5, -1, -1, -1, 5, -1, 6, -1, 6], 'scores': [0.6450645923614502, 0.5741387009620667, 0.3904433250427246, 0.3968397378921509, 0.4096798896789551, 0.6481410264968872, 0.4380836486816406, 0.5929954051971436, 0.45273053646087646, 0.5793903470039368]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1180751323699951})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5748661756515503})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4168483018875122})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35289520025253296})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3708617687225342})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3338496685028076})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3329595625400543})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3822230398654938})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31714460253715515})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3487222194671631})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3328358829021454})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3740938901901245})
store['active_learning_steps'][57]['training']['best_epoch']=9
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9653, 'crossentropy': 0.31188759765625}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6251766681671143})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.44612640142440796})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37096744775772095})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3463941216468811})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2894243896007538})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2876030206680298})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26369863748550415})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.274303138256073})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27401575446128845})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2756728529930115})
store['active_learning_steps'][57]['eval_training']['best_epoch']=7
store['active_learning_steps'][57]['acquisition']={'indices': [40549, 12598, 5452, 59255, 47428, 32509, 25024, 43704, 57780, 5679], 'labels': [8, -1, -1, -1, -1, 8, -1, -1, -1, 3], 'scores': [0.6682736575603485, 0.5031157732009888, 0.38131260871887207, 0.3862340450286865, 0.3767472505569458, 0.4738841950893402, 0.4243617653846741, 0.4707084894180298, 0.4330790042877197, 0.7243124842643738]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0434768199920654})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5377662181854248})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41311055421829224})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36057233810424805})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38119539618492126})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3031209707260132})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3420974016189575})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36146122217178345})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34112125635147095})
store['active_learning_steps'][58]['training']['best_epoch']=6
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9647, 'crossentropy': 0.3010135986328125}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5875457525253296})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3955039083957672})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37869757413864136})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.35551750659942627})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3487829566001892})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3046681880950928})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2775871753692627})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.2773035168647766})
store['active_learning_steps'][58]['eval_training']['best_epoch']=8
store['active_learning_steps'][58]['acquisition']={'indices': [57821, 31587, 29056, 27940, 13496, 35330, 16658, 2668, 49161, 13466], 'labels': [-1, -1, -1, -1, -1, -1, 8, -1, 6, -1], 'scores': [0.5895421504974365, 0.3493761420249939, 0.4577498435974121, 0.46791207790374756, 0.4289720058441162, 0.5049868822097778, 0.46405208110809326, 0.40028417110443115, 0.3753310441970825, 0.2660437822341919]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.964891791343689})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5105776190757751})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34745925664901733})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30998164415359497})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38832348585128784})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3327435851097107})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3954075574874878})
store['active_learning_steps'][59]['training']['best_epoch']=4
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9634, 'crossentropy': 0.2972882568359375}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.738444983959198})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4503313899040222})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.38495659828186035})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3560023307800293})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3369763493537903})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35267138481140137})
store['active_learning_steps'][59]['eval_training']['best_epoch']=5
store['active_learning_steps'][59]['acquisition']={'indices': [54089, 9543, 47680, 8879, 6509, 4457, 39355, 40016, 31286, 42774], 'labels': [-1, 8, -1, 3, -1, 2, 8, -1, -1, 4], 'scores': [0.40261101722717285, 0.42066776752471924, 0.3860185146331787, 0.44442880153656006, 0.303585410118103, 0.4278915524482727, 0.641968309879303, 0.30793070793151855, 0.30906951427459717, 0.42141157388687134]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0821889638900757})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5754613876342773})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4096727967262268})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3306625485420227})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30213093757629395})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.343424916267395})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3071640431880951})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32990002632141113})
store['active_learning_steps'][60]['training']['best_epoch']=5
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9596, 'crossentropy': 0.31904306640625}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5643278360366821})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.41181913018226624})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.39800724387168884})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3540725111961365})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33537113666534424})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3241434395313263})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.31216681003570557})
store['active_learning_steps'][60]['eval_training']['best_epoch']=7
store['active_learning_steps'][60]['acquisition']={'indices': [16564, 7392, 55896, 32469, 26072, 20436, 20230, 52044, 35828, 40378], 'labels': [3, -1, 7, 4, 1, 2, 4, -1, 6, -1], 'scores': [0.29971182346343994, 0.3433619737625122, 0.532067060470581, 0.3381345272064209, 0.3860723376274109, 0.5751147270202637, 0.5735317468643188, 0.4317389726638794, 0.3907701373100281, 0.4646953344345093]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1045458316802979})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4855941832065582})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37813177704811096})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37771567702293396})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33971741795539856})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3144795298576355})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3014073967933655})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31342703104019165})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32119399309158325})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.297695517539978})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29515284299850464})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.315646767616272})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.300667941570282})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3337399959564209})
store['active_learning_steps'][61]['training']['best_epoch']=11
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9686, 'crossentropy': 0.293134326171875}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7038960456848145})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.43057310581207275})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.36877673864364624})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.32263806462287903})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28927624225616455})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.28889137506484985})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.25552961230278015})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25330376625061035})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.23649585247039795})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24359837174415588})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24643829464912415})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23468555510044098})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2280321717262268})
store['active_learning_steps'][61]['eval_training']['best_epoch']=13
store['active_learning_steps'][61]['acquisition']={'indices': [41921, 13993, 13605, 9124, 35742, 5502, 47050, 111, 22435, 13473], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5677127838134766, 0.4097784757614136, 0.5485285520553589, 0.6095147728919983, 0.62770015001297, 0.5885145664215088, 0.5485122203826904, 0.42267972230911255, 0.6292136907577515, 0.4829331636428833]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0801609754562378})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5051125288009644})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.361092746257782})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3178256154060364})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29191237688064575})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30591124296188354})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32442858815193176})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34596800804138184})
store['active_learning_steps'][62]['training']['best_epoch']=5
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.963, 'crossentropy': 0.2876139404296875}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7179540991783142})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4385959804058075})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36674022674560547})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32994478940963745})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31157374382019043})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31766510009765625})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28948354721069336})
store['active_learning_steps'][62]['eval_training']['best_epoch']=7
store['active_learning_steps'][62]['acquisition']={'indices': [6289, 6394, 48702, 16791, 54049, 8549, 34035, 7949, 48994, 2574], 'labels': [2, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.6380730271339417, 0.5394970178604126, 0.4574850797653198, 0.2976975440979004, 0.44701993465423584, 0.491640567779541, 0.2896547317504883, 0.5166295170783997, 0.42618119716644287, 0.5426973104476929]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.957973301410675})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4688226580619812})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3848627507686615})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3545173406600952})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3288115859031677})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33264175057411194})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31814560294151306})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32947927713394165})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3498556315898895})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3240209221839905})
store['active_learning_steps'][63]['training']['best_epoch']=7
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.965, 'crossentropy': 0.278489892578125}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6351898908615112})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.44613730907440186})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3788829445838928})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3398371934890747})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28434500098228455})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27284112572669983})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33419787883758545})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.260673850774765})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26047682762145996})
store['active_learning_steps'][63]['eval_training']['best_epoch']=9
store['active_learning_steps'][63]['acquisition']={'indices': [31871, 54746, 49282, 37432, 57866, 57718, 29238, 55742, 20730, 57741], 'labels': [-1, -1, 2, -1, -1, 7, -1, -1, -1, -1], 'scores': [0.2625004053115845, 0.3214285373687744, 0.4754098057746887, 0.439192533493042, 0.3556671142578125, 0.6673064827919006, 0.4567619562149048, 0.4579031467437744, 0.3020373582839966, 0.456653356552124]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0391654968261719})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.49850112199783325})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3894420862197876})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3142879903316498})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3047731816768646})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2930712103843689})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28349658846855164})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29403263330459595})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2919742465019226})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33073464035987854})
store['active_learning_steps'][64]['training']['best_epoch']=7
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9688, 'crossentropy': 0.255283984375}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6449540853500366})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4206353425979614})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3741689920425415})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3184550404548645})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2966693043708801})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30044615268707275})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2669971287250519})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2916510999202728})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2641001343727112})
store['active_learning_steps'][64]['eval_training']['best_epoch']=9
store['active_learning_steps'][64]['acquisition']={'indices': [20072, 25281, 36536, 22704, 23731, 6121, 10526, 40479, 17234, 8204], 'labels': [3, 2, -1, 5, -1, -1, -1, -1, -1, -1], 'scores': [0.4252750873565674, 0.33897513151168823, 0.34199702739715576, 0.4389466643333435, 0.3382316827774048, 0.36538100242614746, 0.3659327030181885, 0.22315895557403564, 0.3551023006439209, 0.46041274070739746]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0579103231430054})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5471606254577637})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.37870579957962036})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3269383907318115})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3182380199432373})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3394288718700409})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31942248344421387})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32706978917121887})
store['active_learning_steps'][65]['training']['best_epoch']=5
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.965, 'crossentropy': 0.30745107421875}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6964898109436035})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4710491895675659})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.38040047883987427})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3561208248138428})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3400092124938965})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30463874340057373})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3058168292045593})
store['active_learning_steps'][65]['eval_training']['best_epoch']=6
store['active_learning_steps'][65]['acquisition']={'indices': [41781, 55754, 56508, 4382, 59919, 39079, 17265, 45577, 57923, 50756], 'labels': [-1, 6, 2, 4, 1, -1, -1, -1, -1, -1], 'scores': [0.40136754512786865, 0.5617939829826355, 0.3877321481704712, 0.3515106439590454, 0.5469477772712708, 0.3816138505935669, 0.2761092185974121, 0.43644964694976807, 0.3546717166900635, 0.343913197517395]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0242245197296143})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5513509511947632})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4129955470561981})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3568006157875061})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3592751622200012})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.347555935382843})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34441259503364563})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31237712502479553})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2955763339996338})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34844571352005005})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3386245369911194})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3405480980873108})
store['active_learning_steps'][66]['training']['best_epoch']=9
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9668, 'crossentropy': 0.286020166015625}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6350462436676025})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4233441948890686})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.39802175760269165})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33093494176864624})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2998514473438263})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27863508462905884})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26281365752220154})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.23115716874599457})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2905076742172241})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24532118439674377})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2953510284423828})
store['active_learning_steps'][66]['eval_training']['best_epoch']=8
store['active_learning_steps'][66]['acquisition']={'indices': [8350, 44154, 18440, 27660, 22058, 11288, 17032, 18270, 12663, 29247], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 8, -1], 'scores': [0.6113182306289673, 0.5161446928977966, 0.5227199792861938, 0.4297565221786499, 0.6968920230865479, 0.5000159740447998, 0.5202659368515015, 0.5910872220993042, 0.4771488308906555, 0.39016497135162354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9823490381240845})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5369943380355835})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32784393429756165})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35285684466362})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28879761695861816})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3306277394294739})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34078267216682434})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.328977108001709})
store['active_learning_steps'][67]['training']['best_epoch']=5
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9637, 'crossentropy': 0.307237646484375}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7232897281646729})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4871458411216736})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3868009150028229})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3625636100769043})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.34823548793792725})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.32639211416244507})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.32967454195022583})
store['active_learning_steps'][67]['eval_training']['best_epoch']=6
store['active_learning_steps'][67]['acquisition']={'indices': [32413, 46236, 46003, 29259, 4557, 52103, 19474, 15259, 21686, 52115], 'labels': [1, -1, -1, 8, -1, 4, -1, -1, 9, -1], 'scores': [0.3602794408798218, 0.3332606554031372, 0.2943159341812134, 0.4871368408203125, 0.4135345220565796, 0.3365917503833771, 0.2947028875350952, 0.3917943239212036, 0.39906108379364014, 0.42188847064971924]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.02912437915802})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.43417787551879883})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3631010353565216})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3022410273551941})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.301582396030426})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31893691420555115})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3061596155166626})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31138017773628235})
store['active_learning_steps'][68]['training']['best_epoch']=5
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9665, 'crossentropy': 0.2710280517578125}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.701996922492981})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.457836389541626})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.361020028591156})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3179472088813782})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3031933605670929})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28314778208732605})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2963835299015045})
store['active_learning_steps'][68]['eval_training']['best_epoch']=6
store['active_learning_steps'][68]['acquisition']={'indices': [42240, 38275, 46724, 6990, 59920, 16305, 11482, 44994, 45437, 10854], 'labels': [-1, -1, 7, -1, -1, -1, 8, -1, 1, -1], 'scores': [0.3346729278564453, 0.2947046756744385, 0.40955838561058044, 0.4617370367050171, 0.21995508670806885, 0.3400888442993164, 0.6236755847930908, 0.35238444805145264, 0.3974730968475342, 0.33337289094924927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0387446880340576})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5633571147918701})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.40544402599334717})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3602712154388428})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3154769539833069})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2877020239830017})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3184965252876282})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2721431255340576})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29819291830062866})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2964528203010559})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29660752415657043})
store['active_learning_steps'][69]['training']['best_epoch']=8
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.972, 'crossentropy': 0.24858740234375}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6182659864425659})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43741440773010254})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3428247272968292})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30098479986190796})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.29747188091278076})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26295217871665955})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.263238787651062})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23532819747924805})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.22851014137268066})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2443716824054718})
store['active_learning_steps'][69]['eval_training']['best_epoch']=9
store['active_learning_steps'][69]['acquisition']={'indices': [32170, 14948, 5422, 40009, 28803, 26658, 46056, 4127, 45745, 10310], 'labels': [-1, -1, 7, -1, -1, 2, -1, -1, -1, -1], 'scores': [0.6274317502975464, 0.5997104644775391, 0.6793540716171265, 0.500449538230896, 0.6417179703712463, 0.4457632899284363, 0.5808835625648499, 0.5312122702598572, 0.6944208145141602, 0.5781496167182922]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1078104972839355})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5735783576965332})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.408782035112381})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3437630236148834})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3404558300971985})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2975428104400635})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3004319667816162})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3034817576408386})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33316725492477417})
store['active_learning_steps'][70]['training']['best_epoch']=6
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9655, 'crossentropy': 0.280174365234375}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6429029703140259})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.40131670236587524})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3585056662559509})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33285146951675415})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2879685163497925})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29649287462234497})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29357343912124634})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28452497720718384})
store['active_learning_steps'][70]['eval_training']['best_epoch']=8
store['active_learning_steps'][70]['acquisition']={'indices': [51863, 34828, 33130, 8297, 11495, 11708, 44961, 58044, 54080, 56152], 'labels': [9, 3, 9, 7, -1, -1, 8, -1, -1, 9], 'scores': [0.526057779788971, 0.23230040073394775, 0.4712402820587158, 0.43065452575683594, 0.504793643951416, 0.607342004776001, 0.30976957082748413, 0.24947404861450195, 0.3892884850502014, 0.4209970235824585]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.092024803161621})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5149086117744446})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37747424840927124})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32667505741119385})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3210058808326721})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3176512122154236})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30800050497055054})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31645017862319946})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2906078100204468})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.32887548208236694})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.29466572403907776})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3065100610256195})
store['active_learning_steps'][71]['training']['best_epoch']=9
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.279910498046875}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6367547512054443})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.46231287717819214})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3614272475242615})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2817782163619995})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2708970308303833})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27526116371154785})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25368377566337585})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24393783509731293})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.22110748291015625})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23367828130722046})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.21582768857479095})
store['active_learning_steps'][71]['eval_training']['best_epoch']=11
store['active_learning_steps'][71]['acquisition']={'indices': [4800, 17804, 27113, 10187, 56838, 635, 21029, 45542, 28654, 50782], 'labels': [6, 8, 2, 8, 5, 5, -1, -1, 5, 5], 'scores': [0.48276200890541077, 0.7519481182098389, 0.5171492099761963, 0.3074713945388794, 0.7046414613723755, 0.631391167640686, 0.4439784288406372, 0.4466657042503357, 0.3990662097930908, 0.4956354796886444]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0750281810760498})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5045130848884583})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.43233537673950195})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.34823694825172424})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3047531247138977})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2762208580970764})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27402356266975403})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28852710127830505})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.33590275049209595})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3165014386177063})
store['active_learning_steps'][72]['training']['best_epoch']=7
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.270887646484375}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6067768335342407})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.40927791595458984})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.340199738740921})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3339197635650635})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2985095679759979})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27299410104751587})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27856749296188354})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24851803481578827})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2548123002052307})
store['active_learning_steps'][72]['eval_training']['best_epoch']=8
store['active_learning_steps'][72]['acquisition']={'indices': [5164, 54520, 19189, 16932, 32921, 16632, 52394, 43606, 2591, 52990], 'labels': [-1, 9, -1, -1, -1, -1, -1, -1, -1, 1], 'scores': [0.3271496295928955, 0.37772029638290405, 0.5287374258041382, 0.37033557891845703, 0.5484666228294373, 0.419769287109375, 0.48406553268432617, 0.5720019936561584, 0.46070897579193115, 0.36587250232696533]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1788561344146729})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6628385782241821})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44296517968177795})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3353174030780792})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28507620096206665})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3067052960395813})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31172677874565125})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.310324490070343})
store['active_learning_steps'][73]['training']['best_epoch']=5
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.2964529052734375}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7042344808578491})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.449931800365448})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.448438823223114})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41064581274986267})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3317457437515259})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36680448055267334})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3261318802833557})
store['active_learning_steps'][73]['eval_training']['best_epoch']=7
store['active_learning_steps'][73]['acquisition']={'indices': [30029, 16002, 42504, 48160, 20184, 6846, 57274, 18313, 15609, 25058], 'labels': [-1, -1, 8, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.45146435499191284, 0.5279393196105957, 0.5724939107894897, 0.5693419575691223, 0.37746453285217285, 0.43705010414123535, 0.2626458406448364, 0.40430617332458496, 0.4729328155517578, 0.4537981152534485]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1334128379821777})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5678967237472534})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44716012477874756})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35461729764938354})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3505871295928955})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30323511362075806})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31116440892219543})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3003847599029541})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3069491386413574})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28870588541030884})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3027113974094391})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2980946898460388})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3407955467700958})
store['active_learning_steps'][74]['training']['best_epoch']=10
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.2906900146484375}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6255663633346558})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43039470911026})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34739962220191956})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3042515516281128})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2820231020450592})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2958824634552002})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2774319052696228})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2644590735435486})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2344391942024231})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23448193073272705})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25097495317459106})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.23856228590011597})
store['active_learning_steps'][74]['eval_training']['best_epoch']=9
store['active_learning_steps'][74]['acquisition']={'indices': [51652, 19791, 8761, 46366, 54869, 14524, 26004, 30041, 13823, 36746], 'labels': [4, -1, 8, -1, -1, -1, -1, -1, -1, 6], 'scores': [0.7204810380935669, 0.454922080039978, 0.6182767152786255, 0.35380232334136963, 0.33320486545562744, 0.6567933559417725, 0.4224075675010681, 0.48822641372680664, 0.2875952124595642, 0.6626299619674683]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0956366062164307})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5126879215240479})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3501909077167511})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30648958683013916})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30565810203552246})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28551897406578064})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.275324285030365})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25836417078971863})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29431337118148804})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2707529664039612})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26323214173316956})
store['active_learning_steps'][75]['training']['best_epoch']=8
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.245757470703125}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6554991006851196})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.40565478801727295})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33128732442855835})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33264315128326416})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27481791377067566})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26606112718582153})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2837620675563812})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2620493769645691})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2621021866798401})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2506495416164398})
store['active_learning_steps'][75]['eval_training']['best_epoch']=10
store['active_learning_steps'][75]['acquisition']={'indices': [26275, 4811, 34727, 41661, 14565, 58882, 17406, 26259, 43424, 56412], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.45327848196029663, 0.47479248046875, 0.4185922145843506, 0.5163201093673706, 0.44321370124816895, 0.5159290432929993, 0.522639811038971, 0.3798924684524536, 0.4864155054092407, 0.4834122657775879]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1965465545654297})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5830854773521423})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3843298554420471})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31674742698669434})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2881033718585968})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3672536611557007})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31140100955963135})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3096902370452881})
store['active_learning_steps'][76]['training']['best_epoch']=5
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9679, 'crossentropy': 0.26795810546875}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6593360900878906})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4483914077281952})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4124089479446411})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34011310338974})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33316776156425476})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3256528377532959})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3042449951171875})
store['active_learning_steps'][76]['eval_training']['best_epoch']=7
store['active_learning_steps'][76]['acquisition']={'indices': [50078, 58485, 9782, 47322, 45240, 59336, 25138, 13850, 33053, 14815], 'labels': [9, -1, 8, 8, -1, -1, -1, -1, -1, 9], 'scores': [0.586124062538147, 0.409206748008728, 0.3653978109359741, 0.5395383238792419, 0.3969435691833496, 0.3462367057800293, 0.3979703187942505, 0.3003624677658081, 0.4053887128829956, 0.3937495946884155]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9917372465133667})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5539382696151733})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3787768483161926})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32315731048583984})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31168127059936523})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27730029821395874})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25371700525283813})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28095942735671997})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.278960645198822})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27434176206588745})
store['active_learning_steps'][77]['training']['best_epoch']=7
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9696, 'crossentropy': 0.24631796875}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6421765089035034})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4095441997051239})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34549903869628906})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2986716032028198})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2786959707736969})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.294272243976593})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2799912691116333})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28167006373405457})
store['active_learning_steps'][77]['eval_training']['best_epoch']=5
store['active_learning_steps'][77]['acquisition']={'indices': [5613, 30851, 22420, 16089, 18255, 40159, 15781, 45155, 27372, 54193], 'labels': [-1, -1, -1, -1, -1, -1, 5, -1, -1, -1], 'scores': [0.5440893173217773, 0.6271842122077942, 0.5837645530700684, 0.31196320056915283, 0.7032343149185181, 0.42877864837646484, 0.5227910280227661, 0.3247087001800537, 0.5631914138793945, 0.21309566497802734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1845394372940063})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.550896406173706})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.45448780059814453})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3432697653770447})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32242366671562195})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32071882486343384})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3167561888694763})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32348084449768066})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3227745592594147})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31261029839515686})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33920520544052124})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2818472981452942})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3221276104450226})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32631003856658936})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3308809697628021})
store['active_learning_steps'][78]['training']['best_epoch']=12
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9706, 'crossentropy': 0.266636083984375}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6477709412574768})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.45447707176208496})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3605859875679016})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3168065845966339})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26124808192253113})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2903488874435425})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27026885747909546})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27743250131607056})
store['active_learning_steps'][78]['eval_training']['best_epoch']=5
store['active_learning_steps'][78]['acquisition']={'indices': [16556, 9583, 5073, 18288, 38912, 9411, 33681, 11100, 13864, 15501], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.556841254234314, 0.30376648902893066, 0.6166893243789673, 0.539503812789917, 0.5935065746307373, 0.37044596672058105, 0.4468398094177246, 0.5112059116363525, 0.38641607761383057, 0.37875717878341675]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.261432409286499})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5950911641120911})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39672237634658813})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3509249687194824})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2869243025779724})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33399319648742676})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2934887707233429})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3270941972732544})
store['active_learning_steps'][79]['training']['best_epoch']=5
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9661, 'crossentropy': 0.2749619873046875}
store['active_learning_steps'][79]['eval_training']={}
store['active_learning_steps'][79]['eval_training']['epochs']=[]
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6760426759719849})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4361012279987335})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.360933780670166})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36998674273490906})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3284726142883301})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32267332077026367})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32312583923339844})
store['active_learning_steps'][79]['eval_training']['best_epoch']=6
store['active_learning_steps'][79]['acquisition']={'indices': [13003, 56960, 41608, 54319, 59059, 17440, 33966, 47770, 13286, 32180], 'labels': [-1, 1, -1, -1, -1, -1, -1, 1, -1, -1], 'scores': [0.4573237895965576, 0.39785897731781006, 0.6039214134216309, 0.33214545249938965, 0.25286924839019775, 0.48119795322418213, 0.44128644466400146, 0.46449363231658936, 0.44274401664733887, 0.24554312229156494]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.2781728506088257})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.640731930732727})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.43150418996810913})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.341943621635437})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2956662178039551})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35376936197280884})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3126879930496216})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3393615782260895})
store['active_learning_steps'][80]['training']['best_epoch']=5
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9621, 'crossentropy': 0.3009336181640625}
store['active_learning_steps'][80]['eval_training']={}
store['active_learning_steps'][80]['eval_training']['epochs']=[]
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6889301538467407})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.45959174633026123})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42824292182922363})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3864920139312744})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35914093255996704})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30932655930519104})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3524567484855652})
store['active_learning_steps'][80]['eval_training']['best_epoch']=6
store['active_learning_steps'][80]['acquisition']={'indices': [49828, 19189, 308, 8456, 16638, 20130, 6271, 15494, 33253, 12630], 'labels': [-1, -1, -1, -1, -1, -1, -1, 7, -1, -1], 'scores': [0.45408737659454346, 0.5156713724136353, 0.28915441036224365, 0.34006381034851074, 0.3914581537246704, 0.352486789226532, 0.2790924310684204, 0.48558729887008667, 0.25957441329956055, 0.4844282865524292]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9884001016616821})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.48461371660232544})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3427598476409912})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29847824573516846})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2535442113876343})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28527095913887024})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3041658103466034})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2513171434402466})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2570562958717346})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.274020254611969})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27852874994277954})
store['active_learning_steps'][81]['training']['best_epoch']=8
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.242835791015625}
store['active_learning_steps'][81]['eval_training']={}
store['active_learning_steps'][81]['eval_training']['epochs']=[]
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6549527049064636})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.41056808829307556})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3412136435508728})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29091230034828186})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3239229917526245})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.26060751080513})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2584719955921173})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2390338033437729})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.260052353143692})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23974084854125977})
store['active_learning_steps'][81]['eval_training']['best_epoch']=8
store['active_learning_steps'][81]['acquisition']={'indices': [43960, 23366, 15852, 54376, 51146, 38829, 32544, 28826, 20369, 30774], 'labels': [-1, 9, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.38660764694213867, 0.46522021293640137, 0.5304391384124756, 0.46183204650878906, 0.485376238822937, 0.4115426540374756, 0.24834072589874268, 0.37799036502838135, 0.4557197093963623, 0.46668028831481934]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.1883454322814941})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6256129741668701})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.42412465810775757})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3722585439682007})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30176717042922974})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29035231471061707})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2837267220020294})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2984076738357544})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.302107036113739})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3050938844680786})
store['active_learning_steps'][82]['training']['best_epoch']=7
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9691, 'crossentropy': 0.259409521484375}
store['active_learning_steps'][82]['eval_training']={}
store['active_learning_steps'][82]['eval_training']['epochs']=[]
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7390186190605164})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4231376647949219})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3627995550632477})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3397902846336365})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3128010034561157})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3029888868331909})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2907545566558838})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2753435969352722})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27852100133895874})
store['active_learning_steps'][82]['eval_training']['best_epoch']=8
store['active_learning_steps'][82]['acquisition']={'indices': [22613, 440, 3814, 11145, 8952, 29935, 5581, 43783, 17605, 53705], 'labels': [-1, 0, -1, -1, 2, -1, -1, 3, -1, -1], 'scores': [0.3937370777130127, 0.5968550443649292, 0.424884557723999, 0.5983333587646484, 0.5840885639190674, 0.2940737009048462, 0.379286527633667, 0.4648042917251587, 0.37076693773269653, 0.4184708595275879]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.00194251537323})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5427243709564209})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4046112298965454})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33713775873184204})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3063458800315857})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2853561341762543})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2881149649620056})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3373105227947235})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2811558246612549})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30893152952194214})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30595022439956665})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3110423982143402})
store['active_learning_steps'][83]['training']['best_epoch']=9
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9728, 'crossentropy': 0.2541154541015625}
store['active_learning_steps'][83]['eval_training']={}
store['active_learning_steps'][83]['eval_training']['epochs']=[]
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6645087003707886})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3835963010787964})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35630515217781067})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.28075385093688965})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25597459077835083})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27657148241996765})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25338196754455566})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25537586212158203})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2633104622364044})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.22675612568855286})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2317701280117035})
store['active_learning_steps'][83]['eval_training']['best_epoch']=10
store['active_learning_steps'][83]['acquisition']={'indices': [15919, 9625, 17735, 15049, 53188, 39929, 59844, 38918, 6053, 13434], 'labels': [-1, 2, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.3088940978050232, 0.5169138312339783, 0.18757367134094238, 0.4314178228378296, 0.38887298107147217, 0.4109286069869995, 0.3229649066925049, 0.5022448897361755, 0.31819260120391846, 0.5643904805183411]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0380380153656006})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5078117847442627})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35778164863586426})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29505661129951477})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2665524184703827})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3077079951763153})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.268117755651474})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2696647644042969})
store['active_learning_steps'][84]['training']['best_epoch']=5
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.250174609375}
store['active_learning_steps'][84]['eval_training']={}
store['active_learning_steps'][84]['eval_training']['epochs']=[]
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6365604996681213})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4346598982810974})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3832167387008667})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3455359935760498})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3069782853126526})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2808228135108948})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29687944054603577})
store['active_learning_steps'][84]['eval_training']['best_epoch']=6
store['active_learning_steps'][84]['acquisition']={'indices': [30086, 10405, 11975, 25920, 5520, 4446, 51764, 1735, 11641, 18069], 'labels': [-1, -1, -1, -1, -1, -1, 5, -1, -1, -1], 'scores': [0.516337513923645, 0.5034265518188477, 0.5598585605621338, 0.4172307252883911, 0.3519276976585388, 0.4456753134727478, 0.6698916554450989, 0.3852999210357666, 0.3650308847427368, 0.3927963972091675]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.2068090438842773})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5554320812225342})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40950626134872437})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36844784021377563})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36198297142982483})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3202376365661621})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3490746319293976})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30155521631240845})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31198301911354065})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30028489232063293})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3223001956939697})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3399812877178192})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34537890553474426})
store['active_learning_steps'][85]['training']['best_epoch']=10
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9695, 'crossentropy': 0.2630390625}
store['active_learning_steps'][85]['eval_training']={}
store['active_learning_steps'][85]['eval_training']['epochs']=[]
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6835213303565979})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.43210145831108093})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36989888548851013})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3139170706272125})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3376395106315613})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3224756717681885})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2722432613372803})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25175541639328003})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25990837812423706})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23548978567123413})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23685410618782043})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26752954721450806})
store['active_learning_steps'][85]['eval_training']['best_epoch']=10
store['active_learning_steps'][85]['acquisition']={'indices': [16226, 29779, 41286, 23673, 41882, 42139, 27900, 22636, 15728, 3392], 'labels': [-1, -1, -1, -1, 8, 4, 0, -1, -1, 6], 'scores': [0.4862668514251709, 0.6044236421585083, 0.5155662298202515, 0.35511159896850586, 0.46873247623443604, 0.4709135890007019, 0.4644806385040283, 0.4469187259674072, 0.38716185092926025, 0.5119988322257996]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0519771575927734})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5407748222351074})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3642628788948059})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35837993025779724})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.302931010723114})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2985621392726898})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2895910143852234})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29587647318840027})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27003368735313416})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2912934124469757})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3093959093093872})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3172643184661865})
store['active_learning_steps'][86]['training']['best_epoch']=9
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9714, 'crossentropy': 0.2505587158203125}
store['active_learning_steps'][86]['eval_training']={}
store['active_learning_steps'][86]['eval_training']['epochs']=[]
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6309809684753418})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.45965468883514404})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.35835960507392883})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.31438326835632324})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29205143451690674})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2860300540924072})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.265900194644928})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26593106985092163})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25371062755584717})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24896140396595})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23465943336486816})
store['active_learning_steps'][86]['eval_training']['best_epoch']=11
store['active_learning_steps'][86]['acquisition']={'indices': [13214, 49444, 13932, 45358, 57972, 47836, 29713, 2127, 11006, 20295], 'labels': [-1, -1, -1, -1, 4, -1, 0, -1, -1, -1], 'scores': [0.47287774085998535, 0.42450642585754395, 0.4393887519836426, 0.3331162929534912, 0.6435427665710449, 0.4091513156890869, 0.6040713787078857, 0.45306479930877686, 0.48737597465515137, 0.34585416316986084]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0790574550628662})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5799264907836914})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.42161381244659424})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3260068893432617})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3403467535972595})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27615034580230713})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27248069643974304})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2700014114379883})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28548896312713623})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2824695408344269})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3018198013305664})
store['active_learning_steps'][87]['training']['best_epoch']=8
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.25006396484375}
store['active_learning_steps'][87]['eval_training']={}
store['active_learning_steps'][87]['eval_training']['epochs']=[]
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6833889484405518})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.46459442377090454})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3688109517097473})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.30796003341674805})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.29388105869293213})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31672564148902893})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27192598581314087})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24638086557388306})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26032325625419617})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2533147633075714})
store['active_learning_steps'][87]['eval_training']['best_epoch']=8
store['active_learning_steps'][87]['acquisition']={'indices': [21208, 14553, 13969, 9924, 28564, 42133, 6565, 12012, 10384, 23958], 'labels': [-1, 8, 3, -1, -1, -1, -1, 3, -1, -1], 'scores': [0.4414186477661133, 0.2569272816181183, 0.793645977973938, 0.2225250005722046, 0.5334205627441406, 0.5678697824478149, 0.5324658155441284, 0.5987515449523926, 0.4552013874053955, 0.5997498035430908]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1244620084762573})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5788047313690186})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4147457480430603})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.36962175369262695})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30398041009902954})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.301693320274353})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2887963056564331})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30041950941085815})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2910957932472229})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31529489159584045})
store['active_learning_steps'][88]['training']['best_epoch']=7
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9643, 'crossentropy': 0.2778943359375}
store['active_learning_steps'][88]['eval_training']={}
store['active_learning_steps'][88]['eval_training']['epochs']=[]
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6351016759872437})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4693385362625122})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34976500272750854})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38098710775375366})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2999587655067444})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3052673637866974})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2745720148086548})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2840985655784607})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27493810653686523})
store['active_learning_steps'][88]['eval_training']['best_epoch']=7
store['active_learning_steps'][88]['acquisition']={'indices': [34673, 46615, 47243, 29018, 36981, 26842, 12780, 1706, 9551, 30569], 'labels': [-1, -1, 1, -1, -1, 5, -1, -1, -1, -1], 'scores': [0.3573392629623413, 0.35307347774505615, 0.3400267958641052, 0.5921615958213806, 0.40711724758148193, 0.5338233113288879, 0.2774771451950073, 0.43425071239471436, 0.4018291234970093, 0.5046665668487549]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.3066623210906982})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6119111776351929})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4485759139060974})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3837554454803467})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.32275331020355225})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3225058913230896})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31302767992019653})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3204566240310669})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.31775587797164917})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30975356698036194})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32912933826446533})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36272570490837097})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.30847591161727905})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32436704635620117})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3601726293563843})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32495540380477905})
store['active_learning_steps'][89]['training']['best_epoch']=13
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.262064892578125}
store['active_learning_steps'][89]['eval_training']={}
store['active_learning_steps'][89]['eval_training']['epochs']=[]
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.709770917892456})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4243627190589905})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3710724413394928})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31414610147476196})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2774745225906372})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24407371878623962})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.253135085105896})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2297828644514084})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2750086188316345})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24146661162376404})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2143404483795166})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.21500463783740997})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23247765004634857})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.22849130630493164})
store['active_learning_steps'][89]['eval_training']['best_epoch']=11
store['active_learning_steps'][89]['acquisition']={'indices': [23860, 16094, 18832, 51351, 23683, 57114, 17432, 35278, 22642, 19433], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.6476877927780151, 0.5178477764129639, 0.5121880769729614, 0.7817525267601013, 0.3845095634460449, 0.566821813583374, 0.3634830713272095, 0.4547358751296997, 0.6143448352813721, 0.42685985565185547]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0555946826934814})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5690928101539612})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38175708055496216})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34418076276779175})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31061607599258423})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2900761663913727})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2727532982826233})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30524730682373047})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28095269203186035})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.333848237991333})
store['active_learning_steps'][90]['training']['best_epoch']=7
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9723, 'crossentropy': 0.2593896240234375}
store['active_learning_steps'][90]['eval_training']={}
store['active_learning_steps'][90]['eval_training']['epochs']=[]
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6181544661521912})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4195899963378906})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.36896681785583496})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3492901921272278})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31334182620048523})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2945441007614136})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27067917585372925})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.261513352394104})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2528053820133209})
store['active_learning_steps'][90]['eval_training']['best_epoch']=9
store['active_learning_steps'][90]['acquisition']={'indices': [32599, 44567, 23486, 21900, 16488, 30156, 46640, 42608, 34093, 15108], 'labels': [-1, -1, 4, 6, 9, 0, -1, 0, 4, 0], 'scores': [0.3667142391204834, 0.4442988634109497, 0.49078160524368286, 0.8034536242485046, 0.7403609752655029, 0.5602458715438843, 0.5110474824905396, 0.5469156801700592, 0.4306858777999878, 0.4858860969543457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1927790641784668})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5285482406616211})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35062935948371887})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32454854249954224})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2935020625591278})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2825128138065338})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2631244957447052})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3026747703552246})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25439777970314026})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27594679594039917})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30710381269454956})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3091505169868469})
store['active_learning_steps'][91]['training']['best_epoch']=9
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9729, 'crossentropy': 0.2429462890625}
store['active_learning_steps'][91]['eval_training']={}
store['active_learning_steps'][91]['eval_training']['epochs']=[]
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.638867199420929})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4530588984489441})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.35329097509384155})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29794037342071533})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2931443452835083})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2708284854888916})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2541292905807495})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26955896615982056})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2573816180229187})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.21583369374275208})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.22698989510536194})
store['active_learning_steps'][91]['eval_training']['best_epoch']=10
store['active_learning_steps'][91]['acquisition']={'indices': [15272, 51441, 19378, 54350, 47609, 4036, 42472, 59726, 49790, 7010], 'labels': [-1, -1, -1, -1, -1, -1, 2, -1, -1, 7], 'scores': [0.4363292455673218, 0.3944894075393677, 0.44031083583831787, 0.4171351194381714, 0.3825916051864624, 0.6949840188026428, 0.6169491410255432, 0.6442012786865234, 0.5459151268005371, 0.39572152495384216]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.1475856304168701})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6063888072967529})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36270758509635925})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3312520980834961})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32114410400390625})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26402977108955383})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29443594813346863})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28666114807128906})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30079716444015503})
store['active_learning_steps'][92]['training']['best_epoch']=6
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9715, 'crossentropy': 0.25060380859375}
store['active_learning_steps'][92]['eval_training']={}
store['active_learning_steps'][92]['eval_training']['epochs']=[]
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.694447934627533})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4387383460998535})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3473268449306488})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30470627546310425})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2981361150741577})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28731459379196167})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27466604113578796})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2796952724456787})
store['active_learning_steps'][92]['eval_training']['best_epoch']=7
store['active_learning_steps'][92]['acquisition']={'indices': [37407, 30110, 8575, 4761, 37367, 16849, 6228, 3420, 1626, 47161], 'labels': [-1, -1, -1, 8, -1, -1, -1, -1, -1, -1], 'scores': [0.35282814502716064, 0.4201864004135132, 0.3239097595214844, 0.4258221387863159, 0.3624657392501831, 0.24977171421051025, 0.3696608543395996, 0.22319209575653076, 0.34029197692871094, 0.31834542751312256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9920254945755005})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.553615152835846})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.44202619791030884})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3068087697029114})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29753386974334717})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.288438081741333})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29191291332244873})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29145655035972595})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28173714876174927})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.29797548055648804})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2915416359901428})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2869829535484314})
store['active_learning_steps'][93]['training']['best_epoch']=9
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9718, 'crossentropy': 0.24430859375}
store['active_learning_steps'][93]['eval_training']={}
store['active_learning_steps'][93]['eval_training']['epochs']=[]
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6964261531829834})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4068370461463928})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3420504331588745})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2995314598083496})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3047107458114624})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2715773582458496})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25190913677215576})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2846861183643341})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.23667138814926147})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2583748996257782})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.22990185022354126})
store['active_learning_steps'][93]['eval_training']['best_epoch']=11
store['active_learning_steps'][93]['acquisition']={'indices': [57191, 6990, 1955, 29361, 54019, 16638, 20328, 31635, 6512, 5619], 'labels': [-1, -1, -1, 5, -1, -1, -1, -1, -1, -1], 'scores': [0.39656078815460205, 0.4491511583328247, 0.3767348527908325, 0.49938106536865234, 0.5419931411743164, 0.5370506644248962, 0.49858009815216064, 0.5292683839797974, 0.5510079860687256, 0.5382342338562012]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1273949146270752})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5941569805145264})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.41580137610435486})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.32237333059310913})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2955193519592285})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32596319913864136})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30345606803894043})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29227644205093384})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25681835412979126})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31785106658935547})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3114805817604065})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.35358986258506775})
store['active_learning_steps'][94]['training']['best_epoch']=9
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9727, 'crossentropy': 0.245499462890625}
store['active_learning_steps'][94]['eval_training']={}
store['active_learning_steps'][94]['eval_training']['epochs']=[]
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6791644096374512})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.42981722950935364})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3775426149368286})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2871800661087036})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.303669810295105})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2871551215648651})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2731435298919678})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.24952912330627441})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.23153701424598694})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23000869154930115})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24950286746025085})
store['active_learning_steps'][94]['eval_training']['best_epoch']=10
store['active_learning_steps'][94]['acquisition']={'indices': [53565, 6512, 16858, 25105, 51520, 1127, 56196, 10039, 57839, 5156], 'labels': [-1, -1, -1, -1, -1, 7, -1, -1, -1, -1], 'scores': [0.43162643909454346, 0.5086090564727783, 0.5058544874191284, 0.522108793258667, 0.2996879816055298, 0.49151134490966797, 0.6090319156646729, 0.3959794044494629, 0.48225581645965576, 0.5060585737228394]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.1311407089233398})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.594092071056366})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41703277826309204})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3259311318397522})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35879260301589966})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2781449854373932})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30145543813705444})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3025435209274292})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2916049063205719})
store['active_learning_steps'][95]['training']['best_epoch']=6
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.2514485595703125}
store['active_learning_steps'][95]['eval_training']={}
store['active_learning_steps'][95]['eval_training']['epochs']=[]
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6548961400985718})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.426730751991272})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38178446888923645})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3310600221157074})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3084218502044678})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3018072843551636})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29953548312187195})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27950119972229004})
store['active_learning_steps'][95]['eval_training']['best_epoch']=8
store['active_learning_steps'][95]['acquisition']={'indices': [28116, 21925, 20, 59032, 41505, 27843, 51989, 393, 27540, 10516], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.28144168853759766, 0.357998251914978, 0.4892045259475708, 0.2940727472305298, 0.4307730197906494, 0.3298581838607788, 0.3849388360977173, 0.4673241376876831, 0.3411058187484741, 0.35391926765441895]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.2195183038711548})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6402207612991333})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.47557389736175537})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.362179696559906})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3328925371170044})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3208141326904297})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2980841398239136})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.291145384311676})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3343825936317444})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33916109800338745})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36692294478416443})
store['active_learning_steps'][96]['training']['best_epoch']=8
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9714, 'crossentropy': 0.2409968994140625}
store['active_learning_steps'][96]['eval_training']={}
store['active_learning_steps'][96]['eval_training']['epochs']=[]
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6661077737808228})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4415266513824463})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3776816725730896})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.33063602447509766})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3281114101409912})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28418833017349243})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2767702341079712})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2603943347930908})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24910469353199005})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26659470796585083})
store['active_learning_steps'][96]['eval_training']['best_epoch']=9
store['active_learning_steps'][96]['acquisition']={'indices': [42180, 34583, 23538, 19868, 37952, 42703, 34839, 373, 7005, 13831], 'labels': [0, 7, 4, 5, 8, 0, 0, -1, 2, 3], 'scores': [0.3947274088859558, 0.4833512306213379, 0.45375365018844604, 0.5989127159118652, 0.39042145013809204, 0.6180498003959656, 0.440151572227478, 0.4736565351486206, 0.34447962045669556, 0.5729382038116455]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.1880192756652832})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5819157361984253})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.40093693137168884})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33379632234573364})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.321066677570343})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2976325452327728})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2795822322368622})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28553298115730286})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.286260724067688})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27853724360466003})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29293519258499146})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27471739053726196})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2838473618030548})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2924623191356659})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3312898278236389})
store['active_learning_steps'][97]['training']['best_epoch']=12
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.2618526611328125}
store['active_learning_steps'][97]['eval_training']={}
store['active_learning_steps'][97]['eval_training']['epochs']=[]
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7202520370483398})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.43520641326904297})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.351274311542511})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.338050901889801})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28442415595054626})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2684805691242218})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2677619755268097})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2484700083732605})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.22216448187828064})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25498998165130615})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24011510610580444})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.22127020359039307})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24307674169540405})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24875953793525696})
store['active_learning_steps'][97]['eval_training']['best_epoch']=12
store['active_learning_steps'][97]['acquisition']={'indices': [27047, 47954, 15852, 6036, 42200, 44289, 47840, 41344, 57318, 15287], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4919307231903076, 0.43518567085266113, 0.6237213015556335, 0.47637826204299927, 0.3913542628288269, 0.34929072856903076, 0.32187628746032715, 0.30515193939208984, 0.5660455226898193, 0.4450717568397522]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.1420762538909912})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5752781629562378})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.37921813130378723})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3103683888912201})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2859683632850647})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3353527784347534})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27566659450531006})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2693066895008087})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.289924681186676})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2657354474067688})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2703802287578583})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2791505455970764})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2837156355381012})
store['active_learning_steps'][98]['training']['best_epoch']=10
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9747, 'crossentropy': 0.242852392578125}
store['active_learning_steps'][98]['eval_training']={}
store['active_learning_steps'][98]['eval_training']['epochs']=[]
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6885354518890381})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4511984586715698})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3882509171962738})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.31811630725860596})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28901082277297974})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2558373808860779})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23626968264579773})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23266610503196716})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23282456398010254})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2513207793235779})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25452443957328796})
store['active_learning_steps'][98]['eval_training']['best_epoch']=8
store['active_learning_steps'][98]['acquisition']={'indices': [26501, 13011, 5822, 12453, 40932, 29439, 30279, 11186, 15607, 22083], 'labels': [-1, -1, -1, 7, -1, -1, -1, -1, -1, 2], 'scores': [0.40807902812957764, 0.5093698501586914, 0.42898082733154297, 0.6377983093261719, 0.36480581760406494, 0.5694745779037476, 0.37799298763275146, 0.38314616680145264, 0.48974406719207764, 0.6724908351898193]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1778650283813477})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6061639785766602})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4284941256046295})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33057600259780884})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32925403118133545})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3106817305088043})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28936126828193665})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2981876730918884})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29524192214012146})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3126142621040344})
store['active_learning_steps'][99]['training']['best_epoch']=7
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9718, 'crossentropy': 0.25706513671875}
store['active_learning_steps'][99]['eval_training']={}
store['active_learning_steps'][99]['eval_training']['epochs']=[]
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6930472254753113})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.45811641216278076})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.39405685663223267})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3652454614639282})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2897820472717285})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28568005561828613})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26831650733947754})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24035795032978058})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2580862045288086})
store['active_learning_steps'][99]['eval_training']['best_epoch']=8
store['active_learning_steps'][99]['acquisition']={'indices': [58290, 43957, 37644, 36030, 15857, 5689, 34909, 14883, 11809, 12385], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4216427803039551, 0.41618645191192627, 0.35258913040161133, 0.5049245357513428, 0.5806580781936646, 0.570235013961792, 0.5244708061218262, 0.4612749218940735, 0.458632230758667, 0.6145732402801514]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.2642369270324707})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.619385838508606})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.43546921014785767})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34479379653930664})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3315504193305969})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3196520209312439})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30009591579437256})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30911076068878174})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30137479305267334})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30415260791778564})
store['active_learning_steps'][100]['training']['best_epoch']=7
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.2515253173828125}
store['active_learning_steps'][100]['eval_training']={}
store['active_learning_steps'][100]['eval_training']['epochs']=[]
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6679762601852417})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43107476830482483})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3655433654785156})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3228451609611511})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2694655656814575})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2633122205734253})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27606362104415894})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2777066230773926})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2722906470298767})
store['active_learning_steps'][100]['eval_training']['best_epoch']=6
store['active_learning_steps'][100]['acquisition']={'indices': [16688, 41553, 4810, 41584, 57193, 54490, 51557, 46135, 53114, 30588], 'labels': [8, -1, -1, -1, -1, 6, -1, -1, -1, -1], 'scores': [0.5246738791465759, 0.3544301986694336, 0.2264854907989502, 0.34052157402038574, 0.34225988388061523, 0.42547160387039185, 0.3204033374786377, 0.24362623691558838, 0.44084489345550537, 0.3861290216445923]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.160041332244873})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5323249101638794})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3797469139099121})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.312056303024292})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2824209928512573})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2957882285118103})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28382155299186707})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27608203887939453})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28411388397216797})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28732141852378845})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9794921875, 'crossentropy': 0.2633555829524994})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.258706271648407})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28887444734573364})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.26762694120407104})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2755002975463867})
store['active_learning_steps'][101]['training']['best_epoch']=12
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9722, 'crossentropy': 0.24600263671875}
store['active_learning_steps'][101]['eval_training']={}
store['active_learning_steps'][101]['eval_training']['epochs']=[]
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6874032020568848})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4657458961009979})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.33887141942977905})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29365888237953186})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29196470975875854})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2762339115142822})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.253503680229187})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23571676015853882})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24125881493091583})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.21963690221309662})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.22938355803489685})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23115324974060059})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.22754038870334625})
store['active_learning_steps'][101]['eval_training']['best_epoch']=10
store['active_learning_steps'][101]['acquisition']={'indices': [26211, 46590, 10112, 18517, 50303, 33239, 40247, 1635, 14908, 34871], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4831331968307495, 0.49667084217071533, 0.4922536611557007, 0.481408953666687, 0.4403507709503174, 0.45847779512405396, 0.4277998208999634, 0.4220515489578247, 0.6220824718475342, 0.37993335723876953]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0557172298431396})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5576251149177551})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4070659279823303})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3264316916465759})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2774145305156708})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.280200332403183})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2723407745361328})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2642216086387634})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.255111962556839})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.27116671204566956})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.259889155626297})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2532563805580139})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24973785877227783})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27753946185112})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2827453017234802})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.28112292289733887})
store['active_learning_steps'][102]['training']['best_epoch']=13
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.974, 'crossentropy': 0.2379696533203125}
store['active_learning_steps'][102]['eval_training']={}
store['active_learning_steps'][102]['eval_training']['epochs']=[]
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6826590299606323})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4296342730522156})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33371394872665405})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27028539776802063})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2632535696029663})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25327181816101074})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2622199058532715})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.21938598155975342})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2557451128959656})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23475053906440735})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2388092577457428})
store['active_learning_steps'][102]['eval_training']['best_epoch']=8
store['active_learning_steps'][102]['acquisition']={'indices': [4379, 50978, 33655, 28504, 5470, 33653, 33475, 39201, 59492, 28468], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.6256554126739502, 0.4150775671005249, 0.2751067876815796, 0.5573967695236206, 0.3640514612197876, 0.5339553356170654, 0.5893527269363403, 0.6227666139602661, 0.5551432967185974, 0.4557262659072876]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1988872289657593})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.6099791526794434})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3680170178413391})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31259626150131226})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2719504237174988})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.2815776765346527})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2610895335674286})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26479700207710266})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.25519847869873047})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25728824734687805})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28577959537506104})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.25645676255226135})
store['active_learning_steps'][103]['training']['best_epoch']=9
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.2467923828125}
store['active_learning_steps'][103]['eval_training']={}
store['active_learning_steps'][103]['eval_training']['epochs']=[]
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.687666654586792})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4557947814464569})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3642333149909973})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3337551951408386})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2804560661315918})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.26648250222206116})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.29160863161087036})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29175466299057007})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.22697420418262482})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.228038489818573})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2698764204978943})
store['active_learning_steps'][103]['eval_training']['best_epoch']=9
store['active_learning_steps'][103]['acquisition']={'indices': [38232, 25608, 18587, 13538, 34726, 17079, 262, 52249, 22098, 2148], 'labels': [-1, -1, -1, 5, -1, 6, 2, -1, -1, 6], 'scores': [0.46997547149658203, 0.47330236434936523, 0.3930191993713379, 0.6160808205604553, 0.5098539590835571, 0.6640635132789612, 0.6621449589729309, 0.5104255676269531, 0.5820778608322144, 0.6091071963310242]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.1543118953704834})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6459690928459167})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4165537357330322})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33784377574920654})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.317569375038147})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32206642627716064})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28304174542427063})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28302431106567383})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2823660671710968})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29914575815200806})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2468542754650116})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2584534287452698})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2834520637989044})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.25850242376327515})
store['active_learning_steps'][104]['training']['best_epoch']=11
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9714, 'crossentropy': 0.244006298828125}
store['active_learning_steps'][104]['eval_training']={}
store['active_learning_steps'][104]['eval_training']['epochs']=[]
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7121156454086304})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42754966020584106})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3431413769721985})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2930675745010376})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2788434624671936})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24326172471046448})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23821116983890533})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23936501145362854})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24418213963508606})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23694752156734467})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23759877681732178})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2223241627216339})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23447014391422272})
store['active_learning_steps'][104]['eval_training']['best_epoch']=12
store['active_learning_steps'][104]['acquisition']={'indices': [23757, 7991, 14146, 59819, 46397, 11708, 53507, 29485, 21054, 31834], 'labels': [-1, -1, -1, -1, -1, -1, 5, -1, -1, -1], 'scores': [0.36836397647857666, 0.46126788854599, 0.4831259250640869, 0.43260443210601807, 0.5354130268096924, 0.6025023460388184, 0.3975107669830322, 0.5726804137229919, 0.45936059951782227, 0.4472135305404663]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.1445661783218384})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5056990385055542})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.36726757884025574})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3224617540836334})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24573954939842224})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.24687373638153076})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.98046875, 'crossentropy': 0.2273343801498413})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2540160119533539})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.22380778193473816})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.24672479927539825})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.27194514870643616})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24744996428489685})
store['active_learning_steps'][105]['training']['best_epoch']=9
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.2274128173828125}
store['active_learning_steps'][105]['eval_training']={}
store['active_learning_steps'][105]['eval_training']['epochs']=[]
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7056639194488525})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4949086904525757})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35437461733818054})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29800188541412354})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2683246433734894})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.28999465703964233})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2441805601119995})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.25805336236953735})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2473503053188324})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2387644648551941})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2117149531841278})
store['active_learning_steps'][105]['eval_training']['best_epoch']=11
store['active_learning_steps'][105]['acquisition']={'indices': [9963, 19931, 2208, 1940, 46153, 7402, 9730, 26324, 46765, 1596], 'labels': [-1, -1, 4, 9, -1, -1, -1, -1, -1, -1], 'scores': [0.5344910621643066, 0.5011192560195923, 0.3640621304512024, 0.3203345835208893, 0.44039011001586914, 0.6390095353126526, 0.4265094995498657, 0.4541022777557373, 0.4252047538757324, 0.6011266708374023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.178543210029602})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6099737882614136})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.42371463775634766})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3292689919471741})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27861544489860535})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.28441864252090454})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2693689465522766})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30013155937194824})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2693539261817932})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2984640598297119})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27339357137680054})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2891432046890259})
store['active_learning_steps'][106]['training']['best_epoch']=9
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.971, 'crossentropy': 0.2390593994140625}
store['active_learning_steps'][106]['eval_training']={}
store['active_learning_steps'][106]['eval_training']['epochs']=[]
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7437379360198975})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.44719693064689636})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34634873270988464})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2943030297756195})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28725603222846985})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26001930236816406})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2650868892669678})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27170318365097046})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.21739627420902252})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.21763160824775696})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2244652807712555})
store['active_learning_steps'][106]['eval_training']['best_epoch']=9
store['active_learning_steps'][106]['acquisition']={'indices': [59401, 5124, 57331, 49790, 27898, 54049, 12504, 48270, 33694, 30738], 'labels': [4, -1, 2, 2, 2, -1, -1, 2, 3, -1], 'scores': [0.42047393321990967, 0.4394593834877014, 0.7704339623451233, 0.5100752115249634, 0.5157969892024994, 0.42417317628860474, 0.2945901155471802, 0.5429876446723938, 0.39657700061798096, 0.3983362913131714]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.1198642253875732})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.49804896116256714})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4253232479095459})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3093340992927551})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2633596360683441})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28435444831848145})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2446497678756714})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2408096194267273})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.2339218109846115})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2702230215072632})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.23331071436405182})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24333149194717407})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.29174771904945374})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27793067693710327})
store['active_learning_steps'][107]['training']['best_epoch']=11
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9739, 'crossentropy': 0.2223200439453125}
store['active_learning_steps'][107]['eval_training']={}
store['active_learning_steps'][107]['eval_training']['epochs']=[]
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6460340023040771})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44849127531051636})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33899420499801636})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2672877311706543})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25329530239105225})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2677399814128876})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2243882715702057})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2252269983291626})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2328033447265625})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.201214000582695})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2099822759628296})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.22020819783210754})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.22435593605041504})
store['active_learning_steps'][107]['eval_training']['best_epoch']=10
store['active_learning_steps'][107]['acquisition']={'indices': [18918, 53188, 3187, 47847, 55778, 59581, 59380, 49980, 48735, 7984], 'labels': [-1, -1, 6, -1, -1, -1, 8, -1, -1, 4], 'scores': [0.45053672790527344, 0.482851505279541, 0.5474200248718262, 0.4830203056335449, 0.6134222149848938, 0.3153752088546753, 0.30630722641944885, 0.40242624282836914, 0.5567842721939087, 0.4939584732055664]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.171921730041504})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5980018973350525})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3756211996078491})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3348720073699951})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30476099252700806})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2785617411136627})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.27274399995803833})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27253037691116333})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25954681634902954})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.27557680010795593})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27459967136383057})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25523245334625244})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.25059065222740173})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3061007857322693})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2741558253765106})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2565433382987976})
store['active_learning_steps'][108]['training']['best_epoch']=13
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.2318583740234375}
store['active_learning_steps'][108]['eval_training']={}
store['active_learning_steps'][108]['eval_training']['epochs']=[]
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6148425936698914})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4590267539024353})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.31367433071136475})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32112643122673035})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29347267746925354})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2739804983139038})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24252909421920776})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25739163160324097})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2549266219139099})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.22417816519737244})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.24347421526908875})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.20888376235961914})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2334129959344864})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.22280529141426086})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23297560214996338})
store['active_learning_steps'][108]['eval_training']['best_epoch']=12
store['active_learning_steps'][108]['acquisition']={'indices': [7222, 4495, 9633, 39656, 4194, 58170, 1082, 55910, 50844, 56113], 'labels': [-1, -1, 9, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4910855293273926, 0.37843048572540283, 0.6784916520118713, 0.5422183871269226, 0.4337460398674011, 0.4740704298019409, 0.5695915222167969, 0.624466061592102, 0.47817230224609375, 0.4636622667312622]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.2299675941467285})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6061057448387146})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.41362714767456055})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.33418819308280945})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3084317445755005})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24879702925682068})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2552950978279114})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2538316249847412})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.2250380963087082})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2711741626262665})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2717650234699249})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2659207582473755})
store['active_learning_steps'][109]['training']['best_epoch']=9
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.9692, 'crossentropy': 0.2313496337890625}
store['active_learning_steps'][109]['eval_training']={}
store['active_learning_steps'][109]['eval_training']['epochs']=[]
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6288015246391296})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4241498112678528})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34730756282806396})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3336676061153412})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30762386322021484})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2770161032676697})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26257845759391785})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2599846124649048})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2547524869441986})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24902981519699097})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23801568150520325})
store['active_learning_steps'][109]['eval_training']['best_epoch']=11
store['active_learning_steps'][109]['acquisition']={'indices': [28505, 16836, 56190, 10044, 51365, 12005, 16051, 53804, 5659, 10549], 'labels': [-1, 7, 4, 6, -1, -1, -1, -1, -1, -1], 'scores': [0.3901151418685913, 0.6060891151428223, 0.4125693440437317, 0.4149840772151947, 0.44055235385894775, 0.5864354372024536, 0.36091768741607666, 0.5079119801521301, 0.3728177547454834, 0.26585566997528076]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0794951915740967})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.539104700088501})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36670616269111633})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.33178791403770447})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2489711046218872})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28081852197647095})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24937298893928528})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.23555988073349})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.22964239120483398})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2563248872756958})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2551851272583008})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9794921875, 'crossentropy': 0.24206772446632385})
store['active_learning_steps'][110]['training']['best_epoch']=9
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9708, 'crossentropy': 0.2354265869140625}
store['active_learning_steps'][110]['eval_training']={}
store['active_learning_steps'][110]['eval_training']['epochs']=[]
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6726557016372681})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4359402656555176})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35610973834991455})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3128817677497864})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29187917709350586})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26317504048347473})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2444499135017395})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2563987672328949})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23053474724292755})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.25541555881500244})
store['active_learning_steps'][110]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.21987590193748474})
store['active_learning_steps'][110]['eval_training']['best_epoch']=11
store['active_learning_steps'][110]['acquisition']={'indices': [31301, 30895, 517, 1942, 54525, 48382, 9158, 52078, 56412, 32546], 'labels': [5, -1, 8, -1, -1, -1, 0, -1, -1, -1], 'scores': [0.6778002381324768, 0.4083983898162842, 0.5442138314247131, 0.40041422843933105, 0.41007769107818604, 0.3788580894470215, 0.5134290456771851, 0.4349929094314575, 0.4565316438674927, 0.3559621572494507]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1562681198120117})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5392588376998901})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3555169403553009})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.303094744682312})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.261006236076355})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2522623538970947})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.247563898563385})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25341367721557617})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.25384464859962463})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2615251839160919})
store['active_learning_steps'][111]['training']['best_epoch']=7
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9729, 'crossentropy': 0.240742724609375}
