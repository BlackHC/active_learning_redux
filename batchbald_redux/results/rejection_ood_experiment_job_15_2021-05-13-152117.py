store = {}
store['timestamp']=1620915677
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=15']
store['commit']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['github_url']='7a88a46c213fc419b8e48358058ec72fe5b0f546'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=15
store['worker_id']=15
store['num_workers']=20
store['config']={'seed': 1256, 'acquisition_size': 10, 'max_training_set': 450, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'evaluation_set_size': 1000, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.TemperedEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 55573, 35472, 44048, 48031, 5616, 10110, 47420, 56990, 34198, 3029, 35714, 21536, 48519, 8821, 11261, 35237, 33891, 37129, 46683, 6968, 15917, 30184, 50055, 14637, 45260, 43969, 10437, 2876, 50948, 39707, 3528, 45335, 18929, 9875, 49363, 41508, 9560, 1924, 15787, 5403, 5615, 55510, 50607, 9578, 57007, 57028, 16837, 12013, 2754, 6915, 13601, 7092, 21368, 33017, 9825, 56727, 45538, 47536, 43477, 9094, 11537, 35500, 54546, 9166, 39370, 9048, 10266, 24393, 47437, 34695, 42096, 57189, 55739, 16200, 5792, 29025, 916, 2561, 6478, 47847, 57057, 19875, 35424, 25257, 33756, 19600, 12052, 24009, 32909, 30237, 12576, 52141, 17872, 4550, 39268, 519, 9638, 35936, 15224, 3792, 5715, 15969, 32775, 19757, 34588, 28991, 47417, 26501, 12108, 14035, 42320, 16927, 42102, 39050, 27573, 30980, 53362, 18819, 21800, 44138, 39879, 13092, 51760, 48953, 30134, 8719, 13859, 2289, 52341, 55733, 45005, 31935, 4826, 20497, 27599, 56115, 33474, 56710, 42762, 3681, 19265, 17878, 37986, 38828, 43419, 16975, 28970, 15619, 36523, 36882, 8284, 35602, 6703, 13161, 27076, 15751, 29505, 30910, 8882, 47523, 15845, 22259, 37741, 13860, 26135, 55016, 34935, 25909, 36446, 34336, 2737, 35786, 22086, 27077, 30238, 9395, 47960, 2036, 9848, 23011, 16442, 31019, 20615, 4128, 2169, 29105, 22429, 391, 58140, 56602, 47583, 43918, 10660, 32880, 22512, 20363, 49112, 5384, 44920, 5573, 48032, 40646, 43252, 2404, 36797, 29079, 40018, 37047, 41512, 26129, 37115, 35072, 36688, 54003, 72, 57690, 7382, 7896, 24110, 35372, 37098, 54536, 34513, 37157, 46938, 40741, 2400, 47776, 56137, 26845, 7807, 49378, 55783, 38704, 32188, 40272, 14450, 31833, 15143, 1091, 22123, 2336, 36219, 37784, 47491, 32596, 32632, 46499, 47567, 32654, 32249, 50579, 48013, 18352, 48865, 47630, 4942, 51065, 350, 38185, 33483, 45245, 31525, 27549, 12980, 28641, 57432, 14920, 56349, 26847, 13135, 6994, 54825, 49620, 30829, 1023, 43256, 24410, 11588, 16631, 48652, 6949, 15071, 13848, 23723, 40181, 17107, 47685, 6215, 31937, 16425, 1182, 45658, 7519, 45981, 47286, 39906, 16326, 41971, 45567, 801, 10664, 52801, 42890, 32972, 45974, 20801, 23496, 5803, 26853, 42295, 34121, 19215, 12917, 51600, 27383, 20917, 38856, 15822, 6612, 13359, 28181, 7145, 49775, 50793, 51027, 31010, 17759, 47660, 25349, 13088, 33069, 19857, 37366, 30281, 32857, 28844, 14669, 22037, 51418, 27283, 48147, 43457, 23781, 1480, 7484, 21057, 28830, 33106, 1250, 22780, 28522, 32709, 30979, 13551, 51405, 18748, 35631, 24253, 38171, 60, 371, 41954, 33065, 58882, 17217, 31971, 2976, 21853, 45446, 20316, 48744, 14498, 38160, 3127, 12900, 17728, 44195, 29203, 13469, 14272, 54174, 44209, 28508, 30244, 18016, 13078, 4937, 4418, 24371, 29591, 23197, 30861, 55489, 37175, 42539, 32506, 38702, 42651, 10508, 46870, 49549, 306, 38725, 13074, 19689, 27135, 16068, 18137, 54422, 229, 30072, 4701, 18693, 26516, 43141, 5588, 7356, 55148, 2773, 24971, 57801, 17644, 54479, 22990, 32697, 37709, 24668, 56723, 48176, 1071, 50513, 15825, 57995, 39009, 33461, 2290, 52072, 41379, 35025, 47568, 15139, 19279, 37055, 14957, 3067, 48437, 95, 36994, 17142, 386, 19885, 37042, 47665, 50274, 687, 31224, 46665, 7739, 3271, 33761, 50636, 52414, 10524, 46614, 29251, 58061, 49329, 18866, 14754, 33306, 2185, 30432, 9032, 2691, 53164, 889, 642, 53097, 40610, 22223, 5262, 55022, 19423, 44235, 42084, 213, 42659, 20462, 39393, 22381, 13588, 30727, 13590, 21480, 36776, 23428, 13945, 1926, 2728, 43321, 29950, 380, 27254, 50466, 31965, 24052, 44454, 20076, 43415, 17659, 12075, 26428, 8705, 29556, 8108, 8710, 17032, 17195, 5481, 24223, 17968, 56054, 39333, 7414, 51216, 56096, 14241, 52773, 4205, 4820, 39616, 57036, 31372, 50035, 58080, 55203, 16182, 3531, 10344, 40148, 40970, 30302, 51340, 10202, 8585, 42306, 52950, 18359, 37912, 36608, 16972, 6600, 6571, 21377, 50848, 34357, 20542, 31343, 7626, 4027, 46433, 19376, 14990, 47621, 55413, 45332, 443, 22686, 3816, 57548, 39464, 8648, 22363, 43453, 20776, 14190, 57560, 37225, 27020, 7126, 14587, 36030, 31037, 24073, 36827, 52662, 50002, 32099, 33251, 36584, 56786, 46933, 55356, 26966, 55852, 8256, 50298, 23132, 21423, 58741, 27145, 38430, 37354, 49986, 4321, 12610, 34482, 35794, 33581, 48521, 36270, 57175, 11554, 11773, 41082, 37625, 41077, 13036, 32625, 54017, 24360, 10232, 37544, 52803, 17753, 18076, 45089, 41136, 38817, 46397, 38539, 12171, 38664, 19549, 21628, 50727, 22246, 11552, 18882, 33157, 28222, 44780, 6358, 38063, 25394, 5389, 41879, 10897, 37613, 11836, 35232, 42738, 35317, 4561, 47465, 4686, 23136, 55714, 36355, 25616, 22677, 57008, 2514, 46607, 56228, 37950, 36238, 22669, 52438, 2462, 13513, 8214, 7275, 44709, 53972, 46788, 10361, 56834, 28318, 18899, 2099, 27401, 22631, 39731, 41898, 42040, 103, 40399, 20693, 11800, 41145, 42018, 54663, 35296, 18148, 14398, 25591, 57510, 396, 50036, 46861, 57811, 53831, 49304, 51555, 29614, 767, 23451, 44100, 33464, 18880, 11228, 495, 54097, 25589, 14888, 29546, 48602, 25620, 43587, 16157, 38318, 32996, 5932, 8680, 23148, 21552, 53560, 49567, 33438, 15904, 51589, 1482, 10358, 9909, 46165, 27865, 36980, 34007, 40932, 28404, 46114, 44999, 37616, 35106, 55471, 47102, 5416, 36213, 38604, 27370, 46586, 1058, 41353, 51445, 33147, 29756, 4267, 32143, 32573, 47622, 2067, 56245, 19327, 33491, 8126, 23186, 36972, 37267, 4468, 28935, 38899, 44762, 14585, 13362, 57939, 26314, 45526, 1249, 57336, 48183, 41836, 33520, 22744, 18011, 21583, 48309, 8824, 5922, 37671, 31436, 33673, 21578, 486, 47460, 4253, 5655, 30159, 49512, 26479, 50997, 1774, 44803, 55187, 30013, 33736, 49169, 46464, 5897, 15494, 49595, 27019, 43234, 10432, 52389, 51755, 36367, 26520, 7121, 27580, 29048, 30362, 46700, 54800, 12140, 34361, 50498, 16704, 33140, 16433, 58038, 43507, 1690, 51794, 13738, 32834, 1397, 43375, 41734, 2559, 10799, 43130, 56561, 1241, 578, 2158, 48021, 14652, 16889, 30931, 7442, 27083, 33198, 38006, 36315, 57286, 53653, 15402, 47026, 13995, 17023, 23903, 23338, 16854, 32682, 41782, 34614, 27421, 8861, 51925, 39678, 39206, 23829, 40768, 17870, 3750, 52154, 6187, 42283, 47299, 53098, 50320, 440, 18092, 1399, 40162, 29895, 4779, 4317, 37922, 14631, 40310, 31258, 17291, 7251, 20722, 4795, 7167, 31444, 52440, 33486, 2206, 15675, 54426, 9574, 54012, 28833, 44428, 257, 43981, 10113, 52679, 17506, 48498, 5380, 19457, 55453, 40466, 6051, 50242, 1707, 52890, 57541, 23002, 5870, 9834, 1005, 20860, 53538, 18018, 27468, 36289, 3010, 28768, 31221, 44127, 51305, 55460, 4203, 17948, 3378, 218, 7362, 35374, 24125, 37159, 47110, 23231, 30771, 22938, 16146, 37053, 56977, 54091, 37647, 10682, 46966, 51112, 26852, 5338, 57213, 16725, 14928, 52720, 30893, 37557, 35244, 2178, 33203, 6767, 27619, 22637, 3133, 19806, 12528, 24026, 34553, 4354, 43599, 42186, 10959, 28871, 42870, 56353, 51660, 58378, 29543, 17668, 49438, 12635, 14668, 29643, 35276, 14412, 10542, 41589, 52734, 13669]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.4560861587524414})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.818056344985962})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.2931690216064453})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.3175411224365234})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6433, 'crossentropy': 2.3924369140625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.2934014797210693})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.3035998344421387})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.253909707069397})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [8877, 56857, 27637, 44048, 14202, 53157, 17771, 3346, 4888, 1920], 'labels': [0, 0, 0, 9, 0, -1, -1, 9, -1, 2], 'scores': [0.9891050457954407, 0.9393786489963531, 0.7287912964820862, 0.803618848323822, 0.8609018921852112, 0.5669963359832764, 0.6078512668609619, 0.9025051593780518, 0.4887967109680176, 0.4723051190376282]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.218360185623169})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.352001667022705})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.169111967086792})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.95798921585083})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6667, 'crossentropy': 2.0505021484375}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.187873363494873})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.1468127965927124})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.2736533880233765})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [39679, 23440, 41098, 7719, 57990, 4201, 38295, 55503, 17137, 12712], 'labels': [6, 8, 4, 2, 3, 0, 5, 0, 2, 8], 'scores': [0.742222785949707, 0.5954527258872986, 0.5050246119499207, 0.5992277264595032, 0.6157076954841614, 0.8140060305595398, 0.7076007127761841, 0.682731956243515, 0.753091037273407, 0.840865433216095]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.8940308094024658})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.1267001628875732})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.2882328033447266})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 2.453049659729004})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7247, 'crossentropy': 1.5955052734375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.0989294052124023})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.1141226291656494})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.0493037700653076})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [52439, 45082, 7637, 42110, 41204, 25015, 48055, 21517, 39096, 3379], 'labels': [5, 8, 4, 5, 2, 8, 8, 4, 9, 1], 'scores': [0.534875750541687, 0.5898024439811707, 0.6314542889595032, 0.6785769462585449, 0.6683621406555176, 0.5073035359382629, 0.7773467302322388, 0.7164735198020935, 0.5645166635513306, 0.547418475151062]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.522796392440796})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.959803581237793})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.9673165082931519})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 2.2625539302825928})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7823, 'crossentropy': 1.32494228515625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.9949778914451599})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 0.9252901077270508})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 0.8922642469406128})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [509, 45431, 14737, 45348, 14798, 14015, 18864, 2909, 50562, 17540], 'labels': [3, 9, 5, 2, 2, 9, 2, -1, 9, 1], 'scores': [0.46574801206588745, 0.49741095304489136, 0.6689677238464355, 0.48682844638824463, 0.43260830640792847, 0.5584504008293152, 0.4919256567955017, 0.3575208783149719, 0.4949198365211487, 0.7873310446739197]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.545912265777588})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.6541635990142822})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.849669098854065})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 2.1160504817962646})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7643, 'crossentropy': 1.336644921875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.129154920578003})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 0.9377419948577881})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.0023000240325928})
store['active_learning_steps'][4]['eval_training']['best_epoch']=2
store['active_learning_steps'][4]['acquisition']={'indices': [15656, 41838, 47723, 9256, 23570, 34344, 20223, 32120, 958, 36870], 'labels': [3, -1, 8, 1, 7, 7, 7, 7, 6, 8], 'scores': [0.574383556842804, 0.31735384464263916, 0.5744827389717102, 0.3564378023147583, 0.4527590274810791, 0.5533182621002197, 0.5733486413955688, 0.4709056615829468, 0.5039492845535278, 0.5010092854499817]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1313526630401611})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.3622957468032837})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.3537179231643677})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.5943622589111328})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.812, 'crossentropy': 0.9734634765625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9361000061035156})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 0.8473302125930786})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.7883061766624451})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [14512, 24356, 32687, 35694, 30487, 31891, 41060, 48513, 30738, 9620], 'labels': [5, 3, -1, 9, 2, 5, 6, 1, 8, 3], 'scores': [0.5155112743377686, 0.38484781980514526, 0.20275533199310303, 0.5448611974716187, 0.5305193662643433, 0.41281968355178833, 0.40721893310546875, 0.4549952745437622, 0.5586298108100891, 0.4367297291755676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9524751901626587})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.2507461309432983})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.3135324716567993})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.3405914306640625})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8147, 'crossentropy': 0.91127783203125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.868324875831604})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.8336922526359558})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.8130170106887817})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [14679, 5332, 27420, 5485, 53133, 50007, 34115, 26966, 10218, 20683], 'labels': [8, 3, 3, 6, 8, 3, 5, 7, 6, -1], 'scores': [0.5136411190032959, 0.5527465343475342, 0.572284996509552, 0.5135822296142578, 0.44133496284484863, 0.46748828887939453, 0.45128118991851807, 0.5083109140396118, 0.46355152130126953, 0.351542592048645]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 0.9965500831604004})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9517421722412109})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0909947156906128})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.2134419679641724})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.2020211219787598})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8761, 'crossentropy': 0.779683984375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.721021294593811})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.6403464078903198})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6022723913192749})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.5939019918441772})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [55947, 21436, 52686, 30386, 13831, 4111, 39929, 44491, 42532, 250], 'labels': [3, 2, 5, 3, 3, 2, 2, -1, 2, 3], 'scores': [0.5379973649978638, 0.4020717442035675, 0.729513943195343, 0.3389723300933838, 0.5430104732513428, 0.7221868634223938, 0.5083074569702148, 0.39980387687683105, 0.732265293598175, 0.5973093509674072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8461782932281494})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8933271169662476})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8948447704315186})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.044095516204834})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8596, 'crossentropy': 0.75100498046875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.7877331972122192})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7055705189704895})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.6769119501113892})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [19101, 4058, 41847, 26918, 35073, 22354, 57090, 17535, 42193, 25590], 'labels': [3, 8, 5, 5, 3, 5, 8, 0, 5, 3], 'scores': [0.4930678606033325, 0.5966670513153076, 0.637843132019043, 0.5071001648902893, 0.521292507648468, 0.33650004863739014, 0.4803335666656494, 0.4455922245979309, 0.5872836112976074, 0.5527418851852417]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8495590686798096})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8191187977790833})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.901235044002533})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8346773982048035})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.969188392162323})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8804, 'crossentropy': 0.72914453125}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7615869045257568})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.6106864213943481})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.5866439342498779})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.5826352834701538})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [7879, 43278, 53150, 49525, 25281, 13881, 4842, 52113, 57747, 18637], 'labels': [2, 4, 8, 8, 2, 6, 7, -1, 4, 4], 'scores': [0.43250179290771484, 0.7081658244132996, 0.5644120573997498, 0.5007237195968628, 0.4958324432373047, 0.44079482555389404, 0.6423457860946655, 0.3676140308380127, 0.4357132911682129, 0.5242973566055298]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8453291058540344})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7758524417877197})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.828849196434021})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8261992931365967})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.1031289100646973})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8937, 'crossentropy': 0.640982568359375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7514477968215942})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.5885686278343201})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5628095865249634})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5451550483703613})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [5106, 4592, 45062, 55302, 18056, 1646, 48899, 14896, 50660, 15723], 'labels': [9, 7, 9, 0, 4, -1, 2, 8, 8, 8], 'scores': [0.6284507513046265, 0.3924727439880371, 0.5863298773765564, 0.5300471484661102, 0.42943131923675537, 0.5890191793441772, 0.4836485981941223, 0.5818778276443481, 0.5016680359840393, 0.5735544562339783]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9151089191436768})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6278841495513916})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7258793115615845})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.796754002571106})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7410578727722168})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9086, 'crossentropy': 0.60229912109375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6648696660995483})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.5667867064476013})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.536379337310791})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5095391273498535})
store['active_learning_steps'][11]['eval_training']['best_epoch']=4
store['active_learning_steps'][11]['acquisition']={'indices': [47930, 25711, 1423, 33420, 45138, 34540, 28731, 7096, 11755, 40492], 'labels': [-1, 5, 0, -1, 6, 8, 2, 6, 3, 6], 'scores': [0.4507880210876465, 0.38726210594177246, 0.6803522109985352, 0.371431827545166, 0.47127604484558105, 0.4299255609512329, 0.6022934317588806, 0.489477276802063, 0.40137577056884766, 0.7462618947029114]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8003636002540588})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5958192348480225})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7054382562637329})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5968126058578491})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6682344675064087})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9183, 'crossentropy': 0.566156201171875}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7230687141418457})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.4992949366569519})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.48537391424179077})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.46932610869407654})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [10195, 25493, 29626, 16473, 52273, 30065, 26367, 3392, 53529, 19037], 'labels': [0, -1, -1, 2, 6, 7, 4, 6, 5, 6], 'scores': [0.5493676662445068, 0.2739311456680298, 0.33448100090026855, 0.5750682353973389, 0.4860107898712158, 0.3636934459209442, 0.23403114080429077, 0.5670298933982849, 0.37571442127227783, 0.43424177169799805]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.802606463432312})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6308004856109619})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5754452347755432})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6432062983512878})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5478542447090149})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.644489049911499})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6613476276397705})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6454408168792725})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.934, 'crossentropy': 0.50918349609375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5813416242599487})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.43834465742111206})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.41808706521987915})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.3771582245826721})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.381033718585968})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.3804881274700165})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3798861801624298})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [25910, 47929, 41133, 39122, 28420, 42971, 55054, 14127, 9428, 32120], 'labels': [1, -1, 8, -1, 1, -1, 3, -1, 9, -1], 'scores': [0.6048091650009155, 0.4113043546676636, 0.6087384819984436, 0.546443521976471, 0.5076397061347961, 0.24927175045013428, 0.4452667236328125, 0.4490323066711426, 0.5738092660903931, 0.5396303534507751]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.8529917001724243})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5429949760437012})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.50953209400177})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5839524269104004})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.550366997718811})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5551295280456543})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9291, 'crossentropy': 0.49437373046875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6666665077209473})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.4796667993068695})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4290101230144501})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4258449077606201})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4060150980949402})
store['active_learning_steps'][14]['eval_training']['best_epoch']=5
store['active_learning_steps'][14]['acquisition']={'indices': [17450, 15869, 6387, 32543, 26338, 19512, 53872, 29899, 7214, 2735], 'labels': [4, -1, 6, -1, 0, -1, 8, 3, 3, -1], 'scores': [0.4582866430282593, 0.37948668003082275, 0.4543111324310303, 0.44009149074554443, 0.5556786060333252, 0.5030558705329895, 0.648652970790863, 0.610740602016449, 0.4663233160972595, 0.4742986559867859]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9041051864624023})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6118031740188599})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5508769750595093})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5895487070083618})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6461189985275269})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6172311305999756})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.932, 'crossentropy': 0.49349931640625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6231605410575867})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4926448166370392})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.43781381845474243})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4120824933052063})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4055216908454895})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [20711, 35332, 51003, 33860, 20289, 55092, 53826, 58138, 8722, 6696], 'labels': [4, 9, -1, 9, -1, -1, 5, 8, -1, -1], 'scores': [0.32755815982818604, 0.5220082998275757, 0.2786877155303955, 0.5523669719696045, 0.325872540473938, 0.5384731292724609, 0.4019286632537842, 0.390280157327652, 0.4133028984069824, 0.5427569150924683]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8224878311157227})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5178266167640686})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5492845773696899})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5142048597335815})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5668296813964844})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.57110995054245})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5616133809089661})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9376, 'crossentropy': 0.47151328125}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6363382935523987})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4855091869831085})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4221450090408325})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.36253952980041504})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.38095033168792725})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4006001353263855})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [27458, 42004, 2151, 25420, 29259, 48098, 14649, 2872, 20856, 40943], 'labels': [2, 7, -1, -1, 8, 7, 0, 1, -1, -1], 'scores': [0.5354892611503601, 0.4288449287414551, 0.5139567255973816, 0.45535731315612793, 0.6987335681915283, 0.7852046489715576, 0.5121023654937744, 0.664821445941925, 0.24606215953826904, 0.5043429136276245]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8659980297088623})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5370582938194275})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5364699363708496})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5011327266693115})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5135296583175659})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5332046747207642})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6151959896087646})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9381, 'crossentropy': 0.45092734375}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6307339072227478})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.45049482583999634})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.3670974373817444})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.3745361566543579})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.38017737865448})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3582967519760132})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [9417, 37696, 39348, 17958, 54287, 49039, 31308, 33798, 31651, 57280], 'labels': [-1, 2, -1, 9, -1, -1, 8, -1, -1, 7], 'scores': [0.45890843868255615, 0.5661236047744751, 0.4445977210998535, 0.7523305416107178, 0.3952445983886719, 0.47389113903045654, 0.5596656203269958, 0.48596030473709106, 0.2283710241317749, 0.5104170441627502]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8714848160743713})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5444023609161377})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5359817743301392})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5199689865112305})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4919547438621521})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5159123539924622})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5565471649169922})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5470033288002014})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9419, 'crossentropy': 0.46108017578125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6888415813446045})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.46364909410476685})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.38640183210372925})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.3865596354007721})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3700129985809326})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.3356485068798065})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.3477969169616699})
store['active_learning_steps'][18]['eval_training']['best_epoch']=6
store['active_learning_steps'][18]['acquisition']={'indices': [33975, 24424, 528, 26768, 8702, 32817, 14780, 47952, 56296, 56758], 'labels': [-1, 1, 8, -1, 9, -1, 9, -1, -1, -1], 'scores': [0.4015388488769531, 0.6203787922859192, 0.48066073656082153, 0.41905415058135986, 0.6972026228904724, 0.3339040279388428, 0.31253159046173096, 0.4577890634536743, 0.36093491315841675, 0.4558295011520386]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8136166930198669})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5316650867462158})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5616055130958557})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5505613088607788})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.582412838935852})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.9312, 'crossentropy': 0.480378271484375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6379249095916748})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5125791430473328})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.48961377143859863})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.46796274185180664})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [32173, 52834, 38178, 38593, 56824, 8516, 22241, 38050, 9107, 22743], 'labels': [7, 2, 7, 3, 2, 7, 8, 6, 3, 7], 'scores': [0.47579729557037354, 0.5040147304534912, 0.3890218734741211, 0.39688926935195923, 0.3987811207771301, 0.4638194441795349, 0.3588801622390747, 0.3949546813964844, 0.39152687788009644, 0.5405375361442566]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7895914316177368})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5298133492469788})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5232887268066406})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4858449101448059})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.542896032333374})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5744725465774536})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5484435558319092})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9388, 'crossentropy': 0.439808056640625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5641183853149414})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.44269707798957825})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3875822424888611})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.3596774935722351})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.38455522060394287})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.3426787853240967})
store['active_learning_steps'][20]['eval_training']['best_epoch']=6
store['active_learning_steps'][20]['acquisition']={'indices': [46288, 44737, 53568, 45282, 29168, 14484, 27719, 8350, 17777, 22948], 'labels': [2, 7, 5, -1, -1, 2, -1, -1, 3, -1], 'scores': [0.466302752494812, 0.48694127798080444, 0.46364259719848633, 0.3792458772659302, 0.41965150833129883, 0.6351705193519592, 0.4688127040863037, 0.4999110698699951, 0.6130974888801575, 0.38230741024017334]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8331106305122375})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.49360769987106323})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.4830639362335205})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4579659104347229})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4964550733566284})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.49137020111083984})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5145424604415894})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9432, 'crossentropy': 0.398842236328125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6167178153991699})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.46361255645751953})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4044199287891388})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.3878106474876404})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.37693139910697937})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.3744335472583771})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [53522, 55245, 24145, 36910, 2000, 28216, 35406, 8214, 3030, 3594], 'labels': [2, -1, 3, -1, 5, -1, 5, 7, 9, -1], 'scores': [0.4389922618865967, 0.31592726707458496, 0.48674410581588745, 0.2262789011001587, 0.621300458908081, 0.39574944972991943, 0.5529752373695374, 0.5279478430747986, 0.6578790545463562, 0.3368086814880371]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0305898189544678})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5522564649581909})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.46757346391677856})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5312492251396179})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5119603276252747})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4858609437942505})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9429, 'crossentropy': 0.417490185546875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6478032469749451})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5146611332893372})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.4739629626274109})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4144202470779419})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.38393670320510864})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [59312, 7919, 37643, 31530, 41334, 57308, 53990, 33669, 46412, 16180], 'labels': [4, 4, 3, 8, 9, 3, -1, -1, 0, -1], 'scores': [0.5372150540351868, 0.34803181886672974, 0.5957496762275696, 0.3949927091598511, 0.5307037830352783, 0.36861658096313477, 0.28215545415878296, 0.4570823907852173, 0.45851874351501465, 0.3480546474456787]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.929745078086853})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5581515431404114})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5195505619049072})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5054317712783813})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4426167607307434})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5148171186447144})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5667977333068848})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.5272116661071777})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9458, 'crossentropy': 0.41285009765625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.696718692779541})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.45097848773002625})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.39743876457214355})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.35428735613822937})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.35141780972480774})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3190392255783081})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.34342944622039795})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [42703, 47929, 52166, 15832, 32926, 37138, 7399, 5315, 28499, 17496], 'labels': [0, -1, 7, -1, 8, -1, -1, 3, -1, -1], 'scores': [0.6255188584327698, 0.579002320766449, 0.4856024384498596, 0.6568201780319214, 0.5927231311798096, 0.6493149995803833, 0.31081271171569824, 0.5596974492073059, 0.4274823069572449, 0.36291956901550293]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8867064118385315})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5650919675827026})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.45208853483200073})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.46237075328826904})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4508035182952881})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.48251986503601074})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.453522264957428})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4960741400718689})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9492, 'crossentropy': 0.3969974365234375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6478761434555054})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4665640592575073})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4026569128036499})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3698153495788574})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.34402236342430115})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.3620096743106842})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.34217098355293274})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [22597, 53496, 20087, 44123, 55447, 20169, 1075, 43998, 46937, 49294], 'labels': [9, 9, 6, 8, -1, 4, 7, 7, -1, -1], 'scores': [0.40522003173828125, 0.43735039234161377, 0.5461040735244751, 0.5893898010253906, 0.5790286064147949, 0.7035641670227051, 0.7604888677597046, 0.5475464463233948, 0.5368211269378662, 0.4936171770095825]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9498032331466675})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.541879415512085})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4340164065361023})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4648343324661255})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4737738370895386})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4707000255584717})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9478, 'crossentropy': 0.394346484375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7162319421768188})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4769204258918762})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.45745009183883667})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4301804304122925})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.40291377902030945})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [33340, 48490, 7229, 26733, 18193, 14681, 29952, 39538, 45036, 7787], 'labels': [5, 7, 7, 2, -1, 9, 1, 9, 5, -1], 'scores': [0.4700911045074463, 0.31200024485588074, 0.3528217673301697, 0.4660661220550537, 0.5087903738021851, 0.32288897037506104, 0.4617260694503784, 0.43909043073654175, 0.3756070137023926, 0.38455235958099365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9675396680831909})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4869289696216583})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.40850651264190674})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4378979802131653})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4240661561489105})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4330309331417084})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.9495, 'crossentropy': 0.376738623046875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6349987983703613})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.4488990306854248})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.40959352254867554})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3949006199836731})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.37123632431030273})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [50690, 1083, 6574, 4850, 15870, 47156, 6731, 36867, 39818, 29361], 'labels': [5, -1, -1, 3, 6, 0, -1, -1, -1, 5], 'scores': [0.2760559320449829, 0.39647138118743896, 0.5319640636444092, 0.4524351954460144, 0.40095531940460205, 0.4126599431037903, 0.45160579681396484, 0.4454382061958313, 0.2503242492675781, 0.419070839881897]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8977874517440796})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4721587300300598})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.37829679250717163})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.37111276388168335})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4075038731098175})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4276247024536133})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3975503444671631})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9532, 'crossentropy': 0.3494248046875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5804964303970337})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4963086247444153})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3974888324737549})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3835456967353821})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3431108295917511})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.32917216420173645})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [15855, 54530, 50070, 14673, 13647, 24201, 42317, 17593, 3810, 3411], 'labels': [5, -1, -1, 5, 3, -1, 5, -1, 3, -1], 'scores': [0.535465657711029, 0.5195614099502563, 0.34363436698913574, 0.2803170680999756, 0.5747014284133911, 0.36466383934020996, 0.554776132106781, 0.40051984786987305, 0.42492246627807617, 0.34447336196899414]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9977928400039673})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.529160737991333})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4509500563144684})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.40017279982566833})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38346558809280396})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3906483054161072})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45758599042892456})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4119911789894104})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.9568, 'crossentropy': 0.34957421875}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6335183382034302})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.44456928968429565})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3667612075805664})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.38812169432640076})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.32666486501693726})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.297879159450531})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.29459813237190247})
store['active_learning_steps'][28]['eval_training']['best_epoch']=7
store['active_learning_steps'][28]['acquisition']={'indices': [45101, 41799, 5355, 21023, 33438, 9774, 16951, 20068, 45774, 30584], 'labels': [5, -1, -1, 2, 2, 7, 8, 8, 3, 8], 'scores': [0.4760209321975708, 0.4101628065109253, 0.5633898973464966, 0.5332346558570862, 0.4831712543964386, 0.5865011215209961, 0.4326580762863159, 0.5880944132804871, 0.41618475317955017, 0.5874743461608887]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9292725920677185})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4883875250816345})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37758904695510864})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3671802282333374})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4198612570762634})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.47770535945892334})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.4316459894180298})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9618, 'crossentropy': 0.29625185546875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.622029185295105})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.43039071559906006})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.42093902826309204})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.38147521018981934})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3366926312446594})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.31593310832977295})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [30884, 36008, 10165, 40909, 32343, 45911, 45788, 31060, 34847, 30272], 'labels': [2, 8, -1, 1, 5, -1, -1, -1, 0, -1], 'scores': [0.5986416339874268, 0.6425928473472595, 0.5411139726638794, 0.3872841000556946, 0.39236146211624146, 0.24926990270614624, 0.40019524097442627, 0.4673370122909546, 0.6826084852218628, 0.26896119117736816]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.0392025709152222})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.49493467807769775})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.47967618703842163})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3948327898979187})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42263883352279663})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4018796682357788})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.37856245040893555})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4087679088115692})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38560473918914795})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.47621840238571167})
store['active_learning_steps'][30]['training']['best_epoch']=7
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9641, 'crossentropy': 0.3169839599609375}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6264106035232544})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.41860055923461914})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.347683310508728})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3285554051399231})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3153190016746521})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2913205027580261})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.30485063791275024})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.26518714427948})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.24824252724647522})
store['active_learning_steps'][30]['eval_training']['best_epoch']=9
store['active_learning_steps'][30]['acquisition']={'indices': [4564, 6908, 13834, 32700, 13376, 55778, 17356, 1627, 3044, 32841], 'labels': [-1, -1, -1, -1, 3, -1, -1, -1, -1, -1], 'scores': [0.6878801584243774, 0.49689793586730957, 0.43424123525619507, 0.491502046585083, 0.6012840867042542, 0.7722511887550354, 0.5689513683319092, 0.3906196355819702, 0.4048505425453186, 0.4335262179374695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.075181245803833})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5885772705078125})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.44075167179107666})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.41865068674087524})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.395185261964798})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.4018435478210449})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44663870334625244})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41216811537742615})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9562, 'crossentropy': 0.337227001953125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6419347524642944})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4157630205154419})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.37325748801231384})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.35061824321746826})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3153178095817566})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.31567442417144775})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3025384545326233})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [23280, 38609, 23912, 32250, 12666, 53930, 14125, 697, 26554, 51161], 'labels': [-1, -1, -1, -1, -1, -1, -1, 4, -1, -1], 'scores': [0.36310774087905884, 0.3649340867996216, 0.26299846172332764, 0.3979465961456299, 0.41060590744018555, 0.41829657554626465, 0.4380204677581787, 0.5498137772083282, 0.31326937675476074, 0.508736789226532]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1004745960235596})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5066947937011719})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4266892373561859})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4316225051879883})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.43771475553512573})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3569381833076477})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.4421989321708679})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3728159964084625})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.41095560789108276})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9616, 'crossentropy': 0.3357080322265625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7012860774993896})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4851004481315613})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3625403642654419})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3336176872253418})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3270876407623291})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.31131458282470703})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.28750839829444885})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2618539333343506})
store['active_learning_steps'][32]['eval_training']['best_epoch']=8
store['active_learning_steps'][32]['acquisition']={'indices': [15696, 29552, 37682, 13195, 59455, 37945, 24479, 41567, 55417, 42782], 'labels': [-1, -1, 9, -1, 9, 4, 8, -1, 1, 7], 'scores': [0.4468280076980591, 0.32337403297424316, 0.6589496433734894, 0.488520085811615, 0.2850227653980255, 0.2709157466888428, 0.5489785075187683, 0.36732327938079834, 0.367531418800354, 0.49930572509765625]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0273034572601318})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5455946326255798})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.40495777130126953})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.40836629271507263})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3591439723968506})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38020604848861694})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39165762066841125})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4016379117965698})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9593, 'crossentropy': 0.323561767578125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7043968439102173})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.4757005274295807})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4027074873447418})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.35031965374946594})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3589593172073364})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.31009554862976074})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.2816239595413208})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [1627, 39032, 58748, 19630, 22470, 46987, 23967, 41109, 54719, 16072], 'labels': [-1, -1, -1, -1, 5, -1, -1, -1, -1, 5], 'scores': [0.4919273853302002, 0.4098658561706543, 0.5534712076187134, 0.5137733221054077, 0.3543166518211365, 0.5484579801559448, 0.7832453846931458, 0.46028459072113037, 0.4554678201675415, 0.42964065074920654]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9186045527458191})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5532432794570923})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.44406598806381226})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3900538980960846})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3649371266365051})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.382157564163208})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37761735916137695})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3854210674762726})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9618, 'crossentropy': 0.3172365234375}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6808207035064697})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.43632227182388306})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.3912137746810913})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3913853168487549})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.32998818159103394})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.30935996770858765})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3092786371707916})
store['active_learning_steps'][34]['eval_training']['best_epoch']=7
store['active_learning_steps'][34]['acquisition']={'indices': [1674, 50801, 35154, 55916, 50835, 37221, 43339, 56043, 52874, 26914], 'labels': [9, 4, -1, -1, 4, 4, -1, -1, -1, -1], 'scores': [0.5612467527389526, 0.4647083282470703, 0.29001832008361816, 0.5876063108444214, 0.52727210521698, 0.3843797445297241, 0.3094085454940796, 0.5146967172622681, 0.2684028148651123, 0.49119043350219727]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.1185427904129028})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6233457326889038})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.43434828519821167})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37528544664382935})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3816097676753998})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3718639612197876})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3830333948135376})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36995929479599})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39149385690689087})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40462467074394226})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.43263429403305054})
store['active_learning_steps'][35]['training']['best_epoch']=8
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9618, 'crossentropy': 0.3370864990234375}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5656543970108032})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.41292572021484375})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.33165013790130615})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.3083210289478302})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.29087400436401367})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.27673792839050293})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.27489233016967773})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2758065462112427})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2750151753425598})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2658647894859314})
store['active_learning_steps'][35]['eval_training']['best_epoch']=10
store['active_learning_steps'][35]['acquisition']={'indices': [52288, 57383, 44314, 17131, 47828, 6862, 3160, 19837, 18112, 46015], 'labels': [-1, 5, -1, 3, 5, -1, -1, -1, -1, -1], 'scores': [0.5616928339004517, 0.6728092432022095, 0.2624387741088867, 0.7870697379112244, 0.4626079499721527, 0.4447849988937378, 0.5586692094802856, 0.5220950841903687, 0.3973914384841919, 0.548818051815033]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9948340654373169})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5440952777862549})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4384130835533142})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37471431493759155})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4345954656600952})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35636311769485474})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.38199564814567566})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.36573919653892517})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.44408613443374634})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9595, 'crossentropy': 0.32157470703125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6595265865325928})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4309559464454651})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.34195131063461304})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3272378444671631})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.331223726272583})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.29850301146507263})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2774120569229126})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2727828621864319})
store['active_learning_steps'][36]['eval_training']['best_epoch']=8
store['active_learning_steps'][36]['acquisition']={'indices': [13709, 8762, 7806, 3720, 59303, 46040, 28368, 1346, 9669, 53844], 'labels': [6, 3, -1, -1, 8, 1, 9, 0, -1, 5], 'scores': [0.6886329650878906, 0.44782644510269165, 0.46480870246887207, 0.4307190179824829, 0.5216290354728699, 0.3257882595062256, 0.693174421787262, 0.4377952814102173, 0.25919783115386963, 0.42322659492492676]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.9584727883338928})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49522802233695984})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3759905695915222})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4023435115814209})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3436790108680725})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3573414087295532})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3515699505805969})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3510666787624359})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.9661, 'crossentropy': 0.290725634765625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5641188621520996})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.39976632595062256})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.360353946685791})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3092700242996216})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3593742549419403})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3160223960876465})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2792586088180542})
store['active_learning_steps'][37]['eval_training']['best_epoch']=7
store['active_learning_steps'][37]['acquisition']={'indices': [29376, 49543, 51295, 2036, 28930, 39304, 3762, 43194, 16775, 5093], 'labels': [-1, 8, -1, 4, 7, 4, 8, -1, -1, -1], 'scores': [0.32789546251296997, 0.46480613946914673, 0.4931391477584839, 0.34775716066360474, 0.4826827049255371, 0.5340434312820435, 0.6310844421386719, 0.262719988822937, 0.5647444128990173, 0.3956223726272583]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0736594200134277})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4803704023361206})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3639926314353943})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3805962800979614})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.38664674758911133})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3541230261325836})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3598594069480896})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37669050693511963})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.34987974166870117})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.41218018531799316})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4054761826992035})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3822021186351776})
store['active_learning_steps'][38]['training']['best_epoch']=9
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.3108468505859375}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6457861065864563})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.42151230573654175})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3347344696521759})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2858101427555084})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3076096773147583})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26500245928764343})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2797052264213562})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.26237207651138306})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24762968719005585})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.24397388100624084})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24210089445114136})
store['active_learning_steps'][38]['eval_training']['best_epoch']=11
store['active_learning_steps'][38]['acquisition']={'indices': [28946, 1241, 31014, 51673, 16836, 4675, 9576, 48532, 34369, 40335], 'labels': [-1, -1, -1, 2, 7, -1, -1, -1, -1, -1], 'scores': [0.343539834022522, 0.47150373458862305, 0.494767427444458, 0.5976163744926453, 0.7668452858924866, 0.5015079975128174, 0.5104560852050781, 0.4923449754714966, 0.5140727162361145, 0.5715476274490356]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0605791807174683})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5244793891906738})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4201953411102295})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36208951473236084})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34686729311943054})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33366626501083374})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3917849659919739})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3726942241191864})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39884525537490845})
store['active_learning_steps'][39]['training']['best_epoch']=6
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.9637, 'crossentropy': 0.309102490234375}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6677488088607788})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.46878582239151})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.36941805481910706})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.34995779395103455})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3116784691810608})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.30615711212158203})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2811097502708435})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.28663134574890137})
store['active_learning_steps'][39]['eval_training']['best_epoch']=7
store['active_learning_steps'][39]['acquisition']={'indices': [44987, 32419, 32974, 52661, 27637, 21569, 32932, 44344, 1105, 20153], 'labels': [-1, 4, -1, -1, -1, 8, -1, -1, -1, -1], 'scores': [0.3390008211135864, 0.4789208173751831, 0.5063802003860474, 0.4231301546096802, 0.49094122648239136, 0.32600921392440796, 0.60235595703125, 0.43647754192352295, 0.5111799240112305, 0.4201127290725708]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9390236735343933})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5126478672027588})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.40005484223365784})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39193952083587646})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.4228250980377197})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.41128379106521606})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37141525745391846})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3939872980117798})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.41587579250335693})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.39228153228759766})
store['active_learning_steps'][40]['training']['best_epoch']=7
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.9645, 'crossentropy': 0.295346923828125}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6233751177787781})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.47571831941604614})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.3874322175979614})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.33077263832092285})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.30476802587509155})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.29916414618492126})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.29240062832832336})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3005509078502655})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.29234039783477783})
store['active_learning_steps'][40]['eval_training']['best_epoch']=9
store['active_learning_steps'][40]['acquisition']={'indices': [56799, 14201, 23576, 46548, 31539, 5065, 3122, 37778, 41790, 42381], 'labels': [-1, 7, -1, -1, -1, 2, -1, 8, -1, -1], 'scores': [0.4425177574157715, 0.5209340453147888, 0.41218864917755127, 0.47320556640625, 0.4675333499908447, 0.5624499320983887, 0.40459930896759033, 0.5338268280029297, 0.6751630902290344, 0.5168624520301819]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.105391025543213})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5322467088699341})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3807131052017212})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3689724802970886})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3719130754470825})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36236122250556946})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.359872430562973})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37836503982543945})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3977854251861572})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4024668335914612})
store['active_learning_steps'][41]['training']['best_epoch']=7
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.9629, 'crossentropy': 0.3181803466796875}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6169726848602295})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.44473621249198914})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3310287594795227})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.329845130443573})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3011470139026642})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2693592309951782})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30169546604156494})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.28686290979385376})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27666860818862915})
store['active_learning_steps'][41]['eval_training']['best_epoch']=6
store['active_learning_steps'][41]['acquisition']={'indices': [4564, 35632, 48461, 39107, 47144, 10840, 29264, 55912, 55324, 1995], 'labels': [-1, 0, -1, -1, -1, -1, -1, 2, -1, -1], 'scores': [0.6244763135910034, 0.5487512350082397, 0.6286271214485168, 0.5062141418457031, 0.45017433166503906, 0.32251250743865967, 0.5276552438735962, 0.2831549048423767, 0.6400455832481384, 0.5960608720779419]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0847158432006836})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5514692068099976})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.46225976943969727})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3787156939506531})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3691524565219879})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3589111864566803})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.33423006534576416})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3844068944454193})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.36054062843322754})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.36898982524871826})
store['active_learning_steps'][42]['training']['best_epoch']=7
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.9636, 'crossentropy': 0.2995098876953125}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.662197470664978})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.42787784337997437})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3860938847064972})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3303326964378357})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2977905571460724})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.28519171476364136})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2893756031990051})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.2767668664455414})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.25946033000946045})
store['active_learning_steps'][42]['eval_training']['best_epoch']=9
store['active_learning_steps'][42]['acquisition']={'indices': [32395, 32776, 54167, 59798, 52422, 28686, 13175, 26580, 9924, 41882], 'labels': [-1, 4, -1, -1, -1, -1, -1, -1, 8, -1], 'scores': [0.5157015323638916, 0.6928937435150146, 0.6296541690826416, 0.41979801654815674, 0.544567346572876, 0.5156742334365845, 0.5697087645530701, 0.4082787036895752, 0.4149817228317261, 0.5109125375747681]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.0155205726623535})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5522412061691284})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.36809343099594116})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38007909059524536})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33853858709335327})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36922091245651245})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3570418953895569})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3573957085609436})
store['active_learning_steps'][43]['training']['best_epoch']=5
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.9622, 'crossentropy': 0.3118489501953125}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6875413060188293})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4754411578178406})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3503595292568207})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.35814157128334045})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.32136499881744385})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3185938596725464})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.30881428718566895})
store['active_learning_steps'][43]['eval_training']['best_epoch']=7
store['active_learning_steps'][43]['acquisition']={'indices': [38415, 1403, 59701, 22659, 21711, 10048, 58649, 22842, 21387, 37227], 'labels': [-1, -1, 5, 1, -1, 1, 0, -1, -1, -1], 'scores': [0.5191832780838013, 0.39612406492233276, 0.507210373878479, 0.218977153301239, 0.45118415355682373, 0.49425357580184937, 0.3877902030944824, 0.4144362211227417, 0.5755831599235535, 0.4819856286048889]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0093072652816772})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4910898208618164})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3874524235725403})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.38348591327667236})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37150564789772034})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38901033997535706})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36965224146842957})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3613817095756531})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3602130115032196})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4328446388244629})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.38679832220077515})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.42630642652511597})
store['active_learning_steps'][44]['training']['best_epoch']=9
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.9611, 'crossentropy': 0.3288169677734375}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6204262971878052})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4197114408016205})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.35366836190223694})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3194243311882019})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.27931129932403564})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2741227447986603})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.25879016518592834})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.25666797161102295})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.25735390186309814})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.25557079911231995})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.24339959025382996})
store['active_learning_steps'][44]['eval_training']['best_epoch']=11
store['active_learning_steps'][44]['acquisition']={'indices': [29332, 52938, 42042, 41999, 25918, 34425, 51058, 58670, 40646, 37050], 'labels': [-1, -1, 4, -1, -1, 2, -1, -1, -1, 6], 'scores': [0.49909090995788574, 0.5420064926147461, 0.5014837384223938, 0.6152653098106384, 0.5264790058135986, 0.38202357292175293, 0.5563308000564575, 0.46421563625335693, 0.7570239305496216, 0.39880481362342834]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.974199652671814})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5448431372642517})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3787970542907715})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.369474321603775})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.35542142391204834})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.379519522190094})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3905048668384552})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.36185628175735474})
store['active_learning_steps'][45]['training']['best_epoch']=5
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.9635, 'crossentropy': 0.3028364013671875}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6634812355041504})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.43630582094192505})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.392743319272995})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3473920226097107})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3544861376285553})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3088691830635071})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.30021199584007263})
store['active_learning_steps'][45]['eval_training']['best_epoch']=7
store['active_learning_steps'][45]['acquisition']={'indices': [57281, 5667, 17058, 6442, 27914, 48569, 58568, 53227, 32783, 20277], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.5706807374954224, 0.7122799754142761, 0.5468631386756897, 0.5750967264175415, 0.7040176391601562, 0.6546872854232788, 0.49708664417266846, 0.6570711135864258, 0.22497892379760742, 0.6468251943588257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.081178903579712})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5591578483581543})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.41462182998657227})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39216333627700806})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3831784129142761})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.4053267240524292})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33540886640548706})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36751681566238403})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.40562331676483154})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.41566747426986694})
store['active_learning_steps'][46]['training']['best_epoch']=7
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.9649, 'crossentropy': 0.3078775634765625}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.693535327911377})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.41573870182037354})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3506010174751282})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.33336228132247925})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3098519444465637})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2984876036643982})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27653205394744873})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2929987907409668})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2745288014411926})
store['active_learning_steps'][46]['eval_training']['best_epoch']=9
store['active_learning_steps'][46]['acquisition']={'indices': [15592, 59446, 32724, 55196, 44417, 12773, 28181, 14645, 12783, 51579], 'labels': [9, -1, -1, 6, -1, -1, -1, -1, -1, -1], 'scores': [0.4889828562736511, 0.5416699647903442, 0.5601827502250671, 0.5790219902992249, 0.3608620762825012, 0.6066884398460388, 0.46135902404785156, 0.5802248120307922, 0.4473928213119507, 0.33043259382247925]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8919023871421814})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5077077150344849})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.35812652111053467})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35698115825653076})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.34960874915122986})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3392350971698761})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32394707202911377})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.377189040184021})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3444257974624634})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3414526581764221})
store['active_learning_steps'][47]['training']['best_epoch']=7
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.9644, 'crossentropy': 0.2897378662109375}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6700600385665894})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4250856041908264})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3734983205795288})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3203163743019104})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3044491112232208})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2927064299583435})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2692359685897827})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2742155194282532})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27210870385169983})
store['active_learning_steps'][47]['eval_training']['best_epoch']=7
store['active_learning_steps'][47]['acquisition']={'indices': [58593, 48933, 4564, 21351, 24860, 14722, 44040, 8583, 3748, 29923], 'labels': [-1, 2, -1, 9, 9, 0, 0, -1, -1, -1], 'scores': [0.32738959789276123, 0.6808117032051086, 0.5023397207260132, 0.33955246210098267, 0.5578871965408325, 0.3723753094673157, 0.45570826530456543, 0.30596089363098145, 0.2656219005584717, 0.4414098262786865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0820248126983643})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5198924541473389})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4394941031932831})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3978159427642822})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4078235626220703})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.4169969856739044})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.41704124212265015})
store['active_learning_steps'][48]['training']['best_epoch']=4
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.9513, 'crossentropy': 0.3504303955078125}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7077707052230835})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.508888840675354})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4582519829273224})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.380837619304657})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.379926860332489})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.39252769947052})
store['active_learning_steps'][48]['eval_training']['best_epoch']=5
store['active_learning_steps'][48]['acquisition']={'indices': [31845, 29839, 9409, 33774, 41556, 5778, 30915, 14066, 5600, 39424], 'labels': [8, 2, -1, -1, 0, -1, -1, -1, 6, -1], 'scores': [0.4279352128505707, 0.5926786661148071, 0.4679117202758789, 0.6241452693939209, 0.25019991397857666, 0.5493496656417847, 0.4103572368621826, 0.613816499710083, 0.5093758702278137, 0.5134479999542236]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0921897888183594})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.642913818359375})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.46153151988983154})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.4369644224643707})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.38681524991989136})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36222755908966064})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3891162574291229})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.36811965703964233})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3476116955280304})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37831640243530273})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3607481122016907})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3817889988422394})
store['active_learning_steps'][49]['training']['best_epoch']=9
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.9667, 'crossentropy': 0.3074996337890625}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6531480550765991})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.4303932189941406})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3881412744522095})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3343000113964081})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.336214542388916})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2932106554508209})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2866189479827881})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28409257531166077})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2779741883277893})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2782464027404785})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.28817641735076904})
store['active_learning_steps'][49]['eval_training']['best_epoch']=9
store['active_learning_steps'][49]['acquisition']={'indices': [23309, 4606, 57728, 30322, 39746, 45413, 24765, 19695, 38158, 43636], 'labels': [-1, -1, 9, -1, -1, -1, -1, -1, 8, -1], 'scores': [0.5065526962280273, 0.5307039022445679, 0.46750569343566895, 0.5766052007675171, 0.4420529007911682, 0.6468348503112793, 0.6549559235572815, 0.4239673614501953, 0.6248976588249207, 0.7233572006225586]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.146209955215454})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5370407104492188})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.44465887546539307})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.418673574924469})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3510964810848236})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.39453816413879395})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36825037002563477})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4181658625602722})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.9636, 'crossentropy': 0.297549169921875}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.687954306602478})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4693719744682312})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.370990514755249})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3510527014732361})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3085082769393921})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3320137560367584})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.29940152168273926})
store['active_learning_steps'][50]['eval_training']['best_epoch']=7
store['active_learning_steps'][50]['acquisition']={'indices': [52493, 43569, 42707, 30658, 24066, 29967, 44012, 42332, 58064, 21914], 'labels': [-1, -1, -1, 4, -1, 2, -1, -1, 3, -1], 'scores': [0.39027833938598633, 0.42813944816589355, 0.3882988691329956, 0.489560067653656, 0.47380077838897705, 0.40152716636657715, 0.43176233768463135, 0.4788443446159363, 0.5191724896430969, 0.2920725345611572]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.126312494277954})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5609519481658936})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4951515793800354})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.42307049036026})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3529684245586395})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.37324291467666626})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35900288820266724})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3395521640777588})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3531840443611145})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35224443674087524})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.37573671340942383})
store['active_learning_steps'][51]['training']['best_epoch']=8
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.9668, 'crossentropy': 0.2870136962890625}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6530568599700928})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.45248985290527344})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.38279712200164795})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.35234349966049194})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30277353525161743})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3192811608314514})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2919541597366333})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28804445266723633})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2972904145717621})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2617233693599701})
store['active_learning_steps'][51]['eval_training']['best_epoch']=10
store['active_learning_steps'][51]['acquisition']={'indices': [39748, 22283, 25508, 55773, 24696, 21185, 7072, 44538, 19868, 49361], 'labels': [-1, 9, 5, -1, -1, -1, -1, -1, 5, -1], 'scores': [0.35977721214294434, 0.5142436027526855, 0.477165162563324, 0.476381778717041, 0.5237618684768677, 0.5038984417915344, 0.5192995071411133, 0.4323887228965759, 0.6953141689300537, 0.5390585064888]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.0436313152313232})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.47632282972335815})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3992916941642761})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.33033257722854614})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3466375470161438})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3418576121330261})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.32957929372787476})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3575531542301178})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33671605587005615})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3642703890800476})
store['active_learning_steps'][52]['training']['best_epoch']=7
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.9661, 'crossentropy': 0.308064453125}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6569877862930298})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4281618595123291})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34008538722991943})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3269370198249817})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2985233664512634})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.26273155212402344})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2733672857284546})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2646709382534027})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2627965211868286})
store['active_learning_steps'][52]['eval_training']['best_epoch']=6
store['active_learning_steps'][52]['acquisition']={'indices': [47904, 5951, 16100, 32800, 37675, 41934, 26568, 36329, 10581, 26947], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 8], 'scores': [0.4800475835800171, 0.5245362520217896, 0.3647550344467163, 0.31649839878082275, 0.5572553277015686, 0.5528732538223267, 0.7259061336517334, 0.5870309472084045, 0.30349600315093994, 0.6683086156845093]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0130234956741333})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5076627135276794})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4136798083782196})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35794350504875183})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32446104288101196})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3061451017856598})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36601120233535767})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.375021755695343})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3385242819786072})
store['active_learning_steps'][53]['training']['best_epoch']=6
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.9664, 'crossentropy': 0.277260546875}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6698386669158936})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.4281384348869324})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.3364763855934143})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3051931858062744})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.29126808047294617})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.30559563636779785})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29735657572746277})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2712538242340088})
store['active_learning_steps'][53]['eval_training']['best_epoch']=8
store['active_learning_steps'][53]['acquisition']={'indices': [25596, 21011, 32553, 52703, 8974, 32823, 34539, 36810, 35136, 39863], 'labels': [1, -1, -1, -1, 6, -1, -1, 6, 4, -1], 'scores': [0.5112792253494263, 0.4138603210449219, 0.28908199071884155, 0.34027743339538574, 0.4855578541755676, 0.4074835777282715, 0.3619648218154907, 0.49775946140289307, 0.35089826583862305, 0.4390338063240051]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1175880432128906})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5431647896766663})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4794510006904602})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3607211410999298})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.36924853920936584})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3884977400302887})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.350538432598114})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.399422287940979})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3244699239730835})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3808363676071167})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3518660068511963})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.37248408794403076})
store['active_learning_steps'][54]['training']['best_epoch']=9
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.9696, 'crossentropy': 0.285019873046875}
store['active_learning_steps'][54]['eval_training']={}
store['active_learning_steps'][54]['eval_training']['epochs']=[]
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6288219690322876})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.42113709449768066})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3666006326675415})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3125164210796356})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2820667028427124})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2902209162712097})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.27883756160736084})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26614511013031006})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.25942710041999817})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.270469605922699})
store['active_learning_steps'][54]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2266591489315033})
store['active_learning_steps'][54]['eval_training']['best_epoch']=11
store['active_learning_steps'][54]['acquisition']={'indices': [54844, 50426, 2434, 4063, 9383, 15549, 15185, 12635, 38252, 32718], 'labels': [-1, 7, -1, 8, 2, -1, 2, -1, 5, -1], 'scores': [0.3675886392593384, 0.48748892545700073, 0.476154088973999, 0.4666522145271301, 0.49224215745925903, 0.39514994621276855, 0.6021351218223572, 0.4559502601623535, 0.5890029668807983, 0.36841368675231934]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 1.109856128692627})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5242652893066406})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36913710832595825})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3540544807910919})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3442506194114685})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33823463320732117})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3524933457374573})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3628304898738861})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3599541485309601})
store['active_learning_steps'][55]['training']['best_epoch']=6
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.9716, 'crossentropy': 0.2651380126953125}
store['active_learning_steps'][55]['eval_training']={}
store['active_learning_steps'][55]['eval_training']['epochs']=[]
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6272518634796143})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.4352514147758484})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3797619044780731})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3266836404800415})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.28226083517074585})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.2831710875034332})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2691292464733124})
store['active_learning_steps'][55]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23477138578891754})
store['active_learning_steps'][55]['eval_training']['best_epoch']=8
store['active_learning_steps'][55]['acquisition']={'indices': [12054, 22805, 22591, 17676, 17478, 27008, 15523, 25603, 24531, 26121], 'labels': [-1, -1, -1, -1, 4, -1, -1, -1, 3, -1], 'scores': [0.5106415748596191, 0.34404706954956055, 0.48717200756073, 0.3238551616668701, 0.5907720327377319, 0.5131445527076721, 0.5777292847633362, 0.5076242685317993, 0.513416051864624, 0.41483819484710693]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.0010242462158203})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4683495759963989})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.39868584275245667})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3344481587409973})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.310655415058136})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31935542821884155})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32774120569229126})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31769460439682007})
store['active_learning_steps'][56]['training']['best_epoch']=5
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.9681, 'crossentropy': 0.2712770263671875}
store['active_learning_steps'][56]['eval_training']={}
store['active_learning_steps'][56]['eval_training']['epochs']=[]
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6869981288909912})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.44439345598220825})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.3664934039115906})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3354339003562927})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3088874816894531})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3243703246116638})
store['active_learning_steps'][56]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.2932550013065338})
store['active_learning_steps'][56]['eval_training']['best_epoch']=7
store['active_learning_steps'][56]['acquisition']={'indices': [18879, 48596, 13654, 16697, 10259, 8543, 34505, 19896, 2209, 48471], 'labels': [-1, -1, -1, -1, -1, -1, -1, 6, -1, -1], 'scores': [0.4876549243927002, 0.4445685148239136, 0.32868432998657227, 0.3072512745857239, 0.37468111515045166, 0.4187890291213989, 0.33206915855407715, 0.46852171421051025, 0.49046504497528076, 0.5284252166748047]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.0975141525268555})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4922369718551636})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38115036487579346})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34960854053497314})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.35023877024650574})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.35588714480400085})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.352949321269989})
store['active_learning_steps'][57]['training']['best_epoch']=4
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.9644, 'crossentropy': 0.3278714599609375}
store['active_learning_steps'][57]['eval_training']={}
store['active_learning_steps'][57]['eval_training']['epochs']=[]
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6007453203201294})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.46094560623168945})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.37366655468940735})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.39891481399536133})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3865509033203125})
store['active_learning_steps'][57]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3342110514640808})
store['active_learning_steps'][57]['eval_training']['best_epoch']=6
store['active_learning_steps'][57]['acquisition']={'indices': [13840, 1916, 1046, 22549, 17784, 11012, 30085, 41567, 13997, 7225], 'labels': [-1, -1, 0, -1, 8, -1, 9, -1, -1, 3], 'scores': [0.6129342317581177, 0.39849352836608887, 0.30350232124328613, 0.357696533203125, 0.3184587359428406, 0.39153021574020386, 0.29256749153137207, 0.40677666664123535, 0.4117150902748108, 0.3969162702560425]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.2114702463150024})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.558449387550354})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4562976360321045})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.38225820660591125})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3508012294769287})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.364885151386261})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35757017135620117})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35297057032585144})
store['active_learning_steps'][58]['training']['best_epoch']=5
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.9656, 'crossentropy': 0.298174072265625}
store['active_learning_steps'][58]['eval_training']={}
store['active_learning_steps'][58]['eval_training']['epochs']=[]
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6844606399536133})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47814539074897766})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.3864137530326843})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3854925036430359})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.34230488538742065})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36249014735221863})
store['active_learning_steps'][58]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.32406991720199585})
store['active_learning_steps'][58]['eval_training']['best_epoch']=7
store['active_learning_steps'][58]['acquisition']={'indices': [13434, 2879, 23106, 13333, 25406, 25123, 10295, 18624, 34233, 56539], 'labels': [-1, -1, 2, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4303152561187744, 0.4196659326553345, 0.5083910226821899, 0.5542464256286621, 0.43453145027160645, 0.27997148036956787, 0.48609089851379395, 0.527783989906311, 0.43407177925109863, 0.5247725248336792]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0947661399841309})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5324987173080444})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3914664387702942})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.36448734998703003})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35333800315856934})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.31450337171554565})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3497178554534912})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30631858110427856})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33249330520629883})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.36505067348480225})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.33129769563674927})
store['active_learning_steps'][59]['training']['best_epoch']=8
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.9683, 'crossentropy': 0.266213623046875}
store['active_learning_steps'][59]['eval_training']={}
store['active_learning_steps'][59]['eval_training']['epochs']=[]
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6526998281478882})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3875574767589569})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.36780059337615967})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2995445728302002})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2745617926120758})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2560226619243622})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2762870788574219})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26907503604888916})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.24895036220550537})
store['active_learning_steps'][59]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.23637424409389496})
store['active_learning_steps'][59]['eval_training']['best_epoch']=10
store['active_learning_steps'][59]['acquisition']={'indices': [36742, 547, 25117, 40237, 49297, 50646, 23099, 41381, 33801, 49153], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.34246599674224854, 0.5397524833679199, 0.5483267307281494, 0.6506364345550537, 0.44741982221603394, 0.5573368072509766, 0.5775861740112305, 0.5769766569137573, 0.4138333201408386, 0.5797510743141174]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.187757968902588})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6310569047927856})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.45891284942626953})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32922035455703735})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3779257833957672})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3267720937728882})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3710363209247589})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.39414745569229126})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3615248203277588})
store['active_learning_steps'][60]['training']['best_epoch']=6
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.9648, 'crossentropy': 0.3110519775390625}
store['active_learning_steps'][60]['eval_training']={}
store['active_learning_steps'][60]['eval_training']['epochs']=[]
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6964054703712463})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.47688791155815125})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.3706097900867462})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3432738780975342})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33653461933135986})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2828642725944519})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.30226635932922363})
store['active_learning_steps'][60]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27779603004455566})
store['active_learning_steps'][60]['eval_training']['best_epoch']=8
store['active_learning_steps'][60]['acquisition']={'indices': [58072, 15132, 2782, 26763, 48270, 32335, 41503, 30171, 51658, 22525], 'labels': [-1, -1, -1, -1, 2, 1, -1, -1, -1, 4], 'scores': [0.36901843547821045, 0.6513398885726929, 0.5955239534378052, 0.44458281993865967, 0.5980857014656067, 0.5815109610557556, 0.5784876346588135, 0.2831437587738037, 0.48397064208984375, 0.41838496923446655]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.105779767036438})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.537458062171936})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4008724093437195})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3805621862411499})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3532155156135559})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3228037357330322})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.363783597946167})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3356683850288391})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33571571111679077})
store['active_learning_steps'][61]['training']['best_epoch']=6
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.9654, 'crossentropy': 0.2776533447265625}
store['active_learning_steps'][61]['eval_training']={}
store['active_learning_steps'][61]['eval_training']['epochs']=[]
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6542516946792603})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.47455480694770813})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.34904587268829346})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3392666280269623})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3196938633918762})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30871033668518066})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30189239978790283})
store['active_learning_steps'][61]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2870551347732544})
store['active_learning_steps'][61]['eval_training']['best_epoch']=8
store['active_learning_steps'][61]['acquisition']={'indices': [33063, 47789, 468, 15905, 11880, 5727, 58597, 55303, 34199, 30308], 'labels': [-1, -1, -1, -1, 8, -1, -1, -1, -1, -1], 'scores': [0.3837856352329254, 0.31491899490356445, 0.30523157119750977, 0.40914177894592285, 0.3665034770965576, 0.43143314123153687, 0.3860633373260498, 0.3796374201774597, 0.39985668659210205, 0.39432287216186523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.1743600368499756})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5687216520309448})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.40872690081596375})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.37459444999694824})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.36299431324005127})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3519153594970703})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34161001443862915})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35703542828559875})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3571806252002716})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4133932590484619})
store['active_learning_steps'][62]['training']['best_epoch']=7
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.9679, 'crossentropy': 0.282852685546875}
store['active_learning_steps'][62]['eval_training']={}
store['active_learning_steps'][62]['eval_training']['epochs']=[]
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6395077109336853})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.42169326543807983})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.3736708164215088})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31329384446144104})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3160884976387024})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29650968313217163})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28899726271629333})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2702063322067261})
store['active_learning_steps'][62]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2662511467933655})
store['active_learning_steps'][62]['eval_training']['best_epoch']=9
store['active_learning_steps'][62]['acquisition']={'indices': [10992, 40371, 12061, 42355, 58772, 7949, 24822, 49512, 55586, 5759], 'labels': [-1, 9, 9, 3, -1, -1, 4, -1, 8, -1], 'scores': [0.5979245901107788, 0.31209415197372437, 0.4481101632118225, 0.49596333503723145, 0.49905574321746826, 0.6179655194282532, 0.5382372736930847, 0.3649517297744751, 0.3767011761665344, 0.33073484897613525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.1291766166687012})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6247297525405884})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4286435842514038})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38056012988090515})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3816404938697815})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3477475345134735})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.36790743470191956})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3643551170825958})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.346025675535202})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.37417763471603394})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.42401665449142456})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.4114595949649811})
store['active_learning_steps'][63]['training']['best_epoch']=9
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.9672, 'crossentropy': 0.2994166748046875}
store['active_learning_steps'][63]['eval_training']={}
store['active_learning_steps'][63]['eval_training']['epochs']=[]
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6900749206542969})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4690827429294586})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37414318323135376})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3275831937789917})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3154846429824829})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.29570165276527405})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2707366347312927})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28742048144340515})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27727949619293213})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.25417259335517883})
store['active_learning_steps'][63]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.288061261177063})
store['active_learning_steps'][63]['eval_training']['best_epoch']=10
store['active_learning_steps'][63]['acquisition']={'indices': [45292, 30852, 38644, 40962, 30988, 36013, 2075, 22031, 32480, 59785], 'labels': [-1, -1, -1, -1, -1, 9, -1, 4, -1, -1], 'scores': [0.5584395527839661, 0.524467945098877, 0.5311357378959656, 0.6190168261528015, 0.4351387023925781, 0.38515445590019226, 0.5834358930587769, 0.271935373544693, 0.5441972017288208, 0.25375640392303467]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9946691393852234})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4911429286003113})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.4354292154312134})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3713534474372864})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29402607679367065})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3258737623691559})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.32319027185440063})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.32621079683303833})
store['active_learning_steps'][64]['training']['best_epoch']=5
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.9685, 'crossentropy': 0.2802545166015625}
store['active_learning_steps'][64]['eval_training']={}
store['active_learning_steps'][64]['eval_training']['epochs']=[]
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6712841987609863})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.43131697177886963})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.395546555519104})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33275219798088074})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.339414119720459})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2735289931297302})
store['active_learning_steps'][64]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3051086664199829})
store['active_learning_steps'][64]['eval_training']['best_epoch']=6
store['active_learning_steps'][64]['acquisition']={'indices': [28149, 15949, 28143, 36761, 31499, 40544, 2426, 40819, 49362, 13752], 'labels': [9, 5, -1, -1, -1, -1, 1, -1, 1, 9], 'scores': [0.4533065855503082, 0.6901158094406128, 0.37599456310272217, 0.46548032760620117, 0.30515551567077637, 0.3515355587005615, 0.4734419584274292, 0.29646944999694824, 0.43890100717544556, 0.29636919498443604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1192735433578491})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5936635732650757})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.40177780389785767})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3400252163410187})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32296472787857056})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.34552305936813354})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33898529410362244})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32466766238212585})
store['active_learning_steps'][65]['training']['best_epoch']=5
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.9643, 'crossentropy': 0.2820488525390625}
store['active_learning_steps'][65]['eval_training']={}
store['active_learning_steps'][65]['eval_training']['epochs']=[]
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6465516090393066})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4278559684753418})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3647306561470032})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.34335726499557495})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3481072187423706})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.32150664925575256})
store['active_learning_steps'][65]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3127286732196808})
store['active_learning_steps'][65]['eval_training']['best_epoch']=7
store['active_learning_steps'][65]['acquisition']={'indices': [56682, 54950, 31121, 1688, 58628, 35368, 30844, 27791, 52446, 12306], 'labels': [-1, 8, -1, 6, -1, -1, 8, -1, -1, -1], 'scores': [0.4844151735305786, 0.632258415222168, 0.49557626247406006, 0.3339850902557373, 0.5512003898620605, 0.4558204412460327, 0.5332614183425903, 0.47759103775024414, 0.34498101472854614, 0.5972291827201843]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.2799949645996094})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.544080376625061})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.43479418754577637})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.38074809312820435})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.36648494005203247})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3643948435783386})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31856903433799744})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3440321087837219})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.31623685359954834})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3471076190471649})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.34020519256591797})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.34723925590515137})
store['active_learning_steps'][66]['training']['best_epoch']=9
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.9722, 'crossentropy': 0.2481729736328125}
store['active_learning_steps'][66]['eval_training']={}
store['active_learning_steps'][66]['eval_training']['epochs']=[]
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7168551683425903})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4498848021030426})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.352824866771698})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.320435106754303})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27241984009742737})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2700422406196594})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.27138710021972656})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2537555694580078})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.25429868698120117})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.24967263638973236})
store['active_learning_steps'][66]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23107747733592987})
store['active_learning_steps'][66]['eval_training']['best_epoch']=11
store['active_learning_steps'][66]['acquisition']={'indices': [32603, 26434, 2508, 14175, 48596, 25727, 56249, 53598, 23844, 20072], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 3], 'scores': [0.5388121008872986, 0.38835424184799194, 0.590446412563324, 0.5347931385040283, 0.5247824788093567, 0.5508903861045837, 0.6134899854660034, 0.613318681716919, 0.501096248626709, 0.5086771845817566]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.0411102771759033})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.4748980402946472})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.38435128331184387})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.35193702578544617})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3199138045310974})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3566153645515442})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28887319564819336})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3159559369087219})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3049832582473755})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3014290928840637})
store['active_learning_steps'][67]['training']['best_epoch']=7
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.9698, 'crossentropy': 0.261340966796875}
store['active_learning_steps'][67]['eval_training']={}
store['active_learning_steps'][67]['eval_training']['epochs']=[]
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6797612905502319})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.43410417437553406})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.33586668968200684})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.31884732842445374})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3264240026473999})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2832601070404053})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.25827738642692566})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2835237979888916})
store['active_learning_steps'][67]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24439752101898193})
store['active_learning_steps'][67]['eval_training']['best_epoch']=9
store['active_learning_steps'][67]['acquisition']={'indices': [29632, 28168, 34071, 32863, 23101, 48205, 50473, 17440, 54475, 3015], 'labels': [-1, -1, 6, -1, -1, -1, 9, -1, -1, -1], 'scores': [0.38481956720352173, 0.6446772813796997, 0.4347548484802246, 0.7118260264396667, 0.5443230271339417, 0.47115635871887207, 0.2551308274269104, 0.4630167484283447, 0.55497145652771, 0.5773245692253113]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.18454110622406})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5818697214126587})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.411973774433136})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3522741198539734})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35735732316970825})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3331957161426544})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.31501027941703796})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3641703128814697})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3254687190055847})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3378925919532776})
store['active_learning_steps'][68]['training']['best_epoch']=7
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.9671, 'crossentropy': 0.2698959716796875}
store['active_learning_steps'][68]['eval_training']={}
store['active_learning_steps'][68]['eval_training']['epochs']=[]
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6518827676773071})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4251375198364258})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.3693639636039734})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3204595446586609})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.30353111028671265})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.287837415933609})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.30242720246315})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.26711684465408325})
store['active_learning_steps'][68]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.26872265338897705})
store['active_learning_steps'][68]['eval_training']['best_epoch']=8
store['active_learning_steps'][68]['acquisition']={'indices': [33885, 47765, 59029, 26190, 27321, 41567, 53450, 9990, 11525, 17080], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.7079185247421265, 0.6427531242370605, 0.6042946577072144, 0.5865797400474548, 0.6862372756004333, 0.6770164966583252, 0.5463253259658813, 0.3861183524131775, 0.6973099708557129, 0.6171698570251465]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.2253491878509521})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5802410840988159})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.42856526374816895})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3216527998447418})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3367322087287903})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.33819255232810974})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32824236154556274})
store['active_learning_steps'][69]['training']['best_epoch']=4
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9678, 'crossentropy': 0.2850497802734375}
store['active_learning_steps'][69]['eval_training']={}
store['active_learning_steps'][69]['eval_training']['epochs']=[]
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6688982248306274})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.47903501987457275})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.4563707113265991})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.38900089263916016})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3458300232887268})
store['active_learning_steps'][69]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3729337453842163})
store['active_learning_steps'][69]['eval_training']['best_epoch']=5
store['active_learning_steps'][69]['acquisition']={'indices': [49064, 5217, 53552, 53472, 49587, 45577, 5155, 37558, 50051, 33989], 'labels': [-1, 4, 5, -1, 4, -1, 4, 5, -1, -1], 'scores': [0.34691321849823, 0.5381791591644287, 0.3701605200767517, 0.3651333451271057, 0.45369040966033936, 0.3534804582595825, 0.5567803382873535, 0.2745599150657654, 0.41733741760253906, 0.3768136501312256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.2257084846496582})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5742839574813843})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3941259980201721})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.37296122312545776})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3154929280281067})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3517422676086426})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.317527711391449})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.34492063522338867})
store['active_learning_steps'][70]['training']['best_epoch']=5
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.9687, 'crossentropy': 0.2758322265625}
store['active_learning_steps'][70]['eval_training']={}
store['active_learning_steps'][70]['eval_training']['epochs']=[]
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6990253329277039})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.45844566822052})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.365736186504364})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32023999094963074})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.310434490442276})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2960415482521057})
store['active_learning_steps'][70]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3119579553604126})
store['active_learning_steps'][70]['eval_training']['best_epoch']=6
store['active_learning_steps'][70]['acquisition']={'indices': [43176, 28536, 50435, 34408, 8178, 37745, 26940, 54586, 27420, 32453], 'labels': [2, 3, -1, -1, 5, -1, 6, 9, -1, 8], 'scores': [0.31109723448753357, 0.43740272521972656, 0.36667144298553467, 0.3459627628326416, 0.36524099111557007, 0.4514963626861572, 0.537264347076416, 0.49342697858810425, 0.515389084815979, 0.5441762208938599]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0248706340789795})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5587704181671143})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.36082661151885986})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35886359214782715})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.35114604234695435})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30506736040115356})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3017702102661133})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.33756011724472046})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33934485912323})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.30003654956817627})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29097476601600647})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.35997653007507324})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.34332334995269775})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.32489365339279175})
store['active_learning_steps'][71]['training']['best_epoch']=11
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9731, 'crossentropy': 0.2598108154296875}
store['active_learning_steps'][71]['eval_training']={}
store['active_learning_steps'][71]['eval_training']['epochs']=[]
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6696028709411621})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.429171085357666})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.326629638671875})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.2991224527359009})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27957093715667725})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25938522815704346})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2607065439224243})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27228063344955444})
store['active_learning_steps'][71]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.29128497838974})
store['active_learning_steps'][71]['eval_training']['best_epoch']=6
store['active_learning_steps'][71]['acquisition']={'indices': [5391, 54808, 40256, 46247, 8684, 47242, 56643, 20897, 521, 27751], 'labels': [-1, -1, -1, 3, -1, -1, 2, -1, -1, -1], 'scores': [0.3469146490097046, 0.36210477352142334, 0.414609432220459, 0.6130949854850769, 0.43981409072875977, 0.427524209022522, 0.38335055112838745, 0.4652385711669922, 0.4238588809967041, 0.5009217858314514]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0728631019592285})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5142943859100342})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.394901841878891})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3258211016654968})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.34198516607284546})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3208402395248413})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3067595362663269})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32851511240005493})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3398759663105011})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32508349418640137})
store['active_learning_steps'][72]['training']['best_epoch']=7
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.97, 'crossentropy': 0.264340380859375}
store['active_learning_steps'][72]['eval_training']={}
store['active_learning_steps'][72]['eval_training']['epochs']=[]
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5594210624694824})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4372757077217102})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3378205895423889})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3261534571647644})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25239115953445435})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.265900194644928})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2624940276145935})
store['active_learning_steps'][72]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2551450729370117})
store['active_learning_steps'][72]['eval_training']['best_epoch']=5
store['active_learning_steps'][72]['acquisition']={'indices': [33029, 27512, 1269, 31757, 19939, 9396, 38911, 46108, 20614, 56014], 'labels': [-1, -1, -1, 2, -1, 2, -1, -1, 8, 5], 'scores': [0.38736820220947266, 0.4688141345977783, 0.4754018783569336, 0.4762797951698303, 0.6638250350952148, 0.6035222709178925, 0.5435802936553955, 0.317043662071228, 0.5239299535751343, 0.5765566229820251]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1925134658813477})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5855058431625366})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.42793935537338257})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.34924405813217163})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.33504214882850647})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3008202314376831})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28677111864089966})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30446356534957886})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29888197779655457})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29753950238227844})
store['active_learning_steps'][73]['training']['best_epoch']=7
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.971, 'crossentropy': 0.2643923828125}
store['active_learning_steps'][73]['eval_training']={}
store['active_learning_steps'][73]['eval_training']['epochs']=[]
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6438508033752441})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.45758056640625})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3176654577255249})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.29587286710739136})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3184623122215271})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.2840319871902466})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2677149772644043})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2529948055744171})
store['active_learning_steps'][73]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2597525119781494})
store['active_learning_steps'][73]['eval_training']['best_epoch']=8
store['active_learning_steps'][73]['acquisition']={'indices': [40605, 21914, 29332, 13351, 20932, 24398, 1598, 52708, 27147, 39982], 'labels': [-1, -1, -1, -1, -1, -1, -1, 4, -1, 3], 'scores': [0.4799236059188843, 0.37960338592529297, 0.49373698234558105, 0.4417271614074707, 0.5287128686904907, 0.47582125663757324, 0.6328810453414917, 0.3619323968887329, 0.3630383610725403, 0.42918121814727783]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0490310192108154})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.4957817494869232})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.35408198833465576})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.33853718638420105})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30297544598579407})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2862370014190674})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2723606824874878})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28683674335479736})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2965708076953888})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29810675978660583})
store['active_learning_steps'][74]['training']['best_epoch']=7
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9712, 'crossentropy': 0.2481327880859375}
store['active_learning_steps'][74]['eval_training']={}
store['active_learning_steps'][74]['eval_training']['epochs']=[]
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6386210918426514})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4077122211456299})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.35699203610420227})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.32750368118286133})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2828879654407501})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2908785939216614})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.27904778718948364})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2977279722690582})
store['active_learning_steps'][74]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2508498430252075})
store['active_learning_steps'][74]['eval_training']['best_epoch']=9
store['active_learning_steps'][74]['acquisition']={'indices': [57960, 2273, 39967, 59787, 48916, 19025, 28338, 9084, 33663, 10031], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.403300404548645, 0.4823533892631531, 0.2755398750305176, 0.29877257347106934, 0.49005794525146484, 0.32633817195892334, 0.4525001049041748, 0.4498872756958008, 0.5550140738487244, 0.6102282404899597]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.1388596296310425})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4886147379875183})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.38893669843673706})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34383535385131836})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.32250118255615234})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29691484570503235})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3097921907901764})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2983638048171997})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28754669427871704})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2965661287307739})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29715850949287415})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.33008188009262085})
store['active_learning_steps'][75]['training']['best_epoch']=9
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.2573765625}
store['active_learning_steps'][75]['eval_training']={}
store['active_learning_steps'][75]['eval_training']['epochs']=[]
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6815966367721558})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4178523123264313})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.37208062410354614})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.34352776408195496})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2954658269882202})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.26576125621795654})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23484914004802704})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25925612449645996})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.23879657685756683})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.22553806006908417})
store['active_learning_steps'][75]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.22482165694236755})
store['active_learning_steps'][75]['eval_training']['best_epoch']=11
store['active_learning_steps'][75]['acquisition']={'indices': [39262, 3872, 33457, 37774, 55194, 14627, 32880, 54360, 11474, 49217], 'labels': [-1, 8, -1, -1, 3, -1, 0, -1, -1, -1], 'scores': [0.4230501651763916, 0.43218493461608887, 0.4196434020996094, 0.44733619689941406, 0.5458891987800598, 0.2940305471420288, 0.6724105477333069, 0.27526533603668213, 0.6861070394515991, 0.2754274606704712]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0951337814331055})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5521918535232544})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3763327896595001})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.34606537222862244})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3260667324066162})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32634687423706055})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.34493905305862427})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3379153907299042})
store['active_learning_steps'][76]['training']['best_epoch']=5
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9679, 'crossentropy': 0.2915644775390625}
store['active_learning_steps'][76]['eval_training']={}
store['active_learning_steps'][76]['eval_training']['epochs']=[]
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6458934545516968})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.46753108501434326})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.37584275007247925})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.34092530608177185})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3236142098903656})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2942773699760437})
store['active_learning_steps'][76]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2824096083641052})
store['active_learning_steps'][76]['eval_training']['best_epoch']=7
store['active_learning_steps'][76]['acquisition']={'indices': [1289, 4086, 36614, 28674, 7247, 2225, 37894, 9810, 35934, 37582], 'labels': [-1, -1, -1, 9, -1, -1, 5, 9, -1, -1], 'scores': [0.44180989265441895, 0.37905967235565186, 0.4222787022590637, 0.5204201340675354, 0.46335840225219727, 0.3897184133529663, 0.26340365409851074, 0.4426940083503723, 0.40082526206970215, 0.38882482051849365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0464403629302979})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5724591016769409})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.38940978050231934})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.33841344714164734})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3058350682258606})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.34846508502960205})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3012920618057251})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2984692454338074})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3287779688835144})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.31217652559280396})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3670593798160553})
store['active_learning_steps'][77]['training']['best_epoch']=8
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9719, 'crossentropy': 0.2434431396484375}
store['active_learning_steps'][77]['eval_training']={}
store['active_learning_steps'][77]['eval_training']['epochs']=[]
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6279276609420776})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.46742910146713257})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3467068672180176})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.31865638494491577})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29428136348724365})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2891644239425659})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.282929927110672})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28967392444610596})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.24715560674667358})
store['active_learning_steps'][77]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2383546233177185})
store['active_learning_steps'][77]['eval_training']['best_epoch']=10
store['active_learning_steps'][77]['acquisition']={'indices': [42184, 29890, 30016, 19998, 55124, 34074, 7340, 2381, 42581, 52800], 'labels': [-1, 5, 4, -1, -1, -1, -1, 7, -1, 9], 'scores': [0.378440260887146, 0.24339362978935242, 0.524440348148346, 0.5424613356590271, 0.42764806747436523, 0.5060649514198303, 0.5192259550094604, 0.23686403036117554, 0.4475826025009155, 0.5019419193267822]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1268235445022583})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.51771080493927})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3856414258480072})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3468064069747925})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31454598903656006})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3098493814468384})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3062271475791931})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29104626178741455})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3172950744628906})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.33423593640327454})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3287563920021057})
store['active_learning_steps'][78]['training']['best_epoch']=8
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9717, 'crossentropy': 0.2724636474609375}
store['active_learning_steps'][78]['eval_training']={}
store['active_learning_steps'][78]['eval_training']['epochs']=[]
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6493587493896484})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.4079618453979492})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3551366925239563})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3219112157821655})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3242032825946808})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2992008626461029})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.25848448276519775})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.258461058139801})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27080976963043213})
store['active_learning_steps'][78]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.23658037185668945})
store['active_learning_steps'][78]['eval_training']['best_epoch']=10
store['active_learning_steps'][78]['acquisition']={'indices': [5520, 10038, 8867, 45888, 45502, 1916, 46021, 1347, 47729, 966], 'labels': [-1, 9, 8, 9, 1, -1, 9, -1, -1, 3], 'scores': [0.49097198247909546, 0.50571608543396, 0.7032480239868164, 0.45851844549179077, 0.7512020468711853, 0.7171800136566162, 0.7556515336036682, 0.511583685874939, 0.4448217749595642, 0.7654189467430115]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.148797869682312})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5390274524688721})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3652089834213257})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.379523903131485})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3339608907699585})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.31385594606399536})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29879307746887207})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31166577339172363})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3660963177680969})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32281821966171265})
store['active_learning_steps'][79]['training']['best_epoch']=7
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9707, 'crossentropy': 0.2596566162109375}
store['active_learning_steps'][79]['eval_training']={}
store['active_learning_steps'][79]['eval_training']['epochs']=[]
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7144469022750854})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.42991843819618225})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.3507257401943207})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29848021268844604})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.29690462350845337})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.2890405058860779})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2866377532482147})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.27631837129592896})
store['active_learning_steps'][79]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.27899813652038574})
store['active_learning_steps'][79]['eval_training']['best_epoch']=8
store['active_learning_steps'][79]['acquisition']={'indices': [4153, 44621, 3251, 34464, 30042, 30209, 58805, 21380, 47471, 16562], 'labels': [2, -1, 8, -1, 5, -1, -1, -1, -1, 1], 'scores': [0.541962206363678, 0.4878746271133423, 0.4550763964653015, 0.5109278559684753, 0.45548057556152344, 0.45771926641464233, 0.5949662923812866, 0.4838324785232544, 0.6021524667739868, 0.39468222856521606]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1349457502365112})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5436220169067383})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3707582354545593})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3195682764053345})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31642234325408936})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28311052918434143})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3482876718044281})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.302411288022995})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29453063011169434})
store['active_learning_steps'][80]['training']['best_epoch']=6
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9691, 'crossentropy': 0.2605679931640625}
store['active_learning_steps'][80]['eval_training']={}
store['active_learning_steps'][80]['eval_training']['epochs']=[]
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.610362708568573})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4713387191295624})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3536284565925598})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.32410985231399536})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.30748021602630615})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3096524477005005})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2760368585586548})
store['active_learning_steps'][80]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2659481167793274})
store['active_learning_steps'][80]['eval_training']['best_epoch']=8
store['active_learning_steps'][80]['acquisition']={'indices': [18556, 14042, 33798, 22083, 18879, 35729, 32863, 3517, 18012, 31706], 'labels': [-1, -1, -1, 2, -1, -1, -1, -1, -1, -1], 'scores': [0.5343639850616455, 0.4097141623497009, 0.6449262499809265, 0.6986196637153625, 0.4936908483505249, 0.33205604553222656, 0.5531442761421204, 0.6104875206947327, 0.48313242197036743, 0.37058985233306885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1312344074249268})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5436469316482544})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.38499560952186584})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3323945701122284})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3379364013671875})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3358423709869385})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32690709829330444})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.31903931498527527})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3131153881549835})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31983682513237})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31917500495910645})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.31287437677383423})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.32104355096817017})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.33429548144340515})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3435076177120209})
store['active_learning_steps'][81]['training']['best_epoch']=12
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.9676, 'crossentropy': 0.2780419921875}
store['active_learning_steps'][81]['eval_training']={}
store['active_learning_steps'][81]['eval_training']['epochs']=[]
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6700900793075562})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4634574055671692})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3648703098297119})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.34196653962135315})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.31026482582092285})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.283221960067749})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2678656280040741})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2637854814529419})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24686875939369202})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.24147546291351318})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2419481873512268})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2370484620332718})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.23713567852973938})
store['active_learning_steps'][81]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2409595251083374})
store['active_learning_steps'][81]['eval_training']['best_epoch']=12
store['active_learning_steps'][81]['acquisition']={'indices': [1859, 5873, 19966, 43317, 49653, 25158, 13016, 53654, 49694, 45377], 'labels': [1, -1, -1, -1, -1, 5, -1, -1, -1, -1], 'scores': [0.30894356966018677, 0.6430336833000183, 0.5798239707946777, 0.46849364042282104, 0.5748062133789062, 0.4965144395828247, 0.4381186366081238, 0.5971627235412598, 0.4824965000152588, 0.32615959644317627]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.009300947189331})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5284305810928345})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.4230208396911621})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3321150839328766})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3126682937145233})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3135824203491211})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.29904961585998535})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3029688596725464})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28261956572532654})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2942270040512085})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3336609899997711})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.30790531635284424})
store['active_learning_steps'][82]['training']['best_epoch']=9
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9729, 'crossentropy': 0.2400723876953125}
store['active_learning_steps'][82]['eval_training']={}
store['active_learning_steps'][82]['eval_training']['epochs']=[]
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6700836420059204})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4251216650009155})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3794907331466675})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3191024959087372})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.29670101404190063})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2915698289871216})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27325528860092163})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.25556451082229614})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23594650626182556})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.24293935298919678})
store['active_learning_steps'][82]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.22966063022613525})
store['active_learning_steps'][82]['eval_training']['best_epoch']=11
store['active_learning_steps'][82]['acquisition']={'indices': [21700, 8765, 27393, 13729, 54652, 17094, 1422, 11864, 51546, 47513], 'labels': [7, 3, -1, 0, -1, -1, -1, -1, -1, 0], 'scores': [0.5763463377952576, 0.5218678414821625, 0.38732749223709106, 0.5219295024871826, 0.6935684680938721, 0.4705747961997986, 0.42205435037612915, 0.35687124729156494, 0.4193471670150757, 0.6229610443115234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1939655542373657})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5521689653396606})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3993498682975769})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3160530924797058})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.310802698135376})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.31216028332710266})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26851868629455566})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3080545663833618})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3170679807662964})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2981851398944855})
store['active_learning_steps'][83]['training']['best_epoch']=7
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9716, 'crossentropy': 0.2406951904296875}
store['active_learning_steps'][83]['eval_training']={}
store['active_learning_steps'][83]['eval_training']['epochs']=[]
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6709031462669373})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.43514448404312134})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.33304327726364136})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.3038737177848816})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.275711327791214})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2962225675582886})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2839784622192383})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.24259468913078308})
store['active_learning_steps'][83]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.24576601386070251})
store['active_learning_steps'][83]['eval_training']['best_epoch']=8
store['active_learning_steps'][83]['acquisition']={'indices': [10910, 636, 29709, 26568, 55555, 59977, 27832, 28199, 30536, 35629], 'labels': [-1, -1, -1, -1, -1, -1, -1, 3, -1, -1], 'scores': [0.29276740550994873, 0.3234207034111023, 0.2738553285598755, 0.5610427856445312, 0.4832085371017456, 0.31290411949157715, 0.3965715169906616, 0.3885571360588074, 0.39786767959594727, 0.4260215759277344]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 1.0257065296173096})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5336964130401611})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38804250955581665})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.30053263902664185})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.30206298828125})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3223678767681122})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30142679810523987})
store['active_learning_steps'][84]['training']['best_epoch']=4
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9652, 'crossentropy': 0.295827490234375}
store['active_learning_steps'][84]['eval_training']={}
store['active_learning_steps'][84]['eval_training']['epochs']=[]
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6441143751144409})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4638178050518036})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.4278741180896759})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33594268560409546})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3744852542877197})
store['active_learning_steps'][84]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3392517566680908})
store['active_learning_steps'][84]['eval_training']['best_epoch']=4
store['active_learning_steps'][84]['acquisition']={'indices': [36818, 17808, 43759, 49745, 25748, 58134, 17684, 14152, 6900, 17417], 'labels': [7, 8, -1, -1, 7, -1, -1, 7, -1, 4], 'scores': [0.5898951292037964, 0.4114745855331421, 0.2746093273162842, 0.20878338813781738, 0.4139874577522278, 0.2621372938156128, 0.2934356927871704, 0.40929239988327026, 0.3612077236175537, 0.3741586208343506]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.1879925727844238})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5662702918052673})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3705710768699646})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3191365599632263})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.352533221244812})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3338729441165924})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28767240047454834})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27517902851104736})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3192160725593567})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.29011157155036926})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3034612536430359})
store['active_learning_steps'][85]['training']['best_epoch']=8
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9694, 'crossentropy': 0.25873583984375}
store['active_learning_steps'][85]['eval_training']={}
store['active_learning_steps'][85]['eval_training']['epochs']=[]
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7051377296447754})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.426059365272522})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3873024582862854})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.31759899854660034})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.30680710077285767})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2689063251018524})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2738147974014282})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.25378987193107605})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24936699867248535})
store['active_learning_steps'][85]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2487717866897583})
store['active_learning_steps'][85]['eval_training']['best_epoch']=10
store['active_learning_steps'][85]['acquisition']={'indices': [47394, 37424, 36997, 52690, 59726, 19961, 12005, 26358, 21923, 49744], 'labels': [-1, -1, -1, -1, -1, -1, -1, 3, -1, 8], 'scores': [0.4486958980560303, 0.42191916704177856, 0.4718132019042969, 0.24136579036712646, 0.5660560131072998, 0.5631135106086731, 0.4803670048713684, 0.5902899503707886, 0.5332866907119751, 0.46884870529174805]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.128190040588379})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.5210844278335571})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3791196942329407})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2754247188568115})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.28989896178245544})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.29917651414871216})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2736485004425049})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27690017223358154})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.290524959564209})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27593258023262024})
store['active_learning_steps'][86]['training']['best_epoch']=7
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9736, 'crossentropy': 0.2242652099609375}
store['active_learning_steps'][86]['eval_training']={}
store['active_learning_steps'][86]['eval_training']['epochs']=[]
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6974506378173828})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.43105390667915344})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.367502361536026})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3436380624771118})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.31860122084617615})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2711314857006073})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2736511826515198})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2459375113248825})
store['active_learning_steps'][86]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2630549967288971})
store['active_learning_steps'][86]['eval_training']['best_epoch']=8
store['active_learning_steps'][86]['acquisition']={'indices': [13481, 48461, 29429, 44033, 3769, 5456, 33798, 23200, 43806, 5440], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4088064432144165, 0.4621564745903015, 0.4907442331314087, 0.25242137908935547, 0.5060651302337646, 0.42925798892974854, 0.5357807874679565, 0.234186053276062, 0.5305032730102539, 0.393338680267334]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1514986753463745})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6005951166152954})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3779089152812958})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.34956395626068115})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29297053813934326})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2901294529438019})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30967000126838684})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2780935764312744})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2887948453426361})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2800331711769104})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3030779957771301})
store['active_learning_steps'][87]['training']['best_epoch']=8
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.972, 'crossentropy': 0.2444828369140625}
store['active_learning_steps'][87]['eval_training']={}
store['active_learning_steps'][87]['eval_training']['epochs']=[]
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6287617087364197})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.41290244460105896})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3294091820716858})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3023519814014435})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.3167172372341156})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2650953233242035})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.26099228858947754})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2720772624015808})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2604914903640747})
store['active_learning_steps'][87]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.24116215109825134})
store['active_learning_steps'][87]['eval_training']['best_epoch']=10
store['active_learning_steps'][87]['acquisition']={'indices': [11255, 57265, 57638, 35482, 5905, 50125, 30585, 58445, 29332, 20932], 'labels': [-1, -1, -1, 4, -1, -1, -1, -1, -1, -1], 'scores': [0.427348256111145, 0.4327235221862793, 0.38954460620880127, 0.5745605826377869, 0.39008402824401855, 0.518535852432251, 0.6020968556404114, 0.5661696195602417, 0.6241143941879272, 0.5909736156463623]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.1083366870880127})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5629138946533203})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.39604005217552185})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3719857335090637})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29392576217651367})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28682029247283936})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.28886711597442627})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.29349207878112793})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2646859586238861})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3043449819087982})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.3065341114997864})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32418256998062134})
store['active_learning_steps'][88]['training']['best_epoch']=9
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.9736, 'crossentropy': 0.2310875244140625}
store['active_learning_steps'][88]['eval_training']={}
store['active_learning_steps'][88]['eval_training']['epochs']=[]
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.729649543762207})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4515007734298706})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3706352412700653})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3288723826408386})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2830343544483185})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26378363370895386})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2743423581123352})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2538659870624542})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2525981068611145})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24364623427391052})
store['active_learning_steps'][88]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26012951135635376})
store['active_learning_steps'][88]['eval_training']['best_epoch']=10
store['active_learning_steps'][88]['acquisition']={'indices': [30725, 21880, 47748, 37141, 26863, 56639, 39627, 13654, 40711, 13966], 'labels': [-1, 2, 8, -1, -1, -1, -1, 2, -1, -1], 'scores': [0.514877438545227, 0.29844850301742554, 0.39793431758880615, 0.3957446813583374, 0.5797234773635864, 0.4509493112564087, 0.49838608503341675, 0.38388943672180176, 0.24206197261810303, 0.2936670780181885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.089121699333191})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5505967140197754})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.35431790351867676})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2984994649887085})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2826085686683655})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2607727348804474})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2650342881679535})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2620471119880676})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27599161863327026})
store['active_learning_steps'][89]['training']['best_epoch']=6
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.9716, 'crossentropy': 0.2494162109375}
store['active_learning_steps'][89]['eval_training']={}
store['active_learning_steps'][89]['eval_training']['epochs']=[]
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.696977972984314})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.4446418881416321})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3238668739795685})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3197738528251648})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3325916528701782})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2804902493953705})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.2967742085456848})
store['active_learning_steps'][89]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2563249468803406})
store['active_learning_steps'][89]['eval_training']['best_epoch']=8
store['active_learning_steps'][89]['acquisition']={'indices': [13364, 30422, 5642, 12091, 1317, 14667, 5603, 42554, 1786, 31185], 'labels': [-1, -1, -1, -1, 3, -1, -1, -1, -1, 2], 'scores': [0.38408660888671875, 0.43306589126586914, 0.4401901960372925, 0.5487262606620789, 0.3076259195804596, 0.26466095447540283, 0.27367258071899414, 0.4682295322418213, 0.4326481223106384, 0.47292858362197876]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1479064226150513})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.5594375133514404})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3812600374221802})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3148968517780304})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3235395848751068})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.31019511818885803})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3271997272968292})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.28145554661750793})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.305408775806427})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29714980721473694})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.30712082982063293})
store['active_learning_steps'][90]['training']['best_epoch']=8
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9714, 'crossentropy': 0.2363990478515625}
store['active_learning_steps'][90]['eval_training']={}
store['active_learning_steps'][90]['eval_training']['epochs']=[]
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6863701343536377})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.4234907627105713})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.35673314332962036})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.30750715732574463})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3230787217617035})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.281827837228775})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2504643499851227})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23502083122730255})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.25002989172935486})
store['active_learning_steps'][90]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2345523238182068})
store['active_learning_steps'][90]['eval_training']['best_epoch']=10
store['active_learning_steps'][90]['acquisition']={'indices': [28776, 57397, 28754, 36127, 27178, 18521, 22675, 59885, 27998, 23628], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 6], 'scores': [0.43074941635131836, 0.22955024242401123, 0.4105337858200073, 0.33197295665740967, 0.3604327440261841, 0.485071063041687, 0.42556601762771606, 0.43225884437561035, 0.5105814933776855, 0.5425606966018677]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.111609697341919})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5941232442855835})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.39080795645713806})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33649420738220215})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29968899488449097})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.286984384059906})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27284154295921326})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31205058097839355})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27275407314300537})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2836192548274994})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2926906943321228})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2721875309944153})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2740086317062378})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.27338680624961853})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3141838610172272})
store['active_learning_steps'][91]['training']['best_epoch']=12
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9764, 'crossentropy': 0.2405456787109375}
store['active_learning_steps'][91]['eval_training']={}
store['active_learning_steps'][91]['eval_training']['epochs']=[]
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6675014495849609})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4669145941734314})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.3286682665348053})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.30362433195114136})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2804158329963684})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.26189884543418884})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2668135166168213})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.22186991572380066})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.21618926525115967})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.23988065123558044})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.21992230415344238})
store['active_learning_steps'][91]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23305800557136536})
store['active_learning_steps'][91]['eval_training']['best_epoch']=9
store['active_learning_steps'][91]['acquisition']={'indices': [34879, 28395, 36193, 20667, 31958, 864, 16493, 28814, 16648, 7499], 'labels': [-1, 5, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.4500312805175781, 0.48191016912460327, 0.5679551362991333, 0.30681073665618896, 0.5364934802055359, 0.43859970569610596, 0.4511834979057312, 0.4226877689361572, 0.4062459468841553, 0.5023446083068848]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.1489787101745605})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5540472865104675})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3731011152267456})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.316657692193985})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3250330984592438})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24937903881072998})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2619030475616455})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23315131664276123})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27618682384490967})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2604765295982361})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2536248564720154})
store['active_learning_steps'][92]['training']['best_epoch']=8
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9765, 'crossentropy': 0.2248483154296875}
store['active_learning_steps'][92]['eval_training']={}
store['active_learning_steps'][92]['eval_training']['epochs']=[]
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6571859121322632})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.4128657281398773})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3555067181587219})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32320985198020935})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2817305028438568})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.260354220867157})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23383745551109314})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.24626368284225464})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2433893382549286})
store['active_learning_steps'][92]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2285972237586975})
store['active_learning_steps'][92]['eval_training']['best_epoch']=10
store['active_learning_steps'][92]['acquisition']={'indices': [21052, 13067, 22058, 52033, 38021, 12302, 44738, 14413, 51394, 48404], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 8, -1], 'scores': [0.5383706092834473, 0.39145326614379883, 0.5433952808380127, 0.5406306385993958, 0.605899453163147, 0.40836501121520996, 0.4979649782180786, 0.3727240562438965, 0.34286797046661377, 0.493269681930542]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.0756521224975586})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5651559233665466})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.40728330612182617})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3154606223106384})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.31020206212997437})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.29940786957740784})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.26989108324050903})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.29137128591537476})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2948691248893738})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.26341086626052856})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.28531554341316223})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3084198832511902})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2989276647567749})
store['active_learning_steps'][93]['training']['best_epoch']=10
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.9755, 'crossentropy': 0.237969921875}
store['active_learning_steps'][93]['eval_training']={}
store['active_learning_steps'][93]['eval_training']['epochs']=[]
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6875002384185791})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9423828125, 'crossentropy': 0.4172554314136505})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.31279468536376953})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.28673943877220154})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.26914113759994507})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2703430652618408})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.26362892985343933})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.23376744985580444})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.23588737845420837})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.23657314479351044})
store['active_learning_steps'][93]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2423563301563263})
store['active_learning_steps'][93]['eval_training']['best_epoch']=8
store['active_learning_steps'][93]['acquisition']={'indices': [55058, 23086, 20110, 17160, 8535, 39363, 36964, 674, 21816, 30011], 'labels': [-1, 8, 4, -1, -1, -1, -1, -1, -1, 3], 'scores': [0.4591919183731079, 0.6187714338302612, 0.6322873830795288, 0.481674462556839, 0.34768372774124146, 0.4896949529647827, 0.4799131155014038, 0.49647289514541626, 0.7395833730697632, 0.565994143486023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.2199658155441284})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5573996305465698})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.42524564266204834})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.32065385580062866})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3107079267501831})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2988681197166443})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.27137577533721924})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.29015421867370605})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2678670287132263})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29869022965431213})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.3098612427711487})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3166138529777527})
store['active_learning_steps'][94]['training']['best_epoch']=9
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.9726, 'crossentropy': 0.245847021484375}
store['active_learning_steps'][94]['eval_training']={}
store['active_learning_steps'][94]['eval_training']['epochs']=[]
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6797207593917847})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.4088129997253418})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3316565752029419})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.271869957447052})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2949388027191162})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28196895122528076})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.24882400035858154})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2392531782388687})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2555594742298126})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23697128891944885})
store['active_learning_steps'][94]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24282564222812653})
store['active_learning_steps'][94]['eval_training']['best_epoch']=10
store['active_learning_steps'][94]['acquisition']={'indices': [16860, 42764, 41942, 42562, 16043, 2003, 53927, 4675, 50369, 2627], 'labels': [8, -1, 9, -1, 0, -1, -1, -1, 3, -1], 'scores': [0.42040640115737915, 0.2887864112854004, 0.463804692029953, 0.44035840034484863, 0.3807997703552246, 0.45076262950897217, 0.5240541696548462, 0.5384166240692139, 0.6076668500900269, 0.48846447467803955]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.1756105422973633})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5894936919212341})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.38807880878448486})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3471263349056244})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.3365340232849121})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2981592118740082})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.289448082447052})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2930490970611572})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2682437300682068})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2734184265136719})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.27698832750320435})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.264923632144928})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2989327907562256})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28756576776504517})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29661262035369873})
store['active_learning_steps'][95]['training']['best_epoch']=12
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9755, 'crossentropy': 0.2313361328125}
store['active_learning_steps'][95]['eval_training']={}
store['active_learning_steps'][95]['eval_training']['epochs']=[]
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6479432582855225})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.4171191453933716})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.331831157207489})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2971671521663666})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.27329131960868835})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.2996106743812561})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.24407556653022766})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2532612085342407})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24953080713748932})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.22923269867897034})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2423292100429535})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.258024662733078})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.21238255500793457})
store['active_learning_steps'][95]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.21062180399894714})
store['active_learning_steps'][95]['eval_training']['best_epoch']=14
store['active_learning_steps'][95]['acquisition']={'indices': [5224, 28656, 30629, 15450, 26831, 26892, 57523, 14385, 51283, 36262], 'labels': [-1, -1, -1, 6, -1, -1, 3, 8, -1, -1], 'scores': [0.4441900849342346, 0.30326712131500244, 0.6078158020973206, 0.41886115074157715, 0.3460758924484253, 0.6599612236022949, 0.7220640182495117, 0.47589045763015747, 0.6408345699310303, 0.587633490562439]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.224570631980896})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6143122911453247})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.42145979404449463})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.36712515354156494})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.33541709184646606})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.33870917558670044})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2913779616355896})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2997455298900604})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3081813156604767})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3169980049133301})
store['active_learning_steps'][96]['training']['best_epoch']=7
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.9737, 'crossentropy': 0.240957177734375}
store['active_learning_steps'][96]['eval_training']={}
store['active_learning_steps'][96]['eval_training']['epochs']=[]
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6888412237167358})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4690309762954712})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3837529420852661})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.32894548773765564})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.323756605386734})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.28181278705596924})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2734209895133972})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.28387919068336487})
store['active_learning_steps'][96]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2443331778049469})
store['active_learning_steps'][96]['eval_training']['best_epoch']=9
store['active_learning_steps'][96]['acquisition']={'indices': [7072, 27620, 27566, 23790, 57677, 45656, 30550, 12343, 25146, 52512], 'labels': [-1, -1, -1, -1, -1, 3, -1, -1, -1, -1], 'scores': [0.6290966272354126, 0.5636283159255981, 0.5057427883148193, 0.545630931854248, 0.48913562297821045, 0.33774858713150024, 0.46359336376190186, 0.5729241371154785, 0.5440723299980164, 0.5782556533813477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.131737232208252})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5538992881774902})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.37833815813064575})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3480357527732849})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2892574071884155})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2751491069793701})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.30043458938598633})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.277643620967865})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2660701274871826})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2855421304702759})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27634379267692566})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.25609514117240906})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.27937111258506775})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2539580464363098})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.29456475377082825})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.30026787519454956})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.27058953046798706})
store['active_learning_steps'][97]['training']['best_epoch']=14
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9737, 'crossentropy': 0.23385595703125}
store['active_learning_steps'][97]['eval_training']={}
store['active_learning_steps'][97]['eval_training']['epochs']=[]
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7385962009429932})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.44411852955818176})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.3636321425437927})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3040824830532074})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2643943428993225})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.247714564204216})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2574799060821533})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2377733439207077})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2237423062324524})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2480272799730301})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.22110512852668762})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.21039867401123047})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.21068978309631348})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.21879222989082336})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.20221571624279022})
store['active_learning_steps'][97]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.20143190026283264})
store['active_learning_steps'][97]['eval_training']['best_epoch']=16
store['active_learning_steps'][97]['acquisition']={'indices': [14655, 20674, 43424, 39974, 520, 14650, 45024, 38884, 19136, 18440], 'labels': [3, -1, -1, -1, -1, 4, 5, -1, -1, -1], 'scores': [0.5196071863174438, 0.4226193428039551, 0.4938035011291504, 0.5516355037689209, 0.39190512895584106, 0.6816580295562744, 0.5777851939201355, 0.44604700803756714, 0.456571102142334, 0.5281932353973389]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.297991156578064})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.571008563041687})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4334939122200012})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28871434926986694})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2855415344238281})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.30334147810935974})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28993284702301025})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3068539798259735})
store['active_learning_steps'][98]['training']['best_epoch']=5
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.9721, 'crossentropy': 0.258919970703125}
store['active_learning_steps'][98]['eval_training']={}
store['active_learning_steps'][98]['eval_training']['epochs']=[]
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6626172065734863})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4026305079460144})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.3463483452796936})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.3051193356513977})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3157810568809509})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.311374694108963})
store['active_learning_steps'][98]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27953410148620605})
store['active_learning_steps'][98]['eval_training']['best_epoch']=7
store['active_learning_steps'][98]['acquisition']={'indices': [224, 8241, 20849, 56854, 22546, 37512, 23911, 45026, 47225, 999], 'labels': [1, 3, 3, -1, -1, -1, 1, 8, 3, -1], 'scores': [0.566204309463501, 0.4698527455329895, 0.5155706405639648, 0.33753108978271484, 0.44655048847198486, 0.255193829536438, 0.4494108557701111, 0.3388875126838684, 0.4125651717185974, 0.35693275928497314]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.4642581939697266})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6644570827484131})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.953125, 'crossentropy': 0.39728105068206787})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3581070303916931})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.3058134913444519})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2710508704185486})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3068905472755432})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27620482444763184})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.28704527020454407})
store['active_learning_steps'][99]['training']['best_epoch']=6
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9726, 'crossentropy': 0.262308837890625}
store['active_learning_steps'][99]['eval_training']={}
store['active_learning_steps'][99]['eval_training']['epochs']=[]
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7275866270065308})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.943359375, 'crossentropy': 0.4459744691848755})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.37594521045684814})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3492772579193115})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3055614233016968})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.32376259565353394})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3009416460990906})
store['active_learning_steps'][99]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.30504828691482544})
store['active_learning_steps'][99]['eval_training']['best_epoch']=7
store['active_learning_steps'][99]['acquisition']={'indices': [16015, 25632, 5184, 411, 37704, 59445, 29106, 57469, 22642, 47858], 'labels': [-1, -1, -1, -1, 8, -1, -1, -1, -1, -1], 'scores': [0.5334388017654419, 0.5025932788848877, 0.5224906206130981, 0.46638286113739014, 0.5325837731361389, 0.510993480682373, 0.44346630573272705, 0.4346585273742676, 0.5369423031806946, 0.6323691606521606]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.169775128364563})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.6241335868835449})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.4141848683357239})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.32574760913848877})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.30737730860710144})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28630179166793823})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.25347229838371277})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.29514771699905396})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28267234563827515})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2773655652999878})
store['active_learning_steps'][100]['training']['best_epoch']=7
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9728, 'crossentropy': 0.247685546875}
store['active_learning_steps'][100]['eval_training']={}
store['active_learning_steps'][100]['eval_training']['epochs']=[]
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6495823860168457})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.432295024394989})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.39627888798713684})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3571089506149292})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2840823531150818})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.314936101436615})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.27441802620887756})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2865736186504364})
store['active_learning_steps'][100]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.24545152485370636})
store['active_learning_steps'][100]['eval_training']['best_epoch']=9
store['active_learning_steps'][100]['acquisition']={'indices': [56268, 25414, 50403, 24767, 7074, 9611, 9126, 16882, 1522, 40192], 'labels': [4, -1, -1, 4, 1, 8, -1, 7, -1, -1], 'scores': [0.47142648696899414, 0.41581976413726807, 0.4055107831954956, 0.29663461446762085, 0.41147375106811523, 0.3088945150375366, 0.35942912101745605, 0.508143961429596, 0.37484705448150635, 0.40781891345977783]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.1813085079193115})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.6286613345146179})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.40596646070480347})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3460114002227783})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2768876552581787})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2741897702217102})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.2734959125518799})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.276800274848938})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2604060471057892})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2782399654388428})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2843637466430664})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.26434236764907837})
store['active_learning_steps'][101]['training']['best_epoch']=9
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9723, 'crossentropy': 0.2330233154296875}
store['active_learning_steps'][101]['eval_training']={}
store['active_learning_steps'][101]['eval_training']['epochs']=[]
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5950316786766052})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.38116586208343506})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9384765625, 'crossentropy': 0.34274572134017944})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.3142280578613281})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.27696648240089417})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2490319013595581})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.27020448446273804})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.2429538071155548})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.9501953125, 'crossentropy': 0.2558130621910095})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2509719133377075})
store['active_learning_steps'][101]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2513697147369385})
store['active_learning_steps'][101]['eval_training']['best_epoch']=8
store['active_learning_steps'][101]['acquisition']={'indices': [46042, 33150, 50340, 54482, 31284, 21816, 43537, 22486, 26150, 32364], 'labels': [-1, 8, 3, -1, 7, -1, 3, -1, 5, 7], 'scores': [0.3886580467224121, 0.6364345550537109, 0.5242070555686951, 0.4007542133331299, 0.4138466715812683, 0.5491077899932861, 0.4122712016105652, 0.3241233825683594, 0.6033399105072021, 0.5632646679878235]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.1689929962158203})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5156106948852539})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.3665483593940735})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.33711323142051697})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2839871644973755})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27487942576408386})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2606293559074402})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9736328125, 'crossentropy': 0.2501445710659027})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.27028101682662964})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2932250499725342})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2810963988304138})
store['active_learning_steps'][102]['training']['best_epoch']=8
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.976, 'crossentropy': 0.221667333984375}
store['active_learning_steps'][102]['eval_training']={}
store['active_learning_steps'][102]['eval_training']['epochs']=[]
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6515442132949829})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.3924739360809326})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3453146815299988})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29071295261383057})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3251887559890747})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.2767691910266876})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25357115268707275})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2477422058582306})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24657031893730164})
store['active_learning_steps'][102]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24024999141693115})
store['active_learning_steps'][102]['eval_training']['best_epoch']=10
store['active_learning_steps'][102]['acquisition']={'indices': [34458, 40945, 34238, 53802, 31596, 15179, 41989, 2762, 9687, 4217], 'labels': [-1, -1, -1, -1, 3, -1, -1, -1, 0, -1], 'scores': [0.5745428800582886, 0.4298971891403198, 0.43897396326065063, 0.4222269058227539, 0.41418272256851196, 0.45484262704849243, 0.4775305390357971, 0.4083116054534912, 0.5153206586837769, 0.40198713541030884]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.1780831813812256})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5767978429794312})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.40009409189224243})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.3208935260772705})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2967330515384674})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28149348497390747})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2845015227794647})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2614158093929291})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2801409363746643})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2786155641078949})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2765920162200928})
store['active_learning_steps'][103]['training']['best_epoch']=8
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9764, 'crossentropy': 0.228058349609375}
store['active_learning_steps'][103]['eval_training']={}
store['active_learning_steps'][103]['eval_training']['epochs']=[]
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7240910530090332})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.4256407916545868})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.36585891246795654})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.2984422743320465})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2750870883464813})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2397724837064743})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2487214207649231})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.2630727291107178})
store['active_learning_steps'][103]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.249373197555542})
store['active_learning_steps'][103]['eval_training']['best_epoch']=6
store['active_learning_steps'][103]['acquisition']={'indices': [43704, 51266, 23717, 11539, 8628, 18256, 44148, 46920, 7270, 44172], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, 5, 8], 'scores': [0.3016153573989868, 0.4341427683830261, 0.32698726654052734, 0.6099017858505249, 0.33463072776794434, 0.4201616048812866, 0.5115526914596558, 0.45473432540893555, 0.34641677141189575, 0.49541348218917847]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.2472038269042969})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5766500234603882})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3771979808807373})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3090324401855469})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.2847873270511627})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.28061071038246155})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.24122262001037598})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2549475431442261})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.25602662563323975})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.2849946916103363})
store['active_learning_steps'][104]['training']['best_epoch']=7
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.976, 'crossentropy': 0.226991064453125}
store['active_learning_steps'][104]['eval_training']={}
store['active_learning_steps'][104]['eval_training']['epochs']=[]
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7565200328826904})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.44983845949172974})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.9541015625, 'crossentropy': 0.3976472020149231})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.32308003306388855})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3054065704345703})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.32274776697158813})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.29250389337539673})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2727617919445038})
store['active_learning_steps'][104]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.26088517904281616})
store['active_learning_steps'][104]['eval_training']['best_epoch']=9
store['active_learning_steps'][104]['acquisition']={'indices': [337, 35269, 2591, 14324, 59983, 45863, 35411, 13517, 57599, 7668], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1], 'scores': [0.23342156410217285, 0.6057629585266113, 0.4774731397628784, 0.3114996552467346, 0.35156166553497314, 0.45535051822662354, 0.43545305728912354, 0.4744222164154053, 0.4955601096153259, 0.34312593936920166]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.2826271057128906})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5778276920318604})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3883143365383148})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.3632085919380188})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.27911776304244995})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2868943214416504})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3035699427127838})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2604218125343323})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.26857128739356995})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28381675481796265})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.28814995288848877})
store['active_learning_steps'][105]['training']['best_epoch']=8
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.9729, 'crossentropy': 0.2391584716796875}
store['active_learning_steps'][105]['eval_training']={}
store['active_learning_steps'][105]['eval_training']['epochs']=[]
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7147127389907837})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.45057129859924316})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.3775162100791931})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3270348906517029})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.28392842411994934})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.27194786071777344})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.26836663484573364})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2700762152671814})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.974609375, 'crossentropy': 0.2854980230331421})
store['active_learning_steps'][105]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2546166181564331})
store['active_learning_steps'][105]['eval_training']['best_epoch']=10
store['active_learning_steps'][105]['acquisition']={'indices': [56196, 44754, 57276, 12484, 39595, 20138, 13147, 41977, 12058, 35583], 'labels': [-1, -1, -1, 5, -1, -1, -1, -1, -1, -1], 'scores': [0.5781789422035217, 0.495150625705719, 0.6221790313720703, 0.46289658546447754, 0.5255817174911499, 0.4993845224380493, 0.25540196895599365, 0.37496596574783325, 0.4319422245025635, 0.3286018371582031]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.3388422727584839})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6373147964477539})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.4453486502170563})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.3531475365161896})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.31655043363571167})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.3061750829219818})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.26313507556915283})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2633606791496277})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27815499901771545})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.26142653822898865})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.2741628885269165})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.28431951999664307})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.294677734375})
store['active_learning_steps'][106]['training']['best_epoch']=10
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9737, 'crossentropy': 0.23954248046875}
store['active_learning_steps'][106]['eval_training']={}
store['active_learning_steps'][106]['eval_training']['epochs']=[]
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7014170289039612})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.4192914366722107})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.357265830039978})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3026618957519531})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.29495805501937866})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9560546875, 'crossentropy': 0.2808971405029297})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2666398286819458})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.24280023574829102})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.225999653339386})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.2500298023223877})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.23571686446666718})
store['active_learning_steps'][106]['eval_training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.23193880915641785})
store['active_learning_steps'][106]['eval_training']['best_epoch']=9
store['active_learning_steps'][106]['acquisition']={'indices': [17543, 31716, 13334, 21526, 11427, 55007, 32018, 14924, 16809, 55610], 'labels': [-1, -1, -1, -1, -1, -1, 8, -1, 7, 8], 'scores': [0.35658228397369385, 0.4265905022621155, 0.3906806707382202, 0.5096055865287781, 0.3752344846725464, 0.24798858165740967, 0.445611834526062, 0.4485057592391968, 0.49615949392318726, 0.46748650074005127]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.164169430732727})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5219972729682922})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.955078125, 'crossentropy': 0.47645869851112366})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3644351363182068})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.29654622077941895})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.3163883090019226})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.28891614079475403})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2831854820251465})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.962890625, 'crossentropy': 0.28802645206451416})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.30220896005630493})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28648948669433594})
store['active_learning_steps'][107]['training']['best_epoch']=8
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9723, 'crossentropy': 0.2515947265625}
store['active_learning_steps'][107]['eval_training']={}
store['active_learning_steps'][107]['eval_training']['epochs']=[]
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6675761938095093})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.42557570338249207})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.94921875, 'crossentropy': 0.3445362150669098})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.3075275123119354})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.2719650864601135})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2746707797050476})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2688087821006775})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2799438238143921})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.25531360507011414})
store['active_learning_steps'][107]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24077925086021423})
store['active_learning_steps'][107]['eval_training']['best_epoch']=10
store['active_learning_steps'][107]['acquisition']={'indices': [53371, 15666, 37045, 53697, 58679, 47515, 51743, 53537, 3705, 32829], 'labels': [-1, -1, -1, -1, -1, -1, -1, -1, -1, 4], 'scores': [0.5135719180107117, 0.4025990962982178, 0.33818817138671875, 0.30316221714019775, 0.4301173686981201, 0.41156935691833496, 0.45246613025665283, 0.3520853519439697, 0.43766599893569946, 0.46036243438720703]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.2489233016967773})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9453125, 'crossentropy': 0.5608674883842468})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.371450811624527})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.330874502658844})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.3224605321884155})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3012181222438812})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2693132162094116})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.2796948552131653})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.96484375, 'crossentropy': 0.3323556184768677})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2645387649536133})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3284755349159241})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9658203125, 'crossentropy': 0.28204840421676636})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.29699504375457764})
store['active_learning_steps'][108]['training']['best_epoch']=10
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9761, 'crossentropy': 0.2348728515625}
store['active_learning_steps'][108]['eval_training']={}
store['active_learning_steps'][108]['eval_training']['epochs']=[]
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6602517366409302})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.9521484375, 'crossentropy': 0.38976436853408813})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3269411027431488})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.3236335515975952})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.2786504626274109})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.2601166069507599})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.26198869943618774})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.24747000634670258})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2479773461818695})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.23934966325759888})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2439054697751999})
store['active_learning_steps'][108]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.21273116767406464})
store['active_learning_steps'][108]['eval_training']['best_epoch']=12
store['active_learning_steps'][108]['acquisition']={'indices': [28338, 5042, 46126, 39444, 31548, 15096, 48014, 17553, 47947, 9161], 'labels': [-1, 8, 3, -1, -1, -1, -1, 3, -1, -1], 'scores': [0.5673171281814575, 0.46329426765441895, 0.4753512144088745, 0.5211409330368042, 0.5015404224395752, 0.3824467658996582, 0.3942685127258301, 0.4671021103858948, 0.34969985485076904, 0.5160733461380005]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.2822749614715576})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6421512961387634})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.951171875, 'crossentropy': 0.45397141575813293})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.3469129800796509})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.28684520721435547})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2929772138595581})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.2760698199272156})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2965649366378784})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.2763957977294922})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.97265625, 'crossentropy': 0.263526976108551})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.27493909001350403})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2901824116706848})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9697265625, 'crossentropy': 0.28882038593292236})
store['active_learning_steps'][109]['training']['best_epoch']=10
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.9756, 'crossentropy': 0.2209133544921875}
store['active_learning_steps'][109]['eval_training']={}
store['active_learning_steps'][109]['eval_training']['epochs']=[]
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6879827976226807})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.43045544624328613})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9462890625, 'crossentropy': 0.37641310691833496})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9482421875, 'crossentropy': 0.3217570185661316})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9599609375, 'crossentropy': 0.2861800193786621})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.95703125, 'crossentropy': 0.294523149728775})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9609375, 'crossentropy': 0.2539319097995758})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9638671875, 'crossentropy': 0.2492627203464508})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.25562670826911926})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9677734375, 'crossentropy': 0.21634763479232788})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.9619140625, 'crossentropy': 0.23319122195243835})
store['active_learning_steps'][109]['eval_training']['epochs'].append({'accuracy': 0.966796875, 'crossentropy': 0.24280281364917755})
store['active_learning_steps'][109]['eval_training']['best_epoch']=10
store['active_learning_steps'][109]['acquisition']={'indices': [44508, 7646, 53478, 8339, 47955, 14222, 17937, 4358, 51736, 43588], 'labels': [-1, -1, 7, 5, 5, 9, 8, -1, 5, 8], 'scores': [0.38317108154296875, 0.5365070104598999, 0.4695299565792084, 0.511239230632782, 0.6275855302810669, 0.6717022061347961, 0.4789399206638336, 0.534894585609436, 0.7098138332366943, 0.49595212936401367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.2534537315368652})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.6052591800689697})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.947265625, 'crossentropy': 0.42044776678085327})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.958984375, 'crossentropy': 0.3593282699584961})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9580078125, 'crossentropy': 0.28872057795524597})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.970703125, 'crossentropy': 0.3065299987792969})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.96875, 'crossentropy': 0.301688551902771})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9716796875, 'crossentropy': 0.2920757532119751})
store['active_learning_steps'][110]['training']['best_epoch']=5
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9709, 'crossentropy': 0.281153076171875}
