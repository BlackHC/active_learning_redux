store = {}
store['timestamp']=1620914146
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=9']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=9
store['worker_id']=9
store['num_workers']=20
store['config']={'seed': 1247, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 1000, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.237905979156494})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.6937150955200195})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.7671799659729004})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.8729186058044434})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6896, 'crossentropy': 2.03115}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.134763479232788})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.103419542312622})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1140166521072388})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [37974, 1413, 4918, 28928, 14595, 6650, 15503, 10355, 24457, 32433], 'labels': [2, 5, 0, 9, -1, 7, 9, 6, 8, 9], 'scores': [0.6350317597389221, 0.9490948915481567, 0.6411916017532349, 0.8011754751205444, 0.5418620109558105, 0.8741342425346375, 0.8429852724075317, 0.8407161235809326, 0.7072444558143616, 0.5970459580421448]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.1133828163146973})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 2.3641233444213867})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.791292190551758})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.702803134918213})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6926, 'crossentropy': 1.922855859375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1429696083068848})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.083305835723877})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1312369108200073})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [21156, 43538, 12351, 34475, 36766, 35604, 38208, 43961, 4681, 3258], 'labels': [3, 8, 0, 2, 6, 8, 2, 0, 3, 3], 'scores': [0.5643802881240845, 0.6362847685813904, 0.5155928730964661, 0.7422375679016113, 0.5169933140277863, 0.5750599503517151, 0.259464293718338, 0.7697128653526306, 0.6066511273384094, 0.5999274849891663]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.7424423694610596})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.072697639465332})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.2881784439086914})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 2.054819107055664})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7071, 'crossentropy': 1.6029837890625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0734912157058716})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.0243866443634033})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.0033999681472778})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [32637, 4495, 34076, 44968, 9721, 49593, 47471, 52981, 47122, 1788], 'labels': [2, 5, -1, 8, 2, 6, 5, -1, 8, 8], 'scores': [0.5307788848876953, 0.6056972146034241, 0.2644972801208496, 0.44455528259277344, 0.5835167169570923, 0.5252828001976013, 0.5734901428222656, 0.4474412202835083, 0.5057467818260193, 0.6134152412414551]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.4544119834899902})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.5815110206604004})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.8047831058502197})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.8492070436477661})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7516, 'crossentropy': 1.3993302734375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.010151982307434})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 0.9570764899253845})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 0.9029541611671448})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [11822, 5755, 20063, 58613, 14629, 58018, 5770, 14222, 28655, 53142], 'labels': [7, 4, 4, 4, -1, 4, 3, 9, 4, 9], 'scores': [0.605305552482605, 0.7114487886428833, 0.7388136982917786, 0.6500018835067749, 0.4853261709213257, 0.7016764879226685, 0.5810027122497559, 0.5651453733444214, 0.601518452167511, 0.5452929735183716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0679593086242676})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.179726004600525})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.3176844120025635})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.4229347705841064})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8324, 'crossentropy': 0.99982109375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.8683089017868042})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.8304587602615356})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.7966738939285278})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [1454, 13647, 31130, 48811, 52538, 18615, 8865, 22945, 16629, 17207], 'labels': [0, 3, 9, 2, 9, 3, 3, 2, 5, 3], 'scores': [0.4316323399543762, 0.6230601072311401, 0.5219849944114685, 0.6040016412734985, 0.5577303171157837, 0.5011588931083679, 0.4451429843902588, 0.6078721284866333, 0.5394577980041504, 0.4349488615989685]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0426201820373535})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1070671081542969})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2068493366241455})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.4388055801391602})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8165, 'crossentropy': 0.9963603515625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9240946769714355})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.8384218215942383})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.7994223833084106})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [45118, 25321, 58836, 4488, 2245, 39639, 9799, 54788, 18431, 37390], 'labels': [5, 8, 7, 0, -1, 0, 8, 6, 5, 6], 'scores': [0.29758507013320923, 0.5279024839401245, 0.3608245849609375, 0.4608423709869385, 0.36571764945983887, 0.6049679517745972, 0.688362181186676, 0.3629191517829895, 0.416351318359375, 0.5629472732543945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.1074872016906738})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.1283425092697144})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.3201782703399658})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.4583017826080322})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7914, 'crossentropy': 1.05196748046875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.0195651054382324})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 0.8897432088851929})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 0.8529613018035889})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [37307, 53156, 45047, 53114, 15887, 56246, 10258, 55496, 4489, 12736], 'labels': [2, 3, 2, 5, 2, 5, 5, 9, 2, 5], 'scores': [0.404596209526062, 0.47127723693847656, 0.5338461399078369, 0.4562017321586609, 0.43588876724243164, 0.476055383682251, 0.4416848421096802, 0.49095970392227173, 0.48772287368774414, 0.3402581214904785]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9698307514190674})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0133233070373535})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9695200324058533})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.120976448059082})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.2078280448913574})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.345432162284851})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8604, 'crossentropy': 0.95609501953125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7886261940002441})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.6791012287139893})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.6061112880706787})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.6241843700408936})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.5825198888778687})
store['active_learning_steps'][7]['eval_training']['best_epoch']=5
store['active_learning_steps'][7]['acquisition']={'indices': [23611, 2634, 59686, 2076, 12327, 45203, 529, 55530, 41587, 52204], 'labels': [9, 7, 1, 3, 4, 2, 9, 8, 5, 0], 'scores': [0.5589248538017273, 0.41337141394615173, 0.5679459571838379, 0.506041407585144, 0.696108341217041, 0.4100506007671356, 0.5335438251495361, 0.5067660808563232, 0.4322283864021301, 0.8369733691215515]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8439403772354126})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7978401780128479})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8526766300201416})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.799836277961731})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9224871397018433})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8791, 'crossentropy': 0.731938720703125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.7770182490348816})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.6463731527328491})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.5928109884262085})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.5807605981826782})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [30548, 23463, 17214, 11406, 18145, 29943, 2738, 49547, 46234, 19770], 'labels': [-1, 9, -1, 8, 4, 7, 2, -1, -1, 0], 'scores': [0.31242692470550537, 0.5859782099723816, 0.2599325180053711, 0.5886827707290649, 0.5368632078170776, 0.5006937384605408, 0.342279314994812, 0.3328615427017212, 0.22264575958251953, 0.3865842819213867]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.9227885007858276})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7378298044204712})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8196765184402466})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7386739253997803})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.875577449798584})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8961, 'crossentropy': 0.67239609375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7310340404510498})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5846998691558838})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5620439052581787})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5364354252815247})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [57445, 47741, 2040, 1019, 10390, 4066, 5482, 29094, 27194, 7112], 'labels': [-1, 5, 1, 7, 3, 1, 4, 3, 7, 5], 'scores': [0.2539489269256592, 0.589927613735199, 0.5393253564834595, 0.6601671576499939, 0.4740593433380127, 0.5803180932998657, 0.5286133289337158, 0.48078423738479614, 0.5420414805412292, 0.46439695358276367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8355913758277893})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7057489156723022})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7574119567871094})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6918070912361145})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8674213886260986})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7496868371963501})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.861156165599823})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9073, 'crossentropy': 0.656881396484375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6737490296363831})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.5416404008865356})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5016101598739624})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4906565546989441})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.460771381855011})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.4301829934120178})
store['active_learning_steps'][10]['eval_training']['best_epoch']=6
store['active_learning_steps'][10]['acquisition']={'indices': [46312, 16190, 1801, 37769, 55241, 36202, 26471, 7259, 16894, 16836], 'labels': [-1, 3, -1, 7, 8, 4, 8, 2, 6, 7], 'scores': [0.48262667655944824, 0.6015998125076294, 0.5549333095550537, 0.5572654008865356, 0.5961096882820129, 0.6958562731742859, 0.4206496477127075, 0.3071628212928772, 0.3773571252822876, 0.7267667055130005]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8132783770561218})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5906481146812439})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6104134917259216})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5840072631835938})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.655755877494812})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6625805497169495})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6655013561248779})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9232, 'crossentropy': 0.52632333984375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6616548299789429})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5137227773666382})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4501798748970032})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4374443292617798})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.3958272933959961})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.39367133378982544})
store['active_learning_steps'][11]['eval_training']['best_epoch']=6
store['active_learning_steps'][11]['acquisition']={'indices': [54782, 13533, 54950, 16025, 15491, 15954, 52713, 8887, 34550, 16117], 'labels': [3, -1, 8, 2, -1, -1, 3, 4, 4, 9], 'scores': [0.48757457733154297, 0.47551000118255615, 0.5702458620071411, 0.5811787843704224, 0.36747896671295166, 0.42146778106689453, 0.637370228767395, 0.6834332346916199, 0.6643155217170715, 0.4574012756347656]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9119948148727417})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6222683191299438})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.612328052520752})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6292414665222168})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6841901540756226})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7019811868667603})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9163, 'crossentropy': 0.5677916015625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6419742703437805})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.538147509098053})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.45842674374580383})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.42569687962532043})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.44870615005493164})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [33981, 41328, 33035, 50461, 11487, 22619, 44179, 33883, 34765, 30056], 'labels': [-1, -1, 6, 7, 6, -1, 6, 8, 6, -1], 'scores': [0.3508768081665039, 0.27916038036346436, 0.6940307021141052, 0.6186935305595398, 0.5104829668998718, 0.4211697578430176, 0.6332560777664185, 0.33986735343933105, 0.644167423248291, 0.2993755340576172]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.819695234298706})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5247750878334045})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5385315418243408})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5318889617919922})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5195900797843933})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5213143825531006})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5613170862197876})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.558160662651062})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9354, 'crossentropy': 0.48966884765625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6228538751602173})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5251578092575073})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3893885314464569})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3896472156047821})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.37609702348709106})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.37985947728157043})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3645097017288208})
store['active_learning_steps'][13]['eval_training']['best_epoch']=7
store['active_learning_steps'][13]['acquisition']={'indices': [9161, 41426, 52816, 32276, 53713, 31345, 34864, 11427, 52117, 1707], 'labels': [-1, 4, -1, 3, -1, 3, -1, -1, 9, -1], 'scores': [0.5336747169494629, 0.5105100572109222, 0.5022864937782288, 0.8424184322357178, 0.35408878326416016, 0.6981884241104126, 0.33405637741088867, 0.48067790269851685, 0.43689846992492676, 0.5605461001396179]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8432683348655701})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5939440727233887})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5435187816619873})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5575805902481079})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6007150411605835})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6190985441207886})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9228, 'crossentropy': 0.52969150390625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6774929761886597})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4961053431034088})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4590643048286438})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.41925492882728577})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.3962835669517517})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [53170, 29585, 44350, 47890, 18193, 44040, 56412, 19590, 51981, 53897], 'labels': [8, -1, 3, -1, -1, -1, 8, 5, -1, 0], 'scores': [0.5307140350341797, 0.5099883079528809, 0.6905948519706726, 0.48228245973587036, 0.4579324722290039, 0.5670009255409241, 0.3933819532394409, 0.4258456826210022, 0.5809261798858643, 0.5194422602653503]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8164947032928467})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6579068303108215})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5823971629142761})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5990325808525085})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6393575668334961})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6329411864280701})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.925, 'crossentropy': 0.549435791015625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6200181245803833})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.46918928623199463})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.45568639039993286})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4158878028392792})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4056406617164612})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [52845, 16957, 52418, 23273, 11097, 54736, 23561, 31014, 56300, 37340], 'labels': [-1, 6, -1, 0, -1, 3, -1, 8, 9, -1], 'scores': [0.39026135206222534, 0.5484373569488525, 0.41893863677978516, 0.3900294899940491, 0.42167139053344727, 0.46888595819473267, 0.4746789336204529, 0.7182360291481018, 0.6525588035583496, 0.4740126132965088]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8664042949676514})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5653908252716064})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5338132977485657})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5669664144515991})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5549212694168091})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6195697784423828})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9314, 'crossentropy': 0.496198779296875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6462855339050293})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.45511093735694885})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4567212462425232})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.43394380807876587})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3986395001411438})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
store['active_learning_steps'][16]['acquisition']={'indices': [52954, 40553, 14201, 9531, 39771, 18018, 17747, 44706, 38599, 19637], 'labels': [8, 8, 7, 5, 8, 5, 5, 5, 0, -1], 'scores': [0.4561014771461487, 0.6884196400642395, 0.45690762996673584, 0.588964581489563, 0.5101057887077332, 0.5435771942138672, 0.7063211798667908, 0.6753059029579163, 0.5571051239967346, 0.31894636154174805]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8820468187332153})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4855114221572876})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5503433346748352})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.49731287360191345})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47113072872161865})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5094314813613892})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4989018440246582})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5816643238067627})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9439, 'crossentropy': 0.419897265625}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6298022270202637})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.45819348096847534})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.38664132356643677})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.37129145860671997})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.33416658639907837})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.31121164560317993})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3344404995441437})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [30457, 24970, 49472, 2502, 30147, 55612, 5155, 52407, 56086, 24625], 'labels': [1, 1, -1, 7, 8, -1, 4, -1, -1, 1], 'scores': [0.5026634335517883, 0.473392128944397, 0.5759871006011963, 0.43143218755722046, 0.331451416015625, 0.48929744958877563, 0.7122579216957092, 0.6083784699440002, 0.5056781768798828, 0.6593514680862427]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.804842472076416})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4823480248451233})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.45565712451934814})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4855281710624695})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5155426263809204})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4879862368106842})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9421, 'crossentropy': 0.42891181640625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6411315202713013})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4750259816646576})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.41765642166137695})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.40263253450393677})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.41432857513427734})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [26863, 109, 43677, 6698, 4584, 7665, 49790, 6540, 14384, 34548], 'labels': [-1, -1, -1, -1, -1, -1, -1, 2, -1, -1], 'scores': [0.464308500289917, 0.256941556930542, 0.4132542610168457, 0.3735862970352173, 0.3804861307144165, 0.30795419216156006, 0.34180378913879395, 0.5076909065246582, 0.41501402854919434, 0.36761391162872314]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.73444002866745})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.45138806104660034})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45182329416275024})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4298819303512573})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4798266887664795})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.48381251096725464})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5059809684753418})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9399, 'crossentropy': 0.4441607421875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6630960702896118})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4672284722328186})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.40615618228912354})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.35473647713661194})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.35677093267440796})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3611094355583191})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [10331, 58437, 5572, 11394, 21243, 38061, 22098, 34486, 33397, 9180], 'labels': [-1, -1, -1, 2, -1, 2, -1, 0, -1, 3], 'scores': [0.4466082453727722, 0.6272034049034119, 0.36721158027648926, 0.44482287764549255, 0.5557242631912231, 0.6289422512054443, 0.5640308856964111, 0.5029113292694092, 0.48090338706970215, 0.582871675491333]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7307314872741699})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.48922860622406006})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4855327606201172})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4849596917629242})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.480255663394928})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5415376424789429})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5256045460700989})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5405423641204834})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.939, 'crossentropy': 0.44932412109375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6507259607315063})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4436216354370117})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.38977107405662537})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.36269378662109375})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3561473488807678})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3531378507614136})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3354109525680542})
store['active_learning_steps'][20]['eval_training']['best_epoch']=7
store['active_learning_steps'][20]['acquisition']={'indices': [7793, 36908, 30400, 57798, 29472, 33411, 24230, 48975, 38256, 24803], 'labels': [8, 1, -1, -1, 9, -1, -1, 2, 2, 2], 'scores': [0.5014527440071106, 0.49503666162490845, 0.4235020875930786, 0.42781925201416016, 0.571512758731842, 0.5767407417297363, 0.39004337787628174, 0.734089195728302, 0.4896755814552307, 0.44854819774627686]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7784024477005005})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4782630205154419})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4757125973701477})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4574998617172241})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.45164066553115845})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45918548107147217})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5337680578231812})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5310174822807312})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9489, 'crossentropy': 0.3893174072265625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6014516353607178})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.441367506980896})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.35029977560043335})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.34594595432281494})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3324139714241028})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.30890336632728577})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.28978872299194336})
store['active_learning_steps'][21]['eval_training']['best_epoch']=7
store['active_learning_steps'][21]['acquisition']={'indices': [54452, 36421, 25435, 39487, 20767, 56526, 4977, 9633, 45344, 30688], 'labels': [4, 3, -1, 2, 9, -1, 7, 9, 5, 8], 'scores': [0.5339125394821167, 0.5598855018615723, 0.42432594299316406, 0.6351891160011292, 0.5311673879623413, 0.2622877359390259, 0.34836721420288086, 0.46971309185028076, 0.4915100932121277, 0.612643301486969]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7993712425231934})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4510926604270935})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.38774675130844116})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4043705463409424})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4400879144668579})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4345596730709076})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9425, 'crossentropy': 0.3932288330078125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6345805525779724})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.49814707040786743})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3872935473918915})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.38945263624191284})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3640531301498413})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [19502, 41832, 15116, 55128, 27595, 46737, 13085, 55943, 32507, 24730], 'labels': [2, 2, 5, 8, 6, -1, 6, -1, 5, 5], 'scores': [0.5801001787185669, 0.5081266164779663, 0.4193546175956726, 0.5961813926696777, 0.3811342716217041, 0.37946319580078125, 0.583147406578064, 0.3384120464324951, 0.49921900033950806, 0.4453890323638916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7293720245361328})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4945611357688904})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42420077323913574})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4164999723434448})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4757401645183563})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.45227423310279846})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4908641278743744})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9494, 'crossentropy': 0.37590478515625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.596580982208252})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4572940468788147})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36281341314315796})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3528551459312439})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3325561285018921})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.32106053829193115})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [3730, 8216, 56617, 14697, 23890, 15859, 36850, 4446, 1475, 49636], 'labels': [8, -1, -1, 8, -1, -1, -1, -1, -1, -1], 'scores': [0.43789708614349365, 0.4900779724121094, 0.3987809419631958, 0.5400992631912231, 0.41820991039276123, 0.43594682216644287, 0.5042345523834229, 0.5014422535896301, 0.5258808135986328, 0.5021840333938599]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.807957649230957})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5014129877090454})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.44573697447776794})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.466094434261322})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4644622206687927})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4378264546394348})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41443994641304016})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4433504641056061})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4742281436920166})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.46605193614959717})
store['active_learning_steps'][24]['training']['best_epoch']=7
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9482, 'crossentropy': 0.3953200439453125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6293721199035645})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.42938166856765747})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.35131287574768066})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3790038526058197})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.33444344997406006})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.312164843082428})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3072635531425476})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.301723837852478})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.29534053802490234})
store['active_learning_steps'][24]['eval_training']['best_epoch']=9
store['active_learning_steps'][24]['acquisition']={'indices': [46240, 40766, 21040, 27035, 10589, 26300, 40633, 1171, 1380, 23628], 'labels': [1, 4, 9, 0, -1, 0, -1, -1, 4, 6], 'scores': [0.45901399850845337, 0.685096025466919, 0.7848069071769714, 0.6776559352874756, 0.3617098331451416, 0.5193066000938416, 0.4570424556732178, 0.2669792175292969, 0.4484478831291199, 0.6414066553115845]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9288243055343628})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5018672943115234})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4399130642414093})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4576338529586792})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4998107850551605})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47756704688072205})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9459, 'crossentropy': 0.3857818603515625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6776131391525269})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.48199737071990967})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4454330801963806})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44048774242401123})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4297100305557251})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [34583, 31487, 57713, 23968, 49064, 12924, 9782, 4158, 30041, 50960], 'labels': [7, -1, 4, 7, 8, -1, 8, 9, 3, -1], 'scores': [0.42732322216033936, 0.23021459579467773, 0.3101573586463928, 0.4595564603805542, 0.5512902736663818, 0.3252694606781006, 0.46499693393707275, 0.4401925206184387, 0.3667398691177368, 0.4261476993560791]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8438119888305664})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44993123412132263})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.42897796630859375})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4411785304546356})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4175179600715637})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4407307505607605})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.43045181035995483})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.46594810485839844})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9527, 'crossentropy': 0.401205517578125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.627383291721344})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.395107626914978})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3587961792945862})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.31842663884162903})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3403729200363159})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3103991150856018})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3168463110923767})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [48397, 3070, 51318, 6309, 57311, 12837, 51679, 1784, 55311, 53978], 'labels': [5, 1, -1, 3, 5, -1, 5, 6, 8, 5], 'scores': [0.6325784921646118, 0.5677505731582642, 0.5062137246131897, 0.5062889158725739, 0.5498877167701721, 0.6422395706176758, 0.6709555387496948, 0.5820607542991638, 0.7372951507568359, 0.4855308532714844]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1436517238616943})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5167045593261719})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4083462655544281})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3987525701522827})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4483528733253479})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.48623722791671753})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45200076699256897})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9538, 'crossentropy': 0.361787548828125}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.613216757774353})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.41762465238571167})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.38322627544403076})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.34558114409446716})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3466763198375702})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3548702895641327})
store['active_learning_steps'][27]['eval_training']['best_epoch']=4
store['active_learning_steps'][27]['acquisition']={'indices': [19915, 28216, 9687, 3030, 12909, 37460, 44736, 36363, 30753, 5429], 'labels': [-1, -1, 0, 9, -1, 8, 5, 6, -1, -1], 'scores': [0.30675041675567627, 0.4871147871017456, 0.5105818510055542, 0.575875997543335, 0.41946232318878174, 0.5801442265510559, 0.5936549305915833, 0.4027317762374878, 0.3460872173309326, 0.45982789993286133]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.901465654373169})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5155269503593445})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3991459608078003})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.42033475637435913})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3861924409866333})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4165409505367279})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4661487340927124})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.42333364486694336})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9574, 'crossentropy': 0.351699560546875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6422499418258667})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.40250688791275024})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.35899776220321655})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.31160229444503784})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3515724241733551})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.324506938457489})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3087843060493469})
store['active_learning_steps'][28]['eval_training']['best_epoch']=7
store['active_learning_steps'][28]['acquisition']={'indices': [14749, 30569, 34847, 6772, 50370, 52646, 21636, 54076, 33475, 18125], 'labels': [0, -1, 0, -1, 7, 9, 2, -1, -1, -1], 'scores': [0.39254623651504517, 0.46729105710983276, 0.4114310145378113, 0.3882010579109192, 0.5395025610923767, 0.440319299697876, 0.46897488832473755, 0.4164302349090576, 0.3343214988708496, 0.41343891620635986]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9782427549362183})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49806562066078186})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.416618287563324})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43534624576568604})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4217410683631897})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3825159966945648})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39935606718063354})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.47908395528793335})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4596882462501526})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.957, 'crossentropy': 0.343903857421875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5737807750701904})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4668000340461731})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3904101550579071})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3355579376220703})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3187658488750458})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.29313474893569946})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.28910595178604126})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.29177168011665344})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [17338, 25259, 53731, 42355, 48045, 153, 52914, 14619, 14655, 10455], 'labels': [-1, -1, 4, 3, 3, -1, 5, 3, 3, -1], 'scores': [0.3961380124092102, 0.404679536819458, 0.4291437864303589, 0.45931094884872437, 0.37287476658821106, 0.5472875833511353, 0.4110277593135834, 0.5689059495925903, 0.5711498260498047, 0.2562717795372009]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.824886679649353})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5436314344406128})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.44828522205352783})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4348104000091553})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43852052092552185})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44249239563941956})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.46643221378326416})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9477, 'crossentropy': 0.3850677978515625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5956730842590332})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.45957720279693604})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.380806028842926})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34859907627105713})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3730431795120239})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3226146697998047})
store['active_learning_steps'][30]['eval_training']['best_epoch']=6
store['active_learning_steps'][30]['acquisition']={'indices': [10256, 10795, 32289, 14337, 5536, 34396, 14299, 14760, 37590, 56067], 'labels': [2, 7, 7, 7, 8, 3, 7, 2, 5, -1], 'scores': [0.48108971118927, 0.47329288721084595, 0.4148004651069641, 0.4962541460990906, 0.5459596514701843, 0.48011529445648193, 0.5415063500404358, 0.42927801609039307, 0.4727647304534912, 0.307666540145874]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.881152868270874})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5208770036697388})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4273592531681061})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3974909782409668})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37825292348861694})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3890548348426819})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36743804812431335})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.433205246925354})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3854273557662964})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4414657652378082})
store['active_learning_steps'][31]['training']['best_epoch']=7
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9588, 'crossentropy': 0.356667626953125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6270517110824585})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.42372047901153564})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.36344724893569946})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.314735472202301})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2881741523742676})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.28614819049835205})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.27197808027267456})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2831459641456604})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2827683091163635})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [31919, 10039, 19971, 52790, 54387, 28674, 1088, 27072, 9758, 11017], 'labels': [-1, -1, -1, -1, 8, 9, 7, 8, 9, -1], 'scores': [0.5537989139556885, 0.5699232220649719, 0.601040244102478, 0.4064834713935852, 0.5635682940483093, 0.45544546842575073, 0.6606771349906921, 0.5771433711051941, 0.4247346520423889, 0.4105566740036011]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9284337162971497})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5212889909744263})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4054130017757416})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39103084802627563})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42244982719421387})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39803779125213623})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3974756896495819})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9488, 'crossentropy': 0.36321025390625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5855258703231812})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.43020904064178467})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.38745391368865967})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33733537793159485})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.32646703720092773})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.31084945797920227})
store['active_learning_steps'][32]['eval_training']['best_epoch']=6
store['active_learning_steps'][32]['acquisition']={'indices': [47454, 52169, 46373, 20614, 267, 12828, 5548, 22006, 17772, 18775], 'labels': [-1, 2, 9, -1, -1, -1, 8, -1, 7, -1], 'scores': [0.3222610354423523, 0.7639549374580383, 0.5548858046531677, 0.39557909965515137, 0.41086655855178833, 0.3942486047744751, 0.45233529806137085, 0.4798325300216675, 0.5608550906181335, 0.3973226547241211]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.0819120407104492})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5667623281478882})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.44143104553222656})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37264057993888855})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33927595615386963})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37273022532463074})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3738006353378296})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3817210793495178})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9595, 'crossentropy': 0.3191185546875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6083590388298035})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4263473153114319})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3848024308681488})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36543357372283936})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.31525540351867676})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3139270544052124})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2987385392189026})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [15741, 54586, 22344, 36074, 17319, 31892, 52834, 25845, 13838, 43827], 'labels': [-1, 9, -1, -1, -1, -1, 2, -1, 6, -1], 'scores': [0.49661922454833984, 0.4352108836174011, 0.5612601041793823, 0.3784193992614746, 0.4972291588783264, 0.4443674087524414, 0.44791871309280396, 0.27518224716186523, 0.5066112279891968, 0.5419414043426514]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.9872628450393677})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5056307315826416})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3885653018951416})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3773730993270874})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39714300632476807})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3518703281879425})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4021914005279541})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39629065990448})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3768334984779358})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9554, 'crossentropy': 0.3374927734375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6670435667037964})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4520796537399292})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3767663836479187})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32870882749557495})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3008238673210144})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28699222207069397})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2647913694381714})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29945987462997437})
store['active_learning_steps'][34]['eval_training']['best_epoch']=7
store['active_learning_steps'][34]['acquisition']={'indices': [30682, 27793, 44053, 50555, 20335, 50389, 7851, 35316, 15869, 55368], 'labels': [-1, 1, -1, -1, -1, -1, 8, -1, -1, 8], 'scores': [0.4630963206291199, 0.6369815468788147, 0.40935826301574707, 0.6249661445617676, 0.446895956993103, 0.5676506161689758, 0.6291874647140503, 0.33463096618652344, 0.4225901961326599, 0.515997588634491]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9925611019134521})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.47747802734375})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3426465392112732})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3407015800476074})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33031970262527466})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3407769203186035})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37772688269615173})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3506631553173065})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9612, 'crossentropy': 0.315609814453125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6617989540100098})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.44392716884613037})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.39660289883613586})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.368036687374115})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32233142852783203})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3120079040527344})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2825912833213806})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [55739, 38549, 25624, 8765, 20069, 12314, 42032, 55488, 32342, 14100], 'labels': [5, 3, -1, 3, -1, 1, 4, 3, 9, 5], 'scores': [0.683164119720459, 0.5727824568748474, 0.46005988121032715, 0.5329293012619019, 0.34388959407806396, 0.39332956075668335, 0.41432130336761475, 0.4147687554359436, 0.47824621200561523, 0.357145756483078]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0412720441818237})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5036678314208984})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4081326127052307})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36500847339630127})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3651919960975647})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3371025323867798})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3402222990989685})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3745807707309723})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3398321568965912})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.958, 'crossentropy': 0.327088134765625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.69016432762146})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4178304374217987})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.38167333602905273})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.333457887172699})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2935783863067627})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.30965733528137207})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3009810149669647})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.29471874237060547})
store['active_learning_steps'][36]['eval_training']['best_epoch']=5
store['active_learning_steps'][36]['acquisition']={'indices': [53736, 30660, 39017, 44645, 39516, 901, 39130, 17640, 21293, 6013], 'labels': [9, -1, -1, -1, 5, -1, 6, -1, -1, -1], 'scores': [0.49699294567108154, 0.3772711753845215, 0.2690299153327942, 0.4415658712387085, 0.6114591956138611, 0.5282577276229858, 0.5523779988288879, 0.3427000045776367, 0.4226747751235962, 0.42462098598480225]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.0986742973327637})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5290859937667847})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4104403555393219})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36105024814605713})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.347662091255188})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.327099084854126})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3601313531398773})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3404896855354309})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36039772629737854})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9601, 'crossentropy': 0.3166044677734375}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6702836751937866})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.43191081285476685})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.408264696598053})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3412685692310333})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.33723241090774536})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.322512686252594})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.301389217376709})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3087034225463867})
store['active_learning_steps'][37]['eval_training']['best_epoch']=7
store['active_learning_steps'][37]['acquisition']={'indices': [19657, 9601, 17684, 8488, 5790, 42112, 58615, 28547, 18568, 24110], 'labels': [-1, 8, -1, 6, 2, 8, 8, -1, 1, 8], 'scores': [0.5278043746948242, 0.5266993641853333, 0.46151793003082275, 0.5478980541229248, 0.5302625298500061, 0.56109619140625, 0.5183257460594177, 0.49908196926116943, 0.42049145698547363, 0.6669008731842041]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.9168015718460083})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4935145974159241})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3423762321472168})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.332332968711853})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3432188928127289})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3238179385662079})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33905279636383057})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32608622312545776})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3547400236129761})
store['active_learning_steps'][38]['training']['best_epoch']=6
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9593, 'crossentropy': 0.30517431640625}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6083846092224121})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4333255887031555})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3446589708328247})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3089755177497864})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.298933207988739})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31007152795791626})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27553462982177734})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29702329635620117})
store['active_learning_steps'][38]['eval_training']['best_epoch']=7
store['active_learning_steps'][38]['acquisition']={'indices': [43481, 1183, 18381, 54035, 52814, 8715, 17192, 59294, 13998, 49493], 'labels': [-1, -1, -1, 7, 9, -1, 3, 8, 9, 8], 'scores': [0.5193184614181519, 0.4248086214065552, 0.210921049118042, 0.3223370909690857, 0.541875958442688, 0.5039640665054321, 0.37268543243408203, 0.48771870136260986, 0.5445680618286133, 0.654358446598053]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9444175958633423})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.49582868814468384})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37043237686157227})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30901414155960083})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3305650055408478})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.325575053691864})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3388671875})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9617, 'crossentropy': 0.3059620849609375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6703810691833496})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45500242710113525})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37199681997299194})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35729241371154785})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30977582931518555})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32518646121025085})
store['active_learning_steps'][39]['eval_training']['best_epoch']=5
store['active_learning_steps'][39]['acquisition']={'indices': [33383, 19807, 39208, 33050, 14883, 20072, 58392, 47090, 50137, 26889], 'labels': [-1, -1, 5, 7, -1, 3, -1, -1, -1, -1], 'scores': [0.43762123584747314, 0.449429452419281, 0.5783417224884033, 0.4303218126296997, 0.38600486516952515, 0.5881609916687012, 0.4961131811141968, 0.38349783420562744, 0.44904470443725586, 0.42347073554992676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.9934239387512207})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5202060341835022})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.41712474822998047})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38435715436935425})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35939666628837585})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3468184471130371})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3568679690361023})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3784007430076599})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3459509015083313})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3745821714401245})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4335760474205017})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3954296112060547})
store['active_learning_steps'][40]['training']['best_epoch']=9
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9578, 'crossentropy': 0.3272803466796875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6571968793869019})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.40193647146224976})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3294668197631836})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.323555052280426})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3244985044002533})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29660382866859436})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.26779234409332275})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25925377011299133})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2684088349342346})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27730610966682434})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.23350094258785248})
store['active_learning_steps'][40]['eval_training']['best_epoch']=11
store['active_learning_steps'][40]['acquisition']={'indices': [34920, 31159, 517, 2118, 26266, 14406, 13715, 54520, 9021, 21218], 'labels': [9, -1, 8, 7, 7, 8, 6, 9, -1, -1], 'scores': [0.6881414651870728, 0.38661718368530273, 0.3911376893520355, 0.5419289469718933, 0.7727312445640564, 0.6189634799957275, 0.5692487359046936, 0.4794606566429138, 0.38679587841033936, 0.3605872392654419]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0128073692321777})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4834933280944824})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3760187029838562})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3498346507549286})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.343533456325531})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3627563714981079})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33651506900787354})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32333430647850037})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32391563057899475})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3051600456237793})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33354657888412476})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3494260311126709})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3486141562461853})
store['active_learning_steps'][41]['training']['best_epoch']=10
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9639, 'crossentropy': 0.3229436279296875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6927495002746582})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4621107578277588})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39560842514038086})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3305378556251526})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.2980051338672638})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28109708428382874})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2583867311477661})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2782241106033325})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26979905366897583})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2647969126701355})
store['active_learning_steps'][41]['eval_training']['best_epoch']=7
store['active_learning_steps'][41]['acquisition']={'indices': [47837, 16557, 59339, 19251, 20002, 9617, 25534, 4165, 37347, 47852], 'labels': [-1, -1, 1, -1, -1, -1, -1, 2, 2, -1], 'scores': [0.6482709646224976, 0.4664100408554077, 0.7444856762886047, 0.5936272144317627, 0.7433183193206787, 0.5315297842025757, 0.6481982469558716, 0.6236812472343445, 0.6701487600803375, 0.4569185972213745]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.0550224781036377})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.48082396388053894})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40576010942459106})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3439384698867798})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3443262279033661})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34526506066322327})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.320743203163147})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3544943928718567})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34701770544052124})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3891751170158386})
store['active_learning_steps'][42]['training']['best_epoch']=7
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9627, 'crossentropy': 0.3123236328125}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6344476938247681})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4298344850540161})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.36486321687698364})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3157040476799011})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.2948576509952545})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28504469990730286})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.27140092849731445})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.24775230884552002})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28385129570961})
store['active_learning_steps'][42]['eval_training']['best_epoch']=8
store['active_learning_steps'][42]['acquisition']={'indices': [49934, 1269, 51939, 46962, 41445, 43953, 8729, 13342, 10855, 9598], 'labels': [-1, -1, -1, -1, 0, -1, -1, -1, 6, -1], 'scores': [0.43602681159973145, 0.5792022347450256, 0.37274467945098877, 0.43869781494140625, 0.5352177023887634, 0.35173606872558594, 0.365175724029541, 0.3883763551712036, 0.5238250494003296, 0.5145859122276306]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0259358882904053})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5674657821655273})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4031938314437866})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3438452184200287})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38275960087776184})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3922620415687561})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32839977741241455})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3479452133178711})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3787623643875122})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31267786026000977})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36463451385498047})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3415284752845764})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3417157530784607})
store['active_learning_steps'][43]['training']['best_epoch']=10
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9623, 'crossentropy': 0.3037249267578125}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6620848178863525})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4249316453933716})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3998011350631714})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.33478471636772156})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.2964516282081604})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2955569922924042})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.28113073110580444})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.25847673416137695})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.289699912071228})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.26490676403045654})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24049651622772217})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2482372224330902})
store['active_learning_steps'][43]['eval_training']['best_epoch']=11
store['active_learning_steps'][43]['acquisition']={'indices': [40624, 27004, 25969, 49227, 20686, 32747, 12253, 29395, 32107, 10672], 'labels': [-1, -1, -1, 9, -1, 8, -1, -1, -1, -1], 'scores': [0.3570379912853241, 0.5262023210525513, 0.46059244871139526, 0.6596614718437195, 0.4831433892250061, 0.7061759829521179, 0.6115685105323792, 0.4873824119567871, 0.26739227771759033, 0.5295944213867188]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.1394879817962646})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4994741678237915})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4080207049846649})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3553023338317871})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35769838094711304})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34721052646636963})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34533530473709106})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3301127552986145})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3319024443626404})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3907143473625183})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3490082025527954})
store['active_learning_steps'][44]['training']['best_epoch']=8
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9616, 'crossentropy': 0.3306628173828125}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.658193826675415})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.46734553575515747})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3584819436073303})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3081943094730377})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.289530873298645})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.2815558910369873})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.276005357503891})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.25865638256073})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2540905773639679})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2630365490913391})
store['active_learning_steps'][44]['eval_training']['best_epoch']=9
store['active_learning_steps'][44]['acquisition']={'indices': [21174, 29814, 39462, 7787, 19458, 17799, 1706, 33879, 5615, 21270], 'labels': [2, -1, -1, -1, -1, -1, -1, -1, -1, 4], 'scores': [0.6209403276443481, 0.40996813774108887, 0.26059019565582275, 0.4002748727798462, 0.4524794816970825, 0.3996460437774658, 0.4052269458770752, 0.5364580154418945, 0.541752815246582, 0.37741389870643616]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0109117031097412})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5607859492301941})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4074540138244629})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3494974970817566})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3242764472961426})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31793826818466187})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3372008204460144})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35731199383735657})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33275526762008667})
store['active_learning_steps'][45]['training']['best_epoch']=6
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9656, 'crossentropy': 0.2905331787109375}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6383323669433594})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41749107837677})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.38721901178359985})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35615429282188416})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33164387941360474})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2835245132446289})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2958306670188904})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2907712161540985})
store['active_learning_steps'][45]['eval_training']['best_epoch']=6
store['active_learning_steps'][45]['acquisition']={'indices': [37147, 6262, 55612, 59747, 48618, 28902, 17799, 8614, 29320, 16156], 'labels': [7, -1, -1, 5, 9, -1, -1, 2, 1, -1], 'scores': [0.5468488931655884, 0.3301873207092285, 0.3390898108482361, 0.6005156636238098, 0.49223601818084717, 0.44965875148773193, 0.4508312940597534, 0.4767754077911377, 0.627720832824707, 0.38919997215270996]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2112447023391724})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5749310255050659})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.42854154109954834})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38915228843688965})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36452144384384155})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35992223024368286})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38518816232681274})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36854565143585205})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3423372805118561})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3528318703174591})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36380264163017273})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38303399085998535})
store['active_learning_steps'][46]['training']['best_epoch']=9
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9606, 'crossentropy': 0.335311572265625}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6364617347717285})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4536214768886566})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.38257068395614624})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.34672611951828003})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3172723650932312})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.27488982677459717})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.30012160539627075})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.28508704900741577})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2773553729057312})
store['active_learning_steps'][46]['eval_training']['best_epoch']=6
store['active_learning_steps'][46]['acquisition']={'indices': [49947, 1792, 11216, 2148, 1837, 14748, 33356, 20236, 46730, 18473], 'labels': [-1, -1, -1, 6, -1, -1, -1, 4, -1, 4], 'scores': [0.32265782356262207, 0.47667407989501953, 0.5804433822631836, 0.4823123812675476, 0.4686065912246704, 0.3298192024230957, 0.4742109775543213, 0.6294876337051392, 0.5722150802612305, 0.48014992475509644]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 1.0603054761886597})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5935622453689575})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.42314326763153076})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35557737946510315})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3444214463233948})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33692866563796997})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3375851809978485})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3425537347793579})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.38907545804977417})
store['active_learning_steps'][47]['training']['best_epoch']=6
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9608, 'crossentropy': 0.3186590576171875}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6287556886672974})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4551718235015869})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3708321452140808})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3146739900112152})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33498436212539673})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32900622487068176})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2905219495296478})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.28622323274612427})
store['active_learning_steps'][47]['eval_training']['best_epoch']=8
store['active_learning_steps'][47]['acquisition']={'indices': [11410, 35672, 35246, 15068, 42428, 37004, 41573, 20120, 37360, 24056], 'labels': [5, 9, 8, 1, 5, 5, 3, 5, 2, 5], 'scores': [0.58924400806427, 0.2504676580429077, 0.6661332249641418, 0.5501202344894409, 0.6507439017295837, 0.3008961081504822, 0.5660794973373413, 0.7947263121604919, 0.3949936628341675, 0.48113101720809937]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 1.0424952507019043})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5565668344497681})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3914620578289032})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34449803829193115})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36359134316444397})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3269405961036682})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3418123424053192})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3617677688598633})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35231757164001465})
store['active_learning_steps'][48]['training']['best_epoch']=6
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9596, 'crossentropy': 0.3087988037109375}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6649253964424133})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.43632692098617554})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.35247892141342163})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3250013589859009})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2856261134147644})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.28130388259887695})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2923726737499237})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.28097307682037354})
store['active_learning_steps'][48]['eval_training']['best_epoch']=8
store['active_learning_steps'][48]['acquisition']={'indices': [4005, 3056, 3220, 42199, 29132, 48904, 57507, 45917, 26568, 20481], 'labels': [2, 4, 3, 3, 8, -1, 0, 9, -1, -1], 'scores': [0.5824839472770691, 0.5623931288719177, 0.4578440189361572, 0.5435786545276642, 0.49797558784484863, 0.4135453701019287, 0.4558393955230713, 0.560665488243103, 0.5327873826026917, 0.3301911950111389]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0984166860580444})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.47399967908859253})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4109463691711426})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35512590408325195})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3481214940547943})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3222103416919708})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33368995785713196})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33674538135528564})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39204663038253784})
store['active_learning_steps'][49]['training']['best_epoch']=6
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9615, 'crossentropy': 0.308707177734375}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6705677509307861})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4367217421531677})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.36609262228012085})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3344029188156128})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3365459740161896})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3138251304626465})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.27101653814315796})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.27841341495513916})
store['active_learning_steps'][49]['eval_training']['best_epoch']=7
store['active_learning_steps'][49]['acquisition']={'indices': [47652, 22293, 454, 42744, 48078, 47936, 45024, 45944, 16777, 27540], 'labels': [-1, -1, -1, -1, -1, 8, 5, 9, 0, -1], 'scores': [0.44029009342193604, 0.5160378217697144, 0.42951029539108276, 0.5746709108352661, 0.2942034602165222, 0.5675521492958069, 0.5262916684150696, 0.5019505620002747, 0.5326907634735107, 0.6395882964134216]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.2899539470672607})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5822564363479614})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4462849497795105})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.39499709010124207})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40765076875686646})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3566683530807495})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36198437213897705})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3762097954750061})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3573598861694336})
store['active_learning_steps'][50]['training']['best_epoch']=6
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9612, 'crossentropy': 0.3189691162109375}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5923409461975098})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4070986211299896})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.37394076585769653})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3294341564178467})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.33024683594703674})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29503563046455383})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3381103277206421})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29391634464263916})
store['active_learning_steps'][50]['eval_training']['best_epoch']=8
store['active_learning_steps'][50]['acquisition']={'indices': [12302, 52024, 55318, 36809, 46143, 20511, 54908, 5967, 18589, 25964], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 4, -1], 'scores': [0.6129515171051025, 0.45339465141296387, 0.29865968227386475, 0.4598994851112366, 0.4850045442581177, 0.386241614818573, 0.43987011909484863, 0.37134361267089844, 0.3612159788608551, 0.407179594039917]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.2448530197143555})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5755463242530823})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40700697898864746})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36003056168556213})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3542061746120453})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33615297079086304})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3435582220554352})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31889182329177856})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31650203466415405})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34518128633499146})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3507204055786133})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33529290556907654})
store['active_learning_steps'][51]['training']['best_epoch']=9
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9646, 'crossentropy': 0.29773837890625}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6051905751228333})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40142083168029785})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32044386863708496})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3041139245033264})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.294736385345459})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2800979018211365})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26549890637397766})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24332301318645477})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25501465797424316})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.26957279443740845})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.24253657460212708})
store['active_learning_steps'][51]['eval_training']['best_epoch']=11
store['active_learning_steps'][51]['acquisition']={'indices': [42807, 29013, 34032, 29109, 29467, 15771, 19440, 25807, 29966, 34199], 'labels': [-1, -1, -1, -1, -1, 5, -1, -1, 6, -1], 'scores': [0.542013943195343, 0.3887364864349365, 0.46229660511016846, 0.5328659415245056, 0.6688196659088135, 0.5459310412406921, 0.6664026975631714, 0.5673026144504547, 0.6452350616455078, 0.6361539959907532]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.9593234062194824})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48154300451278687})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3739060163497925})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33794134855270386})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3358331620693207})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3523370027542114})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34136587381362915})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3305196166038513})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36838099360466003})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37903931736946106})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33485013246536255})
store['active_learning_steps'][52]['training']['best_epoch']=8
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9653, 'crossentropy': 0.28137421875}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6009577512741089})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.44592446088790894})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3611745238304138})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3123016953468323})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3271181583404541})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3009173274040222})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2630085349082947})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2741539180278778})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.27774861454963684})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2535971999168396})
store['active_learning_steps'][52]['eval_training']['best_epoch']=10
store['active_learning_steps'][52]['acquisition']={'indices': [58952, 35425, 57221, 24836, 39146, 2235, 12544, 36078, 11997, 4082], 'labels': [-1, -1, -1, -1, -1, -1, -1, 3, -1, -1], 'scores': [0.489345908164978, 0.40420931577682495, 0.47211652994155884, 0.32894307374954224, 0.38908350467681885, 0.42034292221069336, 0.4178128242492676, 0.3073941469192505, 0.4327918291091919, 0.4200860261917114]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0317630767822266})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5250005722045898})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.41056007146835327})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.33975017070770264})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3445005416870117})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32380446791648865})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3392282724380493})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32282912731170654})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3397851586341858})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31658294796943665})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34346067905426025})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36695313453674316})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3370044529438019})
store['active_learning_steps'][53]['training']['best_epoch']=10
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9658, 'crossentropy': 0.2863189208984375}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6601821780204773})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.45663177967071533})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37599509954452515})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.34449368715286255})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2537223994731903})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2530462145805359})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2597576379776001})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2652999758720398})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2701328694820404})
store['active_learning_steps'][53]['eval_training']['best_epoch']=6
store['active_learning_steps'][53]['acquisition']={'indices': [864, 23860, 50007, 24394, 57134, 16960, 32164, 28603, 34746, 20150], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 3], 'scores': [0.3461484909057617, 0.22114109992980957, 0.5018678903579712, 0.37263405323028564, 0.5814447999000549, 0.440168559551239, 0.2907942533493042, 0.47310739755630493, 0.5125442743301392, 0.688191294670105]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0710041522979736})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5066019296646118})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3888830542564392})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35161304473876953})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34103167057037354})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3123328387737274})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32931703329086304})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3252864181995392})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3071974515914917})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3553473949432373})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34909677505493164})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.34412914514541626})
store['active_learning_steps'][54]['training']['best_epoch']=9
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9659, 'crossentropy': 0.2905585693359375}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6750051975250244})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.472417414188385})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.35678890347480774})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.307204008102417})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27641695737838745})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27044808864593506})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2867920994758606})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27074286341667175})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2590678930282593})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2404790222644806})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24199391901493073})
store['active_learning_steps'][54]['eval_training']['best_epoch']=10
store['active_learning_steps'][54]['acquisition']={'indices': [59354, 33138, 21816, 11403, 36962, 29494, 18510, 16021, 14722, 50959], 'labels': [1, -1, -1, 0, -1, -1, -1, -1, 0, -1], 'scores': [0.33716142177581787, 0.3783257007598877, 0.46907007694244385, 0.6061736941337585, 0.4970870018005371, 0.4689328074455261, 0.40606653690338135, 0.54430091381073, 0.6255435645580292, 0.506242036819458]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1209403276443481})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5056566596031189})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.419316828250885})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35104644298553467})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3641834855079651})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32845836877822876})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3329802453517914})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30995893478393555})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32926860451698303})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3163914680480957})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34644752740859985})
store['active_learning_steps'][55]['training']['best_epoch']=8
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9643, 'crossentropy': 0.2897315185546875}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6288374066352844})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3837616443634033})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3377683758735657})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.319258451461792})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2765492796897888})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2779085338115692})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2701953649520874})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2924051582813263})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2516973912715912})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25372210144996643})
store['active_learning_steps'][55]['eval_training']['best_epoch']=9
store['active_learning_steps'][55]['acquisition']={'indices': [19081, 40589, 5951, 31389, 28710, 13486, 52568, 14634, 22364, 57523], 'labels': [-1, 2, -1, -1, 8, -1, -1, -1, 0, 3], 'scores': [0.377533495426178, 0.5613073706626892, 0.5417738556861877, 0.6701273322105408, 0.30483371019363403, 0.4411395788192749, 0.4690921902656555, 0.6961507797241211, 0.7379288077354431, 0.6264802813529968]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.094298243522644})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.559170126914978})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4188171625137329})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33066844940185547})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3527759313583374})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32125550508499146})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31979280710220337})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31148195266723633})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33114707469940186})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3376002907752991})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32031840085983276})
store['active_learning_steps'][56]['training']['best_epoch']=8
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9631, 'crossentropy': 0.288514404296875}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6721993088722229})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.386591374874115})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3775143027305603})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3219984173774719})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.32296472787857056})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3056488037109375})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2776910662651062})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3083806037902832})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.25761136412620544})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.264375239610672})
store['active_learning_steps'][56]['eval_training']['best_epoch']=9
store['active_learning_steps'][56]['acquisition']={'indices': [36271, 16571, 10186, 50568, 58588, 35148, 11534, 19362, 39994, 26892], 'labels': [-1, -1, -1, -1, -1, -1, 7, 8, -1, -1], 'scores': [0.37584060430526733, 0.4641357660293579, 0.3369181156158447, 0.5365170240402222, 0.47226250171661377, 0.4358654022216797, 0.7635936737060547, 0.7157465219497681, 0.32936978340148926, 0.44289517402648926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1114604473114014})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6153542995452881})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3829531669616699})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3446201682090759})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3256826400756836})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3322303295135498})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3683922290802002})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3980618119239807})
store['active_learning_steps'][57]['training']['best_epoch']=5
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9548, 'crossentropy': 0.3028533935546875}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6993085145950317})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.44818830490112305})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38344359397888184})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34240686893463135})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3462723195552826})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.33667129278182983})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.28647392988204956})
store['active_learning_steps'][57]['eval_training']['best_epoch']=7
store['active_learning_steps'][57]['acquisition']={'indices': [11474, 13184, 40874, 44865, 13348, 8785, 13366, 393, 26417, 41156], 'labels': [-1, 0, 6, 7, -1, -1, 0, -1, 7, 0], 'scores': [0.3738609552383423, 0.25581488013267517, 0.5105380415916443, 0.47477275133132935, 0.2627115249633789, 0.30806243419647217, 0.4433026909828186, 0.3842155933380127, 0.4581054449081421, 0.5075267553329468]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.1875604391098022})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5826283693313599})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40222102403640747})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36421412229537964})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.39851945638656616})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.34980785846710205})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32107657194137573})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3566439151763916})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36141663789749146})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3603566884994507})
store['active_learning_steps'][58]['training']['best_epoch']=7
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9641, 'crossentropy': 0.2830052490234375}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7422815561294556})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.46050962805747986})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.40552714467048645})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3343093693256378})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.30459702014923096})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3343032896518707})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3036317527294159})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27115994691848755})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.271263062953949})
store['active_learning_steps'][58]['eval_training']['best_epoch']=8
store['active_learning_steps'][58]['acquisition']={'indices': [47982, 10442, 41542, 35933, 7410, 16043, 52135, 32926, 28397, 28641], 'labels': [-1, -1, -1, -1, -1, 0, 0, 8, -1, -1], 'scores': [0.49344098567962646, 0.4039636254310608, 0.47700560092926025, 0.3621460199356079, 0.34862983226776123, 0.5919487476348877, 0.6457321047782898, 0.5480655431747437, 0.5268456935882568, 0.5530134439468384]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9255993366241455})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4982133209705353})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3811432421207428})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3446517586708069})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.326149582862854})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34047049283981323})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30034327507019043})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3149629533290863})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3384925127029419})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31283390522003174})
store['active_learning_steps'][59]['training']['best_epoch']=7
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.964, 'crossentropy': 0.2757326904296875}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6479742527008057})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.42085713148117065})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.33458468317985535})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3423345685005188})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.31509673595428467})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.26677069067955017})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27180612087249756})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.25181326270103455})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27362608909606934})
store['active_learning_steps'][59]['eval_training']['best_epoch']=8
store['active_learning_steps'][59]['acquisition']={'indices': [56655, 26214, 22815, 784, 1422, 35400, 28286, 27455, 44948, 52869], 'labels': [-1, 9, -1, 8, -1, -1, -1, -1, 9, -1], 'scores': [0.35881900787353516, 0.4557981491088867, 0.4429246187210083, 0.5648529529571533, 0.3520370125770569, 0.36926305294036865, 0.2865411043167114, 0.4721285104751587, 0.498052716255188, 0.439200758934021]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.1195192337036133})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5279537439346313})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4180372655391693})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35362765192985535})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34328001737594604})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32872819900512695})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31910860538482666})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31421467661857605})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32642436027526855})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3214082717895508})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31148964166641235})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3257397711277008})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31770962476730347})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3317882716655731})
store['active_learning_steps'][60]['training']['best_epoch']=11
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9653, 'crossentropy': 0.30223076171875}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6772000789642334})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3904600739479065})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3532751798629761})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3129461407661438})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.27646905183792114})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.282281756401062})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2823697328567505})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2423820197582245})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.26807901263237})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.24639445543289185})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.24142223596572876})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.25824809074401855})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24110737442970276})
store['active_learning_steps'][60]['eval_training']['best_epoch']=13
store['active_learning_steps'][60]['acquisition']={'indices': [7082, 47297, 38645, 17831, 11848, 10580, 26226, 5563, 37750, 11784], 'labels': [-1, 8, -1, -1, 0, -1, -1, -1, -1, 6], 'scores': [0.4535314440727234, 0.5232383608818054, 0.4479954242706299, 0.5603650808334351, 0.6398866772651672, 0.5766796469688416, 0.405997633934021, 0.5159385204315186, 0.3925168514251709, 0.44344189763069153]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 1.0659568309783936})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5381296873092651})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36985695362091064})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.32997268438339233})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2997370958328247})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29722753167152405})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33047690987586975})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3141043186187744})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3332516551017761})
store['active_learning_steps'][61]['training']['best_epoch']=6
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9673, 'crossentropy': 0.268314208984375}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6692317724227905})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4637218713760376})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3596062958240509})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31657183170318604})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.289419949054718})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.29443007707595825})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24398338794708252})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2561240792274475})
store['active_learning_steps'][61]['eval_training']['best_epoch']=7
store['active_learning_steps'][61]['acquisition']={'indices': [58796, 6213, 34629, 46029, 15790, 51121, 22071, 23033, 10181, 21077], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 4], 'scores': [0.4840483069419861, 0.2755085229873657, 0.48961329460144043, 0.3072925806045532, 0.33933985233306885, 0.3769676685333252, 0.478272020816803, 0.47383803129196167, 0.5911725163459778, 0.4446668028831482]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0894627571105957})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5261119604110718})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36654382944107056})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3507646322250366})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3367226719856262})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2983280122280121})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.330733060836792})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3099024295806885})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2959175109863281})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36483168601989746})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2947997450828552})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3526049852371216})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32119569182395935})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33451026678085327})
store['active_learning_steps'][62]['training']['best_epoch']=11
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.964, 'crossentropy': 0.27902197265625}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6427102088928223})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4458903670310974})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.34767773747444153})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30008456110954285})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.29300373792648315})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2640790343284607})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.291936993598938})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.26318293809890747})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.257712721824646})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.263711541891098})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.275724321603775})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.25303009152412415})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2525491416454315})
store['active_learning_steps'][62]['eval_training']['best_epoch']=13
store['active_learning_steps'][62]['acquisition']={'indices': [54386, 49982, 41567, 27673, 5938, 24630, 14558, 22083, 4185, 11342], 'labels': [-1, -1, -1, -1, -1, 5, -1, 2, 2, 1], 'scores': [0.49256622791290283, 0.34732139110565186, 0.6626818776130676, 0.4786965847015381, 0.45639216899871826, 0.6563071012496948, 0.42408549785614014, 0.6064692735671997, 0.5416048765182495, 0.45175009965896606]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9230396747589111})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.47586163878440857})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3682563304901123})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3270668685436249})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30669277906417847})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36064451932907104})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2826572060585022})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3449520468711853})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3124070167541504})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2921123504638672})
store['active_learning_steps'][63]['training']['best_epoch']=7
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9652, 'crossentropy': 0.267643896484375}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6251273155212402})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.444266676902771})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3274763822555542})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3377339541912079})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2798324525356293})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29329714179039})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3053673803806305})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.28949445486068726})
store['active_learning_steps'][63]['eval_training']['best_epoch']=5
store['active_learning_steps'][63]['acquisition']={'indices': [44450, 20002, 33529, 15945, 17855, 44777, 27381, 44624, 47220, 7434], 'labels': [-1, -1, -1, 3, 6, -1, -1, 8, 6, 6], 'scores': [0.2633477449417114, 0.45905667543411255, 0.3164088726043701, 0.4188501238822937, 0.5056307315826416, 0.5051400661468506, 0.4434674382209778, 0.42120206356048584, 0.5044823884963989, 0.6442318558692932]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.082582950592041})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5144227147102356})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4041597247123718})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32466739416122437})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29585808515548706})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33359724283218384})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3047312796115875})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34021249413490295})
store['active_learning_steps'][64]['training']['best_epoch']=5
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.965, 'crossentropy': 0.27681953125}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6548616290092468})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4388994574546814})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3762418031692505})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33764511346817017})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.336114764213562})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3130464553833008})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3186390995979309})
store['active_learning_steps'][64]['eval_training']['best_epoch']=6
store['active_learning_steps'][64]['acquisition']={'indices': [8287, 44095, 47309, 3168, 15741, 40233, 43512, 13259, 35196, 27574], 'labels': [9, 2, -1, 8, -1, -1, -1, 1, -1, -1], 'scores': [0.3786795139312744, 0.46750104427337646, 0.3335244655609131, 0.2593719959259033, 0.30241644382476807, 0.38146090507507324, 0.4483603239059448, 0.5632928609848022, 0.43636631965637207, 0.29517221450805664]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0732486248016357})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5444357395172119})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36160480976104736})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3735995590686798})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35618627071380615})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32270339131355286})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3440115749835968})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3004595637321472})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32228922843933105})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3248639702796936})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3289288878440857})
store['active_learning_steps'][65]['training']['best_epoch']=8
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.97, 'crossentropy': 0.2518225341796875}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6505304574966431})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.45625096559524536})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.36261457204818726})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32369792461395264})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.29689034819602966})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31071823835372925})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2714599370956421})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2438688576221466})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2656894624233246})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25836002826690674})
store['active_learning_steps'][65]['eval_training']['best_epoch']=8
store['active_learning_steps'][65]['acquisition']={'indices': [29365, 20335, 48160, 46958, 46189, 53211, 32279, 34683, 9428, 17501], 'labels': [8, -1, -1, 9, -1, -1, -1, 4, 9, 9], 'scores': [0.4057176411151886, 0.5281804800033569, 0.44088202714920044, 0.5276538729667664, 0.3706818222999573, 0.5074151754379272, 0.3043501377105713, 0.35412323474884033, 0.5983335375785828, 0.368777871131897]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.030907154083252})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5399810075759888})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3859361708164215})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3286576271057129})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31436091661453247})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30540117621421814})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.297812819480896})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36344391107559204})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2990422248840332})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3094435930252075})
store['active_learning_steps'][66]['training']['best_epoch']=7
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9664, 'crossentropy': 0.2603111083984375}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6265580654144287})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.41792160272598267})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36496996879577637})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2838945984840393})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2746727764606476})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2943817377090454})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.26233285665512085})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24592986702919006})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.26518455147743225})
store['active_learning_steps'][66]['eval_training']['best_epoch']=8
store['active_learning_steps'][66]['acquisition']={'indices': [29249, 37519, 27833, 41851, 12271, 49978, 42504, 24172, 14040, 40737], 'labels': [-1, -1, -1, -1, -1, -1, 8, -1, -1, -1], 'scores': [0.41542506217956543, 0.4528089761734009, 0.45960307121276855, 0.5359979867935181, 0.5654692649841309, 0.3824838399887085, 0.5696039199829102, 0.4951784014701843, 0.5028253793716431, 0.5020550489425659]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1090583801269531})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5328308343887329})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4053523540496826})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3267208933830261})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29471099376678467})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.308665931224823})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28053906559944153})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30379414558410645})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35170644521713257})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31676554679870605})
store['active_learning_steps'][67]['training']['best_epoch']=7
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9673, 'crossentropy': 0.2652871826171875}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6822018623352051})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.42603474855422974})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3591991662979126})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3458239436149597})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.29654622077941895})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29383784532546997})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3155374526977539})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3011626601219177})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27281856536865234})
store['active_learning_steps'][67]['eval_training']['best_epoch']=9
store['active_learning_steps'][67]['acquisition']={'indices': [42337, 55190, 56643, 9057, 23059, 43606, 50517, 37298, 47140, 4573], 'labels': [5, 3, 2, -1, 1, -1, -1, -1, 3, -1], 'scores': [0.6160072088241577, 0.6950263381004333, 0.555377721786499, 0.3970150947570801, 0.429482102394104, 0.5043989419937134, 0.43961477279663086, 0.41848886013031006, 0.5094153881072998, 0.3777235746383667]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.1873369216918945})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5793585777282715})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.40584439039230347})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3340531587600708})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32343047857284546})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33272451162338257})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3121177554130554})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30691230297088623})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2995441257953644})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31096208095550537})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3338578939437866})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3414924740791321})
store['active_learning_steps'][68]['training']['best_epoch']=9
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9712, 'crossentropy': 0.2560104248046875}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.693642258644104})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4677920639514923})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35543134808540344})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.334338515996933})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30318254232406616})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2962772846221924})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2637428641319275})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28299301862716675})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2603471279144287})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2457345724105835})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23803982138633728})
store['active_learning_steps'][68]['eval_training']['best_epoch']=11
store['active_learning_steps'][68]['acquisition']={'indices': [4557, 9916, 51230, 57510, 4123, 19789, 494, 40688, 37848, 11195], 'labels': [-1, -1, 3, 5, -1, -1, -1, -1, -1, -1], 'scores': [0.44496309757232666, 0.4374735355377197, 0.4318307042121887, 0.6508581638336182, 0.6346070766448975, 0.5335628986358643, 0.4084049463272095, 0.5380251407623291, 0.36546194553375244, 0.4393578767776489]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0723789930343628})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.5153230428695679})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3683924674987793})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3316192924976349})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33246558904647827})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30104801058769226})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29145103693008423})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3125823438167572})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2938840687274933})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30732429027557373})
store['active_learning_steps'][69]['training']['best_epoch']=7
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9662, 'crossentropy': 0.265433251953125}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6998881697654724})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5092552304267883})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3877037763595581})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35186195373535156})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3428986370563507})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3018486499786377})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.28444772958755493})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.28587183356285095})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28286439180374146})
store['active_learning_steps'][69]['eval_training']['best_epoch']=9
store['active_learning_steps'][69]['acquisition']={'indices': [8207, 35983, 54085, 6487, 10310, 32665, 2648, 57414, 9023, 16701], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4383198022842407, 0.4316256046295166, 0.39850008487701416, 0.3327016830444336, 0.4921952486038208, 0.37618714570999146, 0.4782300591468811, 0.4452723264694214, 0.36477774381637573, 0.4892842173576355]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 1.083209753036499})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5499610304832458})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38709914684295654})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33942651748657227})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3132689893245697})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30488598346710205})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28546521067619324})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31328660249710083})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27267971634864807})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31016671657562256})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26496896147727966})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.299324631690979})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30522194504737854})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3031996488571167})
store['active_learning_steps'][70]['training']['best_epoch']=11
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9707, 'crossentropy': 0.2508220947265625}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6624178886413574})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4505004584789276})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3520164489746094})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3117220997810364})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2618735432624817})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.279563307762146})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2733868956565857})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26202821731567383})
store['active_learning_steps'][70]['eval_training']['best_epoch']=5
store['active_learning_steps'][70]['acquisition']={'indices': [26651, 34665, 23325, 52653, 4735, 26733, 31572, 55778, 56375, 35477], 'labels': [-1, 9, -1, -1, -1, 2, -1, -1, -1, -1], 'scores': [0.4623851776123047, 0.6928211450576782, 0.4104650020599365, 0.48634445667266846, 0.47695451974868774, 0.6353763341903687, 0.5105201601982117, 0.5254206657409668, 0.5828765034675598, 0.35581690073013306]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.1487233638763428})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5468326807022095})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3458573520183563})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.321475088596344})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3097575008869171})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2982576787471771})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28959181904792786})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29080119729042053})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2757532596588135})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30463773012161255})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3211291432380676})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3019290864467621})
store['active_learning_steps'][71]['training']['best_epoch']=9
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9702, 'crossentropy': 0.2495736328125}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7011841535568237})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4416852593421936})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34853971004486084})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3010689616203308})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2819678783416748})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2686847448348999})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25288474559783936})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2628748416900635})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.21999457478523254})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24432550370693207})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.24018174409866333})
store['active_learning_steps'][71]['eval_training']['best_epoch']=9
store['active_learning_steps'][71]['acquisition']={'indices': [44299, 28291, 51745, 31516, 27042, 46746, 47463, 11788, 15856, 40679], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.38140350580215454, 0.44544553756713867, 0.36813390254974365, 0.5182332992553711, 0.46527349948883057, 0.4595526456832886, 0.34050095081329346, 0.3697616457939148, 0.5120950937271118, 0.5644219517707825]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0256904363632202})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5968033075332642})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4309529960155487})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3613820970058441})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34364408254623413})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29244571924209595})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3010808229446411})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28968605399131775})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35252389311790466})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32985782623291016})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3398820161819458})
store['active_learning_steps'][72]['training']['best_epoch']=8
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9685, 'crossentropy': 0.2476340087890625}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6436448097229004})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4275262951850891})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36564481258392334})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.33792102336883545})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3067724108695984})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2822030186653137})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.27515506744384766})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2730656862258911})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.24478141963481903})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25568217039108276})
store['active_learning_steps'][72]['eval_training']['best_epoch']=9
store['active_learning_steps'][72]['acquisition']={'indices': [48735, 45974, 17110, 37909, 12320, 30032, 54293, 25803, 11446, 16019], 'labels': [-1, -1, -1, -1, -1, -1, -1, 0, -1, -1], 'scores': [0.5230371952056885, 0.450008749961853, 0.6208582520484924, 0.4870644211769104, 0.4631391763687134, 0.4750370383262634, 0.4049731492996216, 0.3881192207336426, 0.4589172601699829, 0.359572172164917]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.154249668121338})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5828112959861755})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3874204754829407})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35124874114990234})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3252705931663513})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32034188508987427})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33334872126579285})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33100759983062744})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30127397179603577})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30417171120643616})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3482293486595154})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30889570713043213})
store['active_learning_steps'][73]['training']['best_epoch']=9
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9674, 'crossentropy': 0.26571337890625}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6483919620513916})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.40721017122268677})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3787902593612671})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31751060485839844})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2974562644958496})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2690163552761078})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24652138352394104})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2392706722021103})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25118935108184814})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2540993392467499})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26155444979667664})
store['active_learning_steps'][73]['eval_training']['best_epoch']=8
store['active_learning_steps'][73]['acquisition']={'indices': [13195, 59569, 52306, 35807, 6211, 30370, 454, 20232, 8166, 11446], 'labels': [-1, -1, 8, -1, 2, -1, -1, -1, -1, -1], 'scores': [0.4329502582550049, 0.46657121181488037, 0.5455357432365417, 0.3563629984855652, 0.7019691467285156, 0.5072410106658936, 0.43410801887512207, 0.5182262659072876, 0.4271116256713867, 0.46178603172302246]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.1226650476455688})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5500411987304688})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43846237659454346})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3218657970428467})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2991194427013397})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3077061176300049})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31594836711883545})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29388612508773804})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3053504526615143})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3238215744495392})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3515060544013977})
store['active_learning_steps'][74]['training']['best_epoch']=8
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9704, 'crossentropy': 0.2586109375}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6763137578964233})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.43375056982040405})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.34944796562194824})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3219794034957886})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2702704071998596})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25811588764190674})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26434749364852905})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24604138731956482})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.283346951007843})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2306772768497467})
store['active_learning_steps'][74]['eval_training']['best_epoch']=10
store['active_learning_steps'][74]['acquisition']={'indices': [54848, 3072, 49264, 1194, 19370, 27998, 43702, 32878, 46105, 38779], 'labels': [2, 4, 2, -1, -1, -1, 3, 9, -1, -1], 'scores': [0.44297754764556885, 0.5404007434844971, 0.3308447003364563, 0.3242417573928833, 0.23862814903259277, 0.5336518883705139, 0.5055727362632751, 0.34947383403778076, 0.4173163175582886, 0.2883644104003906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.128641128540039})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5960385799407959})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4092308282852173})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3193865716457367})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31814366579055786})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31416767835617065})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2948857545852661})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3267273008823395})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35253971815109253})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34068751335144043})
store['active_learning_steps'][75]['training']['best_epoch']=7
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9696, 'crossentropy': 0.248412841796875}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6657392978668213})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.44826969504356384})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.35681015253067017})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.34996771812438965})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3302904963493347})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.28481972217559814})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2622799277305603})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3018776476383209})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2478312849998474})
store['active_learning_steps'][75]['eval_training']['best_epoch']=9
store['active_learning_steps'][75]['acquisition']={'indices': [39960, 4860, 56375, 7392, 57891, 30868, 50555, 16572, 31182, 28643], 'labels': [-1, 8, -1, -1, -1, -1, -1, 4, -1, -1], 'scores': [0.3596538305282593, 0.566183865070343, 0.47694605588912964, 0.5201266407966614, 0.462718665599823, 0.32605600357055664, 0.45419639348983765, 0.5827617645263672, 0.4403223395347595, 0.41208434104919434]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9962998628616333})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5632550716400146})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3827936053276062})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3258399963378906})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30897951126098633})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29182928800582886})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27837616205215454})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30035921931266785})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3035148084163666})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3210814595222473})
store['active_learning_steps'][76]['training']['best_epoch']=7
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9677, 'crossentropy': 0.2472660888671875}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6522145867347717})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.45125526189804077})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3528444170951843})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3165196180343628})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30807334184646606})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2624586224555969})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2945176959037781})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28743046522140503})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24053986370563507})
store['active_learning_steps'][76]['eval_training']['best_epoch']=9
store['active_learning_steps'][76]['acquisition']={'indices': [44029, 44423, 48916, 4945, 47688, 30463, 26358, 19642, 29891, 21953], 'labels': [-1, -1, -1, 7, -1, -1, 3, 7, -1, -1], 'scores': [0.4715040922164917, 0.387519896030426, 0.625074028968811, 0.4558435082435608, 0.49562495946884155, 0.44971656799316406, 0.6470682621002197, 0.5870089530944824, 0.38971203565597534, 0.39193224906921387]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.269773244857788})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5789538621902466})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4154624342918396})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3330162763595581})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3057217597961426})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3361018896102905})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3210141956806183})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31189030408859253})
store['active_learning_steps'][77]['training']['best_epoch']=5
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.2749718017578125}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6845951080322266})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.46619224548339844})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3781741261482239})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36997556686401367})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2972715198993683})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3173382878303528})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2957236170768738})
store['active_learning_steps'][77]['eval_training']['best_epoch']=7
store['active_learning_steps'][77]['acquisition']={'indices': [52686, 13782, 37696, 32338, 22283, 5554, 48586, 33802, 52942, 18102], 'labels': [5, -1, 2, 1, 9, 6, 5, -1, -1, 0], 'scores': [0.595899224281311, 0.24511778354644775, 0.4656972289085388, 0.45349735021591187, 0.34566396474838257, 0.42131108045578003, 0.46411681175231934, 0.35292232036590576, 0.4610726833343506, 0.49062681198120117]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.1274588108062744})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5399659276008606})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39604538679122925})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3012956380844116})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31653761863708496})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2888018488883972})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26333087682724})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29733461141586304})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30720800161361694})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30399563908576965})
store['active_learning_steps'][78]['training']['best_epoch']=7
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9685, 'crossentropy': 0.262815185546875}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6476432085037231})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4263274669647217})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3628010153770447})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3214980959892273})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2826024293899536})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28148025274276733})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.24596944451332092})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2571748197078705})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24775564670562744})
store['active_learning_steps'][78]['eval_training']['best_epoch']=7
store['active_learning_steps'][78]['acquisition']={'indices': [53980, 44582, 7281, 8617, 37945, 1402, 12689, 33583, 17796, 42503], 'labels': [1, 1, 0, -1, 4, -1, -1, -1, -1, 2], 'scores': [0.5447547435760498, 0.40895378589630127, 0.4113921523094177, 0.49932098388671875, 0.3843287229537964, 0.4061698913574219, 0.5235373973846436, 0.6146185398101807, 0.48589611053466797, 0.5088534355163574]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.2021434307098389})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5932108163833618})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.42604565620422363})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3566496670246124})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3119945526123047})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.292667418718338})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2952214777469635})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3102298974990845})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25848251581192017})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3068239390850067})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27930137515068054})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31150954961776733})
store['active_learning_steps'][79]['training']['best_epoch']=9
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9678, 'crossentropy': 0.2609174560546875}
store['active_learning_steps'][79]['eval_training']={}
store['active_learning_steps'][79]['eval_training']['epochs']=[]
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6436423063278198})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42149657011032104})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35699135065078735})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2870851159095764})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29270094633102417})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2811581492424011})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2707839608192444})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2791637182235718})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26768478751182556})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25649377703666687})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24440139532089233})
store['active_learning_steps'][79]['eval_training']['best_epoch']=11
store['active_learning_steps'][79]['acquisition']={'indices': [41539, 7879, 48857, 35401, 21256, 54911, 47927, 33693, 23684, 58310], 'labels': [-1, 2, -1, 3, -1, 4, -1, -1, -1, -1], 'scores': [0.5723003149032593, 0.43343907594680786, 0.3323667049407959, 0.365567147731781, 0.5002458095550537, 0.4394732117652893, 0.4981513023376465, 0.21757376194000244, 0.3298874497413635, 0.42242640256881714]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0164815187454224})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.46862995624542236})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3856433033943176})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33286958932876587})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.292044997215271})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27377748489379883})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2826542854309082})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2927423417568207})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3034732937812805})
store['active_learning_steps'][80]['training']['best_epoch']=6
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9686, 'crossentropy': 0.2473457763671875}
store['active_learning_steps'][80]['eval_training']={}
store['active_learning_steps'][80]['eval_training']['epochs']=[]
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6639758348464966})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.45208829641342163})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.35505911707878113})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.34529685974121094})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3275855779647827})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2903578281402588})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26395243406295776})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.26079919934272766})
store['active_learning_steps'][80]['eval_training']['best_epoch']=8
store['active_learning_steps'][80]['acquisition']={'indices': [49294, 41850, 12768, 31164, 30535, 37098, 26966, 2761, 45528, 57477], 'labels': [-1, 3, -1, -1, -1, -1, -1, 8, -1, 3], 'scores': [0.4519997835159302, 0.3067144751548767, 0.2834653854370117, 0.2870159149169922, 0.38622796535491943, 0.29196858406066895, 0.3909025192260742, 0.45766681432724, 0.32456016540527344, 0.3784905672073364]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.108978033065796})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5567868947982788})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.4195849895477295})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3304336667060852})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29730984568595886})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2737535238265991})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2877468168735504})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.297787070274353})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28050604462623596})
store['active_learning_steps'][81]['training']['best_epoch']=6
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9708, 'crossentropy': 0.25448388671875}
store['active_learning_steps'][81]['eval_training']={}
store['active_learning_steps'][81]['eval_training']['epochs']=[]
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7230346202850342})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4510743021965027})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3858943581581116})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35132649540901184})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33826613426208496})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.280695378780365})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2836609482765198})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.25625842809677124})
store['active_learning_steps'][81]['eval_training']['best_epoch']=8
store['active_learning_steps'][81]['acquisition']={'indices': [44822, 15869, 54253, 49039, 34833, 21056, 22098, 40463, 54556, 27540], 'labels': [9, -1, -1, -1, -1, -1, -1, -1, 2, -1], 'scores': [0.39664018154144287, 0.4449383020401001, 0.2808511257171631, 0.46892058849334717, 0.42825639247894287, 0.3703708052635193, 0.5400397777557373, 0.34682130813598633, 0.612527072429657, 0.31292420625686646]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.162264108657837})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5369147062301636})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.404397189617157})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3195544183254242})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30002906918525696})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2987373471260071})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3033459782600403})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2806260883808136})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2852858304977417})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2979359030723572})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31485456228256226})
store['active_learning_steps'][82]['training']['best_epoch']=8
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9724, 'crossentropy': 0.239696435546875}
store['active_learning_steps'][82]['eval_training']={}
store['active_learning_steps'][82]['eval_training']['epochs']=[]
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6664371490478516})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.40497612953186035})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3323777914047241})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.30766311287879944})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2797836661338806})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2758012115955353})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.24477073550224304})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2603100836277008})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2609059810638428})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.24240735173225403})
store['active_learning_steps'][82]['eval_training']['best_epoch']=10
store['active_learning_steps'][82]['acquisition']={'indices': [51988, 58014, 2002, 29956, 46758, 38518, 41006, 36647, 45640, 44192], 'labels': [7, 0, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4567514657974243, 0.5199342966079712, 0.549260139465332, 0.4416724443435669, 0.31470537185668945, 0.5387418270111084, 0.34724998474121094, 0.5013562440872192, 0.41423726081848145, 0.5377203226089478]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0598633289337158})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5638311505317688})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38455891609191895})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2957015335559845})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3100074529647827})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27758410573005676})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2899377942085266})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2671990394592285})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26565828919410706})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2645076513290405})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2823765277862549})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27781492471694946})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25831085443496704})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26695775985717773})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2723681330680847})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27388495206832886})
store['active_learning_steps'][83]['training']['best_epoch']=13
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9699, 'crossentropy': 0.24274814453125}
store['active_learning_steps'][83]['eval_training']={}
store['active_learning_steps'][83]['eval_training']['epochs']=[]
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6890578269958496})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.44720131158828735})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3466445803642273})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.2946193218231201})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.29144763946533203})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.26279082894325256})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2485126554965973})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.23867207765579224})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2548482418060303})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.23780634999275208})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.22853213548660278})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23682934045791626})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2269946187734604})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.21239811182022095})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.21040943264961243})
store['active_learning_steps'][83]['eval_training']['best_epoch']=15
store['active_learning_steps'][83]['acquisition']={'indices': [6574, 36408, 38921, 1875, 3643, 53114, 5247, 29501, 39201, 53712], 'labels': [-1, 1, -1, -1, -1, -1, 2, -1, -1, -1], 'scores': [0.6010227203369141, 0.6018711924552917, 0.5076553821563721, 0.4070897102355957, 0.5999168753623962, 0.6646909117698669, 0.4320650100708008, 0.5777291655540466, 0.4932887554168701, 0.38942986726760864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1064093112945557})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5146318674087524})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3856603503227234})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3112894296646118})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29919010400772095})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27632707357406616})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2849861979484558})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26374271512031555})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27492254972457886})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29471874237060547})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28169572353363037})
store['active_learning_steps'][84]['training']['best_epoch']=8
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9726, 'crossentropy': 0.24410263671875}
store['active_learning_steps'][84]['eval_training']={}
store['active_learning_steps'][84]['eval_training']['epochs']=[]
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5595797896385193})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.41214680671691895})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33870255947113037})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.265415221452713})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2711702883243561})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24108171463012695})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24744758009910583})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2301635444164276})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2407720685005188})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24508658051490784})
store['active_learning_steps'][84]['eval_training']['best_epoch']=8
store['active_learning_steps'][84]['acquisition']={'indices': [55419, 53927, 53128, 22044, 34121, 52418, 56048, 17592, 16146, 48340], 'labels': [-1, -1, -1, -1, -1, -1, -1, 4, -1, -1], 'scores': [0.38910961151123047, 0.6124767065048218, 0.3345106840133667, 0.5772685408592224, 0.38593828678131104, 0.5755119919776917, 0.5178126692771912, 0.43919703364372253, 0.36144500970840454, 0.5542724132537842]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.0665034055709839})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5500608682632446})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39761632680892944})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3096033036708832})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29224708676338196})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2856355905532837})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28392544388771057})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27317148447036743})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28611433506011963})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31037265062332153})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26670730113983154})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2892172932624817})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3008505702018738})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30727618932724})
store['active_learning_steps'][85]['training']['best_epoch']=11
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9713, 'crossentropy': 0.2404861083984375}
store['active_learning_steps'][85]['eval_training']={}
store['active_learning_steps'][85]['eval_training']['epochs']=[]
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6549144983291626})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.40654462575912476})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3218122720718384})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30843764543533325})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28106173872947693})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2707674503326416})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26139596104621887})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2630300223827362})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.22155854105949402})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23833473026752472})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.255551278591156})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.23430487513542175})
store['active_learning_steps'][85]['eval_training']['best_epoch']=9
store['active_learning_steps'][85]['acquisition']={'indices': [35952, 16638, 13096, 28639, 2765, 5042, 29200, 18579, 50907, 722], 'labels': [-1, -1, 9, -1, 0, 8, -1, 9, -1, -1], 'scores': [0.453660249710083, 0.4300118684768677, 0.565595805644989, 0.4373455047607422, 0.581652045249939, 0.536954939365387, 0.23070484399795532, 0.4217756390571594, 0.43380308151245117, 0.36072254180908203]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8919963240623474})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5051219463348389})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.37169149518013})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3079874515533447})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2624788284301758})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2645244002342224})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25978317856788635})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27435174584388733})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29974958300590515})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27266180515289307})
store['active_learning_steps'][86]['training']['best_epoch']=7
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9691, 'crossentropy': 0.2430726318359375}
store['active_learning_steps'][86]['eval_training']={}
store['active_learning_steps'][86]['eval_training']['epochs']=[]
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5645807981491089})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4495837688446045})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31243252754211426})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30822640657424927})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30257880687713623})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25826147198677063})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2608484625816345})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2595815658569336})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2522137463092804})
store['active_learning_steps'][86]['eval_training']['best_epoch']=9
store['active_learning_steps'][86]['acquisition']={'indices': [29845, 406, 9118, 4926, 54978, 10455, 1422, 58101, 37267, 41901], 'labels': [-1, -1, 9, -1, -1, -1, -1, 4, -1, -1], 'scores': [0.4765375852584839, 0.5079904794692993, 0.46753114461898804, 0.5074173212051392, 0.440374493598938, 0.5131778120994568, 0.42388081550598145, 0.4750469923019409, 0.4323148727416992, 0.2981516122817993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.2115997076034546})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6167208552360535})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.410478413105011})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31362318992614746})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2973726987838745})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2858922481536865})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30329954624176025})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2818032503128052})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2846262753009796})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27583858370780945})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29496484994888306})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2860907316207886})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27491235733032227})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29226481914520264})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2656601071357727})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.303433358669281})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28953710198402405})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2799699306488037})
store['active_learning_steps'][87]['training']['best_epoch']=15
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9725, 'crossentropy': 0.2432759765625}
store['active_learning_steps'][87]['eval_training']={}
store['active_learning_steps'][87]['eval_training']['epochs']=[]
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6553326845169067})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4722844362258911})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3556750416755676})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2869624197483063})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29399967193603516})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.286676287651062})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2808891236782074})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23906436562538147})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2507645785808563})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23261231184005737})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23086965084075928})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.21310466527938843})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.19862042367458344})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23415672779083252})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.22247517108917236})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.1962972730398178})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.21342891454696655})
store['active_learning_steps'][87]['eval_training']['best_epoch']=16
store['active_learning_steps'][87]['acquisition']={'indices': [41879, 12580, 48304, 51000, 6011, 56249, 46817, 40224, 52858, 16701], 'labels': [-1, 8, -1, -1, -1, -1, -1, 4, -1, -1], 'scores': [0.768611490726471, 0.25747212767601013, 0.49668025970458984, 0.5163772106170654, 0.6203081607818604, 0.683574378490448, 0.5262895226478577, 0.3468499332666397, 0.49989181756973267, 0.7247081398963928]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.1109325885772705})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5905829668045044})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4037362337112427})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3258734941482544})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32986342906951904})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2853463888168335})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28436750173568726})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2934299409389496})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2848246693611145})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2915242314338684})
store['active_learning_steps'][88]['training']['best_epoch']=7
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9684, 'crossentropy': 0.2461198486328125}
store['active_learning_steps'][88]['eval_training']={}
store['active_learning_steps'][88]['eval_training']['epochs']=[]
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7114279270172119})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45136651396751404})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.39455243945121765})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.30703479051589966})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31604138016700745})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.30628472566604614})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.25884753465652466})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2818008363246918})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2762978672981262})
store['active_learning_steps'][88]['eval_training']['best_epoch']=7
store['active_learning_steps'][88]['acquisition']={'indices': [58035, 37964, 40674, 18682, 131, 1422, 4625, 34814, 19752, 57736], 'labels': [-1, -1, -1, 7, -1, -1, 5, -1, -1, -1], 'scores': [0.37891697883605957, 0.4684213399887085, 0.4151585102081299, 0.4388216733932495, 0.45243287086486816, 0.46290910243988037, 0.3449382483959198, 0.4252455234527588, 0.360556960105896, 0.5163127779960632]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.1036250591278076})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5163969397544861})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3641374707221985})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3095568120479584})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2738049626350403})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2738350033760071})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27716049551963806})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2542402744293213})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2791052460670471})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29431524872779846})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2713054418563843})
store['active_learning_steps'][89]['training']['best_epoch']=8
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.241050537109375}
store['active_learning_steps'][89]['eval_training']={}
store['active_learning_steps'][89]['eval_training']['epochs']=[]
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6922972202301025})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.43305835127830505})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36047834157943726})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3223496079444885})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2719981074333191})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26154953241348267})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2630089521408081})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24870893359184265})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25497540831565857})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2380688488483429})
store['active_learning_steps'][89]['eval_training']['best_epoch']=10
store['active_learning_steps'][89]['acquisition']={'indices': [45577, 4050, 44873, 56662, 8280, 42866, 32383, 271, 50732, 3825], 'labels': [-1, -1, -1, 0, 7, 2, -1, -1, -1, -1], 'scores': [0.37784814834594727, 0.5031174421310425, 0.5728432536125183, 0.5266714096069336, 0.2817937582731247, 0.5932179689407349, 0.329623818397522, 0.37910473346710205, 0.3876532316207886, 0.4984734058380127]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1594462394714355})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6052700877189636})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3867843747138977})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3192039132118225})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33832937479019165})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29602986574172974})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25615444779396057})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.29747629165649414})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2770156264305115})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3266063332557678})
store['active_learning_steps'][90]['training']['best_epoch']=7
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.971, 'crossentropy': 0.23357939453125}
store['active_learning_steps'][90]['eval_training']={}
store['active_learning_steps'][90]['eval_training']['epochs']=[]
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7382599711418152})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.43612632155418396})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3515666425228119})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.326604425907135})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27574336528778076})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26678377389907837})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2441907823085785})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24487459659576416})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2637535333633423})
store['active_learning_steps'][90]['eval_training']['best_epoch']=7
store['active_learning_steps'][90]['acquisition']={'indices': [49517, 9646, 38698, 53086, 25117, 36744, 43648, 42366, 43574, 19015], 'labels': [6, 5, 5, -1, -1, 1, 5, 2, 5, 3], 'scores': [0.4250396490097046, 0.33793124556541443, 0.5041987895965576, 0.3651435375213623, 0.33237993717193604, 0.6652423739433289, 0.5283437967300415, 0.4364110231399536, 0.4110769033432007, 0.42464685440063477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.3583333492279053})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5267539024353027})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.43094322085380554})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3441847562789917})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2933834493160248})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2949637770652771})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2927299439907074})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2997608780860901})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27013111114501953})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2934429347515106})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2878589928150177})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2750893235206604})
store['active_learning_steps'][91]['training']['best_epoch']=9
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9709, 'crossentropy': 0.24553408203125}
store['active_learning_steps'][91]['eval_training']={}
store['active_learning_steps'][91]['eval_training']['epochs']=[]
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.73020339012146})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4368963837623596})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33887779712677})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31549838185310364})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.25373077392578125})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26570865511894226})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2486351877450943})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23527726531028748})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.23828914761543274})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2177332192659378})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2239462435245514})
store['active_learning_steps'][91]['eval_training']['best_epoch']=10
store['active_learning_steps'][91]['acquisition']={'indices': [8778, 43633, 54378, 59406, 46579, 13479, 11605, 37270, 43388, 11129], 'labels': [-1, -1, -1, -1, -1, -1, -1, 5, 8, -1], 'scores': [0.5327578783035278, 0.42371833324432373, 0.47628509998321533, 0.4961261749267578, 0.5834696292877197, 0.43364202976226807, 0.5271861553192139, 0.41273215413093567, 0.5115742087364197, 0.36511659622192383]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.2443586587905884})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5681637525558472})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4242788851261139})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3258964419364929})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3173642158508301})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2818656861782074})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27185556292533875})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25871342420578003})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24967235326766968})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2609979510307312})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3021446466445923})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26458868384361267})
store['active_learning_steps'][92]['training']['best_epoch']=9
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9697, 'crossentropy': 0.2240159912109375}
store['active_learning_steps'][92]['eval_training']={}
store['active_learning_steps'][92]['eval_training']['epochs']=[]
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.682142972946167})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.47520962357521057})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3672066330909729})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31115806102752686})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2751072645187378})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2912720739841461})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2400147020816803})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2515774667263031})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.23577874898910522})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2255580723285675})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2198714017868042})
store['active_learning_steps'][92]['eval_training']['best_epoch']=11
store['active_learning_steps'][92]['acquisition']={'indices': [58969, 447, 46046, 1269, 30062, 43823, 9124, 19971, 50957, 4749], 'labels': [-1, -1, -1, -1, -1, 8, -1, -1, -1, 0], 'scores': [0.5356797575950623, 0.35018014907836914, 0.4720282554626465, 0.4902212619781494, 0.6515291929244995, 0.4569268822669983, 0.5268853902816772, 0.5626258850097656, 0.36902904510498047, 0.5654217600822449]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9784209132194519})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4720311164855957})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3605140745639801})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31945425271987915})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2764754295349121})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2651227116584778})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27417755126953125})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24002230167388916})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25230327248573303})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26350826025009155})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.256277471780777})
store['active_learning_steps'][93]['training']['best_epoch']=8
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9708, 'crossentropy': 0.225728369140625}
store['active_learning_steps'][93]['eval_training']={}
store['active_learning_steps'][93]['eval_training']['epochs']=[]
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6377753019332886})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4135023355484009})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3390551805496216})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3132842779159546})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2786686420440674})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25873738527297974})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24061784148216248})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2595245838165283})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27011263370513916})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2536929249763489})
store['active_learning_steps'][93]['eval_training']['best_epoch']=7
store['active_learning_steps'][93]['acquisition']={'indices': [38825, 45916, 23489, 999, 45426, 22098, 52033, 32823, 44649, 28291], 'labels': [2, 4, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.303724467754364, 0.444286048412323, 0.3965108394622803, 0.39044415950775146, 0.39875221252441406, 0.5152097940444946, 0.49774324893951416, 0.4683648347854614, 0.3426104187965393, 0.28287339210510254]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.133340835571289})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5343870520591736})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37214478850364685})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.313515841960907})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2895771861076355})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2754380404949188})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2626379132270813})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2594781219959259})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2524091601371765})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26479092240333557})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27773594856262207})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2557116150856018})
store['active_learning_steps'][94]['training']['best_epoch']=9
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9707, 'crossentropy': 0.22777626953125}
store['active_learning_steps'][94]['eval_training']={}
store['active_learning_steps'][94]['eval_training']['epochs']=[]
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6806300282478333})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4458620250225067})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3302496075630188})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3168960213661194})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30855613946914673})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.27812498807907104})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25497543811798096})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24840566515922546})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24392001330852509})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2336839735507965})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.22157156467437744})
store['active_learning_steps'][94]['eval_training']['best_epoch']=11
store['active_learning_steps'][94]['acquisition']={'indices': [17601, 47949, 35025, 47403, 52272, 8741, 27172, 34228, 44040, 53097], 'labels': [-1, 5, -1, 9, 3, -1, -1, -1, 0, -1], 'scores': [0.45557641983032227, 0.5632349848747253, 0.3386484980583191, 0.5477464199066162, 0.490520179271698, 0.4422439932823181, 0.4276026487350464, 0.23430490493774414, 0.47964176535606384, 0.35139572620391846]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.2193994522094727})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5635852813720703})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4271327555179596})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33950474858283997})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2870727479457855})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2958309054374695})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28477147221565247})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27999967336654663})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2586727738380432})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25477850437164307})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26300156116485596})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2665765583515167})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27398285269737244})
store['active_learning_steps'][95]['training']['best_epoch']=10
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9709, 'crossentropy': 0.2305278564453125}
