store = {}
store['timestamp']=1620916631
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=17']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=17
store['worker_id']=17
store['num_workers']=20
store['config']={'seed': 1259, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 1000, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.1025757789611816})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.4431161880493164})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.5705442428588867})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.9611449241638184})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.684, 'crossentropy': 1.975050390625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.2216458320617676})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1291499137878418})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.1289119720458984})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [41515, 54673, 8700, 30359, 34437, 28507, 13078, 23228, 59423, 11731], 'labels': [3, 5, 3, 7, 8, 6, 5, 6, 8, 6], 'scores': [0.7925643920898438, 0.725605845451355, 0.8339285850524902, 0.7416131496429443, 0.7199298739433289, 0.8234462141990662, 0.8894441723823547, 0.9505658149719238, 0.6825652122497559, 0.8116886019706726]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.6288456916809082})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.8054804801940918})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.7135025262832642})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.9587229490280151})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7379, 'crossentropy': 1.4527564453125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 0.9291744232177734})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9257089495658875})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 0.8704893589019775})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [11572, 31301, 9703, 33047, 49475, 50429, 50821, 49926, 25262, 626], 'labels': [5, -1, 0, 2, 2, 8, 8, 3, 8, 9], 'scores': [0.4685894250869751, 0.4356083869934082, 0.6296573877334595, 0.6593844890594482, 0.7052221298217773, 0.5543453693389893, 0.5854328870773315, 0.7037631273269653, 0.6051838994026184, 0.561043381690979]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.34248948097229})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.5471134185791016})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.8673421144485474})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.8621177673339844})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7436, 'crossentropy': 1.385898046875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9805099964141846})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.8688503503799438})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.8774869441986084})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [44248, 4873, 14561, 10203, 53530, 38031, 18419, 23084, 54480, 56992], 'labels': [2, 8, 1, 0, 9, 9, 8, 9, 2, 7], 'scores': [0.6692267060279846, 0.855741024017334, 0.34137219190597534, 0.4859759211540222, 0.5527305006980896, 0.5895804166793823, 0.5881415009498596, 0.4869607090950012, 0.43044549226760864, 0.5906263589859009]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.2446556091308594})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.4800143241882324})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.5164874792099})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.6429649591445923})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7769, 'crossentropy': 1.237889453125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 0.9861999154090881})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 0.8278036117553711})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.8423519134521484})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [1597, 50054, 13227, 41935, 27764, 10995, 51801, 42839, 49550, 43547], 'labels': [1, 8, 1, 8, -1, 5, 1, 2, 6, 2], 'scores': [0.5625594854354858, 0.6604564189910889, 0.5033847689628601, 0.437985897064209, 0.3244750499725342, 0.6755544543266296, 0.41923195123672485, 0.5757570862770081, 0.4577787518501282, 0.466106653213501]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.1646023988723755})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.2755438089370728})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3998820781707764})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.515276551246643})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7665, 'crossentropy': 1.129779296875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9479251503944397})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.8710699081420898})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 0.8351730108261108})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [13650, 2732, 32481, 34063, 36692, 18578, 38638, 51165, 52646, 48431], 'labels': [4, 4, 2, 9, 0, -1, 8, 9, 9, 3], 'scores': [0.5328881740570068, 0.5940552949905396, 0.49226683378219604, 0.4126995801925659, 0.43194764852523804, 0.4020909070968628, 0.33251261711120605, 0.35753053426742554, 0.45701396465301514, 0.6159600019454956]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.0612139701843262})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.1665464639663696})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1662180423736572})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2416343688964844})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.7938, 'crossentropy': 1.00650751953125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.9857271313667297})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.8676735758781433})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.8424701690673828})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [22869, 32475, 760, 10304, 20931, 6235, 24902, 21426, 13930, 9158], 'labels': [6, 2, 3, 6, 6, 4, 9, 6, 2, 0], 'scores': [0.5213376879692078, 0.31280410289764404, 0.3919864892959595, 0.6195467114448547, 0.5022023916244507, 0.37800121307373047, 0.45638686418533325, 0.534263014793396, 0.3194645047187805, 0.3999069929122925]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 0.9927457571029663})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0435752868652344})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1969937086105347})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.2082562446594238})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7969, 'crossentropy': 0.9954078125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 0.8815354108810425})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.8576003313064575})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.7900378704071045})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [52730, 57476, 6053, 15680, 29438, 57710, 38780, 27641, 9905, 36307], 'labels': [7, 9, 7, 2, 0, 5, 6, 2, 7, 7], 'scores': [0.5025976300239563, 0.451671838760376, 0.5222384333610535, 0.5049598217010498, 0.6133908033370972, 0.37359511852264404, 0.4561612606048584, 0.708808422088623, 0.5444195866584778, 0.6448682546615601]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.9027678966522217})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9142879843711853})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.102662205696106})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.2063795328140259})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8197, 'crossentropy': 0.9280443359375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.8194020986557007})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 0.778528094291687})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.7039385437965393})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [37048, 31929, 27997, 33798, 27083, 8426, 56183, 46284, 15723, 54387], 'labels': [9, 5, 5, 7, 7, 5, -1, 9, 8, 8], 'scores': [0.499312162399292, 0.41183120012283325, 0.26046526432037354, 0.47928178310394287, 0.5031331777572632, 0.24368947744369507, 0.25712907314300537, 0.3434000611305237, 0.4174107313156128, 0.3794705867767334]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.8612829446792603})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0082714557647705})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.969537615776062})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9730897545814514})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8561, 'crossentropy': 0.798323681640625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.8001077771186829})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.7338453531265259})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.6994929909706116})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [25624, 40324, 14125, 8031, 33331, 59598, 15871, 2776, 49153, 3803], 'labels': [-1, 8, 2, 8, 3, 3, 4, 1, -1, 3], 'scores': [0.4034862518310547, 0.2923569679260254, 0.40647733211517334, 0.4134211540222168, 0.5045194029808044, 0.3755701184272766, 0.41503357887268066, 0.300028920173645, 0.37307286262512207, 0.5679882764816284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7537364363670349})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6911120414733887})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7960300445556641})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9094429016113281})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9388247728347778})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8983, 'crossentropy': 0.631484716796875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7058513760566711})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.5452401638031006})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.5318958759307861})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.48279061913490295})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [44149, 19717, 34943, 12950, 46187, 58273, 41601, 9782, 18862, 12928], 'labels': [2, 5, 0, 2, 3, 8, 7, 8, 3, 8], 'scores': [0.4699026942253113, 0.48464030027389526, 0.4114731550216675, 0.583184003829956, 0.40367114543914795, 0.4064962863922119, 0.2966339886188507, 0.5211936235427856, 0.452595055103302, 0.5258710384368896]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.7613734006881714})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6514233350753784})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7765494585037231})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6816129088401794})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8699706792831421})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9008, 'crossentropy': 0.6189794921875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.679407000541687})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.5402806997299194})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5173404216766357})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.4897339940071106})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [26444, 47132, 23086, 22139, 22328, 12157, 54541, 39022, 32150, 32048], 'labels': [1, 2, 8, 2, 1, 5, 2, 2, 7, 7], 'scores': [0.7168469429016113, 0.6626988053321838, 0.5158658027648926, 0.5229809284210205, 0.5070111751556396, 0.46031421422958374, 0.36303168535232544, 0.2704133987426758, 0.5354401469230652, 0.48606228828430176]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8287187814712524})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6084568500518799})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.639397382736206})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6982215642929077})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7026628255844116})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.909, 'crossentropy': 0.55006923828125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6615606546401978})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5662682056427002})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.5136525630950928})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5003196001052856})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [27929, 35073, 58047, 38688, 37630, 25958, 58495, 44954, 13190, 13156], 'labels': [-1, 3, -1, 7, -1, -1, 3, -1, 3, 2], 'scores': [0.4166527986526489, 0.4128243327140808, 0.43818604946136475, 0.5413339138031006, 0.46922290325164795, 0.5178882479667664, 0.4024040699005127, 0.3340601921081543, 0.5425652861595154, 0.3819316625595093]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8217756748199463})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6395951509475708})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6054565906524658})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6724085211753845})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7268596887588501})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6800427436828613})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9162, 'crossentropy': 0.553566748046875}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.6419830322265625})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.493884801864624})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.45422887802124023})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.4919734597206116})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4089949131011963})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [16113, 21150, 14105, 32339, 31345, 13335, 41832, 55639, 44438, 37413], 'labels': [-1, -1, 4, 3, 3, 0, 2, 5, 9, 5], 'scores': [0.46952855587005615, 0.47433459758758545, 0.5529483556747437, 0.48100417852401733, 0.5209397673606873, 0.7026731967926025, 0.6196178197860718, 0.5617331862449646, 0.4572276473045349, 0.6544651985168457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.815971851348877})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6021023988723755})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6066074371337891})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5893383026123047})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6095567941665649})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6994261741638184})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7153435945510864})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9326, 'crossentropy': 0.51961123046875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5815958380699158})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4275248348712921})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.41620689630508423})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3928815424442291})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.38022178411483765})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.35988473892211914})
store['active_learning_steps'][13]['eval_training']['best_epoch']=6
store['active_learning_steps'][13]['acquisition']={'indices': [54885, 18202, 11274, 11647, 52879, 29189, 59081, 31793, 31336, 7270], 'labels': [6, 4, -1, 9, -1, 8, -1, 4, 9, 5], 'scores': [0.7389255166053772, 0.6349215507507324, 0.2980121374130249, 0.5863289833068848, 0.397930383682251, 0.41173654794692993, 0.5444169640541077, 0.4956395626068115, 0.3738240897655487, 0.6242761611938477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7726152539253235})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5343519449234009})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6364332437515259})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5469809770584106})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6146557331085205})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9239, 'crossentropy': 0.4965005859375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6345514059066772})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5396007299423218})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.48755842447280884})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.49629366397857666})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [46643, 24444, 49147, 13673, 4165, 8932, 33001, 14623, 14329, 20859], 'labels': [4, -1, -1, 3, 2, 0, 5, 5, 0, 8], 'scores': [0.37424808740615845, 0.3406977653503418, 0.3004724979400635, 0.38070452213287354, 0.6038658618927002, 0.43012535572052, 0.4733889698982239, 0.6016910672187805, 0.6430944204330444, 0.47581255435943604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8752233982086182})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5920131802558899})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5265229940414429})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6149171590805054})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5594853758811951})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5726683139801025})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9273, 'crossentropy': 0.48190341796875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6022087335586548})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.46856489777565})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.45026034116744995})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4394303560256958})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4185637831687927})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [6673, 50418, 40702, 56190, 36314, 25281, 31456, 11585, 20494, 52169], 'labels': [-1, 6, 4, 4, 4, 2, 9, 4, 6, 2], 'scores': [0.4663393497467041, 0.4084007740020752, 0.692759096622467, 0.6459537148475647, 0.39083433151245117, 0.4577287435531616, 0.6633712649345398, 0.5368579030036926, 0.3871273398399353, 0.5079878568649292]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7735350131988525})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4678359627723694})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5521405935287476})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.49685966968536377})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5228316187858582})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9406, 'crossentropy': 0.427225390625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6445139646530151})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4846456050872803})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4625849723815918})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.45275312662124634})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [46884, 16968, 31517, 49616, 49728, 52214, 14729, 31505, 25158, 424], 'labels': [4, 9, 4, 7, 5, 9, -1, 0, 5, 9], 'scores': [0.43128472566604614, 0.49548208713531494, 0.323097288608551, 0.48007678985595703, 0.5253857970237732, 0.32187020778656006, 0.2258669137954712, 0.3527817726135254, 0.2952977418899536, 0.6210339069366455]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7663877010345459})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5211718082427979})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5790409445762634})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5222249031066895})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5229544639587402})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9337, 'crossentropy': 0.45489638671875}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6489349603652954})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4998360276222229})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.43715134263038635})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.4536277651786804})
store['active_learning_steps'][17]['eval_training']['best_epoch']=3
store['active_learning_steps'][17]['acquisition']={'indices': [35232, 51854, 50981, 16951, 17079, 23540, 33218, 48006, 12840, 9778], 'labels': [8, 5, 4, 8, 6, -1, 4, 6, 9, 3], 'scores': [0.38954317569732666, 0.523255467414856, 0.5904300808906555, 0.5328487753868103, 0.5737664103507996, 0.36432945728302, 0.211725652217865, 0.4844720959663391, 0.5744886994361877, 0.4306434988975525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7615046501159668})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5314711332321167})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.482514888048172})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.49904578924179077})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4523744583129883})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5137933492660522})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5576707124710083})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5159448385238647})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9433, 'crossentropy': 0.43965283203125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6146717071533203})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.443358838558197})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3658871054649353})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.349462628364563})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.32556411623954773})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3214064836502075})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3202611804008484})
store['active_learning_steps'][18]['eval_training']['best_epoch']=7
store['active_learning_steps'][18]['acquisition']={'indices': [42209, 26303, 49484, 49828, 31637, 53196, 33408, 41433, 42830, 7264], 'labels': [9, -1, -1, -1, 5, 9, 7, 9, -1, 9], 'scores': [0.7994033098220825, 0.4180164337158203, 0.24358808994293213, 0.41482245922088623, 0.5628637075424194, 0.5479796528816223, 0.7474475800991058, 0.5113400220870972, 0.28687894344329834, 0.602055013179779]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.899543046951294})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.42549657821655273})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4109955430030823})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43737611174583435})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4415218234062195})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.42193371057510376})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9432, 'crossentropy': 0.39091572265625}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5985091924667358})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4966360926628113})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4255450367927551})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.40473899245262146})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.34093546867370605})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [46144, 4323, 3195, 36704, 54002, 46088, 28420, 13827, 6406, 9526], 'labels': [0, -1, -1, 2, 5, 6, 1, 3, 0, 6], 'scores': [0.4616049528121948, 0.2881218194961548, 0.3401038646697998, 0.5968643426895142, 0.5120260715484619, 0.4064066410064697, 0.5187957286834717, 0.3903883695602417, 0.42103809118270874, 0.33887815475463867]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7753393650054932})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4648909568786621})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4015295207500458})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.437784880399704})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4191405773162842})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43814384937286377})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9407, 'crossentropy': 0.413213525390625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.60374915599823})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.46378976106643677})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.38066983222961426})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3540306091308594})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3444579839706421})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [34376, 45925, 40905, 55698, 33364, 23348, 46524, 29759, 41295, 38898], 'labels': [-1, 9, -1, 3, 2, -1, 6, 5, 9, 4], 'scores': [0.2711772918701172, 0.4271012544631958, 0.4091285467147827, 0.5230079293251038, 0.40803611278533936, 0.3430277109146118, 0.5113353133201599, 0.4251624345779419, 0.5417982935905457, 0.5948407053947449]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.723601222038269})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4421805739402771})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4104546308517456})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39888906478881836})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.439918577671051})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40174198150634766})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3949308693408966})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3994111120700836})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.44673067331314087})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4576348662376404})
store['active_learning_steps'][21]['training']['best_epoch']=7
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9488, 'crossentropy': 0.399272509765625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6267128586769104})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4445699155330658})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3442056179046631})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3255004286766052})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.30860447883605957})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.33763551712036133})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.2966024875640869})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3001154661178589})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.27195990085601807})
store['active_learning_steps'][21]['eval_training']['best_epoch']=9
store['active_learning_steps'][21]['acquisition']={'indices': [24426, 36834, 25098, 8745, 54379, 38661, 44745, 41334, 18089, 1707], 'labels': [5, 8, -1, -1, -1, -1, -1, 9, -1, -1], 'scores': [0.6023153364658356, 0.5582648515701294, 0.5770516395568848, 0.6776242256164551, 0.49143779277801514, 0.538428008556366, 0.58868807554245, 0.5036879777908325, 0.6069526076316833, 0.5846364498138428]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 0.8398010730743408})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43581506609916687})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4517475962638855})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37994712591171265})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4127812683582306})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3998224139213562})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4032677710056305})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9494, 'crossentropy': 0.3755630859375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6421524286270142})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.43596699833869934})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4384393095970154})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.36101293563842773})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.35881972312927246})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33435842394828796})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [31917, 17456, 2574, 44040, 42429, 33110, 6574, 15852, 3719, 59492], 'labels': [9, 8, -1, 0, 2, 1, -1, -1, 2, -1], 'scores': [0.23411542177200317, 0.29966187477111816, 0.5226379632949829, 0.3587474524974823, 0.39714038372039795, 0.5086761713027954, 0.692013680934906, 0.4379769563674927, 0.4971204400062561, 0.47527217864990234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7895221710205078})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.48514777421951294})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38793396949768066})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3985934257507324})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4353489875793457})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40139487385749817})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9452, 'crossentropy': 0.3658503662109375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6340672969818115})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.43466833233833313})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.42531365156173706})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3712601959705353})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3867102861404419})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [32387, 6832, 17125, 39841, 42942, 3010, 18835, 11645, 12089, 44155], 'labels': [4, 0, -1, 8, 6, 7, -1, 3, 3, 4], 'scores': [0.4191220998764038, 0.43523919582366943, 0.2657022476196289, 0.4394468069076538, 0.3793373703956604, 0.4951127767562866, 0.2724663019180298, 0.33301568031311035, 0.43273335695266724, 0.43930697441101074]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.83085036277771})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5167242288589478})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38439181447029114})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3924337327480316})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43946677446365356})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3949034512042999})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9504, 'crossentropy': 0.372700830078125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6830089092254639})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4557161331176758})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4087410569190979})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.40014714002609253})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3594181537628174})
store['active_learning_steps'][24]['eval_training']['best_epoch']=5
store['active_learning_steps'][24]['acquisition']={'indices': [4253, 45437, 4804, 42020, 54892, 40561, 35876, 34829, 15913, 12984], 'labels': [8, 1, 0, 9, 3, 1, 3, 5, 9, 8], 'scores': [0.4881722927093506, 0.605548083782196, 0.42043399810791016, 0.5660060048103333, 0.4834427237510681, 0.5332807898521423, 0.4387913942337036, 0.4103630781173706, 0.340789258480072, 0.34657424688339233]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9006212949752808})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4721626043319702})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3849369287490845})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37663882970809937})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.430586576461792})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.36556488275527954})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39440733194351196})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40270674228668213})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3745213747024536})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9532, 'crossentropy': 0.3752467041015625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6429321765899658})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.42580753564834595})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.38593071699142456})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3711484670639038})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.32557934522628784})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.31120455265045166})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.29674816131591797})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.30051082372665405})
store['active_learning_steps'][25]['eval_training']['best_epoch']=7
store['active_learning_steps'][25]['acquisition']={'indices': [53623, 9227, 11202, 19642, 2991, 15754, 31672, 29650, 26756, 16649], 'labels': [9, -1, 9, 7, 8, -1, 6, -1, 7, -1], 'scores': [0.31472286581993103, 0.6862910985946655, 0.43434205651283264, 0.6313973665237427, 0.5901197791099548, 0.49155038595199585, 0.6219372749328613, 0.26629722118377686, 0.5123558640480042, 0.4393656253814697]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8044700622558594})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4819571375846863})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4088999927043915})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4061700701713562})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37006911635398865})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41824662685394287})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3797558844089508})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4009809195995331})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9494, 'crossentropy': 0.3675498291015625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6287140846252441})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4428251087665558})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.38346347212791443})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.36152583360671997})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3293265700340271})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.30941328406333923})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3275182545185089})
store['active_learning_steps'][26]['eval_training']['best_epoch']=6
store['active_learning_steps'][26]['acquisition']={'indices': [56612, 50994, 45989, 13538, 57308, 51194, 13867, 40481, 28757, 32242], 'labels': [2, 7, -1, 5, -1, 9, 7, 3, 3, -1], 'scores': [0.541875958442688, 0.5641344785690308, 0.5677152872085571, 0.4964213967323303, 0.34509217739105225, 0.4092795252799988, 0.53817218542099, 0.43731772899627686, 0.37077462673187256, 0.33060336112976074]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9319557547569275})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4771512746810913})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3714000880718231})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3595881760120392})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3629903495311737})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.39107850193977356})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.364102840423584})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9543, 'crossentropy': 0.3647652587890625}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6390808820724487})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.43438559770584106})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.39300811290740967})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3551403880119324})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3324311375617981})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3428351879119873})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [43126, 29206, 7984, 49172, 27340, 11951, 14332, 49910, 22531, 58644], 'labels': [3, 4, 4, -1, 5, 3, -1, 6, 4, -1], 'scores': [0.6112194657325745, 0.5047025680541992, 0.4511341452598572, 0.39693737030029297, 0.49176228046417236, 0.4822651743888855, 0.2778102159500122, 0.527079701423645, 0.4435150623321533, 0.29288387298583984]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9632619619369507})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4643004536628723})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3928509056568146})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3491308391094208})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.41124796867370605})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3629128932952881})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34452199935913086})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3946176767349243})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3723670244216919})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3632555603981018})
store['active_learning_steps'][28]['training']['best_epoch']=7
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9516, 'crossentropy': 0.377678662109375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5995749235153198})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.40210777521133423})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.39877572655677795})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3164113461971283})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.34979331493377686})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.30204373598098755})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.2960330843925476})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.25721484422683716})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.26796528697013855})
store['active_learning_steps'][28]['eval_training']['best_epoch']=8
store['active_learning_steps'][28]['acquisition']={'indices': [4276, 41000, 27716, 47196, 59344, 27706, 15833, 48712, 31252, 19869], 'labels': [3, 5, 7, -1, 9, 7, 7, 7, 5, 7], 'scores': [0.5563698410987854, 0.5729726552963257, 0.8070111274719238, 0.5206609964370728, 0.6186762452125549, 0.4194028973579407, 0.5564779341220856, 0.7236222624778748, 0.5152150988578796, 0.6720848977565765]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.925663948059082})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4284387230873108})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.375322163105011})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39865732192993164})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3452293276786804})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3637840449810028})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.37316209077835083})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.38003382086753845})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9567, 'crossentropy': 0.3526391357421875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6871234178543091})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.41580700874328613})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.33810555934906006})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3383716940879822})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31886762380599976})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.33704107999801636})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25971975922584534})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [44237, 49417, 42153, 7248, 9049, 40976, 37787, 6574, 25415, 58469], 'labels': [-1, -1, -1, -1, -1, 1, -1, -1, -1, -1], 'scores': [0.4329688549041748, 0.27142250537872314, 0.4680166244506836, 0.30269527435302734, 0.5268710851669312, 0.49886634945869446, 0.38572800159454346, 0.4691232442855835, 0.5488415956497192, 0.5893944501876831]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8531058430671692})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.47977179288864136})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3947935104370117})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34136390686035156})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3288211226463318})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34422409534454346})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3759264349937439})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3463747501373291})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9571, 'crossentropy': 0.33923203125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6881039142608643})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4213073253631592})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.392213374376297})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3258094787597656})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3547651767730713})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30038225650787354})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2884199023246765})
store['active_learning_steps'][30]['eval_training']['best_epoch']=7
store['active_learning_steps'][30]['acquisition']={'indices': [14765, 33150, 45290, 43560, 8522, 41933, 38656, 46328, 11091, 48230], 'labels': [3, 8, -1, 5, -1, 5, 5, -1, -1, 5], 'scores': [0.6578142642974854, 0.7373443245887756, 0.49578142166137695, 0.7311022877693176, 0.5451513528823853, 0.5427181720733643, 0.41601240634918213, 0.5323700904846191, 0.643537163734436, 0.5094959139823914]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9957921504974365})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.50922030210495})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.42045488953590393})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3457622528076172})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34239137172698975})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34053879976272583})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3388817310333252})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35244983434677124})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.37342530488967896})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.35846245288848877})
store['active_learning_steps'][31]['training']['best_epoch']=7
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9594, 'crossentropy': 0.3480263671875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6221839189529419})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4406220614910126})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3500900864601135})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.31797075271606445})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2987522482872009})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30174100399017334})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2936275899410248})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.272544264793396})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29754817485809326})
store['active_learning_steps'][31]['eval_training']['best_epoch']=8
store['active_learning_steps'][31]['acquisition']={'indices': [38143, 37964, 57402, 34486, 8731, 3717, 14462, 793, 28248, 3759], 'labels': [-1, -1, -1, 0, 5, 6, -1, -1, -1, -1], 'scores': [0.44859111309051514, 0.5047225952148438, 0.3747676610946655, 0.4727897047996521, 0.7603158354759216, 0.5020312666893005, 0.5495438575744629, 0.3453638553619385, 0.46240830421447754, 0.37387216091156006]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.88163161277771})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4643634855747223})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4049980342388153})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36258089542388916})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31748369336128235})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32413485646247864})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3694230318069458})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.35164526104927063})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9569, 'crossentropy': 0.32399619140625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6513259410858154})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.47475048899650574})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.36357778310775757})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3342762589454651})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.31581056118011475})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.318528413772583})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.29957979917526245})
store['active_learning_steps'][32]['eval_training']['best_epoch']=7
store['active_learning_steps'][32]['acquisition']={'indices': [35629, 36878, 10747, 26214, 8821, 29923, 14878, 34520, 48360, 608], 'labels': [-1, 8, -1, 9, 3, -1, 3, 6, 3, -1], 'scores': [0.5062450766563416, 0.3771583139896393, 0.42913347482681274, 0.5863453149795532, 0.40454572439193726, 0.5440926551818848, 0.5996280908584595, 0.6291340589523315, 0.7459410429000854, 0.2915618419647217]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0070456266403198})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5458334684371948})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4324078857898712})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38917189836502075})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3648502230644226})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35693830251693726})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3879232108592987})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3852212727069855})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.40274107456207275})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9566, 'crossentropy': 0.3431514404296875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7222672700881958})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4915885329246521})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36867332458496094})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3345877528190613})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3291319012641907})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3048574924468994})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25645726919174194})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25974559783935547})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [18276, 56616, 4705, 2198, 6305, 40378, 51100, 4675, 718, 13376], 'labels': [-1, 3, -1, -1, 5, -1, -1, -1, 4, 3], 'scores': [0.41381406784057617, 0.4982423186302185, 0.48174750804901123, 0.29640400409698486, 0.46568363904953003, 0.5385881066322327, 0.3306698799133301, 0.45639127492904663, 0.5384528338909149, 0.6515601277351379]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.960673451423645})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5258947610855103})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3565664291381836})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36974477767944336})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3841117024421692})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3446090519428253})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.33513498306274414})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3699187636375427})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36783263087272644})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3318164050579071})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3551804721355438})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.34722214937210083})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.34768056869506836})
store['active_learning_steps'][34]['training']['best_epoch']=10
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9613, 'crossentropy': 0.3327782958984375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7148494720458984})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.44451913237571716})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3727838397026062})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3319970667362213})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3112673759460449})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3066897988319397})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.2679734230041504})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27761927247047424})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2709115743637085})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.26719048619270325})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.267940878868103})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.26078474521636963})
store['active_learning_steps'][34]['eval_training']['best_epoch']=12
store['active_learning_steps'][34]['acquisition']={'indices': [14619, 57714, 39, 1423, 48497, 51736, 2845, 10080, 30764, 49412], 'labels': [3, 1, -1, 0, -1, 5, 8, -1, 7, -1], 'scores': [0.48486411571502686, 0.5862027406692505, 0.21563374996185303, 0.5603828430175781, 0.47956550121307373, 0.6013330221176147, 0.38853609561920166, 0.24389207363128662, 0.34293681383132935, 0.34352928400039673]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.9487696290016174})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4827829599380493})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3825223445892334})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35761916637420654})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3782525658607483})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32811248302459717})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3153802156448364})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33575016260147095})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3518787920475006})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3916624188423157})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9565, 'crossentropy': 0.3447052978515625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6393426656723022})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4034245014190674})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3745868504047394})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3242029845714569})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.30512627959251404})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.28781092166900635})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.28185486793518066})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2721957564353943})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3039472699165344})
store['active_learning_steps'][35]['eval_training']['best_epoch']=8
store['active_learning_steps'][35]['acquisition']={'indices': [17230, 41234, 25000, 9715, 843, 4783, 59115, 26348, 7349, 31394], 'labels': [-1, 2, 3, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4020373821258545, 0.5332726836204529, 0.32510247826576233, 0.34547877311706543, 0.4277017116546631, 0.36134982109069824, 0.3526015281677246, 0.49866193532943726, 0.5940201878547668, 0.3516237139701843]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0053199529647827})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5457808971405029})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4510902166366577})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34360069036483765})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.41028323769569397})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38878071308135986})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.340393602848053})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36259761452674866})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3491626977920532})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3285754919052124})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37458857893943787})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2964302897453308})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3665553331375122})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37557268142700195})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3600243926048279})
store['active_learning_steps'][36]['training']['best_epoch']=12
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9604, 'crossentropy': 0.32654697265625}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6040666103363037})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4437471330165863})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3302651047706604})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30986660718917847})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27884596586227417})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.242902010679245})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2465091347694397})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2623039782047272})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.22431761026382446})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23794448375701904})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24118076264858246})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26066479086875916})
store['active_learning_steps'][36]['eval_training']['best_epoch']=9
store['active_learning_steps'][36]['acquisition']={'indices': [40991, 30614, 47938, 15155, 47203, 45098, 3380, 5684, 58459, 2706], 'labels': [-1, 1, -1, -1, -1, -1, -1, 6, -1, 7], 'scores': [0.3932342529296875, 0.5158083438873291, 0.4076250195503235, 0.30868637561798096, 0.32561159133911133, 0.3825817108154297, 0.34570014476776123, 0.6621151268482208, 0.43251949548721313, 0.7904406189918518]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9834386706352234})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4603467583656311})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3517872095108032})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3887487053871155})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3470723032951355})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3317357897758484})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3288167715072632})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3136036992073059})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32466939091682434})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31279808282852173})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31653767824172974})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3694998621940613})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36043763160705566})
store['active_learning_steps'][37]['training']['best_epoch']=10
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9604, 'crossentropy': 0.334938671875}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6133139133453369})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4062606990337372})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3582764267921448})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.32327529788017273})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2607807517051697})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2933598756790161})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.2622816562652588})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.28336161375045776})
store['active_learning_steps'][37]['eval_training']['best_epoch']=5
store['active_learning_steps'][37]['acquisition']={'indices': [37774, 49563, 41287, 8927, 40390, 5103, 25560, 43105, 22682, 12950], 'labels': [-1, 8, 3, -1, 0, 2, -1, -1, -1, -1], 'scores': [0.5140087604522705, 0.6735831499099731, 0.28575223684310913, 0.2772202491760254, 0.7621135711669922, 0.65760338306427, 0.5356745719909668, 0.5607695579528809, 0.5102593898773193, 0.5114116668701172]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9774863719940186})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5159981846809387})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38071882724761963})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.320758581161499})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3177378177642822})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3509795069694519})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30755874514579773})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3338616192340851})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3393276333808899})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33270010352134705})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9631, 'crossentropy': 0.3126808349609375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6036480665206909})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.40539443492889404})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3529713451862335})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3466644883155823})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2987549304962158})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2976072430610657})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2491254359483719})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27515989542007446})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.24032771587371826})
store['active_learning_steps'][38]['eval_training']['best_epoch']=9
store['active_learning_steps'][38]['acquisition']={'indices': [35400, 52551, 45359, 11482, 26358, 10064, 25642, 15998, 57764, 46610], 'labels': [-1, -1, -1, 8, 3, 8, -1, -1, 6, 5], 'scores': [0.40649938583374023, 0.41007715463638306, 0.5939580202102661, 0.38182365894317627, 0.5699648857116699, 0.631850004196167, 0.2706645727157593, 0.33398687839508057, 0.611772894859314, 0.4892650842666626]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.0334597826004028})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5103444457054138})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.38476821780204773})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.371273398399353})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3460444211959839})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37053120136260986})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3275788426399231})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33138322830200195})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3557804226875305})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3389464318752289})
store['active_learning_steps'][39]['training']['best_epoch']=7
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9577, 'crossentropy': 0.3192486572265625}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5679070353507996})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4240120053291321})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.32499778270721436})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.28699877858161926})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.30475419759750366})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28949904441833496})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.2921990752220154})
store['active_learning_steps'][39]['eval_training']['best_epoch']=4
store['active_learning_steps'][39]['acquisition']={'indices': [42535, 2574, 26174, 59566, 45160, 15893, 6212, 36423, 6574, 32032], 'labels': [2, 7, -1, 9, -1, 5, 2, 2, -1, 4], 'scores': [0.4856158196926117, 0.44106072187423706, 0.46094369888305664, 0.367246150970459, 0.3230464458465576, 0.5724861025810242, 0.5147879421710968, 0.6700957417488098, 0.5498643517494202, 0.4595838785171509]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.1534655094146729})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5060346126556396})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3887532949447632})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.35137104988098145})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3340286612510681})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30662864446640015})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2972722053527832})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3167862892150879})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3350808024406433})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.32483887672424316})
store['active_learning_steps'][40]['training']['best_epoch']=7
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9673, 'crossentropy': 0.2822432373046875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5699505805969238})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.39553892612457275})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3513528108596802})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3024263381958008})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.28973865509033203})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3088948130607605})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2639904022216797})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2521900236606598})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24551469087600708})
store['active_learning_steps'][40]['eval_training']['best_epoch']=9
store['active_learning_steps'][40]['acquisition']={'indices': [49135, 28662, 32926, 27266, 1434, 7403, 1424, 39419, 24957, 18501], 'labels': [-1, -1, -1, -1, -1, -1, -1, 8, -1, 4], 'scores': [0.3357551097869873, 0.36929023265838623, 0.3905332088470459, 0.34098339080810547, 0.4041022062301636, 0.4200918674468994, 0.44677913188934326, 0.39919614791870117, 0.47775304317474365, 0.6786743998527527]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0840423107147217})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5303568840026855})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38826340436935425})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34923088550567627})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30583861470222473})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35902535915374756})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3054879903793335})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34691423177719116})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.33902812004089355})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30986812710762024})
store['active_learning_steps'][41]['training']['best_epoch']=7
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.965, 'crossentropy': 0.2788935546875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6852415204048157})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4662967920303345})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.34283629059791565})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33621612191200256})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30153751373291016})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2943434715270996})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27189403772354126})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27218419313430786})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26822930574417114})
store['active_learning_steps'][41]['eval_training']['best_epoch']=9
store['active_learning_steps'][41]['acquisition']={'indices': [24439, 3527, 47410, 36452, 43421, 6990, 22614, 50180, 2427, 2229], 'labels': [-1, -1, -1, 5, -1, -1, -1, 8, 7, -1], 'scores': [0.48364710807800293, 0.4681880474090576, 0.5258523225784302, 0.5071981549263, 0.34187769889831543, 0.5102969408035278, 0.4327125549316406, 0.39725810289382935, 0.5314035415649414, 0.48841679096221924]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0027203559875488})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5595437288284302})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4091764986515045})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.34685343503952026})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35708171129226685})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31863731145858765})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2832157611846924})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.309190034866333})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30858826637268066})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35503461956977844})
store['active_learning_steps'][42]['training']['best_epoch']=7
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9636, 'crossentropy': 0.3022089599609375}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6128589510917664})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.42465686798095703})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.36698538064956665})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.35012245178222656})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.357870876789093})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30275097489356995})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2742343544960022})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2674894332885742})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2938994765281677})
store['active_learning_steps'][42]['eval_training']['best_epoch']=8
store['active_learning_steps'][42]['acquisition']={'indices': [47758, 59747, 39690, 12949, 33035, 30326, 23266, 11798, 50690, 2481], 'labels': [-1, 5, 4, -1, -1, -1, -1, -1, 5, -1], 'scores': [0.4315197467803955, 0.6089083552360535, 0.329215943813324, 0.40112030506134033, 0.4693666696548462, 0.4829442501068115, 0.42498040199279785, 0.4509066939353943, 0.38164547085762024, 0.5863766074180603]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9520806074142456})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4864795207977295})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38404327630996704})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3122329115867615})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31768661737442017})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3304356634616852})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31016236543655396})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3100399374961853})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3402394652366638})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3189542293548584})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.321340948343277})
store['active_learning_steps'][43]['training']['best_epoch']=8
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.967, 'crossentropy': 0.275516064453125}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6230193376541138})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4074186086654663})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3078339695930481})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31011343002319336})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2527981400489807})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2825442850589752})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26720094680786133})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2685069143772125})
store['active_learning_steps'][43]['eval_training']['best_epoch']=5
store['active_learning_steps'][43]['acquisition']={'indices': [21174, 29110, 34500, 27026, 15771, 45917, 41772, 6506, 26879, 34188], 'labels': [2, -1, 8, 2, 5, 9, 5, 8, -1, 3], 'scores': [0.4684775471687317, 0.4250354766845703, 0.3854302167892456, 0.4427109956741333, 0.7077142000198364, 0.5136562585830688, 0.4474913477897644, 0.6735285818576813, 0.40952062606811523, 0.3449360132217407]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1041529178619385})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4843374490737915})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37722596526145935})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3108891248703003})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2995039224624634})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3224538266658783})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29615452885627747})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29756397008895874})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2725469470024109})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2999662160873413})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2806999683380127})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3013319969177246})
store['active_learning_steps'][44]['training']['best_epoch']=9
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.965, 'crossentropy': 0.29520869140625}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6098392605781555})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4051368236541748})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.36233192682266235})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3236691951751709})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2799491584300995})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2898002862930298})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2864408493041992})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26199871301651})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2690471410751343})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.251616895198822})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23572900891304016})
store['active_learning_steps'][44]['eval_training']['best_epoch']=11
store['active_learning_steps'][44]['acquisition']={'indices': [20309, 25648, 29576, 15749, 22729, 7897, 33768, 45445, 16213, 11367], 'labels': [-1, -1, 8, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4471864700317383, 0.2675004005432129, 0.3193494379520416, 0.4066152572631836, 0.3050844669342041, 0.49439823627471924, 0.41436076164245605, 0.42465806007385254, 0.4477849006652832, 0.24734282493591309]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9701570868492126})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49123767018318176})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40065497159957886})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33862560987472534})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3101252019405365})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32439902424812317})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3232145309448242})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3140055537223816})
store['active_learning_steps'][45]['training']['best_epoch']=5
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9616, 'crossentropy': 0.3097484130859375}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6720594167709351})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4602452516555786})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3935950994491577})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.32117247581481934})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3617948293685913})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.32429999113082886})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3190436065196991})
store['active_learning_steps'][45]['eval_training']['best_epoch']=7
store['active_learning_steps'][45]['acquisition']={'indices': [57383, 53693, 33420, 15518, 42673, 43123, 39130, 56735, 16528, 50916], 'labels': [-1, 4, -1, 7, -1, -1, 6, 0, 7, 4], 'scores': [0.4107387065887451, 0.40709346532821655, 0.49330437183380127, 0.5815220475196838, 0.565321147441864, 0.493094801902771, 0.5365396738052368, 0.5265421271324158, 0.5188934206962585, 0.4213827848434448]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0933805704116821})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.501791775226593})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3954940438270569})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33592331409454346})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.329541951417923})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2940386235713959})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2964349389076233})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31403815746307373})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33388185501098633})
store['active_learning_steps'][46]['training']['best_epoch']=6
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9672, 'crossentropy': 0.2713672607421875}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6512246131896973})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3811895251274109})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3355705738067627})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3268932104110718})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.33440345525741577})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2729698717594147})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.268671452999115})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2796548008918762})
store['active_learning_steps'][46]['eval_training']['best_epoch']=7
store['active_learning_steps'][46]['acquisition']={'indices': [34911, 466, 36822, 6011, 16990, 44075, 17394, 55878, 50540, 17956], 'labels': [-1, -1, 1, -1, -1, -1, -1, 5, -1, -1], 'scores': [0.340970516204834, 0.2945282459259033, 0.39904075860977173, 0.5536452531814575, 0.3785349726676941, 0.38832294940948486, 0.3400282859802246, 0.483099102973938, 0.39970552921295166, 0.2590891122817993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9993321895599365})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5260738730430603})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37820714712142944})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34550023078918457})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3375965356826782})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2756778299808502})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.32312047481536865})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3092259466648102})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3004333972930908})
store['active_learning_steps'][47]['training']['best_epoch']=6
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9633, 'crossentropy': 0.303939501953125}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6458366513252258})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.44403111934661865})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.35939913988113403})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3491663932800293})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3258994519710541})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2747304439544678})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27909108996391296})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2888115644454956})
store['active_learning_steps'][47]['eval_training']['best_epoch']=6
store['active_learning_steps'][47]['acquisition']={'indices': [45749, 21965, 54971, 46802, 37315, 1075, 4446, 11777, 16775, 52747], 'labels': [-1, -1, -1, -1, -1, 7, -1, 3, -1, 3], 'scores': [0.4379958510398865, 0.35088229179382324, 0.5260902643203735, 0.4181642532348633, 0.33697009086608887, 0.7150630950927734, 0.37692153453826904, 0.40506529808044434, 0.40493178367614746, 0.5774010419845581]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.0182998180389404})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5639958381652832})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38426706194877625})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3457100987434387})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29554516077041626})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2849237322807312})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2974293529987335})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31582581996917725})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31188538670539856})
store['active_learning_steps'][48]['training']['best_epoch']=6
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.964, 'crossentropy': 0.29179140625}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6639149188995361})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4408625066280365})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38621804118156433})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34490013122558594})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32233232259750366})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2623664140701294})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2856175899505615})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2853918671607971})
store['active_learning_steps'][48]['eval_training']['best_epoch']=6
store['active_learning_steps'][48]['acquisition']={'indices': [17772, 45439, 12970, 859, 55862, 4955, 41999, 22169, 34902, 50316], 'labels': [7, 2, 7, -1, 2, 2, 0, 2, 2, -1], 'scores': [0.3882593512535095, 0.44861894845962524, 0.28028804063796997, 0.33030402660369873, 0.5464107990264893, 0.468269944190979, 0.6027795076370239, 0.4056422710418701, 0.40827035903930664, 0.33665525913238525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0837724208831787})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49770036339759827})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3485688865184784})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3514735698699951})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3061698079109192})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30233022570610046})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2835642993450165})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28825971484184265})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28591644763946533})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2951757311820984})
store['active_learning_steps'][49]['training']['best_epoch']=7
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9647, 'crossentropy': 0.2817874755859375}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6186304092407227})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4034779667854309})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.33872246742248535})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.329925000667572})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2756904363632202})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2795829474925995})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.26395440101623535})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.24581614136695862})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2593044340610504})
store['active_learning_steps'][49]['eval_training']['best_epoch']=8
store['active_learning_steps'][49]['acquisition']={'indices': [31591, 12940, 18324, 58141, 50687, 59297, 17183, 44245, 47877, 41636], 'labels': [8, -1, 0, -1, 8, 1, -1, 1, -1, -1], 'scores': [0.32123667001724243, 0.3515423536300659, 0.5086496770381927, 0.35045552253723145, 0.45591041445732117, 0.39546114206314087, 0.4637467861175537, 0.5427699685096741, 0.37157702445983887, 0.21566259860992432]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 1.0343704223632812})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5340500473976135})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.393015593290329})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.32921111583709717})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2962741255760193})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31596189737319946})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2979419529438019})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.325977087020874})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9637, 'crossentropy': 0.2976205078125}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.657532811164856})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.40432238578796387})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3464491069316864})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3023010492324829})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30996501445770264})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2701118588447571})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28044867515563965})
store['active_learning_steps'][50]['eval_training']['best_epoch']=6
store['active_learning_steps'][50]['acquisition']={'indices': [57460, 17924, 13364, 38654, 31887, 50348, 49744, 2548, 8449, 17494], 'labels': [-1, -1, -1, -1, -1, 2, 8, 4, 0, 5], 'scores': [0.33212339878082275, 0.48917269706726074, 0.6099576950073242, 0.4422656297683716, 0.41311943531036377, 0.3279184103012085, 0.5750145316123962, 0.5424492359161377, 0.4701728820800781, 0.6304027438163757]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1356289386749268})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5730401277542114})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37304991483688354})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33905544877052307})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34886080026626587})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3022545874118805})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30838435888290405})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28580331802368164})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30536821484565735})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29559725522994995})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3139446973800659})
store['active_learning_steps'][51]['training']['best_epoch']=8
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9682, 'crossentropy': 0.262258935546875}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6861870288848877})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.45507752895355225})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3620097041130066})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32276976108551025})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3269510269165039})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.28281456232070923})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25727251172065735})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2545008659362793})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23840254545211792})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24428176879882812})
store['active_learning_steps'][51]['eval_training']['best_epoch']=9
store['active_learning_steps'][51]['acquisition']={'indices': [47448, 29814, 52805, 50836, 44748, 9186, 31114, 3290, 41714, 13046], 'labels': [-1, -1, 9, -1, 8, -1, 4, 4, 4, -1], 'scores': [0.3300588130950928, 0.3738766312599182, 0.39738112688064575, 0.4376729726791382, 0.2721981704235077, 0.39773303270339966, 0.5312900543212891, 0.4400240182876587, 0.6362200975418091, 0.3508889675140381]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 1.0300863981246948})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.46569710969924927})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3772186040878296})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31860628724098206})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28825151920318604})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3127953112125397})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28988632559776306})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29091134667396545})
store['active_learning_steps'][52]['training']['best_epoch']=5
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9708, 'crossentropy': 0.2663791748046875}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6556260585784912})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.45999446511268616})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3656133711338043})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3581071197986603})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30857694149017334})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3057968020439148})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2865234315395355})
store['active_learning_steps'][52]['eval_training']['best_epoch']=7
store['active_learning_steps'][52]['acquisition']={'indices': [41481, 31476, 34870, 29303, 44534, 15974, 31294, 19362, 20169, 51075], 'labels': [-1, -1, 8, 8, 9, -1, -1, 8, 4, -1], 'scores': [0.3636035919189453, 0.3627591133117676, 0.486186146736145, 0.5196705460548401, 0.4763116240501404, 0.2649998664855957, 0.4890075922012329, 0.41822683811187744, 0.6730368137359619, 0.43086671829223633]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.114875316619873})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4416138827800751})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.35667240619659424})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3029722571372986})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2959798574447632})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2941003143787384})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28169605135917664})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2842070758342743})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2825859785079956})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27713045477867126})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.281277596950531})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2791512608528137})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2938658595085144})
store['active_learning_steps'][53]['training']['best_epoch']=10
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.2725752685546875}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6632157564163208})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.45478105545043945})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34025993943214417})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2897840142250061})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2772659957408905})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26941782236099243})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23494333028793335})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2623019814491272})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2212972790002823})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24021704494953156})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.250292032957077})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.24982485175132751})
store['active_learning_steps'][53]['eval_training']['best_epoch']=9
store['active_learning_steps'][53]['acquisition']={'indices': [30708, 56254, 37450, 16858, 5114, 33824, 24287, 35216, 34445, 30115], 'labels': [-1, -1, 4, -1, -1, 4, -1, -1, -1, -1], 'scores': [0.46770262718200684, 0.34252023696899414, 0.5548556447029114, 0.5566756725311279, 0.4238893985748291, 0.47526103258132935, 0.4579218626022339, 0.5258769989013672, 0.40247201919555664, 0.45702898502349854]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9538663029670715})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5327578186988831})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3627166748046875})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2968975901603699})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2707464098930359})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2645348906517029})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2960994839668274})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2496153712272644})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2704542577266693})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2993142008781433})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27432626485824585})
store['active_learning_steps'][54]['training']['best_epoch']=8
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9697, 'crossentropy': 0.2538262939453125}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6015650033950806})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.39842844009399414})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.36930978298187256})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2991204261779785})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25465601682662964})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28904464840888977})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26934289932250977})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.22919313609600067})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.234481081366539})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.24985338747501373})
store['active_learning_steps'][54]['eval_training']['best_epoch']=8
store['active_learning_steps'][54]['acquisition']={'indices': [10432, 12153, 5665, 9312, 12305, 4564, 43008, 49487, 13026, 35090], 'labels': [-1, 3, -1, -1, 9, -1, 8, 8, 3, -1], 'scores': [0.2405790090560913, 0.3694339394569397, 0.31734490394592285, 0.39588844776153564, 0.5660396814346313, 0.4441099166870117, 0.3940224051475525, 0.5021021962165833, 0.48259884119033813, 0.3485569953918457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.2031503915786743})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5344603061676025})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4000934958457947})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.317617803812027})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32735034823417664})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29138684272766113})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29366883635520935})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.256087064743042})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26356416940689087})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.26164481043815613})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2756556570529938})
store['active_learning_steps'][55]['training']['best_epoch']=8
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9714, 'crossentropy': 0.259733837890625}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6893945932388306})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4533235430717468})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34614819288253784})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30079883337020874})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2790411710739136})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.26895034313201904})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24399229884147644})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24104589223861694})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.23698309063911438})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.22038114070892334})
store['active_learning_steps'][55]['eval_training']['best_epoch']=10
store['active_learning_steps'][55]['acquisition']={'indices': [36820, 7198, 25964, 16045, 45446, 11495, 38842, 52170, 29393, 380], 'labels': [8, 9, -1, 0, 7, -1, -1, -1, -1, -1], 'scores': [0.35516661405563354, 0.47268664836883545, 0.42207127809524536, 0.6701461672782898, 0.7281607389450073, 0.4847581386566162, 0.3491162061691284, 0.4525846242904663, 0.36518025398254395, 0.47422778606414795]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.13926100730896})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5570119619369507})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3899134397506714})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33449888229370117})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.33802905678749084})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3217204809188843})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3134939670562744})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29368460178375244})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2798502445220947})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26420071721076965})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29338330030441284})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31631362438201904})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.32508060336112976})
store['active_learning_steps'][56]['training']['best_epoch']=10
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9716, 'crossentropy': 0.2694945068359375}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6712027788162231})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4713120460510254})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3201155960559845})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3123692274093628})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2982015013694763})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2668454647064209})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2599567770957947})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2625736594200134})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24910011887550354})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25681304931640625})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24773669242858887})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2398088574409485})
store['active_learning_steps'][56]['eval_training']['best_epoch']=12
store['active_learning_steps'][56]['acquisition']={'indices': [57605, 44736, 36091, 17382, 29944, 7995, 23607, 48975, 26801, 1269], 'labels': [-1, 5, -1, 6, 6, 8, -1, 2, 7, -1], 'scores': [0.3687632083892822, 0.615839958190918, 0.4541199803352356, 0.5825415253639221, 0.5236063003540039, 0.7550655603408813, 0.37951231002807617, 0.5435992479324341, 0.3244452178478241, 0.48043715953826904]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.0850634574890137})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5358126163482666})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3713042736053467})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3459952175617218})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3012239336967468})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2810954749584198})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2779950797557831})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2822968065738678})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28782445192337036})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.31280118227005005})
store['active_learning_steps'][57]['training']['best_epoch']=7
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9702, 'crossentropy': 0.268338525390625}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6631012558937073})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.474224328994751})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4083138108253479})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3282877802848816})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30165889859199524})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2663367688655853})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2442990243434906})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24706748127937317})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26150017976760864})
store['active_learning_steps'][57]['eval_training']['best_epoch']=7
store['active_learning_steps'][57]['acquisition']={'indices': [36946, 30742, 33394, 56457, 57286, 26760, 26515, 56838, 6335, 20635], 'labels': [-1, 1, -1, 3, -1, 8, 8, 5, -1, 5], 'scores': [0.3564891815185547, 0.42872369289398193, 0.4414163827896118, 0.4174169898033142, 0.3050823211669922, 0.39352238178253174, 0.4493366479873657, 0.5986999273300171, 0.4157853126525879, 0.5200631022453308]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2410519123077393})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5719705820083618})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.43305936455726624})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3617456257343292})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28152185678482056})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2856524884700775})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2864062786102295})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29774099588394165})
store['active_learning_steps'][58]['training']['best_epoch']=5
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9664, 'crossentropy': 0.287183984375}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6514971852302551})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.48291417956352234})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3853558897972107})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3433998227119446})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3181229829788208})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3324491083621979})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2807079553604126})
store['active_learning_steps'][58]['eval_training']['best_epoch']=7
store['active_learning_steps'][58]['acquisition']={'indices': [32335, 26850, 56561, 36361, 56773, 30725, 23505, 32914, 49890, 21880], 'labels': [1, 2, -1, -1, 9, -1, -1, -1, 5, 2], 'scores': [0.5534297823905945, 0.5870364904403687, 0.5737414360046387, 0.2726786136627197, 0.5351244211196899, 0.42514777183532715, 0.454983115196228, 0.2974262237548828, 0.5576478838920593, 0.6083376407623291]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.188903570175171})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.540024995803833})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4149543046951294})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30106115341186523})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2996894121170044})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2922554314136505})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31078046560287476})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30493295192718506})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2966405749320984})
store['active_learning_steps'][59]['training']['best_epoch']=6
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.967, 'crossentropy': 0.2751341552734375}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6804468035697937})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4786731004714966})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3595275580883026})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3636452555656433})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3154907822608948})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2899955213069916})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3099551796913147})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27013179659843445})
store['active_learning_steps'][59]['eval_training']['best_epoch']=8
store['active_learning_steps'][59]['acquisition']={'indices': [22675, 59475, 38242, 23546, 202, 42504, 9472, 22283, 56254, 54950], 'labels': [3, -1, 7, 5, 8, 8, 2, 9, 8, 8], 'scores': [0.34858161211013794, 0.47236859798431396, 0.49113303422927856, 0.599913477897644, 0.38230234384536743, 0.4838986396789551, 0.4619848132133484, 0.41548341512680054, 0.6529428958892822, 0.5703495740890503]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.2085187435150146})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5667295455932617})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3935438394546509})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31834930181503296})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3078915774822235})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2797435522079468})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3029002547264099})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.262592613697052})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2826129198074341})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28465554118156433})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2720944881439209})
store['active_learning_steps'][60]['training']['best_epoch']=8
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9722, 'crossentropy': 0.263457470703125}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6579290628433228})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.43747812509536743})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37436196208000183})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33100417256355286})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29757368564605713})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.267300546169281})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2771017253398895})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.22883307933807373})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2554992437362671})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24244214594364166})
store['active_learning_steps'][60]['eval_training']['best_epoch']=8
store['active_learning_steps'][60]['acquisition']={'indices': [29143, 1870, 12514, 24151, 19328, 8207, 47655, 19837, 4000, 52012], 'labels': [-1, 3, 2, -1, 5, 4, 3, -1, -1, 8], 'scores': [0.5699858665466309, 0.38651442527770996, 0.5185734629631042, 0.291520357131958, 0.39577388763427734, 0.28801393508911133, 0.427048921585083, 0.5828847885131836, 0.322550892829895, 0.37394821643829346]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.2263233661651611})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5944939851760864})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3850281834602356})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36998894810676575})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3268771767616272})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30766060948371887})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29284578561782837})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26730361580848694})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26838362216949463})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26683130860328674})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2993823289871216})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2835862636566162})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26069092750549316})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2771533727645874})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29310697317123413})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2972967326641083})
store['active_learning_steps'][61]['training']['best_epoch']=13
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9741, 'crossentropy': 0.2542589599609375}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7086289525032043})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.44198957085609436})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.34707945585250854})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3103289306163788})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3037979304790497})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2703288793563843})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.23979026079177856})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.24419882893562317})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2216583639383316})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.21794813871383667})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.20781269669532776})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.22328338027000427})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23439791798591614})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2100466787815094})
store['active_learning_steps'][61]['eval_training']['best_epoch']=11
store['active_learning_steps'][61]['acquisition']={'indices': [15983, 49460, 39841, 55268, 45982, 47891, 26863, 56453, 4058, 16847], 'labels': [-1, -1, -1, -1, 4, -1, -1, -1, -1, -1], 'scores': [0.4501953125, 0.602652907371521, 0.6214812994003296, 0.5599281787872314, 0.3763866424560547, 0.4781198501586914, 0.6768492460250854, 0.4676370620727539, 0.31369709968566895, 0.29601800441741943]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.1782236099243164})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5985307693481445})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4237469732761383})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3406144976615906})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2940429747104645})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2605118751525879})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.255950927734375})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2603492736816406})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25215020775794983})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2663760781288147})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2539043724536896})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26772838830947876})
store['active_learning_steps'][62]['training']['best_epoch']=9
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.2477054443359375}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6032165288925171})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4444471299648285})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35805410146713257})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30339887738227844})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3064117431640625})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2653402090072632})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2370918244123459})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2655175030231476})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24359817802906036})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2371331751346588})
store['active_learning_steps'][62]['eval_training']['best_epoch']=7
store['active_learning_steps'][62]['acquisition']={'indices': [54019, 15841, 20820, 11017, 32776, 5359, 4129, 32797, 25150, 21573], 'labels': [-1, -1, 9, -1, 4, -1, 1, -1, -1, -1], 'scores': [0.3983737826347351, 0.4454399347305298, 0.6878908276557922, 0.44124269485473633, 0.6159400343894958, 0.4437757730484009, 0.5150002837181091, 0.522841215133667, 0.523756742477417, 0.4147815704345703]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0952298641204834})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5520260334014893})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3737841844558716})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29537394642829895})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3168606758117676})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27553078532218933})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2536393702030182})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2937084436416626})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27572202682495117})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24370424449443817})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25553205609321594})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2435571849346161})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.29033684730529785})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2805279493331909})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30123600363731384})
store['active_learning_steps'][63]['training']['best_epoch']=12
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9734, 'crossentropy': 0.24306220703125}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7704190015792847})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4403548240661621})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.33036166429519653})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32211142778396606})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2832469940185547})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2601446509361267})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25665852427482605})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2484612762928009})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2239619344472885})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.24438315629959106})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.22984838485717773})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.21800044178962708})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.22930364310741425})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.21715962886810303})
store['active_learning_steps'][63]['eval_training']['best_epoch']=14
store['active_learning_steps'][63]['acquisition']={'indices': [1674, 57718, 21944, 966, 33433, 29967, 57728, 42106, 24533, 23028], 'labels': [9, 7, 1, 3, -1, 2, 9, -1, 8, 2], 'scores': [0.6005560159683228, 0.6023446917533875, 0.27922534942626953, 0.5497409105300903, 0.5088382959365845, 0.38582730293273926, 0.7482830286026001, 0.4579275846481323, 0.43892723321914673, 0.5645481646060944]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0857651233673096})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5256253480911255})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3184968829154968})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30847474932670593})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2886675298213959})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2765280306339264})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.24565595388412476})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2345118671655655})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23012199997901917})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24465438723564148})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2684251368045807})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.2553218901157379})
store['active_learning_steps'][64]['training']['best_epoch']=9
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9748, 'crossentropy': 0.2331469970703125}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6551547050476074})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.41106492280960083})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35151153802871704})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3141195774078369})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2795112133026123})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25252410769462585})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2627781927585602})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2355124056339264})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23536062240600586})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23492905497550964})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24607381224632263})
store['active_learning_steps'][64]['eval_training']['best_epoch']=10
store['active_learning_steps'][64]['acquisition']={'indices': [18585, 54907, 42973, 56800, 45502, 42793, 5247, 59111, 27120, 13945], 'labels': [-1, -1, 4, 9, 1, -1, 2, -1, 2, -1], 'scores': [0.3483160734176636, 0.36348462104797363, 0.6182824969291687, 0.5245838165283203, 0.4483572840690613, 0.44640278816223145, 0.5796740055084229, 0.44756603240966797, 0.6066352128982544, 0.45580559968948364]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.066755771636963})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5663541555404663})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.35411882400512695})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27269312739372253})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28961417078971863})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26385900378227234})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2523881793022156})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2532718777656555})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2532774806022644})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2622312307357788})
store['active_learning_steps'][65]['training']['best_epoch']=7
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9732, 'crossentropy': 0.2490853271484375}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6801127195358276})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.46471166610717773})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3716791868209839})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.29979681968688965})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2806307375431061})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25961852073669434})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2675676941871643})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24110600352287292})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.22399179637432098})
store['active_learning_steps'][65]['eval_training']['best_epoch']=9
store['active_learning_steps'][65]['acquisition']={'indices': [14751, 55043, 10987, 23027, 13584, 49947, 31512, 29018, 37884, 41378], 'labels': [8, -1, -1, -1, -1, -1, 2, -1, -1, -1], 'scores': [0.37303781509399414, 0.5988748073577881, 0.4587981700897217, 0.5672142505645752, 0.5493136048316956, 0.5170643925666809, 0.3170185089111328, 0.4502764940261841, 0.4624992609024048, 0.5457974672317505]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1588544845581055})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5938122272491455})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.4145693778991699})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3330560326576233})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2831392288208008})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28248631954193115})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2663814425468445})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2737147808074951})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.24560467898845673})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.26622554659843445})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.25125592947006226})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2678089141845703})
store['active_learning_steps'][66]['training']['best_epoch']=9
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9723, 'crossentropy': 0.254756982421875}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6753929853439331})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.47051647305488586})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3792913556098938})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32564303278923035})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.292522668838501})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29522866010665894})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26983094215393066})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25574246048927307})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25295594334602356})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26626741886138916})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2366494983434677})
store['active_learning_steps'][66]['eval_training']['best_epoch']=11
store['active_learning_steps'][66]['acquisition']={'indices': [34666, 34121, 26707, 59390, 51163, 4594, 5559, 57137, 28254, 2699], 'labels': [-1, -1, 7, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.25298839807510376, 0.5694235563278198, 0.4156862497329712, 0.3730008602142334, 0.5009297132492065, 0.5024781227111816, 0.31904661655426025, 0.3020116090774536, 0.4571056365966797, 0.42038941383361816]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.1262516975402832})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.577459990978241})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3587339520454407})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3325560688972473})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2639654874801636})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2767041325569153})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2928011417388916})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.278756707906723})
store['active_learning_steps'][67]['training']['best_epoch']=5
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9708, 'crossentropy': 0.2807148681640625}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6726628541946411})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4640358090400696})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3905571699142456})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31899893283843994})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33856263756752014})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3055027723312378})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.31787800788879395})
store['active_learning_steps'][67]['eval_training']['best_epoch']=6
store['active_learning_steps'][67]['acquisition']={'indices': [44506, 44406, 28306, 22272, 48065, 29711, 10992, 56163, 56255, 43476], 'labels': [-1, -1, -1, 5, 3, 8, -1, -1, -1, 3], 'scores': [0.2942211627960205, 0.3109167814254761, 0.4363051652908325, 0.5084604620933533, 0.523655116558075, 0.466361403465271, 0.49900615215301514, 0.27937233448028564, 0.39454495906829834, 0.4106019139289856]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.1506776809692383})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5676553845405579})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43281394243240356})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3471972346305847})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2769298553466797})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2967537045478821})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28688615560531616})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2847449779510498})
store['active_learning_steps'][68]['training']['best_epoch']=5
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9699, 'crossentropy': 0.285801611328125}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6856427192687988})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.45859092473983765})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36161190271377563})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3278621435165405})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30853480100631714})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.329831063747406})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32724428176879883})
store['active_learning_steps'][68]['eval_training']['best_epoch']=5
store['active_learning_steps'][68]['acquisition']={'indices': [55881, 20037, 11938, 39746, 50342, 2818, 56162, 29286, 591, 4475], 'labels': [3, 8, 9, -1, 8, 3, 6, 9, -1, 5], 'scores': [0.37880510091781616, 0.38394856452941895, 0.40171170234680176, 0.3100373148918152, 0.4525502920150757, 0.3619436025619507, 0.3795463442802429, 0.43099188804626465, 0.26695096492767334, 0.45125168561935425]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 1.073257565498352})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5357528328895569})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4381852149963379})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3820517063140869})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30872827768325806})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.271701455116272})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2610247731208801})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25019586086273193})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2826712727546692})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28741392493247986})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.269162654876709})
store['active_learning_steps'][69]['training']['best_epoch']=8
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9775, 'crossentropy': 0.2409639892578125}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7233063578605652})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.45069506764411926})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3355036675930023})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30983999371528625})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2980380654335022})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26759597659111023})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2557891011238098})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23570847511291504})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.258456826210022})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24238529801368713})
store['active_learning_steps'][69]['eval_training']['best_epoch']=8
store['active_learning_steps'][69]['acquisition']={'indices': [56747, 56255, 37077, 9687, 16676, 44598, 7168, 4638, 9476, 57328], 'labels': [-1, -1, -1, 0, 3, 0, 8, 3, -1, -1], 'scores': [0.41713929176330566, 0.564767599105835, 0.29281461238861084, 0.6450739502906799, 0.4103071689605713, 0.843015044927597, 0.5721024870872498, 0.5802592039108276, 0.39737212657928467, 0.3056814670562744]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.1340832710266113})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.5763317346572876})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.39501500129699707})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3186662793159485})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26954448223114014})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2917294204235077})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24213998019695282})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2322496771812439})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24488791823387146})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2818502187728882})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2721354067325592})
store['active_learning_steps'][70]['training']['best_epoch']=8
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.975, 'crossentropy': 0.234400634765625}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7998378276824951})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.41637489199638367})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.34885090589523315})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32532012462615967})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26941239833831787})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2782026529312134})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2636004686355591})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23987045884132385})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.25692471861839294})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.21966242790222168})
store['active_learning_steps'][70]['eval_training']['best_epoch']=10
store['active_learning_steps'][70]['acquisition']={'indices': [32980, 16162, 53568, 47558, 5683, 23853, 4050, 46887, 48160, 54167], 'labels': [-1, -1, 5, 4, 3, 9, 9, -1, -1, -1], 'scores': [0.3175874948501587, 0.42615360021591187, 0.44409477710723877, 0.4193737506866455, 0.5328835248947144, 0.3589172959327698, 0.5712234973907471, 0.38516831398010254, 0.6532713770866394, 0.4859185218811035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.2503552436828613})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5963347554206848})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3941379189491272})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33225587010383606})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30687516927719116})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2797081470489502})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2730284035205841})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24556349217891693})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2654295265674591})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2856578230857849})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.23957720398902893})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9794921875, 'crossentropy': 0.2384285181760788})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2526138424873352})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2625301778316498})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.23134101927280426})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.24192601442337036})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2695867717266083})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26402315497398376})
store['active_learning_steps'][71]['training']['best_epoch']=15
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9766, 'crossentropy': 0.2440245361328125}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6039525866508484})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.40510880947113037})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.32746607065200806})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31207138299942017})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27655917406082153})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2571509778499603})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24769428372383118})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25281640887260437})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.23887881636619568})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.20751962065696716})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.21452465653419495})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.24293957650661469})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.19484470784664154})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2187717854976654})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.21186360716819763})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.1807834506034851})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.19704300165176392})
store['active_learning_steps'][71]['eval_training']['best_epoch']=16
store['active_learning_steps'][71]['acquisition']={'indices': [42153, 39146, 56514, 37168, 48102, 38246, 30751, 22429, 33721, 12198], 'labels': [0, -1, 2, 7, 7, 7, 0, -1, -1, -1], 'scores': [0.4786396026611328, 0.6965410709381104, 0.727524995803833, 0.3894311785697937, 0.8580498099327087, 0.5643489360809326, 0.5662702322006226, 0.38749051094055176, 0.5307497978210449, 0.6362501978874207]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.1917381286621094})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6461420059204102})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37484225630760193})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3045620918273926})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3251010775566101})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.28694653511047363})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.29835113883018494})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.24824248254299164})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2373599112033844})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26489779353141785})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2630177438259125})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.978515625, 'crossentropy': 0.2531619369983673})
store['active_learning_steps'][72]['training']['best_epoch']=9
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9804, 'crossentropy': 0.21960224609375}
