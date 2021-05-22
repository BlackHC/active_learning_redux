store = {}
store['timestamp']=1621608538
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=4']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=4
store['worker_id']=4
store['num_workers']=24
store['config']={'seed': 1238, 'uniform_ood': True, 'id_dataset_name': 'CIFAR-10', 'ood_dataset_name': 'SVHN', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node | one_hot_targets{'num_classes': 10}) + ('SVHN (Train, seed=0, 73257 samples)' | uniform_targets{'num_classes': 10})", 'test': "'CIFAR-10 (Test)'"}
store['initial_training_set_indices']=[12980, 44617, 6984, 21168, 33976, 35571, 33058, 43729, 26944, 24745, 66, 14046, 46542, 39478, 6000, 5915, 39360, 20774, 27084, 44464]
store['evaluation_set_indices']=[3812, 42704, 6729, 38942, 48125, 16968, 5652, 4045, 10740, 19606, 37062, 15768, 44824, 47581, 19482, 4628, 25290, 27933, 27441, 5508, 35131, 18717, 43561, 37318, 8187, 37590, 45717, 1493, 5924, 19803, 23554, 6460, 2962, 36049, 18273, 11023, 27366, 39007, 5305, 46743, 15798, 44136, 20072, 20717, 1152, 8194, 36500, 17618, 35054, 18973, 45734, 16753, 6410, 28807, 8902, 20957, 6625, 41155, 1332, 47376, 36719, 11500, 36383, 7417, 30371, 19517, 33334, 27185, 29033, 42916, 39943, 34789, 18504, 7348, 6096, 28402, 10058, 12011, 34663, 1618, 17887, 41306, 1467, 28071, 12667, 38339, 44920, 44374, 14769, 31145, 21575, 16685, 24836, 48736, 21176, 26844, 45671, 22164, 42503, 10770, 27020, 30182, 37164, 33354, 47307, 17878, 26665, 40819, 14805, 201, 47956, 44739, 8060, 45495, 8139, 27034, 40800, 21802, 18878, 8672, 41175, 48917, 23272, 9952, 23154, 37915, 18669, 18159, 13468, 14436, 16099, 8128, 33349, 31445, 7202, 21948, 10215, 34670, 538, 40015, 17530, 11133, 6028, 12100, 21106, 5614, 30720, 34210, 39322, 40006, 31808, 24717, 34090, 17381, 18164, 17668, 16984, 37856, 41017, 43216, 46788, 26334, 6887, 40485, 39838, 1931, 47231, 37148, 801, 14067, 31951, 7105, 34561, 18698, 45258, 21399, 18558, 26959, 17240, 30502, 39056, 47625, 18880, 37323, 26204, 21788, 1674, 47188, 10526, 25980, 27994, 19871, 22250, 38761, 7182, 14241, 235, 37616, 39973, 35218, 46446, 33361, 39076, 38899, 15578, 36667, 5551, 23088, 32496, 5705, 23255, 25559, 11975, 44032, 45743, 23571, 30475, 15184, 41327, 15827, 33432, 37357, 40250, 16421, 2561, 8533, 25715, 17074, 36811, 30099, 44174, 8029, 1480, 43701, 10198, 38802, 13200, 31615, 28252, 17879, 18749, 16580, 19178, 48034, 4365, 4796, 46033, 47538, 7188, 45076, 13569, 28392, 19457, 41335, 4474, 23022, 11289, 25103, 35813, 40336, 12008, 36695, 28598, 12671, 48831, 18364, 9890, 11804, 37612, 31396, 10683, 31008, 36360, 15312, 26328, 41353, 34761, 4398, 46637, 13891, 32787, 22410, 26463, 4503, 31374, 26143, 7765, 27551, 15340, 16182, 7868, 42518, 34516, 8244, 13037, 39992, 14300, 48188, 42511, 2963, 28224, 28657, 5474, 19682, 682, 25867, 47518, 36303, 18452, 34447, 24821, 36157, 48089, 25120, 44689, 6509, 1852, 17387, 19405, 39441, 42197, 14298, 16443, 1151, 9775, 10834, 44482, 10445, 41434, 37644, 5702, 29159, 17097, 28308, 42161, 29973, 38602, 4592, 24411, 38792, 25200, 28299, 5522, 4441, 4065, 12187, 32012, 41361, 36098, 25224, 27204, 29536, 18785, 28218, 42361, 10437, 8978, 44209, 7804, 35232, 3041, 23251, 41265, 28139, 41350, 18536, 37181, 25352, 16787, 27537, 29568, 45681, 33891, 35667, 31031, 5795, 23494, 7658, 26711, 35750, 34571, 4852, 29601, 14492, 5318, 26987, 11839, 533, 29565, 16424, 43853, 34375, 26710, 37956, 34492, 46294, 12920, 7945, 29669, 14520, 36081, 14478, 37173, 19188, 40253, 23549, 741, 34309, 11001, 6995, 10899, 36881, 7002, 19049, 13388, 40737, 9210, 22684, 43970, 7048, 46803, 45248, 4726, 40534, 23790, 47216, 8585, 7880, 25042, 306, 11939, 45003, 12905, 4052, 45391, 28968, 19408, 6012, 7814, 27790, 10979, 2005, 32156, 16025, 23706, 8236, 24750, 39229, 6968, 7599, 32427, 48001, 12257, 6899, 36229, 19760, 30468, 32347, 15232, 17555, 34373, 1157, 22434, 38137, 3717, 38235, 41506, 10786, 3175, 48043, 24171, 29368, 39765, 16373, 22973, 42399, 32908, 35630, 28508, 29334, 37539, 45770, 29181, 10946, 18072, 18511, 47354, 31444, 42643, 4078, 45028, 45610, 35405, 33751, 7967, 4701, 13378, 48105, 22116, 20599, 45454, 7325, 11304, 12289, 46114, 8359, 41073, 22751, 19402, 8483, 45656, 5604, 9134, 35979, 19757, 43627, 35248, 23566, 727, 34909, 43560, 2888, 12158, 48248, 2094, 47190, 15295, 27629, 15047, 4402, 32595, 6538, 13474, 11538, 10736, 29892, 29786, 1884, 45940, 2144, 37537, 5222, 26418, 10690, 19114, 30223, 17188, 41379, 46182, 20359, 32256, 43739, 41935, 16411, 15933, 22295, 940, 8665, 1154, 32089, 46513, 17506, 39407, 6187, 7878, 37671, 25414, 16789, 37546, 44170, 9921, 22033, 33690, 23656, 5226, 1631, 8671, 45821, 34099, 40039, 31342, 35231, 29621, 31899, 1023, 17082, 38261, 26917, 31921, 5241, 37282, 45513, 46687, 18915, 10796, 8986, 31711, 2185, 29316, 45090, 13383, 5741, 7930, 39306, 13675, 38034, 29826, 48781, 21746, 39559, 31318, 19965, 25443, 45862, 30730, 9611, 43077, 23902, 9541, 38859, 13973, 27923, 25754, 38295, 39261, 15442, 40254, 28002, 23139, 44524, 11458, 10297, 25299, 13617, 28750, 1835, 29505, 23873, 45073, 34640, 5831, 29115, 26568, 6588, 31067, 15001, 4887, 27814, 17283, 23813, 43511, 14398, 13500, 7428, 11090, 11751, 36607, 9712, 43583, 45864, 39972, 14617, 3431, 26470, 33191, 18204, 24481, 28879, 43889, 15015, 36437, 12660, 37650, 405, 36212, 42818, 10677, 15723, 24514, 35518, 42654, 44052, 10218, 37297, 34741, 40715, 37290, 29931, 29774, 25075, 12136, 44466, 25236, 7096, 26190, 14575, 41698, 9068, 24101, 3379, 19906, 15856, 38317, 20799, 17172, 5987, 140, 11530, 38636, 9116, 11151, 25071, 182, 31603, 21547, 47739, 13909, 624, 25621, 30173, 37807, 7053, 30625, 10450, 22316, 23965, 5028, 37725, 1675, 45751, 19683, 26061, 34327, 38096, 30828, 438, 46574, 9121, 4859, 15563, 33935, 39481, 48048, 37730, 35947, 18461, 22658, 35939, 3507, 16223, 5279, 9615, 13583, 28557, 36129, 19326, 23956, 31469, 3397, 36813, 4416, 48955, 27367, 9692, 41380, 27998, 33372, 24467, 24186, 47802, 16612, 46008, 3943, 48514, 42699, 37077, 17401, 39288, 44878, 31226, 14334, 44847, 7473, 42669, 32658, 40101, 11309, 853, 12919, 41501, 26725, 3843, 41314, 16050, 39323, 5916, 19945, 17950, 48824, 8856, 12778, 28765, 13275, 34339, 8883, 36161, 41767, 44449, 7357, 3967, 41737, 3432, 27375, 5603, 1739, 2418, 23760, 26549, 2676, 11659, 40405, 46217, 5207, 28673, 12645, 45982, 48103, 21541, 33384, 28830, 46313, 2540, 17302, 42509, 2321, 40265, 21290, 35387, 48490, 11327, 16529, 40097, 16839, 12570, 17132, 18289, 20343, 22077, 21098, 5426, 8478, 1923, 4941, 48459, 34289, 38039, 44848, 20094, 25546, 19669, 32606, 16624, 28652, 11887, 22863, 48068, 9574, 39941, 2068, 28297, 7225, 41330, 47575, 30080, 25197, 25710, 18030, 16190, 21185, 46949, 1377, 47189, 30166, 28575, 12032, 14160, 11813, 48219, 39348, 42953, 46300, 5559, 15360, 14665, 25279, 42955, 43707, 10089, 10928, 16650, 18156, 4140, 2816, 45019, 25339, 16628, 3925, 25879, 43725, 33970, 17789, 20083, 8873, 41315, 45472, 40526, 4589, 44440, 3184, 4581, 16953, 7585, 45975, 28441, 10956, 22017, 21698, 2107, 44107, 45868, 30293, 15530, 26848, 45705, 811, 22587, 28712, 16591, 45100, 41182, 1225, 40805, 3915, 6545, 8556, 26652, 29708, 24040, 676, 8243, 42597, 17603, 3208, 38902, 15447, 8826, 14791, 38670, 37596, 42980, 17743, 44094, 23778, 32296, 43347, 20210, 6487, 33150, 5095, 35163, 3681, 42450, 21707, 13663, 37987, 13359, 10158, 24531, 21817, 39213, 29424, 38798, 32466, 37354, 27218, 12293, 4133, 14755, 38826, 23328, 48318, 22137, 28379, 35441, 1910, 31964, 26833, 13669, 7484, 43359, 48803, 6853, 47906, 25522, 42533, 16633, 38444, 39544, 13401, 36560, 47222, 1732, 10624, 45339, 24754, 9680, 47728, 4309, 20076, 32836]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 14.433326721191406})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 10.315667152404785})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 10.779623985290527})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 10.575279235839844})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 12.050871849060059})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 10.161626815795898})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.175, 'crossentropy': 11.14251875}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 4252], ['id', 0], ['id', 1], ['id', 2], ['id', 3]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [nan, nan, nan, nan, nan]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 10.944313049316406})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 9.845705032348633})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 9.823013305664062})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 10.72291374206543})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.2045, 'crossentropy': 10.79329765625}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 21857], ['ood', 16540], ['id', 43218], ['ood', 11566], ['ood', 58563]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7320605954560051, 1.3727819046526202, 1.968696350613821, 2.4761194932037363, 2.865329665864544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 10.204225540161133})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 14.427248001098633})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 8.996452331542969})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 7.498571872711182})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 8.271660804748535})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 8.363686561584473})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.2045, 'crossentropy': 8.60539609375}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 39748], ['id', 28510], ['ood', 47020], ['id', 20396], ['ood', 47058]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.9188849804255421, 1.6765903396531083, 2.3322409863635407, 2.911579459078867, 3.3462651861998793]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 5.8410844802856445})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 8.337904930114746})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.8629655838012695})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 6.832333564758301})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.2025, 'crossentropy': 5.847049609375}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 27836], ['id', 43772], ['id', 21475], ['id', 37609], ['ood', 44908]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6221203581279973, 1.1762616493946618, 1.680068869572188, 2.1319062567130826, 2.517434067652186]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 6.206206798553467})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 5.724440097808838})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 7.251952171325684})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 6.191046237945557})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 7.039088249206543})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.2138, 'crossentropy': 5.47571953125}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 29398], ['id', 36981], ['id', 12010], ['id', 28248], ['id', 35221]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5218359388989506, 1.0275466895410146, 1.4668316529145873, 1.877356125528875, 2.25192652565827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.365277290344238})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 6.590762615203857})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 6.2329583168029785})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 6.3650312423706055})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 6.739650726318359})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 6.450377941131592})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.198, 'crossentropy': 6.22451875}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 18221], ['id', 38909], ['id', 31391], ['ood', 29961], ['id', 45238]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7488531394585736, 1.4572430477121898, 2.0267951817484207, 2.544109442566194, 2.9832923718650006]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.270566940307617})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 4.8156208992004395})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 6.109981060028076})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.452413558959961})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 6.009414196014404})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.540694236755371})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.785991191864014})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.2326, 'crossentropy': 4.42123984375}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 7817], ['id', 23204], ['ood', 27300], ['id', 40268], ['id', 46325]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.582944456970929, 1.1196338601997646, 1.6228619685126855, 2.0507310096860785, 2.439724986125775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 4.670283794403076})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 6.77119255065918})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.814205169677734})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.610404014587402})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 5.085106372833252})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 6.788677215576172})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 6.030489921569824})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.2304, 'crossentropy': 5.5300515625}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 7204], ['id', 8765], ['id', 35133], ['id', 16418], ['id', 11917]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.678679700015403, 1.2664981035218865, 1.8261588228947065, 2.3009714918141997, 2.709640518077573]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 5.812619209289551})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 3.9154253005981445})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 5.313283920288086})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 6.5731096267700195})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.997712135314941})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 5.516928672790527})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.083705902099609})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 5.727848052978516})
store['active_learning_steps'][8]['training']['best_epoch']=5
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.229, 'crossentropy': 6.00710390625}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 42476], ['id', 45950], ['id', 47116], ['id', 42569], ['ood', 37304]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7026048269415379, 1.3229766205475415, 1.8944679111781988, 2.3885446992666566, 2.8000194517203862]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.0073657035827637})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 4.044517993927002})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 5.447201728820801})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 7.331506252288818})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.2228, 'crossentropy': 3.0666521484375}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 47658], ['id', 4434], ['id', 43810], ['id', 3762], ['ood', 55117]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5852095496821678, 1.0768510518621843, 1.392856000653488, 1.6935828227524237, 1.9796440168536504]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 3.3547558784484863})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.01845645904541})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 4.614985466003418})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.239272117614746})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 6.089570999145508})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 4.896024703979492})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.1932525634765625})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 5.47902774810791})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.2436, 'crossentropy': 6.24275546875}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 13785], ['id', 24204], ['id', 25664], ['id', 1407], ['id', 34619]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7153045967177101, 1.3312661874044212, 1.8590362057309298, 2.3525542668610546, 2.7539947434870653]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 4.467271327972412})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 4.443589210510254})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.027315616607666})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.037308692932129})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 5.788399696350098})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 4.406271934509277})
store['active_learning_steps'][11]['training']['best_epoch']=3
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.2466, 'crossentropy': 3.94871171875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 25848], ['id', 46933], ['id', 20758], ['ood', 2275], ['id', 41326]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.526736924351858, 1.0208965000240848, 1.4756516424027035, 1.8761890108691217, 2.238552303799241]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 4.38585090637207})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 4.573779106140137})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 5.438794136047363})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 4.673769950866699})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.2484, 'crossentropy': 4.199753125}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 21823], ['id', 39699], ['ood', 59713], ['id', 17713], ['id', 24495]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.663190423095485, 1.187464841778323, 1.644712337497105, 2.0467857846345243, 2.3755393646545464]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 6.736952781677246})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 4.168445587158203})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 5.042017936706543})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 4.7099432945251465})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 4.709303379058838})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.154725074768066})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 4.721765518188477})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.2609, 'crossentropy': 4.990230859375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 5586], ['id', 33918], ['id', 37742], ['id', 43681], ['id', 24120]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.802909348230336, 1.3322069762651818, 1.7527360705753874, 2.149936047284438, 2.52045494977188]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 5.259001731872559})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.536294937133789})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 6.018542289733887})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.718681335449219})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.044878005981445})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 5.25515604019165})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.6378173828125})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 6.223176002502441})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.163066864013672})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 4.2374587059021})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 4.60323429107666})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 6.167636871337891})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 6.233669757843018})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 5.015522003173828})
store['active_learning_steps'][14]['training']['best_epoch']=11
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.2713, 'crossentropy': 4.376712109375}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 23421], ['id', 35824], ['id', 7683], ['id', 10507], ['id', 10917]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4909646694765557, 0.9360353479120633, 1.356311306014784, 1.757400720001066, 2.1263233300250306]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 4.408820629119873})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 4.472132205963135})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 4.138035297393799})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.542906761169434})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 4.11814546585083})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 5.271615982055664})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 5.042040824890137})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 5.094595432281494})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 5.27949333190918})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 5.225656032562256})
store['active_learning_steps'][15]['training']['best_epoch']=7
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.2892, 'crossentropy': 4.9087828125}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 47999], ['id', 15255], ['id', 23273], ['id', 37063], ['ood', 36857]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6588409872227856, 1.2769819750836557, 1.8036020218746653, 2.270492661275723, 2.674367029398466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.5729973316192627})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 4.253089427947998})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.9174294471740723})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 4.78065299987793})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.174276351928711})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 6.219667434692383})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.7771196365356445})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.260566711425781})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.2429, 'crossentropy': 4.90753515625}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 37767], ['id', 26881], ['id', 20228], ['id', 32136], ['id', 30227]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7041639475666348, 1.330526953140991, 1.863169727445189, 2.3315016833415285, 2.730005399191718]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.601839542388916})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 3.9689409732818604})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 3.868577480316162})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.143721580505371})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 4.016923904418945})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.2362, 'crossentropy': 3.932908984375}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 17654], ['id', 18929], ['id', 10150], ['ood', 39176], ['id', 25005]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5474556858095807, 1.031040915123882, 1.4130153097099898, 1.7633695886235117, 2.0809802933679347]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 4.233297348022461})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.9412894248962402})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.130709648132324})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 5.032567024230957})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 5.28834867477417})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 4.759539604187012})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 4.894008159637451})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 4.365174293518066})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.2651, 'crossentropy': 5.07088984375}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 47723], ['id', 13292], ['id', 27477], ['id', 36252], ['id', 47041]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6630749092327952, 1.2464328871225643, 1.7467940858885602, 2.159615820367689, 2.543404949358906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 4.864421367645264})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 6.199338912963867})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 4.118666172027588})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 3.748079299926758})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 5.1584906578063965})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.671428680419922})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 5.10457181930542})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 5.543868064880371})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.2849, 'crossentropy': 5.101725}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 26397], ['id', 22530], ['id', 34028], ['id', 5351], ['id', 42357]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5895615221305932, 1.110659770982077, 1.5852246150546652, 2.0161682179431324, 2.4015877533931995]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.00137996673584})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 3.766460418701172})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 4.0945587158203125})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 5.8842058181762695})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 4.627267837524414})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 4.2255167961120605})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.933489799499512})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 5.449272155761719})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 5.876962184906006})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 4.817659378051758})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 5.956456184387207})
store['active_learning_steps'][20]['training']['best_epoch']=8
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.2801, 'crossentropy': 5.1801484375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 23815], ['id', 13331], ['id', 1779], ['id', 39496], ['ood', 14105]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6750814176313304, 1.17605431300866, 1.616346562465366, 2.022875963725964, 2.400548241023114]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 4.668832778930664})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 2.913750410079956})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 4.171674728393555})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 4.2030110359191895})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.012232780456543})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.328125, 'crossentropy': 4.960766792297363})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 3.601036548614502})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 5.1717939376831055})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.059556007385254})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.2959, 'crossentropy': 4.94925703125}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 47452], ['id', 26583], ['id', 48032], ['ood', 16451], ['id', 11993]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6483799356384479, 1.272027314833577, 1.7993952771200878, 2.276197300254294, 2.6965910616042335]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.2930827140808105})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.466113090515137})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 4.797050476074219})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.599647521972656})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.2496, 'crossentropy': 2.3545181640625}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 29350], ['id', 20136], ['id', 31264], ['id', 2097], ['id', 42610]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4383743369899662, 0.8009513225276912, 1.1142419225974498, 1.3651050500552273, 1.58692032570925]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 3.6393346786499023})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.37148904800415})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 3.6683602333068848})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 4.562671661376953})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 3.430367946624756})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 3.348879814147949})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 4.316687107086182})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.2781, 'crossentropy': 4.3357375}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 11553], ['id', 24063], ['id', 6848], ['id', 20104], ['ood', 48980]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6407508533316002, 1.1287379117908802, 1.5722761178243632, 1.9885614109530216, 2.3817100589159725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 2.5039148330688477})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 3.234579086303711})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 3.8005928993225098})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 3.3419480323791504})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.537672996520996})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 4.006964683532715})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.418585300445557})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 4.107779502868652})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 4.83860445022583})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.2846, 'crossentropy': 3.85163359375}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 8165], ['id', 22280], ['id', 24405], ['id', 10068], ['id', 29337]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.573046513007673, 1.0598997971816222, 1.5165345616763277, 1.913024101251481, 2.2641017592686303]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 2.776428699493408})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 3.223616123199463})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 3.960041046142578})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 3.329535484313965})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 3.938929557800293})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 3.5605735778808594})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.100973129272461})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.2859, 'crossentropy': 3.348816796875}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 43875], ['id', 41911], ['id', 5627], ['id', 32465], ['id', 43406]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5401690623963318, 0.9457706302987976, 1.3379316640360304, 1.6854059601207112, 2.0186656155460536]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 4.07724666595459})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 3.263645648956299})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 3.554943561553955})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 3.9017038345336914})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 4.149584770202637})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 4.49442195892334})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 3.8188912868499756})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 5.414928913116455})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 4.288214683532715})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 4.220523834228516})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 5.068639755249023})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 4.757055282592773})
store['active_learning_steps'][26]['training']['best_epoch']=9
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.2987, 'crossentropy': 4.229153515625}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 36828], ['id', 452], ['id', 28593], ['id', 22945], ['id', 7755]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6211002223350426, 1.1895536323029896, 1.6652227860596964, 2.1083975572836184, 2.5099264811863984]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 4.291811943054199})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 3.932572841644287})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 3.2169392108917236})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 3.8723554611206055})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 3.4253969192504883})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 4.071453094482422})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.2887, 'crossentropy': 3.353169921875}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 30314], ['id', 34911], ['id', 5601], ['id', 20372], ['id', 46554]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5430423118126808, 0.9959686636142138, 1.4110905554726907, 1.8106650210914434, 2.138286890382254]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 2.8924500942230225})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 3.1261134147644043})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 3.6930344104766846})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 3.7983899116516113})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 4.255016326904297})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 4.405398368835449})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 4.2628607749938965})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.3095703125, 'crossentropy': 4.334017276763916})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 4.98642635345459})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 5.3462324142456055})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 4.7093505859375})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.3017, 'crossentropy': 4.09208203125}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 14642], ['id', 29696], ['id', 41974], ['id', 12750], ['id', 32725]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5720984064439278, 1.0858400558947712, 1.531070082053473, 1.9489863837388448, 2.3370916508795236]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 2.626079559326172})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 3.4068212509155273})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 3.118046283721924})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 3.95267915725708})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 3.9278342723846436})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.592347145080566})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 3.843806743621826})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.2754, 'crossentropy': 4.081333203125}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 18705], ['id', 33675], ['id', 14873], ['id', 38831], ['id', 34012]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6002902865662127, 1.1022142812060336, 1.541822061240798, 1.9402343058364968, 2.2725151802087407]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 2.7999281883239746})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 3.215959310531616})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 3.3932480812072754})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 4.314543724060059})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 4.992953777313232})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 3.887791156768799})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 3.157069683074951})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 5.763363361358643})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 4.474891185760498})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.2956, 'crossentropy': 3.789971875}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 1866], ['id', 22331], ['id', 29593], ['id', 27601], ['id', 48738]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6186169823410472, 1.203536550555702, 1.6883117293477912, 2.130770607036612, 2.4861826456618523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 2.3234243392944336})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 2.4651081562042236})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 3.1064038276672363})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.3095703125, 'crossentropy': 3.7318267822265625})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.852443695068359})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 3.937905788421631})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.559473991394043})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.2958, 'crossentropy': 3.651103125}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 29464], ['id', 23605], ['ood', 51723], ['id', 3252], ['id', 19248]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6031307519679019, 1.1536875906768183, 1.6486914795359393, 2.061902394136154, 2.386170615861934]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 2.823941230773926})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 3.699211359024048})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.7288522720336914})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.26347541809082})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 3.5575621128082275})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 3.4896368980407715})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 4.250967979431152})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.3212890625, 'crossentropy': 5.127846717834473})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 5.469020843505859})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 3.707221031188965})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 4.261162281036377})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.3171, 'crossentropy': 4.66484296875}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 48336], ['id', 47891], ['id', 14405], ['id', 41036], ['id', 46498]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6157547448443483, 1.149924109119417, 1.6612982298327976, 2.1088092045407194, 2.503634157694121]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.299405097961426})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 3.2089099884033203})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 4.011153697967529})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 3.793757915496826})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 4.256621360778809})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 4.982934951782227})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 4.243964195251465})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 4.23056697845459})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.2987, 'crossentropy': 3.88117890625}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 30889], ['id', 43785], ['id', 37191], ['id', 12029], ['id', 40881]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5963912093282329, 1.1735974389733168, 1.6625504285828119, 2.0870674997286187, 2.451234786923096]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 2.444523334503174})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 3.1797666549682617})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 3.375321865081787})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 2.9553847312927246})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 3.6205039024353027})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 3.9862585067749023})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 4.39508581161499})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.2985, 'crossentropy': 2.8532259765625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 1717], ['id', 16181], ['id', 19509], ['id', 45559], ['id', 40940]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4725377706486069, 0.9260890980458036, 1.2989785778327931, 1.6183724717394838, 1.9150601084443473]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 2.6640775203704834})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 3.536731719970703})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 2.8425230979919434})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 3.005458354949951})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.3125, 'crossentropy': 3.583557605743408})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.314453125, 'crossentropy': 3.7289328575134277})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.322265625, 'crossentropy': 3.862811803817749})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.318359375, 'crossentropy': 4.180898666381836})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 4.153581142425537})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.310546875, 'crossentropy': 3.941629409790039})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.3149, 'crossentropy': 3.767283203125}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 383], ['id', 19964], ['id', 6850], ['id', 17550], ['id', 35646]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5519619309040933, 1.0714014196704458, 1.5636902850676666, 1.9891680585902538, 2.385601047194312]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 2.2394323348999023})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 2.4543488025665283})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 3.005481719970703})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 3.1326100826263428})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.310546875, 'crossentropy': 3.464615821838379})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.3076171875, 'crossentropy': 3.463441848754883})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 3.933349609375})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.318359375, 'crossentropy': 3.365407943725586})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.3193359375, 'crossentropy': 3.7476186752319336})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 4.581510543823242})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 3.8675551414489746})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 4.325939178466797})
store['active_learning_steps'][36]['training']['best_epoch']=9
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.3012, 'crossentropy': 3.5978984375}
