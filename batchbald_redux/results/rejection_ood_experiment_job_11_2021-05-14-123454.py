store = {}
store['timestamp']=1620992094
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=11']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=11
store['worker_id']=11
store['num_workers']=20
store['config']={'seed': 1250, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 1000, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.2054038047790527})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.5043344497680664})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.852696418762207})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.7694244384765625})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6765, 'crossentropy': 2.0107125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.154167890548706})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1484808921813965})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.12113356590271})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [34245, 47587, 39669, 47683, 28940, 17546, 33827, 12351, 4929, 1724], 'labels': [7, 3, -1, 5, -1, 6, 8, 0, -1, 2], 'scores': [0.4768218994140625, 0.8988175392150879, 0.46037256717681885, 0.8921629190444946, 0.5941917896270752, 0.8252847790718079, 0.8327555656433105, 0.7459602355957031, 0.34447646141052246, 0.7363766431808472]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.7436268329620361})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.7952247858047485})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 2.102169990539551})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 2.2172696590423584})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7557, 'crossentropy': 1.5415958984375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 0.9999811053276062})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.917345404624939})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9521598815917969})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [27228, 58243, 5175, 30099, 48372, 4803, 7897, 22705, 48668, 8655], 'labels': [5, 9, 4, 9, 8, 8, 2, 1, 8, 7], 'scores': [0.5813825726509094, 0.5809025168418884, 0.5423986911773682, 0.6563963890075684, 0.58026123046875, 0.8218101263046265, 0.6344696283340454, 0.45875054597854614, 0.7303665280342102, 0.6339194178581238]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.2015881538391113})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 1.3871376514434814})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.6294536590576172})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.7263144254684448})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7912, 'crossentropy': 1.10523837890625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 0.8718740940093994})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 0.8067606091499329})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.8016769886016846})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [15829, 42933, 48096, 38608, 19847, 56362, 32261, 24726, 22717, 17583], 'labels': [2, 4, 7, 5, 2, 0, 8, 6, 3, 5], 'scores': [0.516403317451477, 0.4170578718185425, 0.6145760416984558, 0.805067777633667, 0.5660871267318726, 0.7774237990379333, 0.3347654938697815, 0.733465313911438, 0.5591901540756226, 0.6643422842025757]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.1131036281585693})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.3208000659942627})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.379225492477417})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.4929556846618652})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7949, 'crossentropy': 1.08381513671875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 0.9008547067642212})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.7589035034179688})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 0.7658704519271851})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [11041, 56940, 22497, 12778, 42509, 6959, 1007, 11538, 11539, 7168], 'labels': [0, 0, 7, 8, -1, 3, 3, 9, 3, 8], 'scores': [0.41966676712036133, 0.4459983706474304, 0.5562261343002319, 0.2636330723762512, 0.25839412212371826, 0.46038830280303955, 0.2947847843170166, 0.4828954339027405, 0.3807758092880249, 0.6205362677574158]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.0913124084472656})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.2020965814590454})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.4270706176757812})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.307647943496704})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.8056, 'crossentropy': 1.05392705078125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.869369626045227})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.8001380562782288})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.7973934412002563})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [693, 4416, 1213, 14321, 42669, 57842, 10554, 15113, 3414, 26938], 'labels': [2, 5, 2, 1, 3, 6, 2, 7, 9, -1], 'scores': [0.5476915836334229, 0.46136754751205444, 0.5595506429672241, 0.5485628843307495, 0.4619307816028595, 0.46750688552856445, 0.3819299042224884, 0.47317731380462646, 0.3093451261520386, 0.37331223487854004]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.048059344291687})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.1442723274230957})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.2813935279846191})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.4080772399902344})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8148, 'crossentropy': 0.96115087890625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.8451691269874573})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.8155025243759155})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.7445353269577026})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [14341, 55743, 43571, 47347, 14720, 14537, 22678, 41838, 14851, 6582], 'labels': [9, 3, 4, 4, 4, 4, 9, 4, 3, 8], 'scores': [0.47417062520980835, 0.6478811502456665, 0.4349043369293213, 0.47243720293045044, 0.615937352180481, 0.5523089170455933, 0.44461554288864136, 0.527794599533081, 0.28545325994491577, 0.49546682834625244]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8037109375, 'crossentropy': 0.9234681129455566})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9097842574119568})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0208961963653564})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9956314563751221})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0933222770690918})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8653, 'crossentropy': 0.8178166015625}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7495124340057373})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6273198127746582})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.5941982865333557})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.620956540107727})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [46288, 14540, 21500, 30530, 7797, 6546, 26325, 42963, 47509, 26866], 'labels': [2, 7, 4, 2, 8, 4, 2, 9, 6, 3], 'scores': [0.6205222606658936, 0.5236912369728088, 0.29516690969467163, 0.5988643169403076, 0.5822319984436035, 0.4636218547821045, 0.6000155806541443, 0.5571643114089966, 0.3650171756744385, 0.3890889286994934]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8662087917327881})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8534089922904968})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9619477987289429})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9183936715126038})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9745988845825195})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8856, 'crossentropy': 0.74798798828125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7613241672515869})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5845404863357544})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.5785346627235413})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.5576708316802979})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [43612, 22543, 51052, 53170, 37275, 15858, 13108, 49050, 50983, 39457], 'labels': [4, 8, -1, 8, 5, 9, 9, 4, -1, 0], 'scores': [0.4910379648208618, 0.6012985110282898, 0.37454521656036377, 0.49754011631011963, 0.4283825755119324, 0.4426812529563904, 0.4104614853858948, 0.5450226664543152, 0.4107661247253418, 0.5130351781845093]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8448103666305542})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7502461671829224})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7826633453369141})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7941329479217529})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.8472402095794678})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8968, 'crossentropy': 0.667680712890625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6633579730987549})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.5738681554794312})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5378446578979492})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5513062477111816})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [7977, 8932, 7098, 25669, 27130, 50847, 4639, 16114, 33574, 34362], 'labels': [9, 0, 9, 5, 9, 1, 1, 8, -1, -1], 'scores': [0.37668997049331665, 0.6261206865310669, 0.5680467486381531, 0.47032904624938965, 0.473827600479126, 0.41253364086151123, 0.38286060094833374, 0.5443205237388611, 0.3090064525604248, 0.3460782766342163]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.907207727432251})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7466459274291992})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7637971639633179})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7610083818435669})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.8101671934127808})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8966, 'crossentropy': 0.6700712890625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7593185901641846})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5866221189498901})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5802425742149353})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5438482761383057})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [15066, 32240, 16832, 55645, 20718, 20476, 13894, 41147, 42141, 20853], 'labels': [-1, 6, 5, 6, 5, 5, 3, 5, 5, 5], 'scores': [0.2568082809448242, 0.5184758305549622, 0.4985603094100952, 0.35410115122795105, 0.48821789026260376, 0.46174174547195435, 0.5412267446517944, 0.5106453895568848, 0.6086857318878174, 0.4800758957862854]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7936586141586304})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5956526398658752})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6878398060798645})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6775792837142944})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7678626775741577})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9175, 'crossentropy': 0.53808642578125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6392903327941895})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5474443435668945})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4598066210746765})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.47315001487731934})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [55614, 53044, 36415, 28262, 59919, 47090, 4081, 20235, 11921, 21642], 'labels': [-1, 9, 6, 9, 1, -1, 7, 9, 3, 4], 'scores': [0.31502586603164673, 0.4978492259979248, 0.5052515268325806, 0.34726476669311523, 0.5295578241348267, 0.38682448863983154, 0.45545339584350586, 0.4133906364440918, 0.4445701241493225, 0.466325044631958]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7098480463027954})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6465164422988892})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5984703302383423})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6146873235702515})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5684560537338257})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6669025421142578})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6512053608894348})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6931416988372803})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9291, 'crossentropy': 0.51033974609375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6281288862228394})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.45648425817489624})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4671492874622345})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4180794060230255})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.356892466545105})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.38064491748809814})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.37433573603630066})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [31117, 23086, 9554, 24689, 45701, 23320, 44820, 43952, 12782, 27931], 'labels': [-1, 8, 8, -1, -1, 3, -1, -1, 8, -1], 'scores': [0.48060762882232666, 0.5113193392753601, 0.6609806418418884, 0.3646676540374756, 0.3421837091445923, 0.502159059047699, 0.5201495885848999, 0.438413143157959, 0.7393940091133118, 0.31442761421203613]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7161155939102173})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5597698092460632})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5666251182556152})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6134406328201294})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.612623929977417})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9281, 'crossentropy': 0.47553994140625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6970365643501282})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5091238617897034})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5189874172210693})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4603721499443054})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [41160, 31349, 57210, 21455, 2248, 35231, 52866, 31758, 50114, 16631], 'labels': [6, 3, 8, 5, 5, -1, 7, 8, 8, 8], 'scores': [0.37372374534606934, 0.3971058130264282, 0.36116504669189453, 0.4658501148223877, 0.5259160995483398, 0.30718880891799927, 0.5138068795204163, 0.35147637128829956, 0.36308640241622925, 0.3864067792892456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8459571599960327})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.567208468914032})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5890803337097168})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6143296957015991})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5226526260375977})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6357332468032837})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6165903806686401})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6332284212112427})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9382, 'crossentropy': 0.500756689453125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6564903259277344})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.49613258242607117})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4003015160560608})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.3944913148880005})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.36728256940841675})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3786062002182007})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3698926568031311})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [20072, 23478, 1106, 55060, 26879, 24783, 31644, 29306, 7659, 49016], 'labels': [3, 4, -1, 5, -1, -1, -1, -1, 5, 8], 'scores': [0.8434230089187622, 0.4966800808906555, 0.4277118444442749, 0.5337631702423096, 0.7010840177536011, 0.3732863664627075, 0.37235724925994873, 0.5622038841247559, 0.4592706859111786, 0.4910852611064911]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8066035509109497})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4910191297531128})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5241031646728516})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5133951306343079})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6208807826042175})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9345, 'crossentropy': 0.442550390625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6592899560928345})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5093408823013306})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.46367934346199036})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4952133893966675})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [13030, 9158, 57956, 44706, 2542, 43833, 4580, 34930, 31047, 35794], 'labels': [0, 0, 2, 5, 4, 3, -1, 9, -1, 3], 'scores': [0.6384906768798828, 0.538948118686676, 0.4456695318222046, 0.4024190604686737, 0.4598669409751892, 0.40753233432769775, 0.3187011480331421, 0.47089827060699463, 0.32243812084198, 0.47275328636169434]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.870388388633728})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5195627212524414})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.508080005645752})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.561639666557312})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5541396737098694})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.532463550567627})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9386, 'crossentropy': 0.44196826171875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5961490869522095})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4804782271385193})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4484631419181824})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4183627963066101})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.37275272607803345})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [4822, 40184, 17540, 15519, 8693, 58172, 49088, 7207, 1429, 18042], 'labels': [4, 3, 1, -1, 3, -1, 8, 2, -1, 0], 'scores': [0.5387513041496277, 0.48360133171081543, 0.6288999915122986, 0.3112983703613281, 0.45205938816070557, 0.3129845857620239, 0.5337290167808533, 0.5670222043991089, 0.4033842086791992, 0.5558006167411804]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0899837017059326})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6315776109695435})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5718411803245544})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5811959505081177})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5970796942710876})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5657394528388977})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.7126271724700928})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6140223741531372})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.6045847535133362})
store['active_learning_steps'][16]['training']['best_epoch']=6
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9436, 'crossentropy': 0.48381396484375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6159274578094482})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.45769885182380676})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3674734830856323})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.39731699228286743})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3517846465110779})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.34662705659866333})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.31311190128326416})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.32652267813682556})
store['active_learning_steps'][16]['eval_training']['best_epoch']=7
store['active_learning_steps'][16]['acquisition']={'indices': [3382, 35406, 55481, 39778, 17555, 49196, 32909, 54756, 1143, 3798], 'labels': [9, 5, 0, 8, -1, 4, 9, 2, 2, 7], 'scores': [0.9114668965339661, 0.613716721534729, 0.5431628227233887, 0.6667637228965759, 0.2812848687171936, 0.593608170747757, 0.5963593125343323, 0.6836709976196289, 0.39636117219924927, 0.6620006561279297]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8485522866249084})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5942971706390381})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5621301531791687})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4834985136985779})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5274522304534912})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5495850443840027})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5318559408187866})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9451, 'crossentropy': 0.4083395751953125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6305917501449585})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4561634063720703})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4112219512462616})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.36574238538742065})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.37351274490356445})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.35757923126220703})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [424, 50520, 58832, 19586, 28844, 8110, 19179, 37397, 43953, 15746], 'labels': [9, -1, 3, 9, 2, 0, -1, 3, -1, 9], 'scores': [0.5849640965461731, 0.37149399518966675, 0.6028890013694763, 0.5644952058792114, 0.5220149755477905, 0.6237114071846008, 0.3934643268585205, 0.46803557872772217, 0.4488511085510254, 0.456232488155365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0589838027954102})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.524274468421936})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5250511169433594})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.48262351751327515})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5331945419311523})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5304028987884521})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5247101783752441})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9412, 'crossentropy': 0.42885947265625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6534990072250366})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.48333740234375})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.39876699447631836})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3879755139350891})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.39250102639198303})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.3482931852340698})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [43063, 16836, 2092, 24347, 6268, 16890, 13896, 59187, 39330, 520], 'labels': [-1, 7, 3, 2, -1, -1, 0, -1, -1, -1], 'scores': [0.36595749855041504, 0.7017025351524353, 0.6236003637313843, 0.5721139311790466, 0.5226832628250122, 0.31734955310821533, 0.31176918745040894, 0.534294068813324, 0.3541601896286011, 0.5230569839477539]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8412333726882935})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5321931838989258})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4519204795360565})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.45710206031799316})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.46856456995010376})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4544726014137268})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9452, 'crossentropy': 0.4168748046875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5855766534805298})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4987941086292267})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.42526885867118835})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4025731086730957})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4023054242134094})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [33469, 26938, 10028, 32926, 31650, 41309, 34785, 4797, 2588, 44328], 'labels': [2, 6, 9, 8, 5, -1, 8, 8, 6, 9], 'scores': [0.5154396891593933, 0.42220088839530945, 0.6212300062179565, 0.4932570457458496, 0.6511346697807312, 0.3087332248687744, 0.6268116235733032, 0.7465819120407104, 0.39230722188949585, 0.5038796067237854]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9028635621070862})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5145764946937561})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4886620044708252})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.46791547536849976})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.43829962611198425})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.47820812463760376})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5264831781387329})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5097708106040955})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9492, 'crossentropy': 0.4088929931640625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5874379277229309})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4470351040363312})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3579484224319458})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.34247010946273804})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3097866177558899})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3254677355289459})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3137360215187073})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [13195, 57976, 27254, 46759, 1244, 18752, 9661, 30838, 24904, 4955], 'labels': [-1, 2, 7, -1, 3, -1, 8, 9, 1, 2], 'scores': [0.4627229571342468, 0.4579949975013733, 0.33449089527130127, 0.4170200228691101, 0.4401624798774719, 0.2276928424835205, 0.4464520812034607, 0.475821852684021, 0.5876770615577698, 0.7669272422790527]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9529279470443726})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5990843176841736})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5129942893981934})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5756819844245911})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5281739234924316})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5431703329086304})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9387, 'crossentropy': 0.43954013671875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6149069666862488})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.4996407628059387})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.42265018820762634})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4100385308265686})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.40260136127471924})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [57718, 37344, 17096, 18527, 53379, 44830, 15372, 45389, 26426, 54476], 'labels': [7, 8, -1, 3, 9, 5, 3, 3, -1, 3], 'scores': [0.573904275894165, 0.470146119594574, 0.45910048484802246, 0.4024782180786133, 0.4333898425102234, 0.3655969500541687, 0.602960467338562, 0.5250022411346436, 0.27984511852264404, 0.4630357623100281]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.081059217453003})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5697733163833618})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.463447630405426})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.46101534366607666})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.49300581216812134})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.5085800886154175})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42753779888153076})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.45980069041252136})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.44273608922958374})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5269056558609009})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9512, 'crossentropy': 0.4084082763671875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6187412738800049})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.41588830947875977})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.37490975856781006})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34745657444000244})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.32914865016937256})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.33474671840667725})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.2935718595981598})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34932011365890503})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30847835540771484})
store['active_learning_steps'][22]['eval_training']['best_epoch']=7
store['active_learning_steps'][22]['acquisition']={'indices': [4650, 53873, 1404, 4530, 17337, 32473, 32747, 42966, 1250, 51764], 'labels': [-1, 4, 8, 7, -1, 8, 8, -1, -1, -1], 'scores': [0.49395084381103516, 0.5314854383468628, 0.5613784193992615, 0.5959869623184204, 0.42465484142303467, 0.499897837638855, 0.5049043297767639, 0.35356491804122925, 0.4843190908432007, 0.35757869482040405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.9953433871269226})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5907620191574097})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.47955143451690674})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5052139163017273})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4978047013282776})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.48752546310424805})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9459, 'crossentropy': 0.41410087890625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.687132716178894})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4516496956348419})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.43585458397865295})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.40864062309265137})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.40656644105911255})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [48765, 58286, 5884, 23629, 2858, 43144, 48548, 10275, 42437, 17478], 'labels': [-1, 1, -1, 5, -1, -1, -1, 6, 9, 4], 'scores': [0.43504446744918823, 0.2883220314979553, 0.4393885135650635, 0.5436347723007202, 0.38994020223617554, 0.527482271194458, 0.2919803261756897, 0.5112237930297852, 0.6192694008350372, 0.520915150642395]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.994545578956604})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5396658182144165})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.45871907472610474})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.420460045337677})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.462377667427063})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.45874422788619995})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4362332224845886})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9541, 'crossentropy': 0.3538566650390625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7375745177268982})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.45660141110420227})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4241939187049866})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4160611629486084})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.36514025926589966})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.39578160643577576})
store['active_learning_steps'][24]['eval_training']['best_epoch']=5
store['active_learning_steps'][24]['acquisition']={'indices': [50320, 35694, 14384, 32668, 43950, 12484, 15739, 17673, 45761, 6044], 'labels': [5, 9, -1, 9, 9, 5, 8, 3, 4, 2], 'scores': [0.541996419429779, 0.2720387578010559, 0.5428375005722046, 0.5192397236824036, 0.6351200342178345, 0.40901660919189453, 0.39210712909698486, 0.5398939251899719, 0.62400221824646, 0.5354229211807251]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.1681621074676514})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5577144622802734})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.444141149520874})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4459385275840759})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4371320605278015})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.46019500494003296})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.452251136302948})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5199077129364014})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9527, 'crossentropy': 0.393341796875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6814225912094116})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.45648840069770813})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.38216862082481384})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3426307737827301})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37003186345100403})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3378256559371948})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3454493284225464})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [29875, 50170, 12196, 42876, 44590, 2022, 34378, 16902, 31468, 58470], 'labels': [-1, -1, 2, -1, 7, -1, 7, -1, 8, 9], 'scores': [0.5013445019721985, 0.6139254570007324, 0.6927786469459534, 0.5419385433197021, 0.4481704831123352, 0.42660951614379883, 0.7182204127311707, 0.33512675762176514, 0.38727253675460815, 0.7607537508010864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.032688856124878})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5143015384674072})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.43864092230796814})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4101581573486328})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5040011405944824})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3880798816680908})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.45129165053367615})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4684583246707916})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4488678574562073})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.955, 'crossentropy': 0.355346142578125}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.628697395324707})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4680502116680145})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36612921953201294})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.34674763679504395})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32613176107406616})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3007136583328247})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.2894672155380249})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3122156858444214})
store['active_learning_steps'][26]['eval_training']['best_epoch']=7
store['active_learning_steps'][26]['acquisition']={'indices': [20874, 54083, 13998, 24879, 19840, 22064, 26405, 49002, 22734, 57597], 'labels': [-1, 0, 9, -1, -1, -1, -1, 1, 5, 2], 'scores': [0.5310428142547607, 0.5756233036518097, 0.6228550672531128, 0.36790454387664795, 0.4521753787994385, 0.49444615840911865, 0.5471099615097046, 0.650061309337616, 0.3875722885131836, 0.6540499925613403]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.0428240299224854})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.513387143611908})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4143688380718231})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3658735752105713})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.41308072209358215})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.37601280212402344})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.40434521436691284})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9574, 'crossentropy': 0.35121796875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6427593231201172})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4399043321609497})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.429923951625824})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.38997358083724976})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3406389653682709})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.34588366746902466})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [28432, 14629, 17552, 46446, 234, 10136, 51260, 23189, 44923, 11177], 'labels': [-1, -1, -1, 0, 0, -1, -1, -1, -1, -1], 'scores': [0.31950855255126953, 0.3551872968673706, 0.40358996391296387, 0.5461936891078949, 0.4042695164680481, 0.39343929290771484, 0.2963089942932129, 0.4109855890274048, 0.41183924674987793, 0.313088059425354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.073357343673706})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5203922986984253})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4253357946872711})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41566503047943115})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40401145815849304})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.45396488904953003})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4666038751602173})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4473784565925598})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9586, 'crossentropy': 0.3421420166015625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.617405891418457})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4769589304924011})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3750886619091034})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.35180360078811646})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3118310570716858})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2895682454109192})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.29620444774627686})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [40752, 39164, 59868, 7768, 35931, 55199, 58101, 45580, 46159, 44339], 'labels': [3, -1, -1, 8, -1, -1, 4, 6, -1, -1], 'scores': [0.6590042114257812, 0.4046863913536072, 0.41311925649642944, 0.585930347442627, 0.48441368341445923, 0.4261510968208313, 0.4663010835647583, 0.35971495509147644, 0.3962087631225586, 0.39014768600463867]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0994147062301636})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5036106705665588})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4422929883003235})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.42756175994873047})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.44015586376190186})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.45728421211242676})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4696948230266571})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9507, 'crossentropy': 0.36700361328125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6560722589492798})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4419270157814026})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42812734842300415})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.36421212553977966})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3454166650772095})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3431784510612488})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [8459, 54394, 48130, 52938, 32080, 5616, 35884, 37193, 45410, 6911], 'labels': [5, 8, -1, 2, 5, 3, -1, 7, -1, -1], 'scores': [0.4252329468727112, 0.40394264459609985, 0.4657222628593445, 0.47497865557670593, 0.4245620369911194, 0.5033613443374634, 0.3870924711227417, 0.36446070671081543, 0.5080074071884155, 0.43502378463745117]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.9688829779624939})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5443651676177979})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4772610664367676})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4171068072319031})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.42711108922958374})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44966259598731995})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4296419024467468})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9576, 'crossentropy': 0.3442904296875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7249290943145752})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5189129114151001})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4048728942871094})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3923647999763489})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.32282355427742004})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3313848674297333})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [991, 54986, 18081, 17256, 4860, 36293, 58459, 48160, 15763, 33200], 'labels': [4, 8, 4, 4, 8, -1, -1, -1, 1, 5], 'scores': [0.48123300075531006, 0.5196889042854309, 0.23156383633613586, 0.42474499344825745, 0.37919479608535767, 0.33735108375549316, 0.33632892370224, 0.5248676538467407, 0.4024866223335266, 0.5309992134571075]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.038271427154541})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.550171971321106})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37856340408325195})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3869437575340271})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3679235577583313})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3598476052284241})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4147327244281769})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.4156251549720764})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.39962705969810486})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9622, 'crossentropy': 0.30225205078125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5978940725326538})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.44716528058052063})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3667754530906677})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3763408958911896})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3300243616104126})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.32011717557907104})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.28960391879081726})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.302048921585083})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [2114, 24210, 2064, 25724, 45029, 24561, 27748, 56086, 44538, 9118], 'labels': [-1, 9, -1, -1, -1, -1, -1, -1, -1, 9], 'scores': [0.4437277317047119, 0.4676893353462219, 0.2618955373764038, 0.39654624462127686, 0.46733319759368896, 0.4882514476776123, 0.30040812492370605, 0.7112078666687012, 0.42106515169143677, 0.7243109345436096]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 0.9842172861099243})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.507527768611908})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4307003617286682})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.40166085958480835})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4309862554073334})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.40445786714553833})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3973733186721802})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3776424527168274})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3918760418891907})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.40977734327316284})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4183688759803772})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9622, 'crossentropy': 0.31643974609375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.644008994102478})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42923182249069214})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3305695056915283})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3226747512817383})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.304648220539093})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.31518399715423584})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.27936023473739624})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30274730920791626})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2630188465118408})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2807210683822632})
store['active_learning_steps'][32]['eval_training']['best_epoch']=9
store['active_learning_steps'][32]['acquisition']={'indices': [30111, 52184, 40818, 47403, 44482, 23206, 3717, 46174, 29287, 26917], 'labels': [8, -1, -1, 9, -1, 3, -1, 7, -1, -1], 'scores': [0.6116095781326294, 0.32264894247055054, 0.4134625196456909, 0.551389753818512, 0.45633184909820557, 0.4183710813522339, 0.1985151767730713, 0.6178871393203735, 0.6774755120277405, 0.2678055763244629]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0476497411727905})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.49219775199890137})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4091428518295288})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3606351315975189})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3723148703575134})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3963946998119354})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.41013407707214355})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9568, 'crossentropy': 0.322279931640625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6636495590209961})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.47025829553604126})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.39120519161224365})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3837341070175171})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.35044223070144653})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31981366872787476})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [27473, 59726, 48004, 4726, 6278, 38402, 13713, 50334, 17082, 17991], 'labels': [4, -1, 5, -1, -1, -1, 3, -1, 3, -1], 'scores': [0.5910181999206543, 0.3880760669708252, 0.45316579937934875, 0.3228271007537842, 0.5012264251708984, 0.4023383855819702, 0.5493993163108826, 0.43200623989105225, 0.4360547661781311, 0.5072380304336548]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0414175987243652})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4925113022327423})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3943147659301758})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34118127822875977})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.37335819005966187})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36117106676101685})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.353604793548584})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9611, 'crossentropy': 0.33285078125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6524443626403809})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5441241264343262})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40888383984565735})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4178888201713562})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3759192228317261})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3767639100551605})
store['active_learning_steps'][34]['eval_training']['best_epoch']=5
store['active_learning_steps'][34]['acquisition']={'indices': [39877, 29179, 31684, 1930, 33773, 15855, 9726, 23027, 56346, 56838], 'labels': [7, 8, -1, -1, -1, 5, -1, -1, 7, 5], 'scores': [0.3605692982673645, 0.5679317712783813, 0.46131134033203125, 0.3572653532028198, 0.29558128118515015, 0.5555654764175415, 0.41320574283599854, 0.6071816086769104, 0.3948933482170105, 0.46408283710479736]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.2006115913391113})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6294737458229065})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.433057576417923})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3742440938949585})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42962074279785156})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3737301230430603})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.39726513624191284})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4388335943222046})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4269189238548279})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9632, 'crossentropy': 0.3173355712890625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6798992156982422})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4380224347114563})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36391395330429077})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33688485622406006})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.29698073863983154})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.28367435932159424})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.308350145816803})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2979702949523926})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [6466, 48681, 11006, 51295, 59734, 11482, 53567, 58395, 45550, 59726], 'labels': [2, 2, -1, -1, 2, 8, 5, -1, -1, 5], 'scores': [0.5787818431854248, 0.5220202207565308, 0.44561493396759033, 0.528359055519104, 0.5359906554222107, 0.4822573661804199, 0.4928920865058899, 0.3681129813194275, 0.5070724487304688, 0.5928369164466858]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.2994723320007324})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6297544240951538})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4646477997303009})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4290165901184082})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38738390803337097})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.41101258993148804})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.41744232177734375})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3995068073272705})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9599, 'crossentropy': 0.321299267578125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.625993013381958})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4537186026573181})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3665638566017151})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3588283360004425})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3714982867240906})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3203144073486328})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.32477062940597534})
store['active_learning_steps'][36]['eval_training']['best_epoch']=6
store['active_learning_steps'][36]['acquisition']={'indices': [23628, 56217, 16488, 29485, 13488, 19820, 35145, 18312, 3756, 21700], 'labels': [6, -1, 9, -1, -1, -1, -1, -1, 3, 7], 'scores': [0.4235724210739136, 0.5266452431678772, 0.6869900524616241, 0.5507560968399048, 0.4709782600402832, 0.36580395698547363, 0.5789651274681091, 0.4686257839202881, 0.5992439985275269, 0.647955060005188]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.1280810832977295})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5458928346633911})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.42367565631866455})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3735295236110687})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.369853675365448})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.33846813440322876})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.38005292415618896})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.37081801891326904})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3693840503692627})
store['active_learning_steps'][37]['training']['best_epoch']=6
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9622, 'crossentropy': 0.3124218994140625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6255588531494141})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4441576600074768})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.37164145708084106})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3943970501422882})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3559272587299347})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3107806444168091})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2863495945930481})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3087261915206909})
store['active_learning_steps'][37]['eval_training']['best_epoch']=7
store['active_learning_steps'][37]['acquisition']={'indices': [635, 36643, 4842, 40380, 34716, 50357, 34758, 37718, 6239, 8978], 'labels': [5, -1, 7, 1, 3, -1, 8, 3, -1, 2], 'scores': [0.6279799938201904, 0.3676443099975586, 0.5086497068405151, 0.2984970211982727, 0.517705500125885, 0.4188898801803589, 0.5001222491264343, 0.5883619785308838, 0.34458374977111816, 0.3279948830604553]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.247745156288147})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5198171734809875})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3927804231643677})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3472577929496765})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.37075865268707275})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35637545585632324})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38130301237106323})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9581, 'crossentropy': 0.322517578125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6237284541130066})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46632611751556396})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.41033798456192017})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.36830979585647583})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3783758878707886})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38349395990371704})
store['active_learning_steps'][38]['eval_training']['best_epoch']=4
store['active_learning_steps'][38]['acquisition']={'indices': [37489, 15136, 12650, 12874, 49525, 38920, 59909, 17941, 32573, 4459], 'labels': [2, 5, 5, 3, 8, 7, 8, 0, 8, 9], 'scores': [0.5442725419998169, 0.36269521713256836, 0.5328127145767212, 0.3565601110458374, 0.6362820267677307, 0.4645302891731262, 0.3370915651321411, 0.32724863290786743, 0.4732009172439575, 0.4599912166595459]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.2466003894805908})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6258226633071899})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4424291253089905})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.43455779552459717})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3866312801837921})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.37267059087753296})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3504658341407776})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3794761300086975})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.4031140208244324})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.36435896158218384})
store['active_learning_steps'][39]['training']['best_epoch']=7
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9617, 'crossentropy': 0.32189267578125}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7050918340682983})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.42349374294281006})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.40157538652420044})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3509502410888672})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33204108476638794})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33171260356903076})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3489750623703003})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2977951467037201})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2995762228965759})
store['active_learning_steps'][39]['eval_training']['best_epoch']=8
store['active_learning_steps'][39]['acquisition']={'indices': [8443, 6914, 46116, 4601, 23205, 21234, 37065, 49064, 30402, 9191], 'labels': [2, -1, -1, -1, -1, -1, -1, 8, -1, -1], 'scores': [0.5455828309059143, 0.6442779302597046, 0.6226150989532471, 0.5108246803283691, 0.45854055881500244, 0.46620047092437744, 0.6593509912490845, 0.4775562286376953, 0.6096013188362122, 0.4741246700286865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0815534591674805})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5551124811172485})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40210971236228943})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3569243550300598})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38300859928131104})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3297848701477051})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3752974271774292})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3695409893989563})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.4077069163322449})
store['active_learning_steps'][40]['training']['best_epoch']=6
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9642, 'crossentropy': 0.2910193359375}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6358175277709961})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4359520673751831})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3848557472229004})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3703078627586365})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.30794864892959595})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27908748388290405})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.26742249727249146})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3148747682571411})
store['active_learning_steps'][40]['eval_training']['best_epoch']=7
store['active_learning_steps'][40]['acquisition']={'indices': [50425, 53844, 56470, 57221, 10350, 29903, 12536, 17947, 12397, 54795], 'labels': [-1, 5, 1, -1, -1, 0, -1, -1, 4, 2], 'scores': [0.4406297206878662, 0.5569117665290833, 0.3937457799911499, 0.5340947508811951, 0.4738660454750061, 0.594865620136261, 0.2960151433944702, 0.3743431568145752, 0.48907172679901123, 0.4569084644317627]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.1062581539154053})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5520334243774414})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.46074166893959045})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.43072831630706787})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3778371810913086})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4157193601131439})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3670661747455597})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.38330864906311035})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3922446370124817})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.398964524269104})
store['active_learning_steps'][41]['training']['best_epoch']=7
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9655, 'crossentropy': 0.3100953125}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.711923360824585})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.41972389817237854})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3836706578731537})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36459267139434814})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3402056097984314})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3062066435813904})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3014788031578064})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28831273317337036})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2817317843437195})
store['active_learning_steps'][41]['eval_training']['best_epoch']=9
store['active_learning_steps'][41]['acquisition']={'indices': [13230, 6336, 9788, 9189, 14103, 48943, 8417, 43526, 2356, 37610], 'labels': [-1, -1, 7, -1, -1, 1, -1, -1, -1, 2], 'scores': [0.4598034620285034, 0.6047153472900391, 0.4076210856437683, 0.5146790742874146, 0.39741766452789307, 0.34627318382263184, 0.33338356018066406, 0.495248019695282, 0.44455814361572266, 0.5306186676025391]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.153799295425415})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.48972535133361816})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38627737760543823})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4309147000312805})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.39373669028282166})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35637813806533813})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3690756559371948})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3389233350753784})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.4025089144706726})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36600595712661743})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.4100240468978882})
store['active_learning_steps'][42]['training']['best_epoch']=8
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9661, 'crossentropy': 0.2878785400390625}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6635420322418213})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.42195573449134827})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34613919258117676})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34412315487861633})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30586743354797363})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2874058187007904})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.26756730675697327})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2657098174095154})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.25827503204345703})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2678905427455902})
store['active_learning_steps'][42]['eval_training']['best_epoch']=9
store['active_learning_steps'][42]['acquisition']={'indices': [56662, 27791, 13540, 21040, 33340, 48034, 39561, 3436, 18237, 46439], 'labels': [0, -1, 7, 9, 5, -1, -1, 4, -1, -1], 'scores': [0.5336537957191467, 0.6451395153999329, 0.4382646679878235, 0.7420101165771484, 0.5567436814308167, 0.3664790391921997, 0.4060651659965515, 0.6893503069877625, 0.37154173851013184, 0.6010653376579285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.1482398509979248})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5085999965667725})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4232513904571533})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3840334415435791})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38896501064300537})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37749233841896057})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.42739754915237427})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.363422691822052})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3719927668571472})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38975048065185547})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36907315254211426})
store['active_learning_steps'][43]['training']['best_epoch']=8
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9602, 'crossentropy': 0.3256072998046875}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6939020156860352})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4435810446739197})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.374969482421875})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.35423630475997925})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.31257301568984985})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3144753575325012})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2816724181175232})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2752994894981384})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.297685444355011})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.28252577781677246})
store['active_learning_steps'][43]['eval_training']['best_epoch']=8
store['active_learning_steps'][43]['acquisition']={'indices': [21344, 53993, 6767, 33549, 10740, 57856, 47036, 43312, 4549, 3118], 'labels': [-1, 6, -1, 6, -1, -1, 2, -1, -1, -1], 'scores': [0.41531556844711304, 0.578239917755127, 0.43218231201171875, 0.6034597158432007, 0.45757997035980225, 0.44581735134124756, 0.5684846341609955, 0.41934412717819214, 0.31561291217803955, 0.534217357635498]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1123418807983398})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5412325263023376})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.42805930972099304})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.39641207456588745})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3355746865272522})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3616781234741211})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35156673192977905})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.35613009333610535})
store['active_learning_steps'][44]['training']['best_epoch']=5
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.959, 'crossentropy': 0.322473095703125}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6523465514183044})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.47513678669929504})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4074944257736206})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3958308696746826})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3567121624946594})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31167861819267273})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33214741945266724})
store['active_learning_steps'][44]['eval_training']['best_epoch']=6
store['active_learning_steps'][44]['acquisition']={'indices': [18714, 843, 14623, 17958, 37722, 5065, 36466, 24894, 38383, 52090], 'labels': [8, -1, 5, 9, -1, 2, -1, -1, -1, -1], 'scores': [0.3570290803909302, 0.2889350652694702, 0.6589519381523132, 0.5400988459587097, 0.3241819143295288, 0.7011270523071289, 0.33503520488739014, 0.496613085269928, 0.42389607429504395, 0.3181041479110718]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.0929183959960938})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6103030443191528})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4931364953517914})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3367224633693695})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.341693639755249})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3759450912475586})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3710198998451233})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9587, 'crossentropy': 0.3186298828125}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6652459502220154})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.44692087173461914})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4074828624725342})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.37840536236763})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40870538353919983})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3374289572238922})
store['active_learning_steps'][45]['eval_training']['best_epoch']=6
store['active_learning_steps'][45]['acquisition']={'indices': [31883, 52897, 37663, 5896, 5790, 11708, 53771, 42671, 55618, 850], 'labels': [4, -1, -1, 8, 2, 3, -1, 2, -1, 4], 'scores': [0.3954191207885742, 0.49271178245544434, 0.3885115385055542, 0.5332481265068054, 0.39752620458602905, 0.4741005301475525, 0.43531692028045654, 0.5022832751274109, 0.5159480571746826, 0.3539673686027527]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.1439034938812256})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5697813034057617})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.41418391466140747})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3690824508666992})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35873615741729736})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35584673285484314})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3558266758918762})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.43134188652038574})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3871661424636841})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36388781666755676})
store['active_learning_steps'][46]['training']['best_epoch']=7
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9675, 'crossentropy': 0.300008154296875}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.644438624382019})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4686962962150574})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4375728964805603})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.39044761657714844})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34059572219848633})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3261461853981018})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2771912217140198})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2678709030151367})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2643773555755615})
store['active_learning_steps'][46]['eval_training']['best_epoch']=9
store['active_learning_steps'][46]['acquisition']={'indices': [29791, 45121, 10746, 44618, 12474, 13573, 26302, 57415, 11675, 1582], 'labels': [-1, 4, 9, 9, -1, -1, 9, -1, 0, -1], 'scores': [0.42653602361679077, 0.5704490542411804, 0.5475161075592041, 0.6337048411369324, 0.37515997886657715, 0.5831295251846313, 0.3807046413421631, 0.4417482614517212, 0.5976464152336121, 0.4471430778503418]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1106370687484741})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5316129922866821})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4437493681907654})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3938109278678894})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4344450533390045})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38971346616744995})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.37481409311294556})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3976922035217285})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3804946541786194})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.39292043447494507})
store['active_learning_steps'][47]['training']['best_epoch']=7
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9649, 'crossentropy': 0.3306483642578125}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6456438302993774})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4579614996910095})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.414821594953537})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.33784013986587524})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3426176607608795})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3328515887260437})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3254528045654297})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31120914220809937})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2815530300140381})
store['active_learning_steps'][47]['eval_training']['best_epoch']=9
store['active_learning_steps'][47]['acquisition']={'indices': [11319, 47376, 19305, 2012, 40688, 55531, 55092, 17357, 2991, 50582], 'labels': [-1, 6, -1, -1, -1, -1, -1, -1, 8, -1], 'scores': [0.6256946325302124, 0.5153573155403137, 0.6081715822219849, 0.3526917099952698, 0.6148161292076111, 0.6452588438987732, 0.5704936385154724, 0.5617731809616089, 0.5698971748352051, 0.4448968768119812]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1452993154525757})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5491522550582886})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3521573543548584})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31438374519348145})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35623377561569214})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3086806535720825})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.32974299788475037})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32164353132247925})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3773031532764435})
store['active_learning_steps'][48]['training']['best_epoch']=6
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.965, 'crossentropy': 0.276924365234375}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.642322838306427})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.44154804944992065})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.37343305349349976})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34334665536880493})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.31138768792152405})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31014585494995117})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28219470381736755})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29778778553009033})
store['active_learning_steps'][48]['eval_training']['best_epoch']=7
store['active_learning_steps'][48]['acquisition']={'indices': [23451, 26781, 3671, 31114, 11374, 57706, 59980, 37984, 22154, 49159], 'labels': [-1, -1, -1, 4, -1, -1, 3, 7, -1, -1], 'scores': [0.47989630699157715, 0.3532031178474426, 0.4209623336791992, 0.7020920515060425, 0.3295276165008545, 0.34937119483947754, 0.466067910194397, 0.5943516492843628, 0.38599735498428345, 0.33268487453460693]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.2408370971679688})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5800520777702332})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3949877619743347})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.37091952562332153})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3350382149219513})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33381372690200806})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.36310887336730957})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3313472270965576})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3164859712123871})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3164462447166443})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.340581476688385})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34985291957855225})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.312987357378006})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3704235851764679})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.4074629545211792})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3808501064777374})
store['active_learning_steps'][49]['training']['best_epoch']=13
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9655, 'crossentropy': 0.2953919921875}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6608773469924927})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.42593008279800415})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.33879411220550537})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.32352060079574585})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2769984304904938})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.28376123309135437})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2746359407901764})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30542659759521484})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2660973072052002})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2624453902244568})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24005275964736938})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2565559148788452})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.22714319825172424})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2525710165500641})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25061699748039246})
store['active_learning_steps'][49]['eval_training']['best_epoch']=13
store['active_learning_steps'][49]['acquisition']={'indices': [24750, 57414, 19324, 42274, 674, 33567, 56468, 4738, 48227, 29006], 'labels': [-1, -1, 2, 5, -1, -1, 5, 0, -1, 5], 'scores': [0.33441174030303955, 0.5237635374069214, 0.4243212044239044, 0.6067919135093689, 0.46301543712615967, 0.5328657627105713, 0.5006122887134552, 0.5732773542404175, 0.4670097827911377, 0.7353492379188538]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.16538405418396})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.566482663154602})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.44308266043663025})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36791154742240906})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.348758339881897})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3559916317462921})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3521156311035156})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3443811535835266})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3265698552131653})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33402907848358154})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3572317957878113})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3841288089752197})
store['active_learning_steps'][50]['training']['best_epoch']=9
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9675, 'crossentropy': 0.2741783935546875}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6538264751434326})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4138353168964386})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33458685874938965})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33727121353149414})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29596763849258423})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27904850244522095})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27434319257736206})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28182539343833923})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2613309323787689})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2621580958366394})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2426835149526596})
store['active_learning_steps'][50]['eval_training']['best_epoch']=11
store['active_learning_steps'][50]['acquisition']={'indices': [11127, 29759, 55674, 15873, 1848, 57665, 4446, 46148, 26355, 39480], 'labels': [4, 5, 8, 5, -1, 8, -1, -1, -1, 9], 'scores': [0.381664514541626, 0.7633634805679321, 0.5516130924224854, 0.556777834892273, 0.23845362663269043, 0.8344383239746094, 0.5336073040962219, 0.3762996196746826, 0.3677316904067993, 0.6002871990203857]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.1546270847320557})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5082511901855469})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4055376648902893})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3396328091621399})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33073559403419495})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31543752551078796})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28773045539855957})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3365834653377533})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.34252578020095825})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3712864816188812})
store['active_learning_steps'][51]['training']['best_epoch']=7
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9679, 'crossentropy': 0.275815234375}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7214996814727783})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47683972120285034})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3582903742790222})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3191123604774475})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2844070792198181})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30031663179397583})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28921711444854736})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26757705211639404})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.26712551712989807})
store['active_learning_steps'][51]['eval_training']['best_epoch']=9
store['active_learning_steps'][51]['acquisition']={'indices': [13756, 37909, 22186, 10093, 43994, 5195, 52624, 24982, 20703, 54342], 'labels': [-1, -1, -1, -1, -1, 4, 1, -1, -1, -1], 'scores': [0.39783716201782227, 0.5037108063697815, 0.569044828414917, 0.5560222864151001, 0.46993887424468994, 0.5467430353164673, 0.6259434223175049, 0.4064241647720337, 0.5873278975486755, 0.4877786636352539]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.0484073162078857})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5878646373748779})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39644089341163635})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3666492998600006})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34124869108200073})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3098902106285095})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3302275538444519})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33032575249671936})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3215600848197937})
store['active_learning_steps'][52]['training']['best_epoch']=6
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9694, 'crossentropy': 0.259808935546875}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7195087671279907})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4320243299007416})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38813334703445435})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3462833762168884})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.30381596088409424})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28545713424682617})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2848237156867981})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27406740188598633})
store['active_learning_steps'][52]['eval_training']['best_epoch']=8
store['active_learning_steps'][52]['acquisition']={'indices': [45502, 20010, 41108, 1088, 14619, 45593, 27357, 55268, 48824, 38064], 'labels': [1, -1, 0, 7, 3, 6, -1, -1, -1, 9], 'scores': [0.48052358627319336, 0.3209686279296875, 0.522847056388855, 0.5371057987213135, 0.46496766805648804, 0.425201952457428, 0.3899083137512207, 0.4001346826553345, 0.4876527786254883, 0.4998542070388794]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.1878197193145752})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5398787260055542})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.4252901077270508})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31865888833999634})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.311880886554718})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2928580641746521})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3032342195510864})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2926219701766968})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31911394000053406})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32004255056381226})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30416643619537354})
store['active_learning_steps'][53]['training']['best_epoch']=8
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9685, 'crossentropy': 0.267388037109375}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6482810974121094})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3956689238548279})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3537173867225647})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3311541676521301})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2864696681499481})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28315800428390503})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27669835090637207})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2654957175254822})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2617783546447754})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2408156394958496})
store['active_learning_steps'][53]['eval_training']['best_epoch']=10
store['active_learning_steps'][53]['acquisition']={'indices': [49968, 54215, 54966, 51580, 5308, 39878, 45758, 31088, 13001, 2426], 'labels': [-1, -1, 7, -1, 7, -1, -1, -1, -1, 1], 'scores': [0.37160444259643555, 0.4504365921020508, 0.5274106860160828, 0.37559497356414795, 0.6184164881706238, 0.5821592807769775, 0.47157084941864014, 0.6010346412658691, 0.47137129306793213, 0.5110538601875305]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.1438446044921875})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5763635635375977})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40788447856903076})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3413410186767578})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34797656536102295})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2810978293418884})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29214197397232056})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3410491347312927})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2990427017211914})
store['active_learning_steps'][54]['training']['best_epoch']=6
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9696, 'crossentropy': 0.265855908203125}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.676720380783081})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4278527498245239})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3283176124095917})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30880600214004517})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3021828532218933})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2906607985496521})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32564055919647217})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24679070711135864})
store['active_learning_steps'][54]['eval_training']['best_epoch']=8
store['active_learning_steps'][54]['acquisition']={'indices': [20869, 3825, 24325, 46718, 33086, 16281, 7674, 52688, 31962, 57185], 'labels': [3, -1, -1, -1, -1, -1, 8, 6, 3, -1], 'scores': [0.5508968234062195, 0.43065953254699707, 0.4049280285835266, 0.34262728691101074, 0.5334897041320801, 0.3305060863494873, 0.45593076944351196, 0.5690829753875732, 0.5702537894248962, 0.41321301460266113]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.1512845754623413})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5488235950469971})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4040094017982483})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3212050795555115})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29665446281433105})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3099626898765564})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31203776597976685})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33773890137672424})
store['active_learning_steps'][55]['training']['best_epoch']=5
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9656, 'crossentropy': 0.2867347900390625}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6841946244239807})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4200524091720581})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3549523949623108})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32930228114128113})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3337184190750122})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.26445257663726807})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26169514656066895})
store['active_learning_steps'][55]['eval_training']['best_epoch']=7
store['active_learning_steps'][55]['acquisition']={'indices': [46134, 48160, 5434, 17248, 13247, 13490, 6680, 39656, 25405, 8047], 'labels': [-1, -1, -1, -1, -1, -1, -1, 0, -1, 8], 'scores': [0.4403836727142334, 0.5490896105766296, 0.505990743637085, 0.5444053411483765, 0.5159173011779785, 0.3984832763671875, 0.5206217169761658, 0.4415554404258728, 0.4539421796798706, 0.6468127369880676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0885183811187744})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5045878887176514})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3833169639110565})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3407447338104248})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32370656728744507})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30131667852401733})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.33630064129829407})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30477380752563477})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29948341846466064})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32320719957351685})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30797767639160156})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.293540894985199})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3349425792694092})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29762059450149536})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29440781474113464})
store['active_learning_steps'][56]['training']['best_epoch']=12
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9718, 'crossentropy': 0.2846223876953125}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6576694250106812})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43531787395477295})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3805636167526245})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28062382340431213})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26894766092300415})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2609529197216034})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23039491474628448})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24480272829532623})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23656252026557922})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.236858069896698})
store['active_learning_steps'][56]['eval_training']['best_epoch']=7
store['active_learning_steps'][56]['acquisition']={'indices': [16336, 3038, 39256, 55163, 1674, 10151, 43646, 2928, 12714, 9608], 'labels': [-1, -1, -1, -1, 9, 8, -1, 5, -1, 8], 'scores': [0.3536374568939209, 0.4994770884513855, 0.4913598895072937, 0.7195613384246826, 0.7438670992851257, 0.6682696342468262, 0.46932852268218994, 0.5016277134418488, 0.5013476014137268, 0.5642079710960388]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.158494472503662})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.584539532661438})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3469339609146118})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32062992453575134})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32592326402664185})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30659425258636475})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3215533494949341})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2971963882446289})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2968328893184662})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.310396671295166})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30174532532691956})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3019043803215027})
store['active_learning_steps'][57]['training']['best_epoch']=9
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9685, 'crossentropy': 0.2806756591796875}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6778801679611206})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.465239018201828})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3797037601470947})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30666229128837585})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32707637548446655})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2650657296180725})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25816065073013306})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2807117998600006})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2964310050010681})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24632102251052856})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24704208970069885})
store['active_learning_steps'][57]['eval_training']['best_epoch']=10
store['active_learning_steps'][57]['acquisition']={'indices': [23550, 26745, 36077, 51032, 52780, 16722, 3412, 37417, 15064, 51349], 'labels': [-1, 1, -1, 9, 1, 1, 1, 8, -1, -1], 'scores': [0.49308156967163086, 0.5488142371177673, 0.39138591289520264, 0.475458025932312, 0.6542370915412903, 0.636476457118988, 0.5809950828552246, 0.4961729049682617, 0.5798195600509644, 0.49228405952453613]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.3115878105163574})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.5952473878860474})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.40249818563461304})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.34653088450431824})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.318994402885437})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31972646713256836})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31116849184036255})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30838000774383545})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.31555232405662537})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3073655366897583})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30742982029914856})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3213444650173187})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31200355291366577})
store['active_learning_steps'][58]['training']['best_epoch']=10
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9677, 'crossentropy': 0.2789519287109375}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7608920335769653})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47847798466682434})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34998995065689087})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29545125365257263})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3238524794578552})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29253947734832764})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26491445302963257})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2593733072280884})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2605600953102112})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2685806155204773})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.25583916902542114})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26148876547813416})
store['active_learning_steps'][58]['eval_training']['best_epoch']=11
store['active_learning_steps'][58]['acquisition']={'indices': [21880, 59099, 1790, 39891, 34199, 6655, 26104, 47911, 58636, 2641], 'labels': [2, -1, -1, 4, -1, -1, -1, -1, -1, -1], 'scores': [0.6003817915916443, 0.7073771953582764, 0.40554285049438477, 0.5166262984275818, 0.5292088389396667, 0.34458744525909424, 0.397491455078125, 0.40219056606292725, 0.4562220573425293, 0.41298210620880127]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1157516241073608})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.47789764404296875})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.34932971000671387})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3336907923221588})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29484423995018005})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28955671191215515})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2811005413532257})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3192458152770996})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3052055835723877})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34529250860214233})
store['active_learning_steps'][59]['training']['best_epoch']=7
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9679, 'crossentropy': 0.250748193359375}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6333735585212708})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.48862865567207336})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3424116373062134})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3102132976055145})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29535070061683655})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3063332438468933})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.23934733867645264})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.247203528881073})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23892971873283386})
store['active_learning_steps'][59]['eval_training']['best_epoch']=9
store['active_learning_steps'][59]['acquisition']={'indices': [13153, 32841, 41081, 42561, 59723, 8780, 52196, 32664, 32827, 18138], 'labels': [9, -1, -1, -1, -1, 8, -1, -1, -1, -1], 'scores': [0.42721492052078247, 0.4775499105453491, 0.565885066986084, 0.3919825553894043, 0.1979057788848877, 0.4689781069755554, 0.3824251890182495, 0.41356194019317627, 0.44530582427978516, 0.4503481388092041]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0957772731781006})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.544483482837677})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4044729173183441})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32988113164901733})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32051903009414673})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3427008390426636})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33075955510139465})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3400142788887024})
store['active_learning_steps'][60]['training']['best_epoch']=5
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9663, 'crossentropy': 0.2814490966796875}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7365120649337769})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4548417925834656})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.431871235370636})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34649714827537537})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.30821532011032104})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3230655789375305})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3035964369773865})
store['active_learning_steps'][60]['eval_training']['best_epoch']=7
store['active_learning_steps'][60]['acquisition']={'indices': [32784, 32609, 2030, 5789, 57177, 12078, 37861, 36744, 14878, 14100], 'labels': [8, -1, 8, -1, 7, 1, -1, 1, 3, 5], 'scores': [0.4056241512298584, 0.4013921022415161, 0.29596471786499023, 0.38747429847717285, 0.3430161476135254, 0.45927029848098755, 0.41394221782684326, 0.5620142221450806, 0.41147279739379883, 0.24462386965751648]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.212968111038208})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5744442939758301})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.37463951110839844})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3341826796531677})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35899579524993896})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30713945627212524})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3151957392692566})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29940474033355713})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3296501338481903})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3149823546409607})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32729893922805786})
store['active_learning_steps'][61]['training']['best_epoch']=8
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9696, 'crossentropy': 0.257574658203125}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6382620334625244})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46103888750076294})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3276773691177368})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3059849143028259})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3069494962692261})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.25317835807800293})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27259910106658936})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.24430006742477417})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24126961827278137})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2741841673851013})
store['active_learning_steps'][61]['eval_training']['best_epoch']=9
store['active_learning_steps'][61]['acquisition']={'indices': [17552, 21726, 4282, 10209, 35477, 25598, 12780, 23366, 13813, 32387], 'labels': [-1, -1, -1, 4, -1, -1, -1, 9, -1, -1], 'scores': [0.4640774726867676, 0.3570348024368286, 0.4552990198135376, 0.37295907735824585, 0.5922925472259521, 0.35555124282836914, 0.43104708194732666, 0.3943970799446106, 0.35142409801483154, 0.5508540868759155]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.1396898031234741})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.552241861820221})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.40388062596321106})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33640849590301514})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3285345733165741})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3239302635192871})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31271710991859436})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28556835651397705})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34124308824539185})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30696651339530945})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3025132417678833})
store['active_learning_steps'][62]['training']['best_epoch']=8
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.2738452880859375}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6640840172767639})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4336915612220764})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3455406725406647})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.33599549531936646})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31127381324768066})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2987349033355713})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27449995279312134})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25987550616264343})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2746007442474365})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2359747439622879})
store['active_learning_steps'][62]['eval_training']['best_epoch']=10
store['active_learning_steps'][62]['acquisition']={'indices': [5559, 43123, 12748, 54475, 31252, 56890, 6255, 15670, 56022, 55680], 'labels': [9, -1, 0, -1, 5, -1, -1, -1, -1, -1], 'scores': [0.4191872775554657, 0.5757769346237183, 0.5259715020656586, 0.5776116251945496, 0.6251714825630188, 0.567875862121582, 0.41433441638946533, 0.5484218597412109, 0.5100311040878296, 0.6239550709724426]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.2341179847717285})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5584207773208618})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36445295810699463})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3482763171195984})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30404919385910034})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3115519881248474})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29721155762672424})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2985277771949768})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2623421549797058})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27298229932785034})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3175022304058075})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33250707387924194})
store['active_learning_steps'][63]['training']['best_epoch']=9
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9677, 'crossentropy': 0.2642321044921875}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6587090492248535})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4305483102798462})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3642956018447876})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3098054528236389})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29898691177368164})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2821064591407776})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24721816182136536})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2474559247493744})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.274875283241272})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2445201575756073})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2135988175868988})
store['active_learning_steps'][63]['eval_training']['best_epoch']=11
store['active_learning_steps'][63]['acquisition']={'indices': [18972, 37149, 45749, 53788, 4602, 51753, 37394, 16951, 59489, 34189], 'labels': [-1, -1, -1, -1, -1, -1, -1, 8, -1, -1], 'scores': [0.35791778564453125, 0.4775683879852295, 0.5001916289329529, 0.4383021593093872, 0.6282633543014526, 0.4343611001968384, 0.2841796875, 0.6164823770523071, 0.2964576482772827, 0.3376675844192505]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.0568954944610596})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5160361528396606})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3674764037132263})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29984819889068604})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2888028025627136})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26274818181991577})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32629016041755676})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.25810661911964417})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.33969050645828247})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2955722212791443})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2703704833984375})
store['active_learning_steps'][64]['training']['best_epoch']=8
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9679, 'crossentropy': 0.2617157470703125}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6330609321594238})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.43239983916282654})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38948339223861694})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3265889286994934})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29498711228370667})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2821652591228485})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2368813455104828})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25249719619750977})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24696433544158936})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.22738705575466156})
store['active_learning_steps'][64]['eval_training']['best_epoch']=10
store['active_learning_steps'][64]['acquisition']={'indices': [33074, 3816, 58448, 14103, 23189, 31748, 343, 844, 32586, 29227], 'labels': [8, -1, -1, -1, -1, 3, -1, -1, -1, -1], 'scores': [0.4247962236404419, 0.18969988822937012, 0.3714064359664917, 0.5899247527122498, 0.258603572845459, 0.4515789747238159, 0.7023439407348633, 0.3567737936973572, 0.39289551973342896, 0.33559155464172363]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.2087833881378174})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.569938063621521})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4042862355709076})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34075671434402466})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33006608486175537})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3290281891822815})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3667774498462677})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3460986614227295})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32045799493789673})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3210493326187134})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2961549758911133})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35145705938339233})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3389069736003876})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.38425785303115845})
store['active_learning_steps'][65]['training']['best_epoch']=11
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9685, 'crossentropy': 0.2701918212890625}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.642413854598999})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4061218202114105})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3508877754211426})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28077471256256104})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2828739285469055})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2570287883281708})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25359582901000977})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26117491722106934})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24387900531291962})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.22783029079437256})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2293122112751007})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23599132895469666})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24614477157592773})
store['active_learning_steps'][65]['eval_training']['best_epoch']=10
store['active_learning_steps'][65]['acquisition']={'indices': [39972, 19244, 9494, 26872, 48310, 2381, 14896, 39395, 14529, 35912], 'labels': [-1, 9, -1, -1, -1, 7, 8, -1, -1, -1], 'scores': [0.3667793273925781, 0.5589282512664795, 0.7263002395629883, 0.4041104316711426, 0.2794785499572754, 0.5045281648635864, 0.5340529680252075, 0.42830705642700195, 0.4495503902435303, 0.5018779635429382]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.1577234268188477})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5483423471450806})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.36559122800827026})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3446965515613556})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31749001145362854})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3121505677700043})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.27148690819740295})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3105982542037964})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3148135542869568})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2817833423614502})
store['active_learning_steps'][66]['training']['best_epoch']=7
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9684, 'crossentropy': 0.2517585693359375}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6444427967071533})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.45921266078948975})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3179437518119812})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29461097717285156})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2884517312049866})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26280272006988525})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.23742514848709106})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.265445351600647})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.255330353975296})
store['active_learning_steps'][66]['eval_training']['best_epoch']=7
store['active_learning_steps'][66]['acquisition']={'indices': [22685, 36067, 38307, 41196, 56066, 49517, 11038, 28631, 3812, 27750], 'labels': [-1, -1, -1, 9, -1, 6, 6, 2, -1, -1], 'scores': [0.4029579162597656, 0.3145015835762024, 0.39540112018585205, 0.7536618709564209, 0.3599890470504761, 0.6331347227096558, 0.5897122025489807, 0.5677648186683655, 0.4061833620071411, 0.26918095350265503]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.1329203844070435})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5710221529006958})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4170706272125244})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3308826684951782})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.35545670986175537})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2925189137458801})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.26787686347961426})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3160574436187744})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.31780946254730225})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27192968130111694})
store['active_learning_steps'][67]['training']['best_epoch']=7
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9697, 'crossentropy': 0.253789013671875}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6548517346382141})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4365808665752411})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3684048056602478})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33224552869796753})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2724738121032715})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29703885316848755})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.25640976428985596})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25915423035621643})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24179257452487946})
store['active_learning_steps'][67]['eval_training']['best_epoch']=9
store['active_learning_steps'][67]['acquisition']={'indices': [30238, 3649, 34847, 22860, 8934, 8865, 52914, 2185, 1720, 33996], 'labels': [1, -1, 0, -1, 1, 3, 5, -1, -1, -1], 'scores': [0.4446386694908142, 0.37775540351867676, 0.44685861468315125, 0.34671735763549805, 0.33185285329818726, 0.39226895570755005, 0.45109421014785767, 0.3303403854370117, 0.4367152452468872, 0.41799092292785645]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.269821047782898})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6106405854225159})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38290196657180786})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.37263622879981995})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3600904941558838})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31818825006484985})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30064713954925537})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3111199736595154})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3300466537475586})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3070216178894043})
store['active_learning_steps'][68]['training']['best_epoch']=7
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9713, 'crossentropy': 0.2714677001953125}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.69912189245224})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4423155188560486})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3641333281993866})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3429563641548157})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3189796507358551})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29358965158462524})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2930722236633301})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2533891499042511})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24831056594848633})
store['active_learning_steps'][68]['eval_training']['best_epoch']=9
store['active_learning_steps'][68]['acquisition']={'indices': [49079, 59303, 47100, 18388, 51800, 13312, 36612, 38820, 43309, 53055], 'labels': [-1, 8, 8, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.2880861759185791, 0.4546527862548828, 0.5209740400314331, 0.28082942962646484, 0.5061999559402466, 0.37717217206954956, 0.33522093296051025, 0.436936616897583, 0.32904481887817383, 0.38287603855133057]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.327135443687439})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5847384929656982})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3833969235420227})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32370877265930176})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30596524477005005})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3192589282989502})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28492826223373413})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30692991614341736})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31635919213294983})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29540714621543884})
store['active_learning_steps'][69]['training']['best_epoch']=7
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9725, 'crossentropy': 0.2554108154296875}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6313278675079346})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4604175090789795})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3708999752998352})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.307197630405426})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.31343376636505127})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3033568263053894})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26644259691238403})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27761954069137573})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31265518069267273})
store['active_learning_steps'][69]['eval_training']['best_epoch']=7
store['active_learning_steps'][69]['acquisition']={'indices': [57182, 23474, 50930, 13030, 45838, 28244, 52649, 34909, 29711, 32596], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 8, 8], 'scores': [0.42955225706100464, 0.6183586120605469, 0.45104771852493286, 0.4327436685562134, 0.38217437267303467, 0.4539836645126343, 0.46585214138031006, 0.5651912689208984, 0.5345804691314697, 0.5080432295799255]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.164290428161621})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6148227453231812})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.35948169231414795})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3357539176940918})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3276500105857849})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30280283093452454})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29814499616622925})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2599705755710602})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3052365183830261})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3215300142765045})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2888476252555847})
store['active_learning_steps'][70]['training']['best_epoch']=8
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9708, 'crossentropy': 0.241548486328125}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7060962915420532})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.42870038747787476})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35630810260772705})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3122662305831909})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2780464291572571})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2555115222930908})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27515512704849243})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26049143075942993})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25408488512039185})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30365949869155884})
store['active_learning_steps'][70]['eval_training']['best_epoch']=9
store['active_learning_steps'][70]['acquisition']={'indices': [47647, 23552, 58014, 34920, 33574, 56943, 26508, 36466, 35349, 39926], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4276835322380066, 0.5747256875038147, 0.397635817527771, 0.5565578937530518, 0.4786813259124756, 0.3889758586883545, 0.4209780693054199, 0.4786146283149719, 0.2999230623245239, 0.44304561614990234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.3215365409851074})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6768975257873535})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.43618154525756836})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3324248790740967})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3141287565231323})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31650716066360474})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30592358112335205})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2860386073589325})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.32658419013023376})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.34265950322151184})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28216034173965454})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3312194347381592})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30687204003334045})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.3019806742668152})
store['active_learning_steps'][71]['training']['best_epoch']=11
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9696, 'crossentropy': 0.2714689208984375}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6930036544799805})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.45320501923561096})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36825841665267944})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29918473958969116})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2909736633300781})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2854255437850952})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.27200818061828613})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23372450470924377})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.257360577583313})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25808852910995483})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23388025164604187})
store['active_learning_steps'][71]['eval_training']['best_epoch']=8
store['active_learning_steps'][71]['acquisition']={'indices': [29287, 33651, 51445, 4446, 26836, 1075, 46284, 4185, 42142, 46032], 'labels': [2, 7, -1, -1, -1, 7, 9, 2, -1, -1], 'scores': [0.4320049285888672, 0.5031299293041229, 0.4016227722167969, 0.5790022015571594, 0.4579727053642273, 0.7235869765281677, 0.626861035823822, 0.6735538244247437, 0.36260539293289185, 0.49159693717956543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.075232744216919})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4848518967628479})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36505749821662903})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29260027408599854})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2987740635871887})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26239287853240967})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3137195110321045})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28738611936569214})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.297664076089859})
store['active_learning_steps'][72]['training']['best_epoch']=6
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.2464690673828125}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6533825993537903})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4252585172653198})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34284141659736633})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27381932735443115})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3206564486026764})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28699809312820435})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25964322686195374})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26825568079948425})
store['active_learning_steps'][72]['eval_training']['best_epoch']=7
store['active_learning_steps'][72]['acquisition']={'indices': [35326, 33061, 57406, 3770, 24239, 18814, 5070, 40087, 11246, 7719], 'labels': [5, -1, -1, -1, -1, 3, -1, -1, -1, 2], 'scores': [0.4710323214530945, 0.2915140390396118, 0.4009779095649719, 0.3735421895980835, 0.29145729541778564, 0.32305026054382324, 0.33683621883392334, 0.4374520778656006, 0.20507752895355225, 0.26224660873413086]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.2085247039794922})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6039581894874573})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38385242223739624})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35050585865974426})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3102330267429352})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3409375548362732})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27645477652549744})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28921499848365784})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2959729731082916})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31548863649368286})
store['active_learning_steps'][73]['training']['best_epoch']=7
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9686, 'crossentropy': 0.2618248046875}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7152339220046997})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4629281163215637})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.37320980429649353})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3442939519882202})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33716291189193726})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3600679636001587})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29483044147491455})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3039771318435669})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29778432846069336})
store['active_learning_steps'][73]['eval_training']['best_epoch']=7
store['active_learning_steps'][73]['acquisition']={'indices': [37633, 50665, 33513, 48404, 7392, 37530, 31258, 38133, 51426, 27420], 'labels': [-1, -1, -1, -1, -1, -1, -1, 7, -1, -1], 'scores': [0.565401554107666, 0.5109353065490723, 0.5111616849899292, 0.5317312479019165, 0.5215793251991272, 0.4233953356742859, 0.46276867389678955, 0.3372054696083069, 0.5235491991043091, 0.7223293781280518]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.4042911529541016})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6894495487213135})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4230839014053345})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34691041707992554})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33368057012557983})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3046923875808716})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29042887687683105})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.31631118059158325})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30804896354675293})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30264800786972046})
store['active_learning_steps'][74]['training']['best_epoch']=7
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9702, 'crossentropy': 0.258179443359375}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6897169947624207})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.437228798866272})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3451697826385498})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3247048854827881})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2916870415210724})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3031194806098938})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2603665888309479})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2596343159675598})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.254788339138031})
store['active_learning_steps'][74]['eval_training']['best_epoch']=9
store['active_learning_steps'][74]['acquisition']={'indices': [8741, 12066, 6309, 35643, 44570, 24140, 40972, 29511, 27968, 50369], 'labels': [-1, 8, 3, 3, 7, -1, -1, -1, 9, 3], 'scores': [0.35418951511383057, 0.5579792261123657, 0.5163165330886841, 0.3188844323158264, 0.5398461818695068, 0.39127659797668457, 0.41029292345046997, 0.5260410308837891, 0.4150431156158447, 0.5703375339508057]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.2249153852462769})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.5917187929153442})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3844548463821411})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37545931339263916})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29520314931869507})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.285449743270874})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2864093482494354})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2860373556613922})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28277096152305603})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30925536155700684})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3011217713356018})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3030102550983429})
store['active_learning_steps'][75]['training']['best_epoch']=9
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9676, 'crossentropy': 0.2572936279296875}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.618491530418396})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.42371296882629395})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35138773918151855})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29122352600097656})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2742849588394165})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30124568939208984})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.307181179523468})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.27067896723747253})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.24339883029460907})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.259383887052536})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23147988319396973})
store['active_learning_steps'][75]['eval_training']['best_epoch']=11
store['active_learning_steps'][75]['acquisition']={'indices': [6199, 46584, 6166, 27357, 14410, 15004, 49573, 54167, 18568, 53360], 'labels': [-1, 8, -1, -1, -1, -1, 2, -1, -1, -1], 'scores': [0.566588282585144, 0.4223305583000183, 0.3897451162338257, 0.5536998510360718, 0.563346266746521, 0.5604046583175659, 0.5281756520271301, 0.6466445922851562, 0.3771224021911621, 0.3650895357131958]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.2414023876190186})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5883704423904419})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3971271216869354})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.32143503427505493})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3061203956604004})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3374519944190979})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26639503240585327})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2872087359428406})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.33361905813217163})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3307540714740753})
store['active_learning_steps'][76]['training']['best_epoch']=7
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9718, 'crossentropy': 0.2508502197265625}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6396366357803345})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.45958441495895386})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3315426707267761})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3582514226436615})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29846006631851196})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2834647297859192})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2835174798965454})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26431095600128174})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2661154866218567})
store['active_learning_steps'][76]['eval_training']['best_epoch']=8
store['active_learning_steps'][76]['acquisition']={'indices': [33186, 4379, 12891, 17080, 44095, 24719, 45967, 41523, 37062, 31066], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 9, -1], 'scores': [0.5152949094772339, 0.5996123552322388, 0.4310678243637085, 0.5687203407287598, 0.3966904282569885, 0.4178812503814697, 0.4383079409599304, 0.471748948097229, 0.4277716875076294, 0.5170127749443054]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.2189679145812988})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6427937746047974})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3761541247367859})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3433181047439575})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.325158953666687})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2935623824596405})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2828992009162903})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2994993329048157})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28584253787994385})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2736884355545044})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29541197419166565})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2842335104942322})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2990500330924988})
store['active_learning_steps'][77]['training']['best_epoch']=10
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9723, 'crossentropy': 0.2585567138671875}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7051644921302795})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.43267160654067993})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3677862286567688})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3020806312561035})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3085170388221741})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29019486904144287})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.25426965951919556})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26323646306991577})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24788865447044373})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24948269128799438})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2216535210609436})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23835411667823792})
store['active_learning_steps'][77]['eval_training']['best_epoch']=11
store['active_learning_steps'][77]['acquisition']={'indices': [10670, 48329, 45989, 15823, 59419, 30855, 4370, 2268, 51248, 45402], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.34203827381134033, 0.6201776266098022, 0.42104101181030273, 0.4299513101577759, 0.3268386125564575, 0.6283765435218811, 0.3219287395477295, 0.5870279669761658, 0.39502978324890137, 0.39253687858581543]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.2073488235473633})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6233561635017395})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37823063135147095})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3452131748199463})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30351102352142334})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28075265884399414})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2864306569099426})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3159879446029663})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.291484534740448})
store['active_learning_steps'][78]['training']['best_epoch']=6
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9695, 'crossentropy': 0.2767354736328125}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.775749683380127})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.44045984745025635})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3768727481365204})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3408834934234619})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2743475139141083})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30110177397727966})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3220617473125458})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.283271461725235})
store['active_learning_steps'][78]['eval_training']['best_epoch']=5
store['active_learning_steps'][78]['acquisition']={'indices': [10055, 55616, 9472, 42798, 35422, 57080, 43250, 17592, 22759, 36446], 'labels': [-1, 6, 2, -1, -1, -1, -1, 4, -1, 6], 'scores': [0.5039176940917969, 0.5474506616592407, 0.4260892868041992, 0.5392993688583374, 0.4490525722503662, 0.5163642168045044, 0.6066904067993164, 0.4911557137966156, 0.36526989936828613, 0.6027335524559021]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.2249929904937744})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.5550580620765686})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4269862174987793})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3273841142654419})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30728286504745483})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30053049325942993})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32390689849853516})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.295595645904541})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30693578720092773})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29616671800613403})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30977556109428406})
store['active_learning_steps'][79]['training']['best_epoch']=8
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9693, 'crossentropy': 0.2677421875}
store['active_learning_steps'][79]['eval_training']={}
store['active_learning_steps'][79]['eval_training']['epochs']=[]
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6508642435073853})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4484034776687622})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.349628210067749})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32171908020973206})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28135764598846436})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2774650454521179})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2815048396587372})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2750030755996704})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2479396015405655})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.25506436824798584})
store['active_learning_steps'][79]['eval_training']['best_epoch']=9
store['active_learning_steps'][79]['acquisition']={'indices': [6774, 8619, 19837, 56184, 7927, 1518, 24626, 55835, 8949, 5194], 'labels': [-1, 8, -1, 4, -1, 9, -1, -1, -1, -1], 'scores': [0.5842733383178711, 0.4357200860977173, 0.4467865228652954, 0.44431719183921814, 0.5360363721847534, 0.7606216073036194, 0.4764835834503174, 0.4675166606903076, 0.674436092376709, 0.5054666996002197]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.2740802764892578})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7394324541091919})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4043348729610443})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.36243098974227905})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32908159494400024})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3299299478530884})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30463284254074097})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33834823966026306})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3209342658519745})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3107041120529175})
store['active_learning_steps'][80]['training']['best_epoch']=7
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9684, 'crossentropy': 0.2714604248046875}
store['active_learning_steps'][80]['eval_training']={}
store['active_learning_steps'][80]['eval_training']['epochs']=[]
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6811510324478149})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4514782428741455})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41255778074264526})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3233495354652405})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3160194158554077})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.2991446256637573})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.2881784439086914})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.29691100120544434})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2635953426361084})
store['active_learning_steps'][80]['eval_training']['best_epoch']=9
store['active_learning_steps'][80]['acquisition']={'indices': [30428, 45473, 31929, 50555, 22149, 38114, 18127, 50619, 23730, 36180], 'labels': [-1, -1, -1, -1, 3, 6, -1, 6, 3, -1], 'scores': [0.3217209577560425, 0.4241673946380615, 0.3863464593887329, 0.48372554779052734, 0.4366854429244995, 0.33045873045921326, 0.41452038288116455, 0.37546417117118835, 0.596926212310791, 0.36400389671325684]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.23569655418396})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.5703436136245728})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4074365198612213})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3163719177246094})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29077738523483276})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26538529992103577})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28995680809020996})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2943892776966095})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31967490911483765})
store['active_learning_steps'][81]['training']['best_epoch']=6
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9705, 'crossentropy': 0.2538533447265625}
store['active_learning_steps'][81]['eval_training']={}
store['active_learning_steps'][81]['eval_training']['epochs']=[]
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7156106233596802})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4070618152618408})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.37343645095825195})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3089064061641693})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3127742409706116})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3011201024055481})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2834462523460388})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2834651470184326})
store['active_learning_steps'][81]['eval_training']['best_epoch']=7
store['active_learning_steps'][81]['acquisition']={'indices': [57754, 46393, 12840, 48974, 59352, 4503, 29304, 37829, 14410, 53816], 'labels': [-1, -1, 9, -1, -1, -1, -1, 6, -1, -1], 'scores': [0.24560558795928955, 0.5026538372039795, 0.5254030823707581, 0.4508761167526245, 0.37905919551849365, 0.33059537410736084, 0.481869101524353, 0.4468015432357788, 0.4832589626312256, 0.4011114835739136]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0914374589920044})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.6163603067398071})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3770332932472229})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2627578377723694})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2980766296386719})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24999220669269562})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.24927380681037903})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2601284980773926})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.265543669462204})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.24237602949142456})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2744966149330139})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2996637225151062})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24323710799217224})
store['active_learning_steps'][82]['training']['best_epoch']=10
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9734, 'crossentropy': 0.240434619140625}
store['active_learning_steps'][82]['eval_training']={}
store['active_learning_steps'][82]['eval_training']['epochs']=[]
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6634164452552795})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4274228811264038})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3498336374759674})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31560641527175903})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2901955246925354})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27171701192855835})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25590792298316956})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2306796908378601})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.23475533723831177})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.233314648270607})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23976606130599976})
store['active_learning_steps'][82]['eval_training']['best_epoch']=8
store['active_learning_steps'][82]['acquisition']={'indices': [19062, 58588, 32945, 29608, 40730, 11028, 29035, 55285, 14275, 49033], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.40393662452697754, 0.575122594833374, 0.43425822257995605, 0.5433486700057983, 0.5417135953903198, 0.5909048318862915, 0.3149920701980591, 0.49533796310424805, 0.4496300220489502, 0.45181775093078613]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.2935049533843994})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.6107968091964722})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3851976990699768})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.31853675842285156})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.323505699634552})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2863052487373352})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2747446596622467})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.27830782532691956})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30643248558044434})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34778809547424316})
store['active_learning_steps'][83]['training']['best_epoch']=7
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.2490583251953125}
store['active_learning_steps'][83]['eval_training']={}
store['active_learning_steps'][83]['eval_training']['epochs']=[]
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.707237184047699})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45238393545150757})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3515590727329254})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32482025027275085})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.31004011631011963})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28845906257629395})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28140509128570557})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28593412041664124})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2618287205696106})
store['active_learning_steps'][83]['eval_training']['best_epoch']=9
store['active_learning_steps'][83]['acquisition']={'indices': [2744, 38905, 39306, 50180, 51394, 55973, 25919, 17205, 363, 56254], 'labels': [-1, 9, -1, 8, 8, -1, -1, -1, -1, 8], 'scores': [0.33385980129241943, 0.3233415484428406, 0.25485336780548096, 0.4439816474914551, 0.6024752259254456, 0.4820760488510132, 0.36292552947998047, 0.4035181999206543, 0.49192893505096436, 0.4478603005409241]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.2149155139923096})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6329928040504456})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39721280336380005})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3154340386390686})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30376332998275757})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27728956937789917})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27622905373573303})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2917191684246063})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.26237913966178894})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.25926029682159424})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.26727399230003357})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27424636483192444})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2729428708553314})
store['active_learning_steps'][84]['training']['best_epoch']=10
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9701, 'crossentropy': 0.25606396484375}
store['active_learning_steps'][84]['eval_training']={}
store['active_learning_steps'][84]['eval_training']['epochs']=[]
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6941831707954407})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.43886417150497437})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33034226298332214})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33435922861099243})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2951619029045105})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.250252366065979})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25426989793777466})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.24273136258125305})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2587013840675354})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.207064688205719})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.21474388241767883})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24796786904335022})
store['active_learning_steps'][84]['eval_training']['best_epoch']=10
store['active_learning_steps'][84]['acquisition']={'indices': [32863, 41268, 28397, 44172, 59378, 52422, 3457, 45640, 26508, 800], 'labels': [-1, -1, -1, 8, -1, -1, -1, -1, -1, 9], 'scores': [0.6249432563781738, 0.38922226428985596, 0.4919389486312866, 0.6878621578216553, 0.49601054191589355, 0.41146934032440186, 0.5066560506820679, 0.537858247756958, 0.49985671043395996, 0.5156043767929077]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2399739027023315})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.6537481546401978})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.42424333095550537})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3215699791908264})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.279089093208313})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29324042797088623})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2915276885032654})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.24722065031528473})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2918098270893097})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32351917028427124})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.30135002732276917})
store['active_learning_steps'][85]['training']['best_epoch']=8
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9751, 'crossentropy': 0.2405766845703125}
store['active_learning_steps'][85]['eval_training']={}
store['active_learning_steps'][85]['eval_training']['epochs']=[]
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7399941682815552})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.46068933606147766})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33456242084503174})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2965713441371918})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2808511257171631})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24638119339942932})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.22961288690567017})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.23443523049354553})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.23651321232318878})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25128695368766785})
store['active_learning_steps'][85]['eval_training']['best_epoch']=7
store['active_learning_steps'][85]['acquisition']={'indices': [23735, 29814, 51295, 2347, 3562, 34229, 27552, 38389, 57308, 56715], 'labels': [-1, -1, -1, -1, -1, -1, -1, 7, -1, -1], 'scores': [0.5947079658508301, 0.5158670544624329, 0.5519393086433411, 0.5368367433547974, 0.46483051776885986, 0.6250238418579102, 0.5389448404312134, 0.4860682487487793, 0.48919159173965454, 0.6303814649581909]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.1428337097167969})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.575574517250061})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3811302185058594})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3458980917930603})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28363192081451416})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30593886971473694})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27171793580055237})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3137485384941101})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28663402795791626})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.3129170536994934})
store['active_learning_steps'][86]['training']['best_epoch']=7
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9704, 'crossentropy': 0.2489048095703125}
store['active_learning_steps'][86]['eval_training']={}
store['active_learning_steps'][86]['eval_training']['epochs']=[]
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7078354358673096})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.48745667934417725})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3776540756225586})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3266528248786926})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3156670928001404})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29271548986434937})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25368571281433105})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2757546901702881})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2674199342727661})
store['active_learning_steps'][86]['eval_training']['best_epoch']=7
store['active_learning_steps'][86]['acquisition']={'indices': [46994, 15180, 57319, 35876, 45917, 33489, 35632, 13020, 49890, 21487], 'labels': [-1, 4, 2, -1, -1, -1, 0, -1, 5, -1], 'scores': [0.4805716276168823, 0.5155766010284424, 0.5321959257125854, 0.34473180770874023, 0.4668072462081909, 0.2345815896987915, 0.43656110763549805, 0.37138402462005615, 0.5806224942207336, 0.47878503799438477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.270089864730835})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6445098519325256})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.4431661069393158})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.38198423385620117})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32781660556793213})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3047303557395935})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30464762449264526})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.295463502407074})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30355045199394226})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3235003650188446})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2820691466331482})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32285332679748535})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30599021911621094})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.315825492143631})
store['active_learning_steps'][87]['training']['best_epoch']=11
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.9722, 'crossentropy': 0.24737958984375}
store['active_learning_steps'][87]['eval_training']={}
store['active_learning_steps'][87]['eval_training']['epochs']=[]
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6840670108795166})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5154622793197632})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.380404531955719})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3441305458545685})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30986306071281433})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3078421950340271})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26307550072669983})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2653288245201111})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24126458168029785})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2606579065322876})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.23456516861915588})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.23255428671836853})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2567090392112732})
store['active_learning_steps'][87]['eval_training']['best_epoch']=12
store['active_learning_steps'][87]['acquisition']={'indices': [59311, 29638, 26122, 51958, 21360, 51464, 56453, 37240, 22555, 52167], 'labels': [-1, -1, -1, -1, -1, 0, -1, -1, -1, -1], 'scores': [0.3963949680328369, 0.5689973831176758, 0.5126561522483826, 0.30283284187316895, 0.30477869510650635, 0.6914872527122498, 0.6211479902267456, 0.4431249499320984, 0.4098626375198364, 0.5351503491401672]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.273173451423645})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6759153604507446})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.42180025577545166})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.34252679347991943})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3119904398918152})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2832828760147095})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2982521653175354})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.297227680683136})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2704007625579834})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30813363194465637})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27406519651412964})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2953694760799408})
store['active_learning_steps'][88]['training']['best_epoch']=9
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9712, 'crossentropy': 0.2480671630859375}
store['active_learning_steps'][88]['eval_training']={}
store['active_learning_steps'][88]['eval_training']['epochs']=[]
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7589759826660156})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4196951985359192})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34021246433258057})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32578518986701965})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3200160562992096})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2830321788787842})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2958531975746155})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2337985634803772})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2511044442653656})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25385090708732605})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.24761085212230682})
store['active_learning_steps'][88]['eval_training']['best_epoch']=8
store['active_learning_steps'][88]['acquisition']={'indices': [56298, 14474, 45295, 4646, 706, 38349, 19211, 19893, 8606, 46847], 'labels': [-1, -1, -1, 2, -1, -1, -1, -1, -1, -1], 'scores': [0.3356490135192871, 0.37856608629226685, 0.30915629863739014, 0.5855859518051147, 0.5364099740982056, 0.4005911350250244, 0.34043991565704346, 0.39557158946990967, 0.5633114576339722, 0.32895171642303467]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.151363730430603})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5860223174095154})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38308006525039673})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.31328922510147095})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28798040747642517})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2897968590259552})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3178660273551941})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29667574167251587})
store['active_learning_steps'][89]['training']['best_epoch']=5
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9661, 'crossentropy': 0.2728269775390625}
store['active_learning_steps'][89]['eval_training']={}
store['active_learning_steps'][89]['eval_training']['epochs']=[]
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7105690836906433})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5091060400009155})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.40646088123321533})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.33178675174713135})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3375072479248047})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32081928849220276})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30830174684524536})
store['active_learning_steps'][89]['eval_training']['best_epoch']=7
store['active_learning_steps'][89]['acquisition']={'indices': [8206, 49112, 38653, 37578, 50960, 20522, 12313, 57342, 25044, 29304], 'labels': [-1, -1, -1, -1, -1, -1, -1, 2, -1, -1], 'scores': [0.3711695671081543, 0.3877648115158081, 0.328342080116272, 0.46648943424224854, 0.4629032611846924, 0.3385077714920044, 0.3910285234451294, 0.4223111867904663, 0.3565812110900879, 0.3095928430557251]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.226482629776001})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5964251756668091})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.39827650785446167})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32433462142944336})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29599395394325256})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30066293478012085})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2767114043235779})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2849504053592682})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.293956995010376})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2746528089046478})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.3124163746833801})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2936946153640747})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9755859375, 'crossentropy': 0.2674846053123474})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29613620042800903})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.29330724477767944})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2847355008125305})
store['active_learning_steps'][90]['training']['best_epoch']=13
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9725, 'crossentropy': 0.2378726318359375}
store['active_learning_steps'][90]['eval_training']={}
store['active_learning_steps'][90]['eval_training']['epochs']=[]
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7560868263244629})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4678471088409424})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.34239476919174194})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.35152125358581543})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2622905671596527})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.21401697397232056})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.26464107632637024})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.22991125285625458})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23719069361686707})
store['active_learning_steps'][90]['eval_training']['best_epoch']=6
store['active_learning_steps'][90]['acquisition']={'indices': [47867, 42988, 50127, 49172, 37093, 43943, 49458, 27411, 52723, 42807], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4012192487716675, 0.5137317180633545, 0.4508552551269531, 0.5451675653457642, 0.4666738510131836, 0.5491452217102051, 0.4237104654312134, 0.47616255283355713, 0.5535953044891357, 0.6385184526443481]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.2370749711990356})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.660335123538971})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.39990660548210144})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3539346158504486})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32734429836273193})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30036798119544983})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28225505352020264})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28523215651512146})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32615745067596436})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3170112371444702})
store['active_learning_steps'][91]['training']['best_epoch']=7
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9737, 'crossentropy': 0.2300233154296875}
store['active_learning_steps'][91]['eval_training']={}
store['active_learning_steps'][91]['eval_training']['epochs']=[]
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6365660429000854})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4135439395904541})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3253362774848938})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.31869426369667053})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.302412748336792})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.283381849527359})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26756641268730164})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.24648523330688477})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25507089495658875})
store['active_learning_steps'][91]['eval_training']['best_epoch']=8
store['active_learning_steps'][91]['acquisition']={'indices': [32012, 30122, 37118, 27706, 13906, 55072, 9242, 21601, 17467, 22795], 'labels': [-1, -1, 3, 7, -1, -1, -1, 1, 3, -1], 'scores': [0.27691924571990967, 0.3204716444015503, 0.5775547027587891, 0.30872809886932373, 0.48056983947753906, 0.212066650390625, 0.4037371873855591, 0.6332525610923767, 0.348446786403656, 0.4422268867492676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.328304409980774})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5972073078155518})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.47069475054740906})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35091331601142883})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27415931224823})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2920680642127991})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26559433341026306})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.23388901352882385})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.30198073387145996})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2977856993675232})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.32883328199386597})
store['active_learning_steps'][92]['training']['best_epoch']=8
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9746, 'crossentropy': 0.2293189453125}
store['active_learning_steps'][92]['eval_training']={}
store['active_learning_steps'][92]['eval_training']['epochs']=[]
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7512719631195068})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.42579033970832825})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3703193664550781})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.35211658477783203})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3108779788017273})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24295905232429504})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28294387459754944})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26136326789855957})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24711394309997559})
store['active_learning_steps'][92]['eval_training']['best_epoch']=6
store['active_learning_steps'][92]['acquisition']={'indices': [21066, 38441, 21341, 20631, 30656, 16939, 18735, 22058, 6408, 8638], 'labels': [0, -1, 3, -1, -1, 9, -1, -1, -1, -1], 'scores': [0.4340156316757202, 0.45282793045043945, 0.5057247281074524, 0.574336051940918, 0.28245270252227783, 0.5532668828964233, 0.6435698866844177, 0.5615748167037964, 0.48182302713394165, 0.43122005462646484]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.3589195013046265})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.6097466945648193})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.45635169744491577})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3671467900276184})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3015335202217102})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2900904417037964})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28920987248420715})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.29912686347961426})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30123722553253174})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28120073676109314})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2688067555427551})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3117973804473877})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.29138851165771484})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3052191138267517})
store['active_learning_steps'][93]['training']['best_epoch']=11
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9761, 'crossentropy': 0.231586669921875}
store['active_learning_steps'][93]['eval_training']={}
store['active_learning_steps'][93]['eval_training']['epochs']=[]
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7350449562072754})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4998708665370941})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34770894050598145})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3075832724571228})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2792710065841675})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2331477254629135})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.23619624972343445})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.21795353293418884})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.20277157425880432})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.21525418758392334})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.22522494196891785})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.20402105152606964})
store['active_learning_steps'][93]['eval_training']['best_epoch']=9
store['active_learning_steps'][93]['acquisition']={'indices': [55414, 35261, 6742, 19880, 8606, 15095, 36048, 49828, 7945, 4123], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.37279701232910156, 0.3086276054382324, 0.26331818103790283, 0.41986024379730225, 0.5998407602310181, 0.38002443313598633, 0.377799391746521, 0.4769771099090576, 0.4269651174545288, 0.4153660535812378]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.2481708526611328})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.6212858557701111})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.42133185267448425})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34396713972091675})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2685871422290802})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29155194759368896})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2998192310333252})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27564799785614014})
store['active_learning_steps'][94]['training']['best_epoch']=5
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9723, 'crossentropy': 0.26391923828125}
store['active_learning_steps'][94]['eval_training']={}
store['active_learning_steps'][94]['eval_training']['epochs']=[]
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7080955505371094})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.44363725185394287})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3630262613296509})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.36971521377563477})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3813774585723877})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3287498950958252})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.30780261754989624})
store['active_learning_steps'][94]['eval_training']['best_epoch']=7
store['active_learning_steps'][94]['acquisition']={'indices': [29871, 53848, 2810, 36214, 33874, 40654, 58268, 33010, 23185, 7847], 'labels': [-1, -1, -1, -1, -1, 5, -1, -1, -1, -1], 'scores': [0.40250205993652344, 0.196905255317688, 0.30313336849212646, 0.43652987480163574, 0.3353031873703003, 0.6494805812835693, 0.24237561225891113, 0.459075927734375, 0.35032641887664795, 0.3105512857437134]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.1619802713394165})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5634678602218628})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3514382541179657})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29409798979759216})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.27192550897598267})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.2642030119895935})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2742002606391907})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9775390625, 'crossentropy': 0.23716066777706146})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9765625, 'crossentropy': 0.2644670903682709})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.27330389618873596})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.2470182627439499})
store['active_learning_steps'][95]['training']['best_epoch']=8
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9722, 'crossentropy': 0.228401611328125}
store['active_learning_steps'][95]['eval_training']={}
store['active_learning_steps'][95]['eval_training']['epochs']=[]
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7145720720291138})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4521329402923584})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3622015714645386})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32790085673332214})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29674190282821655})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2739456593990326})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28131651878356934})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30714690685272217})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2528088688850403})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.248251810669899})
store['active_learning_steps'][95]['eval_training']['best_epoch']=10
store['active_learning_steps'][95]['acquisition']={'indices': [17182, 23012, 13021, 43083, 22521, 3392, 3795, 18308, 42255, 49354], 'labels': [-1, -1, 5, -1, -1, 6, -1, -1, 3, 0], 'scores': [0.45863640308380127, 0.42783546447753906, 0.4888172745704651, 0.37632787227630615, 0.29593682289123535, 0.48523062467575073, 0.3500913381576538, 0.45514988899230957, 0.37414127588272095, 0.5694268941879272]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.4065685272216797})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6637002229690552})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.43884873390197754})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35010582208633423})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3136436343193054})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28847092390060425})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28639158606529236})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2914251685142517})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28456413745880127})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30046436190605164})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2885100245475769})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2697688639163971})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.28985193371772766})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.32545754313468933})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3532763123512268})
store['active_learning_steps'][96]['training']['best_epoch']=12
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.974, 'crossentropy': 0.252268896484375}
