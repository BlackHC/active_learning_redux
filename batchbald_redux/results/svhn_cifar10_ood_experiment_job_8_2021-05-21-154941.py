store = {}
store['timestamp']=1621608581
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=8']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=8
store['worker_id']=8
store['num_workers']=24
store['config']={'seed': 1243, 'uniform_ood': True, 'id_dataset_name': 'CIFAR-10', 'ood_dataset_name': 'SVHN', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node | one_hot_targets{'num_classes': 10}) + ('SVHN (Train, seed=0, 73257 samples)' | uniform_targets{'num_classes': 10})", 'test': "'CIFAR-10 (Test)'"}
store['initial_training_set_indices']=[12980, 44617, 6984, 21168, 33976, 35571, 33058, 43729, 26944, 24745, 66, 14046, 46542, 39478, 6000, 5915, 39360, 20774, 27084, 44464]
store['evaluation_set_indices']=[3812, 42704, 6729, 38942, 48125, 16968, 5652, 4045, 10740, 19606, 37062, 15768, 44824, 47581, 19482, 4628, 25290, 27933, 27441, 5508, 35131, 18717, 43561, 37318, 8187, 37590, 45717, 1493, 5924, 19803, 23554, 6460, 2962, 36049, 18273, 11023, 27366, 39007, 5305, 46743, 15798, 44136, 20072, 20717, 1152, 8194, 36500, 17618, 35054, 18973, 45734, 16753, 6410, 28807, 8902, 20957, 6625, 41155, 1332, 47376, 36719, 11500, 36383, 7417, 30371, 19517, 33334, 27185, 29033, 42916, 39943, 34789, 18504, 7348, 6096, 28402, 10058, 12011, 34663, 1618, 17887, 41306, 1467, 28071, 12667, 38339, 44920, 44374, 14769, 31145, 21575, 16685, 24836, 48736, 21176, 26844, 45671, 22164, 42503, 10770, 27020, 30182, 37164, 33354, 47307, 17878, 26665, 40819, 14805, 201, 47956, 44739, 8060, 45495, 8139, 27034, 40800, 21802, 18878, 8672, 41175, 48917, 23272, 9952, 23154, 37915, 18669, 18159, 13468, 14436, 16099, 8128, 33349, 31445, 7202, 21948, 10215, 34670, 538, 40015, 17530, 11133, 6028, 12100, 21106, 5614, 30720, 34210, 39322, 40006, 31808, 24717, 34090, 17381, 18164, 17668, 16984, 37856, 41017, 43216, 46788, 26334, 6887, 40485, 39838, 1931, 47231, 37148, 801, 14067, 31951, 7105, 34561, 18698, 45258, 21399, 18558, 26959, 17240, 30502, 39056, 47625, 18880, 37323, 26204, 21788, 1674, 47188, 10526, 25980, 27994, 19871, 22250, 38761, 7182, 14241, 235, 37616, 39973, 35218, 46446, 33361, 39076, 38899, 15578, 36667, 5551, 23088, 32496, 5705, 23255, 25559, 11975, 44032, 45743, 23571, 30475, 15184, 41327, 15827, 33432, 37357, 40250, 16421, 2561, 8533, 25715, 17074, 36811, 30099, 44174, 8029, 1480, 43701, 10198, 38802, 13200, 31615, 28252, 17879, 18749, 16580, 19178, 48034, 4365, 4796, 46033, 47538, 7188, 45076, 13569, 28392, 19457, 41335, 4474, 23022, 11289, 25103, 35813, 40336, 12008, 36695, 28598, 12671, 48831, 18364, 9890, 11804, 37612, 31396, 10683, 31008, 36360, 15312, 26328, 41353, 34761, 4398, 46637, 13891, 32787, 22410, 26463, 4503, 31374, 26143, 7765, 27551, 15340, 16182, 7868, 42518, 34516, 8244, 13037, 39992, 14300, 48188, 42511, 2963, 28224, 28657, 5474, 19682, 682, 25867, 47518, 36303, 18452, 34447, 24821, 36157, 48089, 25120, 44689, 6509, 1852, 17387, 19405, 39441, 42197, 14298, 16443, 1151, 9775, 10834, 44482, 10445, 41434, 37644, 5702, 29159, 17097, 28308, 42161, 29973, 38602, 4592, 24411, 38792, 25200, 28299, 5522, 4441, 4065, 12187, 32012, 41361, 36098, 25224, 27204, 29536, 18785, 28218, 42361, 10437, 8978, 44209, 7804, 35232, 3041, 23251, 41265, 28139, 41350, 18536, 37181, 25352, 16787, 27537, 29568, 45681, 33891, 35667, 31031, 5795, 23494, 7658, 26711, 35750, 34571, 4852, 29601, 14492, 5318, 26987, 11839, 533, 29565, 16424, 43853, 34375, 26710, 37956, 34492, 46294, 12920, 7945, 29669, 14520, 36081, 14478, 37173, 19188, 40253, 23549, 741, 34309, 11001, 6995, 10899, 36881, 7002, 19049, 13388, 40737, 9210, 22684, 43970, 7048, 46803, 45248, 4726, 40534, 23790, 47216, 8585, 7880, 25042, 306, 11939, 45003, 12905, 4052, 45391, 28968, 19408, 6012, 7814, 27790, 10979, 2005, 32156, 16025, 23706, 8236, 24750, 39229, 6968, 7599, 32427, 48001, 12257, 6899, 36229, 19760, 30468, 32347, 15232, 17555, 34373, 1157, 22434, 38137, 3717, 38235, 41506, 10786, 3175, 48043, 24171, 29368, 39765, 16373, 22973, 42399, 32908, 35630, 28508, 29334, 37539, 45770, 29181, 10946, 18072, 18511, 47354, 31444, 42643, 4078, 45028, 45610, 35405, 33751, 7967, 4701, 13378, 48105, 22116, 20599, 45454, 7325, 11304, 12289, 46114, 8359, 41073, 22751, 19402, 8483, 45656, 5604, 9134, 35979, 19757, 43627, 35248, 23566, 727, 34909, 43560, 2888, 12158, 48248, 2094, 47190, 15295, 27629, 15047, 4402, 32595, 6538, 13474, 11538, 10736, 29892, 29786, 1884, 45940, 2144, 37537, 5222, 26418, 10690, 19114, 30223, 17188, 41379, 46182, 20359, 32256, 43739, 41935, 16411, 15933, 22295, 940, 8665, 1154, 32089, 46513, 17506, 39407, 6187, 7878, 37671, 25414, 16789, 37546, 44170, 9921, 22033, 33690, 23656, 5226, 1631, 8671, 45821, 34099, 40039, 31342, 35231, 29621, 31899, 1023, 17082, 38261, 26917, 31921, 5241, 37282, 45513, 46687, 18915, 10796, 8986, 31711, 2185, 29316, 45090, 13383, 5741, 7930, 39306, 13675, 38034, 29826, 48781, 21746, 39559, 31318, 19965, 25443, 45862, 30730, 9611, 43077, 23902, 9541, 38859, 13973, 27923, 25754, 38295, 39261, 15442, 40254, 28002, 23139, 44524, 11458, 10297, 25299, 13617, 28750, 1835, 29505, 23873, 45073, 34640, 5831, 29115, 26568, 6588, 31067, 15001, 4887, 27814, 17283, 23813, 43511, 14398, 13500, 7428, 11090, 11751, 36607, 9712, 43583, 45864, 39972, 14617, 3431, 26470, 33191, 18204, 24481, 28879, 43889, 15015, 36437, 12660, 37650, 405, 36212, 42818, 10677, 15723, 24514, 35518, 42654, 44052, 10218, 37297, 34741, 40715, 37290, 29931, 29774, 25075, 12136, 44466, 25236, 7096, 26190, 14575, 41698, 9068, 24101, 3379, 19906, 15856, 38317, 20799, 17172, 5987, 140, 11530, 38636, 9116, 11151, 25071, 182, 31603, 21547, 47739, 13909, 624, 25621, 30173, 37807, 7053, 30625, 10450, 22316, 23965, 5028, 37725, 1675, 45751, 19683, 26061, 34327, 38096, 30828, 438, 46574, 9121, 4859, 15563, 33935, 39481, 48048, 37730, 35947, 18461, 22658, 35939, 3507, 16223, 5279, 9615, 13583, 28557, 36129, 19326, 23956, 31469, 3397, 36813, 4416, 48955, 27367, 9692, 41380, 27998, 33372, 24467, 24186, 47802, 16612, 46008, 3943, 48514, 42699, 37077, 17401, 39288, 44878, 31226, 14334, 44847, 7473, 42669, 32658, 40101, 11309, 853, 12919, 41501, 26725, 3843, 41314, 16050, 39323, 5916, 19945, 17950, 48824, 8856, 12778, 28765, 13275, 34339, 8883, 36161, 41767, 44449, 7357, 3967, 41737, 3432, 27375, 5603, 1739, 2418, 23760, 26549, 2676, 11659, 40405, 46217, 5207, 28673, 12645, 45982, 48103, 21541, 33384, 28830, 46313, 2540, 17302, 42509, 2321, 40265, 21290, 35387, 48490, 11327, 16529, 40097, 16839, 12570, 17132, 18289, 20343, 22077, 21098, 5426, 8478, 1923, 4941, 48459, 34289, 38039, 44848, 20094, 25546, 19669, 32606, 16624, 28652, 11887, 22863, 48068, 9574, 39941, 2068, 28297, 7225, 41330, 47575, 30080, 25197, 25710, 18030, 16190, 21185, 46949, 1377, 47189, 30166, 28575, 12032, 14160, 11813, 48219, 39348, 42953, 46300, 5559, 15360, 14665, 25279, 42955, 43707, 10089, 10928, 16650, 18156, 4140, 2816, 45019, 25339, 16628, 3925, 25879, 43725, 33970, 17789, 20083, 8873, 41315, 45472, 40526, 4589, 44440, 3184, 4581, 16953, 7585, 45975, 28441, 10956, 22017, 21698, 2107, 44107, 45868, 30293, 15530, 26848, 45705, 811, 22587, 28712, 16591, 45100, 41182, 1225, 40805, 3915, 6545, 8556, 26652, 29708, 24040, 676, 8243, 42597, 17603, 3208, 38902, 15447, 8826, 14791, 38670, 37596, 42980, 17743, 44094, 23778, 32296, 43347, 20210, 6487, 33150, 5095, 35163, 3681, 42450, 21707, 13663, 37987, 13359, 10158, 24531, 21817, 39213, 29424, 38798, 32466, 37354, 27218, 12293, 4133, 14755, 38826, 23328, 48318, 22137, 28379, 35441, 1910, 31964, 26833, 13669, 7484, 43359, 48803, 6853, 47906, 25522, 42533, 16633, 38444, 39544, 13401, 36560, 47222, 1732, 10624, 45339, 24754, 9680, 47728, 4309, 20076, 32836]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 19.42593765258789})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 9.412466049194336})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 9.073053359985352})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 9.17324447631836})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 8.958638191223145})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 9.145524978637695})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 9.363409042358398})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 9.911802291870117})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 17.16683578491211})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 11.803617477416992})
store['active_learning_steps'][0]['training']['best_epoch']=7
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.1805, 'crossentropy': 9.51538515625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 3.624757766723633})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 3.8420844078063965})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 4.0341291427612305})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 4.284232139587402})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 38594], ['ood', 51171], ['id', 42714], ['id', 11476], ['ood', 39108]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7816712216508159, 1.5017309947534323, 2.018959918684792, 2.469553476371921, 2.7841478978968777]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 8.570804595947266})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 7.1255598068237305})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 7.1821746826171875})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 7.729313850402832})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 7.677380561828613})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 16.716907501220703})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 6.260994911193848})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.1996, 'crossentropy': 7.75011875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.155993938446045})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.565383195877075})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 3.843258857727051})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 4.173959255218506})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 27836], ['id', 0], ['id', 1], ['id', 2], ['id', 3]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [nan, nan, nan, nan, nan]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 7.088789463043213})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 8.163431167602539})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 6.224665641784668})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 6.641163349151611})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.2229, 'crossentropy': 7.2676953125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.6682915687561035})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 3.8086585998535156})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.8412885665893555})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 68219], ['id', 27425], ['id', 44958], ['id', 48299], ['id', 18361]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5349170693590288, 1.0229519269009821, 1.4593326505849, 1.8114425399540508, 2.0982407369120244]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 6.319777011871338})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 6.691728591918945})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 7.367494106292725})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 7.294583320617676})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.1822, 'crossentropy': 6.5639484375}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 4.454484939575195})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 3.616363525390625})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 3.62058162689209})
store['active_learning_steps'][3]['eval_training']['best_epoch']=1
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 44439], ['id', 5744], ['id', 17251], ['ood', 23917], ['id', 32560]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.46439791982271095, 0.8275344105979263, 1.1529199205914225, 1.454472647756834, 1.7138693866846926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 6.169486045837402})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 7.884946346282959})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 6.21651554107666})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 6.876143455505371})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.2115, 'crossentropy': 6.3937140625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.020383834838867})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 2.944260597229004})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.475125789642334})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 739], ['id', 4], ['id', 5], ['id', 6], ['id', 7]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [nan, nan, nan, nan, nan]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 6.562893390655518})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 6.4019365310668945})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 6.309737205505371})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 8.427878379821777})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 6.055362701416016})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 7.218769550323486})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 6.52175235748291})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 6.450221061706543})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.2201, 'crossentropy': 5.659478125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.2807722091674805})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.0497031211853027})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 3.3315820693969727})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 3.610724449157715})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.472458839416504})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 35632], ['id', 45238], ['id', 34218], ['id', 20702], ['id', 17649]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4723362829642639, 0.8697683623588022, 1.2305911310743434, 1.55620647085291, 1.846788292292727]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 4.364182472229004})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 6.596202850341797})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 6.452390670776367})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 6.401021957397461})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 6.28891658782959})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 6.691921234130859})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 7.104120254516602})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 6.720367431640625})
store['active_learning_steps'][6]['training']['best_epoch']=5
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.2122, 'crossentropy': 6.2407125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 2.8767380714416504})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.162475824356079})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 3.1136703491210938})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 3.0969557762145996})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 3.6805601119995117})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 3.5839943885803223})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 45018], ['id', 20508], ['id', 3424], ['id', 15322], ['id', 20533]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4994759098176038, 0.9500902511775062, 1.3721011270653989, 1.7389368182960556, 2.0528907113846824]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 6.781033515930176})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 5.468283653259277})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.26789665222168})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 5.626553535461426})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 6.14188289642334})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 7.290410041809082})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.203, 'crossentropy': 5.298298828125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 2.829436779022217})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 2.788788318634033})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 3.388415813446045})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 2.6049818992614746})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 3.140479326248169})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 14846], ['id', 247], ['id', 44934], ['id', 16540], ['id', 19280]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5727556946467662, 1.0958997907630055, 1.515226100439821, 1.8875670210058244, 2.203250560474089]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.824550151824951})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.383339881896973})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.410120964050293})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 6.706386566162109})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 5.589417457580566})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 6.4235639572143555})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 7.4542236328125})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 6.16752815246582})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.2116, 'crossentropy': 5.83964453125}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 2.9478578567504883})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 3.40539288520813})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 2.7417001724243164})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.041018009185791})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 4.091790199279785})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.1573069095611572})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 3.510857105255127})
store['active_learning_steps'][8]['eval_training']['best_epoch']=4
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 20536], ['id', 25377], ['ood', 10948], ['id', 17059], ['id', 43015]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.624827854382942, 1.1479100995957592, 1.5494315404995662, 1.905814495786033, 2.2164952279813175]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 4.564322471618652})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 4.336132526397705})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 5.566739082336426})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 6.3738226890563965})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 7.437947750091553})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 6.2799153327941895})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 7.312688827514648})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.2142, 'crossentropy': 6.373965625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 2.5082221031188965})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 2.555062770843506})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 2.761845111846924})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 2.986340045928955})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.6482019424438477})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 3.233135223388672})
store['active_learning_steps'][9]['eval_training']['best_epoch']=6
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 19083], ['id', 35416], ['id', 5138], ['ood', 8609], ['ood', 10772]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5660511154724472, 1.0618149220617294, 1.4765679198407269, 1.8559036495789476, 2.1911509938087117]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.4650449752807617})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 4.426929473876953})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.592296123504639})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 6.660247802734375})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 7.841531276702881})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 7.035079002380371})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 4.883270740509033})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 7.678746223449707})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 6.337199687957764})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 6.138603687286377})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 7.165178298950195})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 7.204218864440918})
store['active_learning_steps'][10]['training']['best_epoch']=9
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.2506, 'crossentropy': 6.4256578125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.149815082550049})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 3.0290591716766357})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.4761710166931152})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 3.1031136512756348})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.346956729888916})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 2.8915767669677734})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.130373954772949})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 7409], ['id', 18086], ['ood', 34175], ['ood', 55891], ['id', 15863]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5856732397708115, 1.070715715495556, 1.5217558473996782, 1.8888765612051062, 2.2158713179940897]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 5.563765525817871})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.894242286682129})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 6.28424072265625})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 4.706294059753418})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.455997467041016})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 5.245535850524902})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 5.338067531585693})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 9.93055534362793})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 5.370366096496582})
store['active_learning_steps'][11]['training']['best_epoch']=6
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.2391, 'crossentropy': 5.296228515625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 2.526738405227661})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 2.544834613800049})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 3.203176975250244})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 2.9828662872314453})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 3.1082797050476074})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 3.099702835083008})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.050154209136963})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 3.28070068359375})
store['active_learning_steps'][11]['eval_training']['best_epoch']=8
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 28026], ['ood', 64436], ['id', 44329], ['id', 36185], ['ood', 19083]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7085949858726324, 1.230576538479957, 1.7329108785787173, 2.1540457666763526, 2.5261192480420167]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 3.5387299060821533})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 5.156868934631348})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 3.5936312675476074})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 4.798544883728027})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 5.340605735778809})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 6.461639404296875})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 6.983351707458496})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.2643, 'crossentropy': 4.599150390625}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 2.458685874938965})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 2.682335615158081})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 2.8808116912841797})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 2.959141731262207})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.392235279083252})
store['active_learning_steps'][12]['eval_training']['best_epoch']=2
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 6391], ['id', 38038], ['id', 18705], ['id', 31459], ['id', 3280]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5635841843394263, 1.1039802685481472, 1.5731708185178088, 1.9895293830506455, 2.340589524910274]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 4.03240442276001})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 4.013391971588135})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 6.049903869628906})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 5.622988700866699})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.967472553253174})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 5.5725908279418945})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 5.836037635803223})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.518545150756836})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 5.95029354095459})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 6.00029182434082})
store['active_learning_steps'][13]['training']['best_epoch']=7
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.2385, 'crossentropy': 5.691121875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 2.5106849670410156})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 2.8837857246398926})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 2.662644147872925})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 3.0114850997924805})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 3.1379637718200684})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.1194205284118652})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.815646171569824})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 3.163483142852783})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.0878419876098633})
store['active_learning_steps'][13]['eval_training']['best_epoch']=8
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 25861], ['ood', 56297], ['id', 44992], ['id', 1579], ['id', 21590]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6825956696954643, 1.2760371065299525, 1.6681121689086376, 2.0054194252171786, 2.2913892996844085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 4.38326358795166})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 5.087747573852539})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 4.691021919250488})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 3.970749616622925})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 4.621344566345215})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 6.3330464363098145})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 5.847600936889648})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.2576, 'crossentropy': 4.03974140625}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 2.7052454948425293})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 2.3357272148132324})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 2.4910271167755127})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 2.490199565887451})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 2.3413045406341553})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 2.510937213897705})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 44443], ['id', 44764], ['id', 487], ['id', 21708], ['id', 18251]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6350486249204961, 1.1571861705886253, 1.6064975914991995, 1.9756351714342957, 2.2889557515012644]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 4.014328479766846})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 3.956742763519287})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.006931304931641})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 5.591211318969727})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.41841983795166})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 5.589641571044922})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.2541, 'crossentropy': 3.9128859375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 2.5318591594696045})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.6600069999694824})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 2.410120964050293})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 2.9822001457214355})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 2.4856810569763184})
store['active_learning_steps'][15]['eval_training']['best_epoch']=3
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 35961], ['id', 13513], ['id', 43936], ['id', 34162], ['id', 10484]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4386773400671595, 0.7715253054839639, 1.055258990037013, 1.3033630506021954, 1.5329253185318308]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 3.257561445236206})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 2.4035098552703857})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 3.471846342086792})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 4.754000663757324})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 4.213669300079346})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 5.759003639221191})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 4.474845886230469})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 4.031280517578125})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.326171875, 'crossentropy': 4.303412914276123})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.237071990966797})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 4.487508296966553})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 4.896934509277344})
store['active_learning_steps'][16]['training']['best_epoch']=9
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.3, 'crossentropy': 4.269512109375}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 2.3292465209960938})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 2.7769131660461426})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 2.3425040245056152})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.573772430419922})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 2.458376884460449})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 2.736618995666504})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 2.58465576171875})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.6874470710754395})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 2.7017593383789062})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.3115234375, 'crossentropy': 2.7719192504882812})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 2.9972963333129883})
store['active_learning_steps'][16]['eval_training']['best_epoch']=10
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 48562], ['id', 5433], ['id', 3587], ['ood', 60585], ['id', 26087]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5615423416531957, 1.0625499639871316, 1.468740821660801, 1.8176376285868754, 2.1224579369628414]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 3.750795602798462})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 4.217555999755859})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.455190181732178})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 5.708840370178223})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 4.821413993835449})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 5.466670989990234})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 7.589935302734375})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 5.445669651031494})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.2799, 'crossentropy': 4.951617578125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.500858783721924})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 3.1442246437072754})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.9263577461242676})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.8950867652893066})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.984809398651123})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 2.894829511642456})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 3.0484251976013184})
store['active_learning_steps'][17]['eval_training']['best_epoch']=7
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 23951], ['id', 5354], ['id', 19225], ['id', 5872], ['ood', 21560]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.4841546359718797, 0.9571913291318344, 1.3585056739212964, 1.736342841892205, 2.0732299884887606]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.4973044395446777})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 4.29718017578125})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 4.13307523727417})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.883272171020508})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 4.439973831176758})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 5.161959171295166})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 5.03514289855957})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 4.473967552185059})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 4.8889055252075195})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 5.886177062988281})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.5389204025268555})
store['active_learning_steps'][18]['training']['best_epoch']=8
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.262, 'crossentropy': 4.584894921875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.381589889526367})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 2.3287482261657715})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.379251003265381})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 2.718890428543091})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.9138946533203125})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 2.6560635566711426})
store['active_learning_steps'][18]['eval_training']['best_epoch']=3
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 36227], ['id', 19518], ['id', 32061], ['id', 26542], ['id', 32574]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5103298420209583, 0.9835085601078855, 1.4043182805630305, 1.7800401686049465, 2.1160342307002633]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 3.0749847888946533})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 4.110500335693359})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.9597315788269043})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 4.479759216308594})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 5.013875961303711})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 3.907639741897583})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 4.8300065994262695})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.021506309509277})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.939615249633789})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 6.316879749298096})
store['active_learning_steps'][19]['training']['best_epoch']=7
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.2855, 'crossentropy': 4.4946125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 3.0179545879364014})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.4158596992492676})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.696809768676758})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 2.5955119132995605})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 2.704582452774048})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 2.4073057174682617})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 2.768859386444092})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 2.674748420715332})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 2.777345657348633})
store['active_learning_steps'][19]['eval_training']['best_epoch']=8
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 10328], ['id', 22805], ['id', 14987], ['id', 29486], ['id', 9136]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5634242777678342, 1.0905170088465246, 1.529680770229465, 1.9112976086989946, 2.2388093589689895]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.498208522796631})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 3.3661811351776123})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 3.688284397125244})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.576652526855469})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.3203125, 'crossentropy': 4.31903600692749})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.536670684814453})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 4.5180792808532715})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 4.142094612121582})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.2986, 'crossentropy': 4.3908640625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 2.479456663131714})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 2.3086867332458496})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.3076171875, 'crossentropy': 2.406557083129883})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 2.7050774097442627})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 2.9034359455108643})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 2.620965003967285})
store['active_learning_steps'][20]['eval_training']['best_epoch']=3
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 22271], ['id', 42768], ['id', 38455], ['id', 18193], ['id', 2367]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6138815858717589, 1.122899222467578, 1.5773273622649517, 1.9657018650330338, 2.293731652264264]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 4.305156707763672})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 3.6658315658569336})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 4.478113651275635})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 4.595160007476807})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 5.005145072937012})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 6.602553367614746})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 5.092996120452881})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 5.518844127655029})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 5.040947914123535})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 5.555248260498047})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 5.37255859375})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 4.781795501708984})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 6.342848777770996})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 5.811800479888916})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 5.382032871246338})
store['active_learning_steps'][21]['training']['best_epoch']=12
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.2852, 'crossentropy': 4.713924609375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 2.2949743270874023})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 2.263308048248291})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 2.2615933418273926})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 2.3250765800476074})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 2.5979702472686768})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.0323338508605957})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.568077802658081})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 2.690551996231079})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 2.3863306045532227})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 2.9626965522766113})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 2.695718288421631})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 2.696125030517578})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.61735200881958})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 2.7446823120117188})
store['active_learning_steps'][21]['eval_training']['best_epoch']=11
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 40243], ['id', 16081], ['id', 31901], ['id', 47671], ['id', 2065]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.714286655395965, 1.2287993145321514, 1.7210363981309014, 2.146508210410214, 2.5029208726802903]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 2.6878809928894043})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 3.7047386169433594})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 2.829949378967285})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 5.103091239929199})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.125340461730957})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 3.743892192840576})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 4.52250862121582})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 4.339837074279785})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 5.579546928405762})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 4.87293815612793})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 5.748743057250977})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 5.576137542724609})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.31640625, 'crossentropy': 6.108116626739502})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 5.284576416015625})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 7.718709468841553})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 6.7558465003967285})
store['active_learning_steps'][22]['training']['best_epoch']=13
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.3071, 'crossentropy': 5.75117734375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 3.06355619430542})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.761681079864502})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 2.448976516723633})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 2.5061726570129395})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 2.48654842376709})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.328125, 'crossentropy': 2.6534130573272705})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.310546875, 'crossentropy': 2.6082968711853027})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.314453125, 'crossentropy': 2.7429611682891846})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 2.700730800628662})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 2118], ['id', 29221], ['id', 7493], ['id', 17229], ['id', 34549]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5496925685487677, 1.0638803892107904, 1.5023610348248753, 1.8870015978300962, 2.2073997718704987]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 3.025066375732422})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 3.329457998275757})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 3.6772117614746094})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 5.39140510559082})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 4.514560699462891})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 8.252426147460938})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 4.708827018737793})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 5.469635963439941})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.2809, 'crossentropy': 4.52006171875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 2.2679195404052734})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 2.617027759552002})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 2.5397260189056396})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 2.2639613151550293})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 2.6894545555114746})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 2.605510711669922})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 2.8633041381835938})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 19392], ['id', 18802], ['id', 44280], ['id', 21679], ['id', 22132]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.47199274854640194, 0.8755119404109308, 1.228992189952364, 1.5447755235240272, 1.8290080184399296]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 2.6277995109558105})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 3.1602258682250977})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 3.093425989151001})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 3.818673849105835})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 4.503956317901611})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 4.629717826843262})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 4.084533214569092})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 4.457402229309082})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 4.859325408935547})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.2636, 'crossentropy': 4.708144140625}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 2.8581671714782715})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 2.5773987770080566})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 2.8229055404663086})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 3.474316358566284})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.6054089069366455})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 2.5625321865081787})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 2.7662363052368164})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 2.6629786491394043})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 29172], ['id', 6449], ['id', 9538], ['id', 40848], ['id', 33852]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5908449673472516, 1.0063606301004957, 1.3995131533429541, 1.7458852934316624, 2.05611840031166]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 2.899831533432007})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 2.8915300369262695})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.31070613861084})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 3.8641204833984375})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 3.937469959259033})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 4.090366840362549})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 5.187688827514648})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 5.06102180480957})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 5.863421440124512})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 4.334323883056641})
store['active_learning_steps'][25]['training']['best_epoch']=7
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.2836, 'crossentropy': 5.143779296875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 2.360407829284668})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 2.4444773197174072})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 2.3435072898864746})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 2.586338520050049})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 2.760657787322998})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 2.968898296356201})
store['active_learning_steps'][25]['eval_training']['best_epoch']=3
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 37448], ['id', 33633], ['id', 4102], ['id', 42861], ['ood', 38161]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5737483738883948, 1.0389514917703084, 1.4490367945234048, 1.821205110877961, 2.16054665145208]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 2.4638171195983887})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 3.1155428886413574})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 3.9791009426116943})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 3.9167590141296387})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 3.707333564758301})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 4.134740352630615})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 4.735879898071289})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 4.924951553344727})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 4.843967437744141})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 4.757113456726074})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 5.298765182495117})
store['active_learning_steps'][26]['training']['best_epoch']=8
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.2933, 'crossentropy': 5.160462109375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 2.251126289367676})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.4998812675476074})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 2.48150634765625})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 2.6573429107666016})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.32421875, 'crossentropy': 2.5694446563720703})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 2.602865695953369})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 2.723670721054077})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.30078125, 'crossentropy': 2.7598788738250732})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 27380], ['id', 4302], ['ood', 27314], ['id', 31880], ['id', 21852]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4893591818395562, 0.9139664637334008, 1.3007049174226069, 1.6378787658905951, 1.9513692628276722]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 2.3311781883239746})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 2.518070697784424})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 3.9949612617492676})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 3.7705817222595215})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 4.187767505645752})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 3.859682083129883})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 5.738472938537598})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 4.642647743225098})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 4.242889404296875})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 4.543403625488281})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 5.437375068664551})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 4.77828311920166})
store['active_learning_steps'][27]['training']['best_epoch']=9
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.3056, 'crossentropy': 3.9763875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 2.2565057277679443})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 2.2543463706970215})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 2.4709067344665527})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 2.273240566253662})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 2.471313953399658})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 2.4672980308532715})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 2.4880990982055664})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.687349319458008})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 3.1367599964141846})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 2.547480583190918})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.3134765625, 'crossentropy': 2.4192099571228027})
store['active_learning_steps'][27]['eval_training']['best_epoch']=11
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 8999], ['id', 11488], ['id', 677], ['id', 31690], ['ood', 5115]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5405465461538301, 0.9918054727267829, 1.3966548425984957, 1.7552602401559145, 2.0687087680933764]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 2.8593623638153076})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 4.180427551269531})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 3.6810336112976074})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 4.082221031188965})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.271230220794678})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 4.5908403396606445})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 3.804701805114746})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 4.599555015563965})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 4.715620994567871})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 3.997697114944458})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 4.290173530578613})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.30859375, 'crossentropy': 4.473188400268555})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 6.693517684936523})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.297446250915527})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.027688980102539})
store['active_learning_steps'][28]['training']['best_epoch']=12
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.2983, 'crossentropy': 4.152278515625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 2.2303810119628906})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 2.2330241203308105})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 2.991032123565674})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 2.2778940200805664})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 2.3065102100372314})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 2.4180550575256348})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.4695076942443848})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 2.7522287368774414})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 2.224550724029541})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 2.5513806343078613})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 2.6014630794525146})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 2.4496641159057617})
store['active_learning_steps'][28]['eval_training']['best_epoch']=9
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 21717], ['id', 24059], ['id', 29655], ['id', 22042], ['ood', 25069]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5275916746314673, 0.9921953749849481, 1.4220417833482193, 1.8196846778582714, 2.187749091376995]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 2.640955924987793})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 3.044956684112549})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.975904941558838})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 3.9733047485351562})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 4.179681777954102})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 5.139091491699219})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 4.283969402313232})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 4.075041770935059})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 6.1047844886779785})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.052367687225342})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 4.884059906005859})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.2861, 'crossentropy': 3.887184765625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 2.2681140899658203})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 2.2755322456359863})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 2.2783398628234863})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 2.3402767181396484})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 2.387874126434326})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 2.367575168609619})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.381009578704834})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 2.629575252532959})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 2.6721482276916504})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 61668], ['id', 29758], ['id', 29670], ['id', 33093], ['id', 42133]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5316356459134606, 0.9721921786886591, 1.3658685230087784, 1.7345543890129997, 2.060942566545581]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 4.19395637512207})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.0690011978149414})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 2.8546640872955322})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.5153884887695312})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 3.4515485763549805})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 3.21278977394104})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 3.82167387008667})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 4.377985000610352})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 4.7129058837890625})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.295, 'crossentropy': 3.23918046875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 2.2518563270568848})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 2.156996011734009})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 2.1678593158721924})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.225208282470703})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 2.2807912826538086})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 2.2269287109375})
store['active_learning_steps'][30]['eval_training']['best_epoch']=3
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 21295], ['id', 15408], ['id', 18943], ['id', 37921], ['id', 34676]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4100643048439476, 0.7564324952893018, 1.059238710019383, 1.3367401750460433, 1.5650386959304718]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 3.084169387817383})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.3169448375701904})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 3.2821764945983887})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 5.336865425109863})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 3.649015426635742})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.8371782302856445})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.247303009033203})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 5.55477237701416})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.2869, 'crossentropy': 3.630493359375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 2.6918110847473145})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 2.5193071365356445})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 2.805388927459717})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 2.4576265811920166})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 2.4690723419189453})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 2.8715944290161133})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 2.6478230953216553})
store['active_learning_steps'][31]['eval_training']['best_epoch']=4
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 9075], ['id', 44601], ['id', 18712], ['id', 36799], ['id', 41170]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.4417208783306751, 0.8230660819698818, 1.1272604636538688, 1.3923787728480006, 1.6373154577623126]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 3.3812990188598633})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.310546875, 'crossentropy': 2.284520149230957})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 3.200596332550049})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.966986656188965})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 3.3820230960845947})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.2968, 'crossentropy': 2.33922421875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 2.051732063293457})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 2.244626045227051})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 2.323641777038574})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 2.1077880859375})
store['active_learning_steps'][32]['eval_training']['best_epoch']=4
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 19077], ['id', 48767], ['id', 14529], ['id', 1816], ['id', 33167]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.36366443733428344, 0.688975903620038, 0.9665586793042307, 1.1739917681249974, 1.356528735098192]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 2.861422061920166})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 2.6603031158447266})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 2.7102479934692383})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 3.229961395263672})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 3.464921236038208})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 3.3135015964508057})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 3.9371650218963623})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.2885, 'crossentropy': 3.1838091796875}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 2.4768080711364746})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 2.155547618865967})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 2.6344151496887207})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.185436487197876})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.2729074954986572})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.4314980506896973})
store['active_learning_steps'][33]['eval_training']['best_epoch']=3
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 15755], ['id', 12514], ['id', 16904], ['id', 28181], ['id', 18967]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4760497546063678, 0.8935982331336021, 1.2852340818219483, 1.580538388809134, 1.8463253343582453]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 2.52492618560791})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 2.9475960731506348})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 3.220198631286621})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 3.138029098510742})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 3.3975069522857666})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 3.6382830142974854})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 4.574104309082031})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 3.617216110229492})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.3076171875, 'crossentropy': 3.7946367263793945})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 4.285836696624756})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 4.130661964416504})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 4.37706184387207})
store['active_learning_steps'][34]['training']['best_epoch']=9
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.3118, 'crossentropy': 3.7286015625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 2.2964296340942383})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 2.204564332962036})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 2.435105800628662})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.719816207885742})
store['active_learning_steps'][34]['eval_training']['best_epoch']=1
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 35885], ['id', 13506], ['id', 10793], ['id', 4713], ['id', 13622]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4656629883459895, 0.8774157013452215, 1.2805936897304746, 1.6414520348484567, 1.9583469664362791]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 2.525214672088623})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.9076812267303467})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 2.942065954208374})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 2.993389129638672})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.30859375, 'crossentropy': 2.702324867248535})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 3.053431987762451})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 3.5999197959899902})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.30078125, 'crossentropy': 4.10092830657959})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.312, 'crossentropy': 2.6112275390625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 1.9936528205871582})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 2.278825283050537})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 2.1188344955444336})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 2.0987892150878906})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.3088831901550293})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 2.1367580890655518})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 2.156869888305664})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 22035], ['id', 3725], ['id', 6202], ['id', 29902], ['id', 10562]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3295367907717748, 0.6242835281625863, 0.8951350830227778, 1.1476578564055604, 1.3608465421855334]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 2.4157750606536865})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 2.6504664421081543})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 2.789402961730957})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 3.944366931915283})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 3.1306865215301514})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.102437973022461})
store['active_learning_steps'][36]['training']['best_epoch']=3
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.2859, 'crossentropy': 2.8584482421875}
