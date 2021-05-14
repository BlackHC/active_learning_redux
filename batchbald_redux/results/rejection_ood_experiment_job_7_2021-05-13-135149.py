store = {}
store['timestamp']=1620910309
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=7']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=7
store['worker_id']=7
store['num_workers']=20
store['config']={'seed': 1244, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 1000, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.3093056678771973})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.505469560623169})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.7020537853240967})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.962874412536621})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6836, 'crossentropy': 2.2131701171875}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.1831841468811035})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.129328966140747})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.12550687789917})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [12999, 43083, 35318, 3877, 17404, 35387, 57882, 46073, 21025, 43149], 'labels': [9, 0, 6, 4, 3, -1, 0, 5, 6, 0], 'scores': [0.8101808428764343, 0.9515773057937622, 0.7804517149925232, 0.773766815662384, 0.8494758009910583, 0.603428840637207, 0.843071699142456, 0.7488469481468201, 0.6919006109237671, 0.9675583243370056]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.941810131072998})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.4460408687591553})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.547574043273926})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.435642719268799})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7071, 'crossentropy': 1.7821630859375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1140046119689941})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0765221118927002})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.0610320568084717})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [37762, 32142, 26356, 8569, 30462, 15899, 36387, 52881, 24424, 42079], 'labels': [7, 2, 7, 5, 7, 9, 8, 8, 1, 8], 'scores': [0.7806946635246277, 0.5170996189117432, 0.739230215549469, 0.6207361221313477, 0.5123562216758728, 0.6121625304222107, 0.5765398740768433, 0.6172159314155579, 0.5941528081893921, 0.7069336175918579]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.5653550624847412})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.7411456108093262})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.7859989404678345})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.7978397607803345})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.77, 'crossentropy': 1.39334052734375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 0.9216742515563965})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.8894764184951782})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 0.8833267092704773})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [54603, 59362, 45405, 38714, 30383, 21939, 18674, 37174, 59490, 6364], 'labels': [3, 9, 2, 3, 8, 3, 8, 3, 3, 8], 'scores': [0.8044177889823914, 0.7738887667655945, 0.6503421068191528, 0.5867021679878235, 0.8281084895133972, 0.6802111864089966, 0.8769589066505432, 0.5162002444267273, 0.594691276550293, 0.8360788226127625]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.242884874343872})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.2951912879943848})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.447793960571289})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.4308199882507324})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7922, 'crossentropy': 1.19299150390625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 0.9551866054534912})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 0.8617502450942993})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.8109899163246155})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [35050, 24074, 33150, 21840, 50352, 13181, 41390, 33203, 3114, 32836], 'labels': [0, 6, 8, 9, 5, 3, 5, 2, 8, 2], 'scores': [0.627750039100647, 0.6293225288391113, 0.6241323947906494, 0.7648162841796875, 0.5382887125015259, 0.6827082633972168, 0.6181696057319641, 0.6264164447784424, 0.4516347646713257, 0.7733348608016968]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9665895700454712})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0440568923950195})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1914896965026855})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.2191205024719238})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8095, 'crossentropy': 0.91802783203125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 0.8572126626968384})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.7620581984519958})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.768765926361084})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [54896, 49784, 37392, 51288, 2551, 17513, 44202, 34730, 23546, 16033], 'labels': [8, 5, 4, 4, 5, 7, 8, 0, 5, 2], 'scores': [0.4094669818878174, 0.6391293406486511, 0.41856497526168823, 0.4692201614379883, 0.28457069396972656, 0.46444517374038696, 0.48592305183410645, 0.3739224076271057, 0.5435759425163269, 0.5790493488311768]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9198468923568726})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0017868280410767})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0345972776412964})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.109654188156128})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8325, 'crossentropy': 0.81483037109375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.8483303785324097})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.7584542036056519})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.7335145473480225})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [46126, 18739, 17542, 29121, 22517, 15494, 14649, 16072, 50290, 35156], 'labels': [3, 3, 6, 3, 5, 7, 0, 5, 2, 3], 'scores': [0.4703022837638855, 0.5575141906738281, 0.4069805145263672, 0.5141081213951111, 0.6626995801925659, 0.3721873164176941, 0.6303565502166748, 0.5233089327812195, 0.4630700945854187, 0.48412901163101196]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8864356279373169})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0049020051956177})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0053181648254395})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.049351453781128})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8505, 'crossentropy': 0.8217732421875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8170977234840393})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.7729989290237427})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.7373599410057068})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [15743, 39830, 42384, 8060, 14189, 14063, 3524, 22041, 26434, 21952], 'labels': [3, 1, 8, 9, 8, 2, 6, 9, 2, 2], 'scores': [0.458682656288147, 0.5970669984817505, 0.5155371427536011, 0.5877683162689209, 0.5829951763153076, 0.6165461540222168, 0.45376163721084595, 0.5589714050292969, 0.5230384469032288, 0.42822277545928955]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9138917326927185})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9273771643638611})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0193299055099487})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.9912520051002502})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.837, 'crossentropy': 0.853484375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.9528913497924805})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.8500974178314209})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.7643001079559326})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [52658, 40350, 36921, 52169, 2608, 37536, 19793, 10923, 9315, 35446], 'labels': [4, 5, 1, 2, 4, 7, -1, 4, -1, 7], 'scores': [0.48180246353149414, 0.39319247007369995, 0.2618526220321655, 0.5204465389251709, 0.4816017150878906, 0.42266643047332764, 0.18434131145477295, 0.3836178779602051, 0.33646130561828613, 0.33876800537109375]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.771816611289978})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8492748737335205})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8486768007278442})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8610553741455078})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8747, 'crossentropy': 0.756583984375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8070036768913269})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7319179177284241})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.696628749370575})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [56646, 41409, 48789, 22300, 49121, 39451, 12933, 25192, 16360, 34625], 'labels': [4, 1, 9, 7, 9, 1, 3, 5, 9, 1], 'scores': [0.38512730598449707, 0.3820953369140625, 0.5463510155677795, 0.4619342088699341, 0.32795071601867676, 0.4305933713912964, 0.401645302772522, 0.40951329469680786, 0.4053801894187927, 0.3415912389755249]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7587007880210876})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6245206594467163})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7137948870658875})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7619693875312805})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7917652130126953})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9124, 'crossentropy': 0.53230791015625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6486825942993164})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6111836433410645})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5269796848297119})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.49388742446899414})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [32467, 43434, 42141, 36234, 55481, 21295, 6498, 32693, 25806, 10850], 'labels': [8, 2, 5, 7, 0, 8, 8, 0, 7, 4], 'scores': [0.5160621404647827, 0.4433453679084778, 0.5558927059173584, 0.38481175899505615, 0.47223323583602905, 0.5188785791397095, 0.30849993228912354, 0.5147469639778137, 0.32611697912216187, 0.41297805309295654]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7222681045532227})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5648713111877441})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7085719108581543})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6456671953201294})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6874622702598572})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9202, 'crossentropy': 0.51342109375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.656270444393158})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5127992033958435})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4826328158378601})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4630633592605591})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [3932, 13259, 4369, 40259, 24158, 6636, 27795, 28371, 45380, 4416], 'labels': [-1, 1, -1, 8, 6, 5, 3, 3, -1, 5], 'scores': [0.3907839059829712, 0.36919689178466797, 0.4553772211074829, 0.4279594421386719, 0.3084588348865509, 0.46991515159606934, 0.4518720507621765, 0.5857532620429993, 0.3135284185409546, 0.5123810768127441]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7645066976547241})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5666074752807617})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5573444366455078})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6204158663749695})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6149457097053528})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6314693093299866})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.921, 'crossentropy': 0.499389208984375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5915152430534363})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.48472315073013306})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4336118698120117})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.45174211263656616})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.404537558555603})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [14355, 623, 38038, 19590, 1375, 50676, 22607, 45853, 41357, 32818], 'labels': [2, 6, 5, 5, 1, 2, 4, 0, 0, 2], 'scores': [0.5841581225395203, 0.4954603314399719, 0.5305711030960083, 0.5865592360496521, 0.3422996401786804, 0.4711766242980957, 0.40928220748901367, 0.3007492423057556, 0.5314468145370483, 0.54514479637146]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6843310594558716})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5369734764099121})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6036504507064819})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5997917652130127})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6604059934616089})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9193, 'crossentropy': 0.496148779296875}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6072572469711304})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5444455742835999})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.4872041940689087})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4726954996585846})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [11708, 31088, 33773, 26940, 58445, 760, 28468, 38995, 46828, 26029], 'labels': [3, 9, -1, 6, 8, 3, -1, 9, 9, 1], 'scores': [0.43137407302856445, 0.41662901639938354, 0.4777846336364746, 0.4190410375595093, 0.41146302223205566, 0.4362117052078247, 0.31972575187683105, 0.2710686922073364, 0.5959316492080688, 0.24148941040039062]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7713489532470703})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5772123336791992})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5937174558639526})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6256381273269653})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6685268878936768})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9189, 'crossentropy': 0.52697421875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6600056886672974})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5130959749221802})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.48403000831604004})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.4862278699874878})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [54240, 7833, 47962, 14872, 47484, 56379, 35632, 34406, 14658, 46046], 'labels': [2, 5, 6, 8, 8, 4, 0, 4, -1, -1], 'scores': [0.5519899129867554, 0.6793614625930786, 0.3777458071708679, 0.5354104042053223, 0.45486193895339966, 0.47171342372894287, 0.527118444442749, 0.5467589497566223, 0.4858052730560303, 0.3277982473373413]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7542502880096436})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5907039642333984})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5357435941696167})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5143496990203857})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6347078084945679})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5587016344070435})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6597550511360168})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9326, 'crossentropy': 0.4860123046875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5751566886901855})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4488508999347687})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4128592610359192})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3760497570037842})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.39334964752197266})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3451422452926636})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [42292, 26072, 17631, 46435, 28295, 30704, 49493, 7182, 58633, 23628], 'labels': [7, 1, 5, 9, -1, 9, 8, 8, -1, 6], 'scores': [0.670839250087738, 0.5058374404907227, 0.4286494851112366, 0.5624096095561981, 0.3716946244239807, 0.5765510201454163, 0.6740553975105286, 0.4986184239387512, 0.29745161533355713, 0.4800828695297241]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7917320728302002})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5773853659629822})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5416746139526367})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5738269686698914})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6465234756469727})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5989494919776917})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9299, 'crossentropy': 0.47740498046875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6507371664047241})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4523293375968933})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.42351531982421875})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.40886372327804565})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.38862144947052})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [45733, 23318, 7924, 18656, 576, 7060, 45822, 11518, 58367, 2184], 'labels': [-1, -1, 8, 1, 4, -1, -1, -1, 7, 2], 'scores': [0.31731152534484863, 0.4311727285385132, 0.4623175859451294, 0.4020296335220337, 0.46810758113861084, 0.31810885667800903, 0.5883792638778687, 0.3966869115829468, 0.42489093542099, 0.5540421009063721]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.880986213684082})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5801210403442383})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.55126953125})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5387603640556335})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5226716995239258})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5927854776382446})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5436568260192871})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.637127161026001})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9408, 'crossentropy': 0.433643798828125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6067533493041992})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4968627095222473})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4101417362689972})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3984256386756897})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.38587498664855957})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3825758695602417})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3665398955345154})
store['active_learning_steps'][16]['eval_training']['best_epoch']=7
store['active_learning_steps'][16]['acquisition']={'indices': [5194, 37005, 52814, 48372, 39707, 25770, 2134, 40226, 50960, 6294], 'labels': [-1, 8, 9, 8, -1, -1, 1, -1, -1, -1], 'scores': [0.4559140205383301, 0.4739868640899658, 0.6139914989471436, 0.4516909718513489, 0.5161413550376892, 0.3480929732322693, 0.4813525676727295, 0.45916372537612915, 0.5570917129516602, 0.4089738726615906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8518725633621216})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5445967316627502})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5674049258232117})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5665102005004883})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5870398283004761})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9248, 'crossentropy': 0.473224853515625}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6615501046180725})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5589131116867065})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.4961605668067932})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4334605038166046})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [20641, 34615, 55598, 12650, 28791, 39899, 16473, 42560, 50461, 10492], 'labels': [9, 9, 4, 5, 7, 2, 2, 5, 7, 5], 'scores': [0.3728135824203491, 0.39375606179237366, 0.46347713470458984, 0.5822181105613708, 0.40505141019821167, 0.40121275186538696, 0.6351589560508728, 0.4225694537162781, 0.43203091621398926, 0.2745320796966553]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8371933102607727})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5539951324462891})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5074180364608765})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4980822205543518})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5507165193557739})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5281908512115479})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5637699365615845})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9371, 'crossentropy': 0.411994873046875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6412984132766724})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5325376987457275})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.4402710199356079})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.38815683126449585})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.36913973093032837})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.3658207952976227})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [43796, 1357, 50308, 7721, 39396, 10038, 20709, 38932, 19832, 28984], 'labels': [7, 3, -1, 3, -1, 9, 8, 5, 9, 9], 'scores': [0.4681752920150757, 0.48132044076919556, 0.3504272699356079, 0.36482542753219604, 0.42566919326782227, 0.4927722215652466, 0.5617284178733826, 0.7004231810569763, 0.40674424171447754, 0.44144630432128906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8452188968658447})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.49797797203063965})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5043429136276245})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4733849763870239})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4525073766708374})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4567245841026306})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5117862224578857})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.518412709236145})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.949, 'crossentropy': 0.400820654296875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6154922842979431})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.42387306690216064})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.41211116313934326})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.36947762966156006})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.37367698550224304})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.32351481914520264})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3302963674068451})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [22546, 42799, 3367, 43397, 47447, 1620, 24918, 57383, 37089, 54711], 'labels': [-1, 2, 0, 5, -1, -1, -1, 5, -1, 0], 'scores': [0.6054401397705078, 0.5603094100952148, 0.5286914110183716, 0.4401246905326843, 0.44345855712890625, 0.4084639549255371, 0.5136197805404663, 0.5630899667739868, 0.5713107585906982, 0.4939507246017456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8309726715087891})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5091664791107178})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5018513798713684})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.48547136783599854})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5192925930023193})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5557371973991394})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5326132774353027})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9438, 'crossentropy': 0.41031728515625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6938717365264893})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.4891214668750763})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.43394285440444946})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3473232388496399})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.38632088899612427})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3516271710395813})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [32348, 40704, 25640, 27801, 966, 22436, 24128, 7847, 43702, 24402], 'labels': [5, 5, 9, -1, 3, 0, 5, -1, 3, 5], 'scores': [0.5198038816452026, 0.602306604385376, 0.3895123600959778, 0.3651531934738159, 0.729752242565155, 0.4378642439842224, 0.5041866898536682, 0.5685652494430542, 0.6440922617912292, 0.5566117763519287]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9311526417732239})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.48817136883735657})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.47200363874435425})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49081236124038696})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5505443215370178})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.543818473815918})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9431, 'crossentropy': 0.404865673828125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6472232341766357})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4699326157569885})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.41691356897354126})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.41709959506988525})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.39566949009895325})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [17477, 44179, 33350, 45013, 52914, 2595, 52922, 57624, 30884, 35411], 'labels': [-1, 6, 0, -1, 5, 9, 3, -1, 2, 6], 'scores': [0.34098386764526367, 0.5271361172199249, 0.29746198654174805, 0.3978993892669678, 0.47568368911743164, 0.43474483489990234, 0.5675453543663025, 0.41028445959091187, 0.7336559295654297, 0.4205527901649475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7336714267730713})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.566103458404541})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.491840124130249})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.49301451444625854})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5069581270217896})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5169739723205566})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9412, 'crossentropy': 0.408374755859375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6604636907577515})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4982417821884155})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4380108118057251})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.41854554414749146})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.397641658782959})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [36282, 18031, 49889, 14697, 26034, 39363, 52892, 17362, 9876, 9120], 'labels': [9, 4, 0, 8, 5, 0, 8, 8, 9, -1], 'scores': [0.5069906711578369, 0.4939107894897461, 0.5743966102600098, 0.4913322925567627, 0.5790601968765259, 0.5201515555381775, 0.5545479655265808, 0.6615472435951233, 0.4292457699775696, 0.3643535375595093]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7987338304519653})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.47763392329216003})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5038831233978271})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4677351713180542})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5411226749420166})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4700011909008026})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5797431468963623})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9466, 'crossentropy': 0.39518369140625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5948185920715332})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4345598816871643})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4099021553993225})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3813154995441437})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3582194745540619})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3627309799194336})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [51075, 30723, 19244, 41233, 46888, 39913, 34301, 41832, 9727, 20538], 'labels': [-1, -1, 9, 3, 7, 7, -1, 2, 2, 3], 'scores': [0.5666036605834961, 0.48349058628082275, 0.7829618453979492, 0.564358115196228, 0.5251924991607666, 0.39181751012802124, 0.3029782772064209, 0.5622796416282654, 0.6193732619285583, 0.574176013469696]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8295908570289612})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5068067908287048})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.48079025745391846})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43564313650131226})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4664537310600281})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.528899073600769})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5269695520401001})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9478, 'crossentropy': 0.375797607421875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6161672472953796})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4688873291015625})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.41504400968551636})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.40187904238700867})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3567197918891907})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.34420979022979736})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [30235, 36421, 37449, 8221, 34520, 52722, 48752, 31552, 50443, 30523], 'labels': [-1, 3, -1, 8, 6, 8, 8, 4, -1, 8], 'scores': [0.32253098487854004, 0.4075806140899658, 0.4196223020553589, 0.40455251932144165, 0.7480366826057434, 0.522292971611023, 0.5192441344261169, 0.3136332631111145, 0.3789263963699341, 0.4502982497215271]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.9519512057304382})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.50472092628479})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4445512890815735})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48235151171684265})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4313862919807434})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4771522283554077})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5247441530227661})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5292178988456726})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9515, 'crossentropy': 0.378266552734375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5976554155349731})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.47316503524780273})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.42177289724349976})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.385503351688385})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.34312137961387634})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3510919213294983})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3046172857284546})
store['active_learning_steps'][25]['eval_training']['best_epoch']=7
store['active_learning_steps'][25]['acquisition']={'indices': [55488, 12253, 17553, 39668, 13551, 57677, 7768, 48880, 52478, 41615], 'labels': [3, 7, 3, 8, 5, -1, 8, 4, 9, 7], 'scores': [0.6609661877155304, 0.5382383763790131, 0.5413861274719238, 0.7525789141654968, 0.42384183406829834, 0.6263928413391113, 0.6217222809791565, 0.5173385739326477, 0.5675288438796997, 0.4854269027709961]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8509026169776917})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4914398789405823})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4279123842716217})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40127575397491455})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40940865874290466})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.44718849658966064})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.44040900468826294})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9528, 'crossentropy': 0.3455629150390625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6285616159439087})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.42098474502563477})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4253966212272644})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.36514896154403687})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.35428377985954285})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.34128689765930176})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [10126, 43878, 45784, 32519, 58429, 5346, 7438, 30448, 17010, 109], 'labels': [-1, 2, 9, 5, 2, -1, 7, -1, 3, 2], 'scores': [0.39312875270843506, 0.27487051486968994, 0.5185217261314392, 0.38901036977767944, 0.5139788389205933, 0.42670702934265137, 0.6047296524047852, 0.3062903881072998, 0.4508448839187622, 0.47233355045318604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.907471776008606})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.46149754524230957})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3978783190250397})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4512752294540405})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4019303321838379})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4067477881908417})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9543, 'crossentropy': 0.3738707275390625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6472445726394653})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4623345136642456})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.42522722482681274})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38483595848083496})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3805379271507263})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [21377, 55203, 55639, 27646, 41196, 55778, 5502, 23434, 15781, 4856], 'labels': [-1, -1, 5, 8, 9, -1, -1, 5, 5, -1], 'scores': [0.4367811679840088, 0.3681721091270447, 0.40753018856048584, 0.45867037773132324, 0.39124393463134766, 0.5645431280136108, 0.2960338592529297, 0.5397371053695679, 0.6223549246788025, 0.3803776502609253]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9426612854003906})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.49301883578300476})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4226856231689453})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39381691813468933})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39374202489852905})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4525909423828125})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.44322484731674194})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4992203712463379})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9569, 'crossentropy': 0.330796923828125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6940344572067261})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4236776530742645})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.408999502658844})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.37926602363586426})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.35278284549713135})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32865196466445923})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34444618225097656})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [38566, 19541, 52520, 11984, 6918, 29812, 13442, 54838, 19097, 22555], 'labels': [-1, 8, -1, -1, 9, -1, -1, -1, -1, -1], 'scores': [0.5412409901618958, 0.46668198704719543, 0.44847333431243896, 0.5425739288330078, 0.3415318727493286, 0.6275242567062378, 0.4904215335845947, 0.4786252975463867, 0.5010473728179932, 0.49220454692840576]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0411157608032227})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4833516478538513})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4119931757450104})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3757423758506775})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.41149163246154785})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3714112937450409})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42240047454833984})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4170186221599579})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.41111743450164795})
store['active_learning_steps'][29]['training']['best_epoch']=6
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9611, 'crossentropy': 0.2978235107421875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.575046181678772})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.44204068183898926})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3943486511707306})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3287380337715149})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3169400095939636})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29906558990478516})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.30844587087631226})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2931472063064575})
store['active_learning_steps'][29]['eval_training']['best_epoch']=8
store['active_learning_steps'][29]['acquisition']={'indices': [30257, 2342, 53758, 46068, 35938, 15566, 58134, 40974, 58883, 36048], 'labels': [-1, -1, 3, 3, 7, -1, -1, -1, -1, -1], 'scores': [0.37212133407592773, 0.4941171407699585, 0.6724842190742493, 0.5142055153846741, 0.3168902099132538, 0.3805210590362549, 0.585057258605957, 0.3649441599845886, 0.2686244249343872, 0.37864553928375244]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9512938261032104})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5319796800613403})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.414351224899292})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.410778284072876})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4503994584083557})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4671558141708374})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.43541955947875977})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9521, 'crossentropy': 0.353864013671875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6482459306716919})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4929634928703308})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.42259901762008667})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.34653377532958984})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.36476320028305054})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.35398203134536743})
store['active_learning_steps'][30]['eval_training']['best_epoch']=4
store['active_learning_steps'][30]['acquisition']={'indices': [54913, 9630, 12206, 32435, 57926, 16396, 18294, 42193, 25799, 53464], 'labels': [-1, -1, 7, -1, -1, -1, -1, -1, 8, -1], 'scores': [0.2809199094772339, 0.31866955757141113, 0.42469626665115356, 0.4041128158569336, 0.35815346240997314, 0.37180638313293457, 0.27680468559265137, 0.2482600212097168, 0.3086797595024109, 0.28047800064086914]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 1.0160183906555176})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5263547897338867})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.431927353143692})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.39814841747283936})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3917153477668762})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42355746030807495})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49531835317611694})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5145255923271179})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9574, 'crossentropy': 0.352766357421875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.583026647567749})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4286940097808838})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.36523377895355225})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.38438141345977783})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.34533101320266724})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.37254947423934937})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3137900233268738})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [11600, 29206, 1160, 47873, 34306, 26733, 3290, 21335, 9633, 3691], 'labels': [-1, 4, 4, -1, -1, 2, 4, 7, 9, 0], 'scores': [0.5038454532623291, 0.4911549687385559, 0.5789231657981873, 0.4365677833557129, 0.34668469429016113, 0.5574159026145935, 0.5066509246826172, 0.44693440198898315, 0.40339529514312744, 0.5556240677833557]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1184804439544678})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5092583894729614})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4327007532119751})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.417732834815979})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4476512372493744})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37870872020721436})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.43121224641799927})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.46038761734962463})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4356720447540283})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9583, 'crossentropy': 0.318894482421875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7212545871734619})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.463834285736084})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.41012775897979736})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3350718021392822})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3218286633491516})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3559005856513977})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.29455646872520447})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2863452434539795})
store['active_learning_steps'][32]['eval_training']['best_epoch']=8
store['active_learning_steps'][32]['acquisition']={'indices': [14801, 8754, 18598, 224, 37512, 31264, 24716, 17719, 51176, 58709], 'labels': [6, -1, 9, 1, -1, 1, 5, -1, 5, 8], 'scores': [0.2571273446083069, 0.32337915897369385, 0.6059550642967224, 0.41707682609558105, 0.38400912284851074, 0.44851958751678467, 0.5637628436088562, 0.198644757270813, 0.4361870288848877, 0.3093035817146301]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.0933785438537598})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5189231038093567})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41552314162254333})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4034404158592224})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.41201484203338623})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.42701053619384766})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.41535305976867676})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9589, 'crossentropy': 0.329689013671875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5854278802871704})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4542422890663147})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3930245637893677})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3696536719799042})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35124239325523376})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3255859911441803})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [26470, 52115, 26338, 34756, 22991, 22083, 49893, 57221, 50443, 53912], 'labels': [6, 8, 0, 4, 4, 2, 3, -1, -1, 4], 'scores': [0.4398384690284729, 0.4483165740966797, 0.5234208106994629, 0.43842649459838867, 0.393041729927063, 0.5607618093490601, 0.527405858039856, 0.5236954689025879, 0.4208611249923706, 0.5781598091125488]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9846318960189819})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.49474483728408813})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.37240171432495117})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.374802827835083})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3494648039340973})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3720259666442871})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40107792615890503})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38779217004776})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9656, 'crossentropy': 0.3015794189453125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6131191253662109})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.45188888907432556})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37435832619667053})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3445473313331604})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32502448558807373})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.31638211011886597})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.276846319437027})
store['active_learning_steps'][34]['eval_training']['best_epoch']=7
store['active_learning_steps'][34]['acquisition']={'indices': [48204, 23886, 30460, 22972, 10778, 46626, 38590, 51027, 28507, 43939], 'labels': [-1, 1, -1, -1, -1, 6, -1, -1, -1, -1], 'scores': [0.43768107891082764, 0.5908373594284058, 0.46662068367004395, 0.46978455781936646, 0.6070208549499512, 0.26014795899391174, 0.48333466053009033, 0.4550725221633911, 0.36430346965789795, 0.3872511386871338]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.910595178604126})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4987790584564209})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4122120141983032})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3665474057197571})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36354193091392517})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3767361342906952})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3743138313293457})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3908378779888153})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9617, 'crossentropy': 0.300177001953125}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6556553244590759})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.43937909603118896})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36584383249282837})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35674017667770386})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3178201913833618})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3458942174911499})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31530308723449707})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [59477, 17472, 53300, 28110, 8814, 34199, 57853, 54195, 34763, 25139], 'labels': [-1, 1, 4, -1, -1, -1, -1, 8, -1, -1], 'scores': [0.43597936630249023, 0.36706823110580444, 0.41524606943130493, 0.48392027616500854, 0.42941439151763916, 0.48295140266418457, 0.3747354745864868, 0.4604400396347046, 0.349148154258728, 0.3141673803329468]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8840255737304688})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4445965886116028})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.42496779561042786})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3500741422176361})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.40846651792526245})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3356166481971741})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3702235817909241})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.37644433975219727})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.36054307222366333})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9648, 'crossentropy': 0.283738671875}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.601211667060852})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.42460888624191284})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38377344608306885})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3475898504257202})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3015784025192261})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29135966300964355})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.2875717878341675})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29337078332901})
store['active_learning_steps'][36]['eval_training']['best_epoch']=7
store['active_learning_steps'][36]['acquisition']={'indices': [1737, 55818, 24425, 34879, 4019, 28366, 622, 49206, 24927, 11323], 'labels': [-1, -1, -1, -1, -1, -1, 5, -1, -1, -1], 'scores': [0.3820648193359375, 0.4118680953979492, 0.48975223302841187, 0.5426673889160156, 0.5284990072250366, 0.37437903881073, 0.48778605461120605, 0.35980504751205444, 0.3989598751068115, 0.37324321269989014]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.9728223085403442})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5258309841156006})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.43206697702407837})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4064894914627075})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.42542141675949097})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4043331742286682})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41652488708496094})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4009915292263031})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.404655396938324})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.389987051486969})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4093114733695984})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4427843689918518})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5197734236717224})
store['active_learning_steps'][37]['training']['best_epoch']=10
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9614, 'crossentropy': 0.3376323974609375}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5869477987289429})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4145570993423462})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3820365071296692})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3324112892150879})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3399222195148468})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.30376729369163513})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3079959750175476})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.26669102907180786})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.28341144323349})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.28147271275520325})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.26934635639190674})
store['active_learning_steps'][37]['eval_training']['best_epoch']=8
store['active_learning_steps'][37]['acquisition']={'indices': [32612, 48616, 3082, 17096, 24123, 9768, 5555, 47570, 24983, 8434], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 9, -1], 'scores': [0.536965012550354, 0.6543177366256714, 0.5261056423187256, 0.5698310136795044, 0.5502820611000061, 0.528472363948822, 0.5404977798461914, 0.5264866948127747, 0.46094781160354614, 0.5500580072402954]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8573629856109619})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.47938504815101624})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3514416217803955})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3623458445072174})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.336648166179657})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36127275228500366})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3634234070777893})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3803030848503113})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9631, 'crossentropy': 0.2994243896484375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6316419839859009})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4265977144241333})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35214775800704956})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36024022102355957})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.297166109085083})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30953919887542725})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2816699147224426})
store['active_learning_steps'][38]['eval_training']['best_epoch']=7
store['active_learning_steps'][38]['acquisition']={'indices': [4503, 4058, 47926, 10772, 53231, 30109, 45056, 15894, 36761, 3933], 'labels': [-1, 8, 8, 9, -1, 7, 8, 9, -1, -1], 'scores': [0.4544004201889038, 0.5859320163726807, 0.40098443627357483, 0.4371979236602783, 0.46084272861480713, 0.3585699200630188, 0.7128333449363708, 0.4315844774246216, 0.42916321754455566, 0.5119612216949463]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9504737854003906})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.49177929759025574})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35508713126182556})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36273032426834106})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3208898901939392})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33368444442749023})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34334784746170044})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3397793173789978})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9649, 'crossentropy': 0.27494267578125}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.640512228012085})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.42886072397232056})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.32921135425567627})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2998396158218384})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.30741065740585327})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2980939745903015})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2854900360107422})
store['active_learning_steps'][39]['eval_training']['best_epoch']=7
store['active_learning_steps'][39]['acquisition']={'indices': [27490, 27444, 26826, 4139, 14579, 48460, 25008, 49890, 55244, 22991], 'labels': [2, -1, 7, 8, 9, 2, 8, 5, -1, -1], 'scores': [0.4393923580646515, 0.4598191976547241, 0.27570414543151855, 0.3342207670211792, 0.43941062688827515, 0.5199243426322937, 0.4463801980018616, 0.6184829473495483, 0.5633023977279663, 0.4862617254257202]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.056525707244873})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4801950752735138})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38876670598983765})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37117934226989746})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3444529175758362})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3453282415866852})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35945451259613037})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3335968255996704})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3476647138595581})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34412798285484314})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3518329858779907})
store['active_learning_steps'][40]['training']['best_epoch']=8
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.966, 'crossentropy': 0.291519482421875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6262705326080322})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4331037402153015})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.35912826657295227})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.34209999442100525})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.28516802191734314})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3166663348674774})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.262653112411499})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2676745057106018})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2671050429344177})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2709604501724243})
store['active_learning_steps'][40]['eval_training']['best_epoch']=7
store['active_learning_steps'][40]['acquisition']={'indices': [30474, 39355, 42929, 30134, 54828, 13969, 22814, 55804, 55545, 20635], 'labels': [6, 8, -1, -1, -1, 3, -1, 5, 2, -1], 'scores': [0.6297473311424255, 0.24051699042320251, 0.36307013034820557, 0.527940034866333, 0.4790409803390503, 0.6673623919487, 0.35228753089904785, 0.46782559156417847, 0.3844074606895447, 0.3749152421951294]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9753497242927551})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5261361002922058})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.41523754596710205})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39806801080703735})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.381008118391037})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3713965117931366})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36955639719963074})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36451148986816406})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3703621029853821})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3893848955631256})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3412685990333557})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3860226273536682})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4167013168334961})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40518951416015625})
store['active_learning_steps'][41]['training']['best_epoch']=11
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9655, 'crossentropy': 0.3152578125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6201609373092651})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.42540013790130615})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.37772923707962036})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.31463921070098877})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.32730185985565186})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27432960271835327})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27726665139198303})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.28634998202323914})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.26178988814353943})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.26458626985549927})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2611076831817627})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25981003046035767})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2421514242887497})
store['active_learning_steps'][41]['eval_training']['best_epoch']=13
store['active_learning_steps'][41]['acquisition']={'indices': [18844, 459, 42607, 52346, 29662, 10179, 23451, 52044, 29052, 846], 'labels': [7, -1, -1, -1, -1, -1, -1, -1, -1, 6], 'scores': [0.4058605432510376, 0.7858352065086365, 0.4816017150878906, 0.46805238723754883, 0.3848416805267334, 0.5969433784484863, 0.5021770596504211, 0.8098683953285217, 0.5708094835281372, 0.6996709704399109]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.024853229522705})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4939873516559601})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3639780282974243})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31138336658477783})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34196001291275024})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3527209162712097})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32908281683921814})
store['active_learning_steps'][42]['training']['best_epoch']=4
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9657, 'crossentropy': 0.304689599609375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6796234846115112})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5075592994689941})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3951987028121948})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36649665236473083})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.36987292766571045})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3709179759025574})
store['active_learning_steps'][42]['eval_training']['best_epoch']=4
store['active_learning_steps'][42]['acquisition']={'indices': [19364, 34516, 20257, 8756, 4642, 39316, 38690, 20683, 29425, 36550], 'labels': [-1, -1, -1, 3, -1, 7, 9, 9, -1, 9], 'scores': [0.25503110885620117, 0.47826099395751953, 0.3355979919433594, 0.35452502965927124, 0.349520206451416, 0.37254852056503296, 0.27322709560394287, 0.27035820484161377, 0.37005746364593506, 0.41117793321609497]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.014883041381836})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5247741937637329})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3661853075027466})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3497610092163086})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31587114930152893})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3100149631500244})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34348630905151367})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33496028184890747})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.380398690700531})
store['active_learning_steps'][43]['training']['best_epoch']=6
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9671, 'crossentropy': 0.2846277587890625}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6381726264953613})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.41199636459350586})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3509589433670044})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29899412393569946})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3237539231777191})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.26624977588653564})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30927783250808716})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2506546080112457})
store['active_learning_steps'][43]['eval_training']['best_epoch']=8
store['active_learning_steps'][43]['acquisition']={'indices': [48948, 42606, 10044, 12834, 52690, 31821, 42658, 51403, 682, 54858], 'labels': [7, 7, 6, 6, 3, -1, 0, -1, -1, 3], 'scores': [0.5785015523433685, 0.48471808433532715, 0.5549827218055725, 0.45511043071746826, 0.3956812620162964, 0.5893999338150024, 0.451736718416214, 0.40306806564331055, 0.4407498836517334, 0.6575974225997925]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0415809154510498})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5332974791526794})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.377357542514801})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34303152561187744})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31643959879875183})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3033243417739868})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29658353328704834})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3128545880317688})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31087014079093933})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.312278151512146})
store['active_learning_steps'][44]['training']['best_epoch']=7
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9676, 'crossentropy': 0.28346796875}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6546260118484497})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.4846550524234772})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34749484062194824})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30833932757377625})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2978188991546631})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27143073081970215})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2862440347671509})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26468610763549805})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2517605423927307})
store['active_learning_steps'][44]['eval_training']['best_epoch']=9
store['active_learning_steps'][44]['acquisition']={'indices': [44649, 32788, 28683, 23714, 23963, 39222, 57408, 13366, 59159, 29555], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5448901057243347, 0.445745587348938, 0.4134962558746338, 0.494204580783844, 0.43131816387176514, 0.35909461975097656, 0.52447509765625, 0.48215174674987793, 0.5208478569984436, 0.6810529232025146]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0476973056793213})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4893188774585724})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3933301866054535})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35859736800193787})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3227245807647705})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31748688220977783})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3135816752910614})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3438355326652527})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3130684494972229})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33737385272979736})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3207865357398987})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3157098591327667})
store['active_learning_steps'][45]['training']['best_epoch']=9
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9641, 'crossentropy': 0.298316162109375}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6965141296386719})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.46125489473342896})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3565220534801483})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.33303219079971313})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28527653217315674})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2920745015144348})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26732897758483887})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.286553293466568})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25754615664482117})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2545425295829773})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2638135850429535})
store['active_learning_steps'][45]['eval_training']['best_epoch']=10
store['active_learning_steps'][45]['acquisition']={'indices': [55058, 47857, 42491, 24216, 34459, 21066, 46588, 20335, 28458, 39355], 'labels': [-1, -1, 2, -1, -1, 0, -1, -1, -1, -1], 'scores': [0.4166821241378784, 0.5312634706497192, 0.4115620255470276, 0.4880681037902832, 0.45723968744277954, 0.36790215969085693, 0.5931423306465149, 0.44450128078460693, 0.4784669280052185, 0.6461936831474304]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 1.0377758741378784})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.480094850063324})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3884795010089874})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3311527967453003})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36501434445381165})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3218989968299866})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3517094850540161})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3355794847011566})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3748084008693695})
store['active_learning_steps'][46]['training']['best_epoch']=6
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9635, 'crossentropy': 0.3212243896484375}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6733843088150024})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4375145435333252})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3864460587501526})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30517786741256714})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3302426338195801})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30053630471229553})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29154497385025024})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2807147204875946})
store['active_learning_steps'][46]['eval_training']['best_epoch']=8
store['active_learning_steps'][46]['acquisition']={'indices': [49082, 20332, 14883, 36064, 59909, 24837, 31065, 13455, 24564, 19852], 'labels': [3, 1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.541979968547821, 0.36603569984436035, 0.5744820833206177, 0.697136640548706, 0.5648196339607239, 0.5024623870849609, 0.49640023708343506, 0.6097201108932495, 0.5404654741287231, 0.5093966722488403]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0213640928268433})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5673556327819824})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3692846894264221})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3427017331123352})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3337910771369934})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.352727472782135})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3166896402835846})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33168572187423706})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30350810289382935})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3152211308479309})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3155423402786255})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36965054273605347})
store['active_learning_steps'][47]['training']['best_epoch']=9
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.297619580078125}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6175379753112793})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4165557622909546})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34823352098464966})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.31569042801856995})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.286898136138916})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28997480869293213})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29649075865745544})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.25400465726852417})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2462569773197174})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2629612684249878})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25596463680267334})
store['active_learning_steps'][47]['eval_training']['best_epoch']=9
store['active_learning_steps'][47]['acquisition']={'indices': [13239, 39936, 53317, 46510, 57560, 14793, 58159, 23055, 17928, 13156], 'labels': [-1, -1, -1, -1, -1, 4, 9, 4, -1, 2], 'scores': [0.5436608791351318, 0.4890340566635132, 0.47110360860824585, 0.504094123840332, 0.5146209001541138, 0.5769950151443481, 0.5418252944946289, 0.3417569696903229, 0.5182369351387024, 0.4843423664569855]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.2596855163574219})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5955997705459595})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4285157322883606})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3497634530067444})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34437960386276245})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3659523129463196})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33615559339523315})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.333513468503952})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33219024538993835})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3313088119029999})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3441096544265747})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.332729697227478})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3448728919029236})
store['active_learning_steps'][48]['training']['best_epoch']=10
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9671, 'crossentropy': 0.306825830078125}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6433556079864502})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4404482841491699})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.36409229040145874})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.32052916288375854})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3228877782821655})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28858259320259094})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2758120894432068})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26348814368247986})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2651571035385132})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25203531980514526})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.22722095251083374})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23494842648506165})
store['active_learning_steps'][48]['eval_training']['best_epoch']=11
store['active_learning_steps'][48]['acquisition']={'indices': [18201, 52458, 18805, 47796, 29340, 46467, 3997, 59465, 39086, 50517], 'labels': [-1, -1, -1, -1, 4, 4, -1, -1, -1, -1], 'scores': [0.47283780574798584, 0.46485835313796997, 0.40178096294403076, 0.5049459934234619, 0.4602222442626953, 0.5151505172252655, 0.4634748697280884, 0.5802602767944336, 0.571164071559906, 0.6429721713066101]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.9079983234405518})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5107817649841309})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3609185218811035})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3523656129837036})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3142615556716919})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30156826972961426})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3016071319580078})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30136263370513916})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29804790019989014})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3013979196548462})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34359538555145264})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3422008156776428})
store['active_learning_steps'][49]['training']['best_epoch']=9
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9685, 'crossentropy': 0.2574463623046875}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.661548912525177})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45116257667541504})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3609071671962738})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31440669298171997})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28601810336112976})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2610089182853699})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2744077742099762})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26506757736206055})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24639828503131866})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24313873052597046})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.21137648820877075})
store['active_learning_steps'][49]['eval_training']['best_epoch']=11
store['active_learning_steps'][49]['acquisition']={'indices': [27883, 54528, 14670, 43483, 26432, 11268, 37733, 43815, 49977, 51733], 'labels': [-1, -1, -1, -1, 5, -1, -1, 2, -1, -1], 'scores': [0.5898735523223877, 0.5426119565963745, 0.48432493209838867, 0.6007212400436401, 0.5048717856407166, 0.46067380905151367, 0.48642122745513916, 0.623294860124588, 0.7089982628822327, 0.5350625514984131]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.0660101175308228})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4698020815849304})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.371661514043808})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3588435649871826})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30121076107025146})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3025352954864502})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2855907380580902})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.27166223526000977})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2953278124332428})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29236918687820435})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2927755117416382})
store['active_learning_steps'][50]['training']['best_epoch']=8
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.968, 'crossentropy': 0.257735498046875}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5775887370109558})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4204585552215576})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.36772069334983826})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.30054327845573425})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26154839992523193})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.278634250164032})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28031402826309204})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2499057501554489})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24241244792938232})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2384539693593979})
store['active_learning_steps'][50]['eval_training']['best_epoch']=10
store['active_learning_steps'][50]['acquisition']={'indices': [58205, 55869, 25799, 42817, 52639, 52516, 26588, 39563, 54654, 30055], 'labels': [-1, -1, -1, -1, -1, 6, 4, -1, 8, -1], 'scores': [0.6071293354034424, 0.5443358421325684, 0.4820787310600281, 0.5627329349517822, 0.5915541648864746, 0.7002731561660767, 0.47340530157089233, 0.7288466691970825, 0.4021907448768616, 0.5530568361282349]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.043591856956482})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.490786075592041})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34507790207862854})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3256192207336426})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31464850902557373})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3245641589164734})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28889286518096924})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3343294858932495})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28140807151794434})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28867626190185547})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33498483896255493})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28736114501953125})
store['active_learning_steps'][51]['training']['best_epoch']=9
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.2556078125}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5702533721923828})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3880443274974823})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.338245153427124})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2733166813850403})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2990107536315918})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25024574995040894})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23779509961605072})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24122333526611328})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.22196726500988007})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.21161387860774994})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23443889617919922})
store['active_learning_steps'][51]['eval_training']['best_epoch']=10
store['active_learning_steps'][51]['acquisition']={'indices': [20369, 58906, 10763, 13511, 59508, 32319, 46038, 32402, 31244, 46437], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.6137843728065491, 0.4499514698982239, 0.6090682744979858, 0.43143439292907715, 0.4455345869064331, 0.4575546979904175, 0.33929187059402466, 0.6310199499130249, 0.3173067569732666, 0.5557304620742798]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.207200288772583})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.48377662897109985})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36245864629745483})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2986820340156555})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29513663053512573})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3314700126647949})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28165799379348755})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29504314064979553})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2844425439834595})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2960164248943329})
store['active_learning_steps'][52]['training']['best_epoch']=7
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9678, 'crossentropy': 0.2689990966796875}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6354504823684692})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.42777517437934875})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3283661901950836})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.28798729181289673})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.28680992126464844})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.271017849445343})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27713802456855774})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2526566982269287})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26594114303588867})
store['active_learning_steps'][52]['eval_training']['best_epoch']=8
store['active_learning_steps'][52]['acquisition']={'indices': [4694, 59303, 2859, 10209, 13948, 49542, 54966, 38246, 20788, 21361], 'labels': [3, 8, 4, 4, 5, -1, 7, 7, 9, 9], 'scores': [0.5923780798912048, 0.6162681579589844, 0.4311560392379761, 0.4771586060523987, 0.39466091990470886, 0.3122856616973877, 0.4718826413154602, 0.6765985488891602, 0.375471830368042, 0.3807944655418396]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.114997148513794})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5225998163223267})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4042908251285553})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.339455783367157})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30808204412460327})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3132897615432739})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3538867235183716})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33455079793930054})
store['active_learning_steps'][53]['training']['best_epoch']=5
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9611, 'crossentropy': 0.2966614013671875}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6779403686523438})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5022841691970825})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.43181610107421875})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3709927797317505})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34412717819213867})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33702903985977173})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3017061948776245})
store['active_learning_steps'][53]['eval_training']['best_epoch']=7
store['active_learning_steps'][53]['acquisition']={'indices': [17344, 19558, 47882, 25220, 48981, 29376, 29093, 54154, 1042, 41378], 'labels': [-1, 9, -1, 2, -1, -1, -1, -1, -1, -1], 'scores': [0.33839309215545654, 0.2839486002922058, 0.49063003063201904, 0.5164216756820679, 0.49145424365997314, 0.7024563550949097, 0.3606327772140503, 0.42399024963378906, 0.3844148516654968, 0.5324642658233643]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0675396919250488})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5450112819671631})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3562666177749634})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3350597023963928})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3284270167350769})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3281360864639282})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3124939501285553})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32811465859413147})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3515312671661377})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35262545943260193})
store['active_learning_steps'][54]['training']['best_epoch']=7
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9661, 'crossentropy': 0.294376611328125}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6174134612083435})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3983098268508911})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3330240845680237})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2902299761772156})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27525851130485535})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26774686574935913})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2767590284347534})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28417855501174927})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2585653066635132})
store['active_learning_steps'][54]['eval_training']['best_epoch']=9
store['active_learning_steps'][54]['acquisition']={'indices': [38050, 55490, 20866, 44364, 56419, 30139, 21130, 48975, 28592, 4919], 'labels': [6, -1, -1, 2, -1, 6, -1, 2, 9, -1], 'scores': [0.6599740386009216, 0.2737826704978943, 0.31697094440460205, 0.4976224899291992, 0.3150317668914795, 0.42266058921813965, 0.30782127380371094, 0.5939066410064697, 0.30417490005493164, 0.327888548374176]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.1090972423553467})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.48137176036834717})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3269428610801697})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29376232624053955})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2977546453475952})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31235718727111816})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30167606472969055})
store['active_learning_steps'][55]['training']['best_epoch']=4
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9636, 'crossentropy': 0.3007363037109375}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6977578997612})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4594501256942749})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.36410099267959595})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.370824933052063})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3688707947731018})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3008885383605957})
store['active_learning_steps'][55]['eval_training']['best_epoch']=6
store['active_learning_steps'][55]['acquisition']={'indices': [10377, 50639, 22561, 10256, 13376, 49872, 50431, 39777, 17299, 13047], 'labels': [-1, 8, 6, 2, 3, -1, 3, 6, -1, 6], 'scores': [0.2025068998336792, 0.4136583209037781, 0.37230384349823, 0.5081632137298584, 0.5043169856071472, 0.3847026824951172, 0.5131439566612244, 0.47365546226501465, 0.5630448460578918, 0.31605589389801025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1156063079833984})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5280920267105103})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.377544105052948})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.318244069814682})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3130941390991211})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30375730991363525})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2821679413318634})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2646755576133728})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3321765959262848})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28233662247657776})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30956894159317017})
store['active_learning_steps'][56]['training']['best_epoch']=8
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9717, 'crossentropy': 0.2638201904296875}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6570348143577576})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4125909209251404})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3483372926712036})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3277260363101959})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32047438621520996})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.25356608629226685})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2619038224220276})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.239478200674057})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.21261030435562134})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2550780475139618})
store['active_learning_steps'][56]['eval_training']['best_epoch']=9
store['active_learning_steps'][56]['acquisition']={'indices': [40128, 40654, 47758, 38252, 23736, 5160, 48793, 37964, 12066, 50038], 'labels': [9, 5, -1, 5, -1, -1, -1, -1, 8, -1], 'scores': [0.426472932100296, 0.5635716319084167, 0.4110780954360962, 0.4098331332206726, 0.4346780776977539, 0.2869389057159424, 0.5533448457717896, 0.5483863353729248, 0.5008407831192017, 0.33819568157196045]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.1273510456085205})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.6036773920059204})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36902374029159546})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31886494159698486})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3206866979598999})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31660425662994385})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2675892412662506})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28978484869003296})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3056700825691223})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29589712619781494})
store['active_learning_steps'][57]['training']['best_epoch']=7
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9714, 'crossentropy': 0.25778359375}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6022557020187378})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.43041086196899414})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3871121406555176})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.31216415762901306})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30081498622894287})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2944926917552948})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26951107382774353})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25407740473747253})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.261539101600647})
store['active_learning_steps'][57]['eval_training']['best_epoch']=8
store['active_learning_steps'][57]['acquisition']={'indices': [19396, 7558, 25091, 34934, 1658, 55739, 11044, 17478, 33529, 50389], 'labels': [5, -1, -1, 7, -1, 5, 4, 4, -1, -1], 'scores': [0.5269494652748108, 0.43952691555023193, 0.32481157779693604, 0.5182785987854004, 0.35206300020217896, 0.511969268321991, 0.416714072227478, 0.49608951807022095, 0.40704071521759033, 0.43996763229370117]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 1.0534456968307495})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.49780651926994324})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39528322219848633})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33332642912864685})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31439462304115295})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3247503340244293})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3496619462966919})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29859912395477295})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31174585223197937})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3168225884437561})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31443721055984497})
store['active_learning_steps'][58]['training']['best_epoch']=8
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9715, 'crossentropy': 0.2541791748046875}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.629601776599884})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.443544864654541})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3430998921394348})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3372840881347656})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30317556858062744})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.280142605304718})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25032269954681396})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24075406789779663})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26951098442077637})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25769010186195374})
store['active_learning_steps'][58]['eval_training']['best_epoch']=8
store['active_learning_steps'][58]['acquisition']={'indices': [25144, 6130, 17620, 18672, 24558, 24733, 42787, 18993, 32513, 58856], 'labels': [-1, 7, 0, -1, 8, 3, 4, -1, 4, -1], 'scores': [0.3620384931564331, 0.5861674547195435, 0.5410236120223999, 0.33462607860565186, 0.6409005522727966, 0.41082727909088135, 0.6308841109275818, 0.311220645904541, 0.6477648615837097, 0.29569709300994873]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.9264271855354309})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4729749858379364})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3714473247528076})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3347165584564209})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2690966725349426})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2921733856201172})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2906815707683563})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28511351346969604})
store['active_learning_steps'][59]['training']['best_epoch']=5
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9698, 'crossentropy': 0.2579160400390625}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6564846038818359})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42558014392852783})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4092509150505066})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.32259124517440796})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31521058082580566})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30045294761657715})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.29811346530914307})
store['active_learning_steps'][59]['eval_training']['best_epoch']=7
store['active_learning_steps'][59]['acquisition']={'indices': [52358, 15984, 36744, 54498, 53188, 26676, 14298, 52418, 20157, 28102], 'labels': [2, -1, 1, -1, -1, -1, -1, -1, -1, 0], 'scores': [0.5185531377792358, 0.4372156858444214, 0.5756094455718994, 0.3489665389060974, 0.3627769947052002, 0.609621524810791, 0.49541962146759033, 0.32657694816589355, 0.38413918018341064, 0.41871947050094604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0820133686065674})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5043197870254517})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3937544822692871})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3438400328159332})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3023563027381897})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3022719621658325})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2883777320384979})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2756451368331909})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3378165662288666})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2781198024749756})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3091934025287628})
store['active_learning_steps'][60]['training']['best_epoch']=8
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9699, 'crossentropy': 0.2414727783203125}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6520509123802185})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.46348363161087036})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3539716601371765})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3142573833465576})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2801303267478943})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2630346119403839})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2635931968688965})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2635679244995117})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.23250505328178406})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.24543055891990662})
store['active_learning_steps'][60]['eval_training']['best_epoch']=9
store['active_learning_steps'][60]['acquisition']={'indices': [3101, 20282, 46731, 51574, 33676, 21647, 5079, 47476, 59468, 36271], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 7, -1], 'scores': [0.46393895149230957, 0.3366098403930664, 0.39727115631103516, 0.23818153142929077, 0.39579880237579346, 0.38292205333709717, 0.34150511026382446, 0.4283598065376282, 0.37660229206085205, 0.4177019000053406]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.1050819158554077})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5701476335525513})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3939359784126282})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3183513283729553})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31892430782318115})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29432550072669983})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30652153491973877})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30755704641342163})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31344762444496155})
store['active_learning_steps'][61]['training']['best_epoch']=6
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.968, 'crossentropy': 0.2542242919921875}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6755962371826172})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44237154722213745})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3601071238517761})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35277894139289856})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3199206590652466})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3080613613128662})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2812482714653015})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2814331352710724})
store['active_learning_steps'][61]['eval_training']['best_epoch']=7
store['active_learning_steps'][61]['acquisition']={'indices': [24479, 57410, 34199, 27238, 47297, 58734, 42337, 57597, 21211, 5740], 'labels': [8, -1, -1, -1, 8, 8, 5, 2, -1, 9], 'scores': [0.5316308736801147, 0.267822265625, 0.4411132335662842, 0.552010178565979, 0.4935184717178345, 0.6037139892578125, 0.5200424790382385, 0.350890576839447, 0.4948960542678833, 0.5045979022979736]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 1.0983760356903076})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4824375510215759})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3570154905319214})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31010374426841736})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30162233114242554})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29535719752311707})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2732681334018707})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29291364550590515})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29814058542251587})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28476712107658386})
store['active_learning_steps'][62]['training']['best_epoch']=7
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9692, 'crossentropy': 0.2582073974609375}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7212331295013428})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.47600480914115906})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.368344783782959})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36555179953575134})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29655778408050537})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2983997166156769})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.261478066444397})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2719910740852356})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28523728251457214})
store['active_learning_steps'][62]['eval_training']['best_epoch']=7
store['active_learning_steps'][62]['acquisition']={'indices': [17796, 14072, 56682, 23008, 57308, 15377, 39877, 44742, 43801, 48831], 'labels': [-1, 6, -1, 8, -1, -1, 7, -1, -1, -1], 'scores': [0.46492570638656616, 0.39182746410369873, 0.4664284586906433, 0.4393543601036072, 0.5026162266731262, 0.31064730882644653, 0.5090986490249634, 0.2525310516357422, 0.40505778789520264, 0.44848597049713135]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.1341922283172607})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5777677297592163})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.41413432359695435})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3353200852870941})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.323306143283844})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2906044125556946})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2603037357330322})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2961234748363495})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3066455125808716})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30953341722488403})
store['active_learning_steps'][63]['training']['best_epoch']=7
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9703, 'crossentropy': 0.266896533203125}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6420900821685791})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4151037335395813})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37402579188346863})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32107388973236084})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28946951031684875})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27943921089172363})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27664387226104736})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2746950387954712})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2664604187011719})
store['active_learning_steps'][63]['eval_training']['best_epoch']=9
store['active_learning_steps'][63]['acquisition']={'indices': [53489, 33385, 14152, 49910, 15261, 47195, 13195, 24014, 3130, 33262], 'labels': [-1, -1, -1, 6, 3, -1, -1, -1, 1, -1], 'scores': [0.34189891815185547, 0.48850488662719727, 0.38754749298095703, 0.5012014508247375, 0.33625346422195435, 0.41792094707489014, 0.5656825304031372, 0.45127296447753906, 0.3591884970664978, 0.29785943031311035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.2459187507629395})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5716723203659058})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.42065006494522095})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3381337523460388})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3039076328277588})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2828248143196106})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3124309182167053})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2906028628349304})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30613842606544495})
store['active_learning_steps'][64]['training']['best_epoch']=6
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9669, 'crossentropy': 0.2792255126953125}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6757165193557739})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4552765488624573})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40702003240585327})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30904433131217957})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34260910749435425})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2627064287662506})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.28663569688796997})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2668333053588867})
store['active_learning_steps'][64]['eval_training']['best_epoch']=6
store['active_learning_steps'][64]['acquisition']={'indices': [53537, 50042, 18104, 44289, 24947, 44382, 50532, 54378, 49892, 16444], 'labels': [-1, -1, -1, -1, -1, 6, -1, -1, 5, 9], 'scores': [0.49399101734161377, 0.6166000366210938, 0.5708138942718506, 0.34755122661590576, 0.5288562774658203, 0.5277234315872192, 0.6090726852416992, 0.6156165599822998, 0.41289693117141724, 0.39216744899749756]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0639930963516235})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5337909460067749})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.44013941287994385})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34722867608070374})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3043094873428345})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31247633695602417})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31052350997924805})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29525136947631836})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2951533794403076})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3043171763420105})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31706178188323975})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3010258078575134})
store['active_learning_steps'][65]['training']['best_epoch']=9
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9674, 'crossentropy': 0.2621197998046875}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.602440357208252})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4074670672416687})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30206042528152466})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3092992305755615})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2668738067150116})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2490874081850052})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2428325116634369})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2637452483177185})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24620625376701355})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24064359068870544})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24253448843955994})
store['active_learning_steps'][65]['eval_training']['best_epoch']=10
store['active_learning_steps'][65]['acquisition']={'indices': [13540, 57660, 44659, 47340, 1153, 11910, 40022, 12545, 12621, 3149], 'labels': [7, -1, -1, 1, -1, -1, 8, -1, 2, -1], 'scores': [0.49192410707473755, 0.5057240724563599, 0.42093729972839355, 0.49881571531295776, 0.576454758644104, 0.44924503564834595, 0.6712753772735596, 0.431962251663208, 0.4451993703842163, 0.4473406672477722]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 1.0290353298187256})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5219494104385376})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.39882391691207886})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29281216859817505})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31882309913635254})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2592542767524719})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2844768762588501})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2863943576812744})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.27776801586151123})
store['active_learning_steps'][66]['training']['best_epoch']=6
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9728, 'crossentropy': 0.246519970703125}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6499858498573303})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.45373469591140747})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33955055475234985})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30429184436798096})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3011009991168976})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29250046610832214})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27023833990097046})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3014944791793823})
store['active_learning_steps'][66]['eval_training']['best_epoch']=7
store['active_learning_steps'][66]['acquisition']={'indices': [25976, 32708, 34199, 27036, 2976, 36195, 27878, 56914, 11808, 29185], 'labels': [-1, -1, -1, -1, -1, -1, -1, 0, -1, 3], 'scores': [0.280362606048584, 0.44335269927978516, 0.4072481393814087, 0.29943734407424927, 0.4291697144508362, 0.43009281158447266, 0.39050984382629395, 0.447068452835083, 0.4057762622833252, 0.4005114734172821]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 1.019775629043579})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5129514336585999})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3303149938583374})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3443529009819031})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2562984824180603})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3128940463066101})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24700528383255005})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2713874578475952})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29862016439437866})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26577773690223694})
store['active_learning_steps'][67]['training']['best_epoch']=7
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9726, 'crossentropy': 0.229754443359375}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7312393188476562})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4169780910015106})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3539685606956482})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.282219260931015})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3123903274536133})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27918297052383423})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2626965045928955})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2742656171321869})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2573065161705017})
store['active_learning_steps'][67]['eval_training']['best_epoch']=9
store['active_learning_steps'][67]['acquisition']={'indices': [30696, 35269, 55092, 21336, 5443, 34483, 33676, 11198, 23140, 19980], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 7, -1], 'scores': [0.4029155969619751, 0.44218504428863525, 0.5483088493347168, 0.5114409923553467, 0.5371517539024353, 0.4128512144088745, 0.5428826808929443, 0.4422541856765747, 0.558567464351654, 0.4591236114501953]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0516008138656616})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.5263964533805847})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.37303513288497925})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3421422839164734})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31666356325149536})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32927027344703674})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2863866686820984})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30365246534347534})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2802807688713074})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3015921711921692})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2990838289260864})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.29167407751083374})
store['active_learning_steps'][68]['training']['best_epoch']=9
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9706, 'crossentropy': 0.2720279541015625}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6217924952507019})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.39204806089401245})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3218725919723511})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31726759672164917})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30973657965660095})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2715137004852295})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2542319595813751})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2827821969985962})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25267353653907776})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.22379927337169647})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26276472210884094})
store['active_learning_steps'][68]['eval_training']['best_epoch']=10
store['active_learning_steps'][68]['acquisition']={'indices': [43092, 53349, 8978, 29360, 48804, 38389, 30322, 23731, 52109, 11749], 'labels': [-1, -1, 2, 8, -1, 7, 8, -1, 2, 8], 'scores': [0.5982319116592407, 0.3905665874481201, 0.5971081554889679, 0.3477221727371216, 0.5164104700088501, 0.4739746153354645, 0.48978787660598755, 0.5872455835342407, 0.5439444184303284, 0.5407108068466187]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.040766716003418})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5243741869926453})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3588254451751709})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2864844799041748})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32997000217437744})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2901496887207031})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2912258505821228})
store['active_learning_steps'][69]['training']['best_epoch']=4
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9688, 'crossentropy': 0.2777560302734375}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6830805540084839})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5076754093170166})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3720138370990753})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3892444968223572})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3705909252166748})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3667110800743103})
store['active_learning_steps'][69]['eval_training']['best_epoch']=6
store['active_learning_steps'][69]['acquisition']={'indices': [1405, 36023, 31345, 9474, 31693, 52407, 40534, 14825, 22363, 49292], 'labels': [1, -1, 3, -1, -1, -1, -1, 3, 5, -1], 'scores': [0.33622628450393677, 0.31403255462646484, 0.3603326082229614, 0.3525080680847168, 0.3116145133972168, 0.3906604051589966, 0.2713054418563843, 0.3809816837310791, 0.24737998843193054, 0.4667614698410034]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.0723779201507568})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.46122249960899353})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.351963609457016})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28123822808265686})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.28871747851371765})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.25620755553245544})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24298633635044098})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.24658271670341492})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2809715270996094})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2421497106552124})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2689248323440552})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2467598021030426})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2548917829990387})
store['active_learning_steps'][70]['training']['best_epoch']=10
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9714, 'crossentropy': 0.2385333251953125}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6640138626098633})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4205736517906189})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3215137720108032})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.31282341480255127})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27713149785995483})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24937552213668823})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2333105206489563})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26461654901504517})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.22459769248962402})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.21887844800949097})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.21786311268806458})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2207891047000885})
store['active_learning_steps'][70]['eval_training']['best_epoch']=11
store['active_learning_steps'][70]['acquisition']={'indices': [54997, 46505, 46230, 23156, 3290, 32744, 48735, 26926, 47895, 46070], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 3], 'scores': [0.5045503377914429, 0.5959609746932983, 0.4683518409729004, 0.41313421726226807, 0.4712008237838745, 0.4559452533721924, 0.4105050563812256, 0.4302147626876831, 0.36227524280548096, 0.5977120399475098]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.1096054315567017})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5231572985649109})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.38451290130615234})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.327494353055954})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2958502769470215})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2611437141895294})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30616962909698486})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28847768902778625})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28270894289016724})
store['active_learning_steps'][71]['training']['best_epoch']=6
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.969, 'crossentropy': 0.273132373046875}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6793951988220215})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4783276319503784})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.39277762174606323})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3565751612186432})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31761884689331055})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3250722587108612})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.296247661113739})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3592568635940552})
store['active_learning_steps'][71]['eval_training']['best_epoch']=7
store['active_learning_steps'][71]['acquisition']={'indices': [18277, 52547, 46917, 39545, 25144, 2597, 16376, 54880, 30776, 58141], 'labels': [-1, -1, -1, -1, -1, -1, 1, 5, 9, -1], 'scores': [0.43795669078826904, 0.2785118818283081, 0.3927652835845947, 0.43711090087890625, 0.3614034652709961, 0.31749236583709717, 0.45968830585479736, 0.3595624566078186, 0.4678674340248108, 0.3485335111618042]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.2344526052474976})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.6001778841018677})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.41840803623199463})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33516812324523926})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28115978837013245})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2971828579902649})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26773539185523987})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2605125904083252})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2781563997268677})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2796492874622345})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2560594081878662})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2995690405368805})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.2605520188808441})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2845962643623352})
store['active_learning_steps'][72]['training']['best_epoch']=11
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9708, 'crossentropy': 0.2438926025390625}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7712429165840149})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.425952672958374})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3582198917865753})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28622013330459595})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2828902006149292})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2946142852306366})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2617114782333374})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24613399803638458})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25635412335395813})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25656530261039734})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2100253850221634})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2175014168024063})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.22917070984840393})
store['active_learning_steps'][72]['eval_training']['best_epoch']=11
store['active_learning_steps'][72]['acquisition']={'indices': [30944, 49451, 7168, 9884, 50959, 35710, 36648, 25236, 52994, 54196], 'labels': [-1, -1, 8, -1, -1, 1, -1, -1, -1, -1], 'scores': [0.479358434677124, 0.35941922664642334, 0.5088204741477966, 0.40836483240127563, 0.4420597553253174, 0.4147232174873352, 0.5164631605148315, 0.38752639293670654, 0.3108510971069336, 0.49147218465805054]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0772298574447632})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5326152443885803})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3793180584907532})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31064754724502563})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27957117557525635})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2940705716609955})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27651047706604004})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2798839509487152})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27224481105804443})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.259662389755249})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26721590757369995})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2535148561000824})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28040337562561035})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2729285955429077})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29474008083343506})
store['active_learning_steps'][73]['training']['best_epoch']=12
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.2572887451171875}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6543083190917969})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.45071691274642944})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3212924003601074})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32211393117904663})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2790569067001343})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2258036732673645})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24928633868694305})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.22324907779693604})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2326011061668396})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2141720950603485})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23968303203582764})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.20994889736175537})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.22779522836208344})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2382502257823944})
store['active_learning_steps'][73]['eval_training']['best_epoch']=12
store['active_learning_steps'][73]['acquisition']={'indices': [50710, 29109, 20976, 19892, 22299, 20744, 55282, 2508, 29193, 14329], 'labels': [9, -1, 5, 5, -1, -1, 4, -1, 4, 0], 'scores': [0.5288246870040894, 0.557073712348938, 0.6631577014923096, 0.5874225795269012, 0.47464120388031006, 0.3949923515319824, 0.44857868552207947, 0.703700065612793, 0.3458632528781891, 0.6020795702934265]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 1.1075866222381592})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.5330262780189514})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3867390751838684})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29760491847991943})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2825210690498352})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2678685188293457})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.28594058752059937})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2588597536087036})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27997416257858276})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2614216208457947})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25135254859924316})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25597459077835083})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2888004183769226})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.28964585065841675})
store['active_learning_steps'][74]['training']['best_epoch']=11
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9711, 'crossentropy': 0.2483694091796875}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6941295266151428})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3831872344017029})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32662254571914673})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3507646322250366})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2637268900871277})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26203805208206177})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2673390507698059})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.21689924597740173})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2191447615623474})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23714055120944977})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.21294452250003815})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25373122096061707})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24210423231124878})
store['active_learning_steps'][74]['eval_training']['best_epoch']=11
store['active_learning_steps'][74]['acquisition']={'indices': [26206, 14904, 33885, 9346, 19362, 25701, 41882, 581, 12564, 15975], 'labels': [5, 4, -1, 9, 8, -1, 8, -1, -1, 5], 'scores': [0.6451457142829895, 0.3279075026512146, 0.47233355045318604, 0.5380536317825317, 0.6671662926673889, 0.5921544432640076, 0.480266809463501, 0.43970727920532227, 0.409778356552124, 0.5246283113956451]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1014747619628906})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5673987865447998})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.38982805609703064})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2891789674758911})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2889227867126465})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.284939706325531})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24998974800109863})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27078351378440857})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28661927580833435})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.29019224643707275})
store['active_learning_steps'][75]['training']['best_epoch']=7
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9699, 'crossentropy': 0.25915517578125}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7297523021697998})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.40663737058639526})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3422587513923645})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3018903136253357})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28205883502960205})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26794737577438354})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2915566563606262})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2598208785057068})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27344009280204773})
store['active_learning_steps'][75]['eval_training']['best_epoch']=8
store['active_learning_steps'][75]['acquisition']={'indices': [41426, 45446, 52926, 58793, 44567, 39308, 26380, 47987, 11628, 33053], 'labels': [4, 7, -1, -1, -1, -1, 9, -1, -1, -1], 'scores': [0.4481881260871887, 0.5539931058883667, 0.4640974998474121, 0.515880823135376, 0.4633694887161255, 0.3675295114517212, 0.25861477851867676, 0.48568010330200195, 0.5001745223999023, 0.3394826650619507]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 1.1859709024429321})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5497804880142212})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3996763527393341})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3498982787132263})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31633874773979187})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29294008016586304})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27094224095344543})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2538611888885498})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2563445270061493})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2616793215274811})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2475716471672058})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2737167477607727})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.253578245639801})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26658526062965393})
store['active_learning_steps'][76]['training']['best_epoch']=11
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9718, 'crossentropy': 0.2438203857421875}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7018542289733887})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4569503366947174})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34016454219818115})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27082374691963196})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2785331904888153})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2745470702648163})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2671525478363037})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2792866826057434})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.23833975195884705})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.22608232498168945})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23017443716526031})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.21470394730567932})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2371216118335724})
store['active_learning_steps'][76]['eval_training']['best_epoch']=12
store['active_learning_steps'][76]['acquisition']={'indices': [29376, 52785, 12088, 8825, 27696, 14341, 57489, 40364, 52798, 52125], 'labels': [-1, -1, -1, -1, 2, -1, -1, -1, -1, -1], 'scores': [0.5704925060272217, 0.43060970306396484, 0.5281937122344971, 0.49255216121673584, 0.3837415874004364, 0.6021678447723389, 0.5592940449714661, 0.5254702568054199, 0.5683565139770508, 0.5473239421844482]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.2912689447402954})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.6113950610160828})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.40085840225219727})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3160468339920044})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26624834537506104})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2840885519981384})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2667681574821472})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.254299521446228})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25916922092437744})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26065531373023987})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2417244017124176})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2532837986946106})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26557883620262146})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2602413594722748})
store['active_learning_steps'][77]['training']['best_epoch']=11
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9709, 'crossentropy': 0.2487466796875}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6441643238067627})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3973747491836548})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3108307421207428})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31478941440582275})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2695358693599701})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2575194835662842})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2268044799566269})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.21385493874549866})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.22718629240989685})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2279711365699768})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.22208109498023987})
store['active_learning_steps'][77]['eval_training']['best_epoch']=8
store['active_learning_steps'][77]['acquisition']={'indices': [39256, 4728, 33423, 15216, 56441, 18140, 24860, 27406, 22567, 7874], 'labels': [-1, -1, -1, -1, -1, -1, 9, 7, -1, -1], 'scores': [0.4738597869873047, 0.47886109352111816, 0.46150386333465576, 0.4993044137954712, 0.5013572573661804, 0.6155483722686768, 0.5819004774093628, 0.5907737016677856, 0.7174948453903198, 0.46782606840133667]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 1.0538530349731445})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4816019535064697})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3702867031097412})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.33683255314826965})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2932553291320801})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25128573179244995})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26077619194984436})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2792658805847168})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.24688851833343506})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2497853934764862})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.232423335313797})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23571991920471191})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25119054317474365})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.2526097297668457})
store['active_learning_steps'][78]['training']['best_epoch']=11
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9736, 'crossentropy': 0.2385904296875}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6784635186195374})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4500071406364441})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3336171507835388})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31260204315185547})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29391229152679443})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24074184894561768})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23028820753097534})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23617325723171234})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.23204204440116882})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.21032315492630005})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.21297623217105865})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.22670915722846985})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2114742249250412})
store['active_learning_steps'][78]['eval_training']['best_epoch']=10
store['active_learning_steps'][78]['acquisition']={'indices': [968, 30062, 13209, 24052, 19430, 6669, 35425, 37021, 48102, 37048], 'labels': [-1, -1, -1, -1, 5, -1, -1, -1, 7, 9], 'scores': [0.4987618923187256, 0.3555736541748047, 0.5004109144210815, 0.5096855163574219, 0.4368801712989807, 0.4557192921638489, 0.3744305968284607, 0.5948346853256226, 0.5435041785240173, 0.6969082951545715]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 1.1028388738632202})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4824146032333374})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34788036346435547})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2861851453781128})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2818237245082855})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2762194573879242})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25459784269332886})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24795323610305786})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2645704448223114})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2580280900001526})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25249791145324707})
store['active_learning_steps'][79]['training']['best_epoch']=8
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9731, 'crossentropy': 0.2326953125}
store['active_learning_steps'][79]['eval_training']={}
store['active_learning_steps'][79]['eval_training']['epochs']=[]
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6293834447860718})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41557055711746216})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3469341993331909})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3117368221282959})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27314049005508423})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25475016236305237})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25097107887268066})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23100009560585022})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2350504994392395})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.21211016178131104})
store['active_learning_steps'][79]['eval_training']['best_epoch']=10
store['active_learning_steps'][79]['acquisition']={'indices': [46368, 11627, 13368, 11504, 25193, 54628, 7058, 55599, 59747, 53897], 'labels': [8, -1, -1, -1, -1, 4, 3, -1, 5, -1], 'scores': [0.4636697769165039, 0.2995753288269043, 0.2463386058807373, 0.24360895156860352, 0.5032082796096802, 0.29700136184692383, 0.3578304648399353, 0.31721031665802, 0.5102154612541199, 0.3569774627685547]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0493664741516113})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.6174989938735962})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3851378858089447})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30090874433517456})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3152756094932556})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28907695412635803})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2483913004398346})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25445401668548584})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25860700011253357})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.22028419375419617})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2543841600418091})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2677035927772522})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28370940685272217})
store['active_learning_steps'][80]['training']['best_epoch']=10
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9735, 'crossentropy': 0.2332630126953125}
store['active_learning_steps'][80]['eval_training']={}
store['active_learning_steps'][80]['eval_training']['epochs']=[]
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6488879919052124})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4003816246986389})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3505537509918213})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30091315507888794})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24115240573883057})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2459157556295395})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.22657358646392822})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2453853189945221})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23564878106117249})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.23163118958473206})
store['active_learning_steps'][80]['eval_training']['best_epoch']=7
store['active_learning_steps'][80]['acquisition']={'indices': [44353, 36048, 38827, 16638, 7851, 23751, 52624, 59111, 33035, 32475], 'labels': [-1, -1, -1, -1, 8, -1, -1, -1, -1, 2], 'scores': [0.2999598979949951, 0.4009469747543335, 0.45174694061279297, 0.45982128381729126, 0.5606606900691986, 0.5252435207366943, 0.3768293857574463, 0.4955188035964966, 0.5055835247039795, 0.49319398403167725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.2722949981689453})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6255324482917786})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.45228201150894165})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3361121416091919})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3101132810115814})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28416985273361206})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28738534450531006})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29292142391204834})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26534825563430786})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25432342290878296})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2935306131839752})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28841012716293335})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26793742179870605})
store['active_learning_steps'][81]['training']['best_epoch']=10
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9708, 'crossentropy': 0.251624755859375}
store['active_learning_steps'][81]['eval_training']={}
store['active_learning_steps'][81]['eval_training']['epochs']=[]
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7019509077072144})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.42201849818229675})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3409345746040344})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3196020722389221})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30718520283699036})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2689640522003174})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.23050367832183838})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.253849595785141})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2671101987361908})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23875828087329865})
store['active_learning_steps'][81]['eval_training']['best_epoch']=7
store['active_learning_steps'][81]['acquisition']={'indices': [47669, 17403, 17046, 34577, 57398, 5841, 24587, 29638, 49573, 59054], 'labels': [-1, -1, -1, -1, 2, 2, 8, -1, 2, -1], 'scores': [0.5425729751586914, 0.43087732791900635, 0.4209260940551758, 0.518212080001831, 0.4672102630138397, 0.23779892921447754, 0.3865833580493927, 0.4161354899406433, 0.5064001679420471, 0.45313966274261475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.305458664894104})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5480503439903259})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4384464919567108})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32352638244628906})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29184359312057495})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2855706810951233})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27843746542930603})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2707918882369995})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.264202356338501})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2818089723587036})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24890942871570587})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2658136487007141})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29992616176605225})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2866910994052887})
store['active_learning_steps'][82]['training']['best_epoch']=11
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9756, 'crossentropy': 0.2359914794921875}
store['active_learning_steps'][82]['eval_training']={}
store['active_learning_steps'][82]['eval_training']['epochs']=[]
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6391290426254272})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4090944528579712})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.340559184551239})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28843826055526733})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23203986883163452})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2697776257991791})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24142268300056458})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.22716712951660156})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.260145366191864})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24019907414913177})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2340969443321228})
store['active_learning_steps'][82]['eval_training']['best_epoch']=8
store['active_learning_steps'][82]['acquisition']={'indices': [52942, 29775, 9547, 12197, 13024, 27357, 36402, 22575, 17494, 37184], 'labels': [-1, -1, -1, -1, -1, -1, 9, -1, 5, -1], 'scores': [0.5994722247123718, 0.4969804286956787, 0.21656739711761475, 0.4525972604751587, 0.5543723106384277, 0.46679913997650146, 0.6949706077575684, 0.5363113284111023, 0.6081681549549103, 0.4798067808151245]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.1115050315856934})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5395487546920776})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33455461263656616})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3030262589454651})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2754283845424652})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2544068992137909})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25698357820510864})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2585785388946533})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2676571011543274})
store['active_learning_steps'][83]['training']['best_epoch']=6
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9694, 'crossentropy': 0.2547697265625}
store['active_learning_steps'][83]['eval_training']={}
store['active_learning_steps'][83]['eval_training']['epochs']=[]
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6078247427940369})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4334605932235718})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3390701413154602})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3228183090686798})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.323017418384552})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30320852994918823})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27319520711898804})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2793925702571869})
store['active_learning_steps'][83]['eval_training']['best_epoch']=7
store['active_learning_steps'][83]['acquisition']={'indices': [8499, 33086, 41617, 8759, 31450, 29193, 10591, 35411, 25405, 13998], 'labels': [-1, -1, 0, -1, 3, -1, -1, -1, -1, 9], 'scores': [0.38571101427078247, 0.5123276710510254, 0.34287768602371216, 0.37952613830566406, 0.3716685175895691, 0.5069054365158081, 0.3476332426071167, 0.44605350494384766, 0.5069825649261475, 0.47944286465644836]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.21059250831604})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5941746234893799})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.45879197120666504})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.362093985080719})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.274513840675354})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2818009853363037})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29253071546554565})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2802444100379944})
store['active_learning_steps'][84]['training']['best_epoch']=5
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9713, 'crossentropy': 0.263232958984375}
store['active_learning_steps'][84]['eval_training']={}
store['active_learning_steps'][84]['eval_training']['epochs']=[]
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7568920254707336})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4727238118648529})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3694232106208801})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3241429328918457})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.320058673620224})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33429449796676636})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3371664881706238})
store['active_learning_steps'][84]['eval_training']['best_epoch']=5
store['active_learning_steps'][84]['acquisition']={'indices': [58491, 22344, 10651, 48393, 31291, 55021, 31357, 27321, 36653, 13840], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 6, -1], 'scores': [0.38335180282592773, 0.4576139450073242, 0.3713850975036621, 0.5190243124961853, 0.4828019142150879, 0.3882543444633484, 0.44889700412750244, 0.44782912731170654, 0.4719986915588379, 0.4859323501586914]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.2950443029403687})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5772552490234375})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.45998233556747437})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3345825970172882})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2929973602294922})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29373663663864136})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2726755738258362})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28476622700691223})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2606596052646637})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2688019275665283})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26681381464004517})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2747167944908142})
store['active_learning_steps'][85]['training']['best_epoch']=9
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9735, 'crossentropy': 0.2354272705078125}
store['active_learning_steps'][85]['eval_training']={}
store['active_learning_steps'][85]['eval_training']['epochs']=[]
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6636683344841003})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.45228564739227295})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3831897974014282})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34451526403427124})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2814561724662781})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2728414237499237})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2648271322250366})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2744814455509186})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24422399699687958})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2391035556793213})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.25806522369384766})
store['active_learning_steps'][85]['eval_training']['best_epoch']=10
store['active_learning_steps'][85]['acquisition']={'indices': [42703, 36648, 23016, 1728, 53887, 29367, 11133, 51939, 5042, 55415], 'labels': [-1, -1, -1, -1, -1, -1, 0, -1, 8, -1], 'scores': [0.55299973487854, 0.6758260130882263, 0.38599449396133423, 0.4232954978942871, 0.24579262733459473, 0.5370864868164062, 0.2530593276023865, 0.6309850215911865, 0.6607707738876343, 0.40162110328674316]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0894081592559814})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.56911301612854})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3720635771751404})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3456546366214752})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3116176128387451})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29224222898483276})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28478944301605225})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2710421681404114})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2521473467350006})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2478184998035431})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27592363953590393})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26278620958328247})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30247193574905396})
store['active_learning_steps'][86]['training']['best_epoch']=10
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9716, 'crossentropy': 0.24551435546875}
