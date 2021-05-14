store = {}
store['timestamp']=1620914260
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
store['active_learning_steps'][0]['acquisition']={'indices': [50106, 35768, 39342, 16070, 26778, 46897, 44989, 15290, 57308, 48170], 'labels': [8, 6, -1, 6, 7, 8, 6, -1, 3, 7], 'scores': [0.8176279664039612, 0.7133044600486755, 0.47583234310150146, 0.7856965661048889, 0.7871488332748413, 0.6816415786743164, 0.6089255213737488, 0.34774506092071533, 0.7051003575325012, 0.626656174659729]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.127321243286133})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.395555019378662})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.670968532562256})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.810883045196533})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7075, 'crossentropy': 1.9362966796875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.131628155708313})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0822176933288574})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1127607822418213})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [53638, 28088, 57662, 855, 26315, 15739, 14338, 17926, 36489, 41291], 'labels': [5, -1, -1, 4, 0, 8, 8, 4, 8, 0], 'scores': [0.8176991939544678, 0.40003180503845215, 0.4218416213989258, 0.5665079355239868, 0.8705611824989319, 0.6205187439918518, 0.6231603622436523, 0.693561315536499, 0.845203161239624, 0.723353385925293]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.7002546787261963})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 2.188601016998291})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 2.2464804649353027})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 2.442004442214966})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7327, 'crossentropy': 1.57399716796875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.0407589673995972})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.0186848640441895})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.9895229339599609})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [57736, 22866, 8115, 55702, 42462, 28561, 17305, 29822, 25260, 27135], 'labels': [8, 5, -1, 9, -1, 3, -1, 9, -1, 3], 'scores': [0.4724910855293274, 0.48424649238586426, 0.6035301089286804, 0.5623688101768494, 0.48110175132751465, 0.755906343460083, 0.5741088390350342, 0.5493602752685547, 0.6169764399528503, 0.4251806139945984]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.5562124252319336})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.6748831272125244})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.7716745138168335})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.9278795719146729})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7455, 'crossentropy': 1.44922978515625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.049184799194336})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 0.9443432092666626})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.9403786063194275})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [30105, 23545, 47005, 25516, 47718, 58317, 22695, 59681, 19671, 12405], 'labels': [3, 2, 0, 2, 5, 2, 3, 0, 1, 5], 'scores': [0.6077789664268494, 0.5577534437179565, 0.5366792678833008, 0.6177458763122559, 0.5446168184280396, 0.6200365424156189, 0.5783390402793884, 0.5103033185005188, 0.48900747299194336, 0.6492341756820679]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.228694200515747})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.3188910484313965})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.5288218259811401})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.6696014404296875})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7903, 'crossentropy': 1.216275390625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 0.8971637487411499})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 0.8617665767669678})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 0.8268786072731018})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [34968, 12404, 50195, 10102, 34678, 46315, 24252, 16303, 28637, 20606], 'labels': [8, 2, 3, 9, 8, 9, 5, 9, 5, 3], 'scores': [0.48236560821533203, 0.4493236541748047, 0.6001261472702026, 0.4245695471763611, 0.6543607115745544, 0.4122201204299927, 0.47700977325439453, 0.39352554082870483, 0.5506463050842285, 0.49869102239608765]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.0095340013504028})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.0567892789840698})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.1741262674331665})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.5107316970825195})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8315, 'crossentropy': 0.9517232421875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8323972225189209})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.799643874168396})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.7263864278793335})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [47435, 57178, 42776, 27697, 12753, 20363, 41399, 54118, 20527, 22097], 'labels': [1, 7, -1, -1, 9, 8, 2, 7, 4, -1], 'scores': [0.4426398277282715, 0.612623393535614, 0.34410274028778076, 0.347322940826416, 0.5984753966331482, 0.5578007698059082, 0.44917887449264526, 0.6510356068611145, 0.293266236782074, 0.4026988744735718]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9839848279953003})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0847303867340088})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0844452381134033})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.195684790611267})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.8222, 'crossentropy': 0.916701953125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8832021951675415})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.8186814785003662})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.7970021367073059})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [9274, 34327, 13207, 25223, 41254, 14107, 18932, 20025, 2211, 47402], 'labels': [7, 3, 6, 5, 9, 3, 5, 8, 5, 7], 'scores': [0.19864368438720703, 0.3868372440338135, 0.4390897750854492, 0.4385414719581604, 0.39562833309173584, 0.47094738483428955, 0.42745697498321533, 0.3962084650993347, 0.5586878657341003, 0.4409175515174866]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7758875489234924})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8633041977882385})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9439831972122192})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9782518744468689})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8544, 'crossentropy': 0.808192236328125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.7493003606796265})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7450257539749146})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.693220853805542})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [33804, 2014, 39389, 16301, 32430, 59433, 34445, 27130, 30925, 59354], 'labels': [2, 7, 8, 8, 2, 0, 7, 9, 2, 1], 'scores': [0.46986299753189087, 0.4900316596031189, 0.3401143550872803, 0.4101301431655884, 0.5538086295127869, 0.5295934677124023, 0.4461294412612915, 0.4380330443382263, 0.41116654872894287, 0.5371085405349731]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7772835493087769})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7759166955947876})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7282255291938782})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7735536098480225})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8092620372772217})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.960597038269043})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.9024, 'crossentropy': 0.6798087890625}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6965205669403076})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.5485415458679199})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.496185839176178})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.4713084101676941})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.47358018159866333})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [19276, 40084, 33510, 21691, 17756, 6574, 7192, 4673, 55285, 29955], 'labels': [6, 2, 3, -1, 8, -1, 3, -1, -1, -1], 'scores': [0.8443738222122192, 0.7036751508712769, 0.5676063299179077, 0.6290351152420044, 0.9527073502540588, 0.38766932487487793, 0.6715435087680817, 0.4430360794067383, 0.5639866590499878, 0.7187068462371826]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8198084831237793})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7638194561004639})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7575428485870361})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.780774712562561})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7822936773300171})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.840546727180481})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.9013, 'crossentropy': 0.69547734375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6324334740638733})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.560441792011261})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.48874908685684204})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.4847535192966461})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.47802168130874634})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [26389, 51988, 10588, 21327, 16600, 4768, 52188, 15135, 52152, 1870], 'labels': [0, -1, 9, 4, 4, 4, 2, -1, 2, -1], 'scores': [0.5659646987915039, 0.48910337686538696, 0.37927061319351196, 0.611014723777771, 0.672585666179657, 0.6069302558898926, 0.5481087565422058, 0.4237023591995239, 0.7116801738739014, 0.40595948696136475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7756906747817993})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7047143578529358})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7249307632446289})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7249895930290222})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6947095394134521})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7192521095275879})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.759818434715271})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8966950178146362})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.9114, 'crossentropy': 0.68781669921875}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6309462785720825})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5007357597351074})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.4574776589870453})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.4153423309326172})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.4275229573249817})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.43492254614830017})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.437358021736145})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [13909, 20206, 35694, 3851, 47484, 45622, 43345, 28611, 46828, 49742], 'labels': [-1, 7, 9, -1, 8, 6, 2, 2, 9, -1], 'scores': [0.476825475692749, 0.4023810923099518, 0.48335736989974976, 0.37844717502593994, 0.4665347933769226, 0.5582230687141418, 0.6556487083435059, 0.7257545292377472, 0.7003054022789001, 0.5218300819396973]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7268024682998657})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6065151691436768})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.677947461605072})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6643715500831604})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7225266098976135})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9155, 'crossentropy': 0.551661865234375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7434237003326416})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5002688765525818})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.49751293659210205})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5231503248214722})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [37247, 52169, 30220, 57985, 40050, 9591, 38142, 18346, 40181, 53790], 'labels': [9, 2, 0, 4, 9, 8, 8, 7, -1, -1], 'scores': [0.4783751368522644, 0.4539144039154053, 0.4934682846069336, 0.6628314852714539, 0.3937283754348755, 0.4139573574066162, 0.4498351812362671, 0.3720859885215759, 0.32759618759155273, 0.36326563358306885]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7493842840194702})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.710728645324707})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6883105039596558})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7183322906494141})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6701064705848694})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.8385072946548462})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.793906569480896})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7635715007781982})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9154, 'crossentropy': 0.630745166015625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6498554944992065})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.5113420486450195})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.4603111147880554})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.43531334400177})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.42857033014297485})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.41327863931655884})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.40394437313079834})
store['active_learning_steps'][12]['eval_training']['best_epoch']=7
store['active_learning_steps'][12]['acquisition']={'indices': [46580, 3251, 12636, 80, 49957, 53083, 21426, 138, 9991, 26466], 'labels': [6, 8, 6, 9, 5, 3, -1, 5, -1, 5], 'scores': [0.5841078758239746, 0.4966643452644348, 0.5008630454540253, 0.7018952369689941, 0.8373034000396729, 0.4915364682674408, 0.39414000511169434, 0.8156755566596985, 0.38771724700927734, 0.6937078833580017]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 0.8890916109085083})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5645716190338135})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.645741879940033})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6767102479934692})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6393470764160156})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.9219, 'crossentropy': 0.52945966796875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6723005771636963})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5578826665878296})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5241110324859619})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5030777454376221})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [8479, 44350, 47494, 635, 37004, 24539, 50348, 56488, 23211, 57029], 'labels': [5, 3, 5, 5, 5, 3, 2, 3, 5, -1], 'scores': [0.40942490100860596, 0.6557874083518982, 0.6026008129119873, 0.3848288059234619, 0.5341662168502808, 0.38428205251693726, 0.42813408374786377, 0.4379071593284607, 0.6790289282798767, 0.6264711618423462]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.78385329246521})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5313252210617065})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5341256856918335})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5669054985046387})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6187782287597656})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9208, 'crossentropy': 0.503449267578125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.630890965461731})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5261849761009216})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.45631322264671326})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.4602426588535309})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [24038, 54782, 49424, 15747, 56852, 29994, 57392, 29890, 16826, 36446], 'labels': [1, 3, 5, 3, 5, 0, 8, 5, 8, 6], 'scores': [0.43783998489379883, 0.5865380764007568, 0.6062285900115967, 0.41623926162719727, 0.662026047706604, 0.620778501033783, 0.7159215807914734, 0.45164090394973755, 0.5429080128669739, 0.5406321287155151]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.881916344165802})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6108897924423218})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5429582595825195})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6583456993103027})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6915140151977539})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6376328468322754})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.9298, 'crossentropy': 0.464493359375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6344904899597168})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.4595409631729126})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4586988687515259})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.39977604150772095})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.39492329955101013})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [21023, 25442, 19404, 33489, 23890, 892, 48539, 21402, 22576, 21042], 'labels': [2, 2, 4, 2, -1, 6, -1, 1, 9, 2], 'scores': [0.5075833797454834, 0.4848518371582031, 0.5724213719367981, 0.45111799240112305, 0.4843288064002991, 0.443603515625, 0.48781681060791016, 0.4535013437271118, 0.45522528886795044, 0.537280261516571]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8726169466972351})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5423260927200317})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5154116153717041})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5866112112998962})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5890793800354004})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5339360237121582})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.9311, 'crossentropy': 0.4596466796875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6141011714935303})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.47852447628974915})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.42133092880249023})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.40111780166625977})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.3996763825416565})
store['active_learning_steps'][16]['eval_training']['best_epoch']=5
