store = {}
store['timestamp']=1621608533
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=0']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=0
store['worker_id']=0
store['num_workers']=24
store['config']={'seed': 1234, 'uniform_ood': True, 'id_dataset_name': 'CIFAR-10', 'ood_dataset_name': 'SVHN', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node | one_hot_targets{'num_classes': 10}) + ('SVHN (Train, seed=0, 73257 samples)' | uniform_targets{'num_classes': 10})", 'test': "'CIFAR-10 (Test)'"}
store['initial_training_set_indices']=[12980, 44617, 6984, 21168, 33976, 35571, 33058, 43729, 26944, 24745, 66, 14046, 46542, 39478, 6000, 5915, 39360, 20774, 27084, 44464]
store['evaluation_set_indices']=[3812, 42704, 6729, 38942, 48125, 16968, 5652, 4045, 10740, 19606, 37062, 15768, 44824, 47581, 19482, 4628, 25290, 27933, 27441, 5508, 35131, 18717, 43561, 37318, 8187, 37590, 45717, 1493, 5924, 19803, 23554, 6460, 2962, 36049, 18273, 11023, 27366, 39007, 5305, 46743, 15798, 44136, 20072, 20717, 1152, 8194, 36500, 17618, 35054, 18973, 45734, 16753, 6410, 28807, 8902, 20957, 6625, 41155, 1332, 47376, 36719, 11500, 36383, 7417, 30371, 19517, 33334, 27185, 29033, 42916, 39943, 34789, 18504, 7348, 6096, 28402, 10058, 12011, 34663, 1618, 17887, 41306, 1467, 28071, 12667, 38339, 44920, 44374, 14769, 31145, 21575, 16685, 24836, 48736, 21176, 26844, 45671, 22164, 42503, 10770, 27020, 30182, 37164, 33354, 47307, 17878, 26665, 40819, 14805, 201, 47956, 44739, 8060, 45495, 8139, 27034, 40800, 21802, 18878, 8672, 41175, 48917, 23272, 9952, 23154, 37915, 18669, 18159, 13468, 14436, 16099, 8128, 33349, 31445, 7202, 21948, 10215, 34670, 538, 40015, 17530, 11133, 6028, 12100, 21106, 5614, 30720, 34210, 39322, 40006, 31808, 24717, 34090, 17381, 18164, 17668, 16984, 37856, 41017, 43216, 46788, 26334, 6887, 40485, 39838, 1931, 47231, 37148, 801, 14067, 31951, 7105, 34561, 18698, 45258, 21399, 18558, 26959, 17240, 30502, 39056, 47625, 18880, 37323, 26204, 21788, 1674, 47188, 10526, 25980, 27994, 19871, 22250, 38761, 7182, 14241, 235, 37616, 39973, 35218, 46446, 33361, 39076, 38899, 15578, 36667, 5551, 23088, 32496, 5705, 23255, 25559, 11975, 44032, 45743, 23571, 30475, 15184, 41327, 15827, 33432, 37357, 40250, 16421, 2561, 8533, 25715, 17074, 36811, 30099, 44174, 8029, 1480, 43701, 10198, 38802, 13200, 31615, 28252, 17879, 18749, 16580, 19178, 48034, 4365, 4796, 46033, 47538, 7188, 45076, 13569, 28392, 19457, 41335, 4474, 23022, 11289, 25103, 35813, 40336, 12008, 36695, 28598, 12671, 48831, 18364, 9890, 11804, 37612, 31396, 10683, 31008, 36360, 15312, 26328, 41353, 34761, 4398, 46637, 13891, 32787, 22410, 26463, 4503, 31374, 26143, 7765, 27551, 15340, 16182, 7868, 42518, 34516, 8244, 13037, 39992, 14300, 48188, 42511, 2963, 28224, 28657, 5474, 19682, 682, 25867, 47518, 36303, 18452, 34447, 24821, 36157, 48089, 25120, 44689, 6509, 1852, 17387, 19405, 39441, 42197, 14298, 16443, 1151, 9775, 10834, 44482, 10445, 41434, 37644, 5702, 29159, 17097, 28308, 42161, 29973, 38602, 4592, 24411, 38792, 25200, 28299, 5522, 4441, 4065, 12187, 32012, 41361, 36098, 25224, 27204, 29536, 18785, 28218, 42361, 10437, 8978, 44209, 7804, 35232, 3041, 23251, 41265, 28139, 41350, 18536, 37181, 25352, 16787, 27537, 29568, 45681, 33891, 35667, 31031, 5795, 23494, 7658, 26711, 35750, 34571, 4852, 29601, 14492, 5318, 26987, 11839, 533, 29565, 16424, 43853, 34375, 26710, 37956, 34492, 46294, 12920, 7945, 29669, 14520, 36081, 14478, 37173, 19188, 40253, 23549, 741, 34309, 11001, 6995, 10899, 36881, 7002, 19049, 13388, 40737, 9210, 22684, 43970, 7048, 46803, 45248, 4726, 40534, 23790, 47216, 8585, 7880, 25042, 306, 11939, 45003, 12905, 4052, 45391, 28968, 19408, 6012, 7814, 27790, 10979, 2005, 32156, 16025, 23706, 8236, 24750, 39229, 6968, 7599, 32427, 48001, 12257, 6899, 36229, 19760, 30468, 32347, 15232, 17555, 34373, 1157, 22434, 38137, 3717, 38235, 41506, 10786, 3175, 48043, 24171, 29368, 39765, 16373, 22973, 42399, 32908, 35630, 28508, 29334, 37539, 45770, 29181, 10946, 18072, 18511, 47354, 31444, 42643, 4078, 45028, 45610, 35405, 33751, 7967, 4701, 13378, 48105, 22116, 20599, 45454, 7325, 11304, 12289, 46114, 8359, 41073, 22751, 19402, 8483, 45656, 5604, 9134, 35979, 19757, 43627, 35248, 23566, 727, 34909, 43560, 2888, 12158, 48248, 2094, 47190, 15295, 27629, 15047, 4402, 32595, 6538, 13474, 11538, 10736, 29892, 29786, 1884, 45940, 2144, 37537, 5222, 26418, 10690, 19114, 30223, 17188, 41379, 46182, 20359, 32256, 43739, 41935, 16411, 15933, 22295, 940, 8665, 1154, 32089, 46513, 17506, 39407, 6187, 7878, 37671, 25414, 16789, 37546, 44170, 9921, 22033, 33690, 23656, 5226, 1631, 8671, 45821, 34099, 40039, 31342, 35231, 29621, 31899, 1023, 17082, 38261, 26917, 31921, 5241, 37282, 45513, 46687, 18915, 10796, 8986, 31711, 2185, 29316, 45090, 13383, 5741, 7930, 39306, 13675, 38034, 29826, 48781, 21746, 39559, 31318, 19965, 25443, 45862, 30730, 9611, 43077, 23902, 9541, 38859, 13973, 27923, 25754, 38295, 39261, 15442, 40254, 28002, 23139, 44524, 11458, 10297, 25299, 13617, 28750, 1835, 29505, 23873, 45073, 34640, 5831, 29115, 26568, 6588, 31067, 15001, 4887, 27814, 17283, 23813, 43511, 14398, 13500, 7428, 11090, 11751, 36607, 9712, 43583, 45864, 39972, 14617, 3431, 26470, 33191, 18204, 24481, 28879, 43889, 15015, 36437, 12660, 37650, 405, 36212, 42818, 10677, 15723, 24514, 35518, 42654, 44052, 10218, 37297, 34741, 40715, 37290, 29931, 29774, 25075, 12136, 44466, 25236, 7096, 26190, 14575, 41698, 9068, 24101, 3379, 19906, 15856, 38317, 20799, 17172, 5987, 140, 11530, 38636, 9116, 11151, 25071, 182, 31603, 21547, 47739, 13909, 624, 25621, 30173, 37807, 7053, 30625, 10450, 22316, 23965, 5028, 37725, 1675, 45751, 19683, 26061, 34327, 38096, 30828, 438, 46574, 9121, 4859, 15563, 33935, 39481, 48048, 37730, 35947, 18461, 22658, 35939, 3507, 16223, 5279, 9615, 13583, 28557, 36129, 19326, 23956, 31469, 3397, 36813, 4416, 48955, 27367, 9692, 41380, 27998, 33372, 24467, 24186, 47802, 16612, 46008, 3943, 48514, 42699, 37077, 17401, 39288, 44878, 31226, 14334, 44847, 7473, 42669, 32658, 40101, 11309, 853, 12919, 41501, 26725, 3843, 41314, 16050, 39323, 5916, 19945, 17950, 48824, 8856, 12778, 28765, 13275, 34339, 8883, 36161, 41767, 44449, 7357, 3967, 41737, 3432, 27375, 5603, 1739, 2418, 23760, 26549, 2676, 11659, 40405, 46217, 5207, 28673, 12645, 45982, 48103, 21541, 33384, 28830, 46313, 2540, 17302, 42509, 2321, 40265, 21290, 35387, 48490, 11327, 16529, 40097, 16839, 12570, 17132, 18289, 20343, 22077, 21098, 5426, 8478, 1923, 4941, 48459, 34289, 38039, 44848, 20094, 25546, 19669, 32606, 16624, 28652, 11887, 22863, 48068, 9574, 39941, 2068, 28297, 7225, 41330, 47575, 30080, 25197, 25710, 18030, 16190, 21185, 46949, 1377, 47189, 30166, 28575, 12032, 14160, 11813, 48219, 39348, 42953, 46300, 5559, 15360, 14665, 25279, 42955, 43707, 10089, 10928, 16650, 18156, 4140, 2816, 45019, 25339, 16628, 3925, 25879, 43725, 33970, 17789, 20083, 8873, 41315, 45472, 40526, 4589, 44440, 3184, 4581, 16953, 7585, 45975, 28441, 10956, 22017, 21698, 2107, 44107, 45868, 30293, 15530, 26848, 45705, 811, 22587, 28712, 16591, 45100, 41182, 1225, 40805, 3915, 6545, 8556, 26652, 29708, 24040, 676, 8243, 42597, 17603, 3208, 38902, 15447, 8826, 14791, 38670, 37596, 42980, 17743, 44094, 23778, 32296, 43347, 20210, 6487, 33150, 5095, 35163, 3681, 42450, 21707, 13663, 37987, 13359, 10158, 24531, 21817, 39213, 29424, 38798, 32466, 37354, 27218, 12293, 4133, 14755, 38826, 23328, 48318, 22137, 28379, 35441, 1910, 31964, 26833, 13669, 7484, 43359, 48803, 6853, 47906, 25522, 42533, 16633, 38444, 39544, 13401, 36560, 47222, 1732, 10624, 45339, 24754, 9680, 47728, 4309, 20076, 32836]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 11.326788902282715})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 10.992145538330078})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 10.940470695495605})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 10.36453628540039})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 12.18789005279541})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 10.493444442749023})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 11.75367546081543})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.1592, 'crossentropy': 10.81040234375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 4.711835861206055})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 4.302168369293213})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 5.316157341003418})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 4.640557289123535})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 5.029726505279541})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 5.16046142578125})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 45892], ['ood', 64204], ['ood', 1451], ['ood', 36641], ['ood', 20063]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.8524844932813194, 1.5424790406714894, 2.157072820676898, 2.6727650403261376, 3.0413943172803544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 6.897332668304443})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 16.731555938720703})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 10.369363784790039})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 7.728503227233887})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.201, 'crossentropy': 7.3337453125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 4.543581962585449})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 3.7797951698303223})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 3.752588987350464})
store['active_learning_steps'][1]['eval_training']['best_epoch']=3
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 1841], ['ood', 2779], ['ood', 53865], ['ood', 38321], ['id', 28994]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9151951475373665, 1.475933964937015, 1.9336802021193749, 2.338647959583829, 2.6679006116390034]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 8.59365177154541})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 6.1916399002075195})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 5.940634727478027})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 7.029569149017334})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 5.905927658081055})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 5.328813552856445})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.2192, 'crossentropy': 6.42367890625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 3.6667656898498535})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.401059150695801})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.84187912940979})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 3.799527406692505})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 3.2017393112182617})
store['active_learning_steps'][2]['eval_training']['best_epoch']=2
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 29398], ['id', 7873], ['id', 32608], ['id', 19172], ['ood', 22791]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.8241268121179499, 1.3554217888524334, 1.8615063354421588, 2.2602995720474963, 2.562918846676019]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 7.794806957244873})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 4.874711036682129})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 6.378064155578613})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 6.404632568359375})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 7.7741851806640625})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.874026298522949})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.2215, 'crossentropy': 6.047312890625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 3.2551136016845703})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 3.1908421516418457})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 3.281168222427368})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 4.188344955444336})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.6570351123809814})
store['active_learning_steps'][3]['eval_training']['best_epoch']=5
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 43191], ['id', 6118], ['id', 19354], ['id', 37983], ['id', 13528]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7665535874558733, 1.3308146356880317, 1.8457275848049082, 2.2413423639792196, 2.5558350844436575]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 4.786484241485596})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 6.333368301391602})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 5.904226303100586})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 5.4470672607421875})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.2135, 'crossentropy': 4.76432421875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.0852975845336914})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 2.7922933101654053})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 2.781632900238037})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 9093], ['id', 38909], ['id', 34837], ['id', 41752], ['id', 33556]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6447412471101854, 1.238481041641434, 1.696721196868535, 2.1085703536845912, 2.4340344666836398]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 4.578510284423828})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 4.710365295410156})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 4.9812726974487305})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 5.243127346038818})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 4.7959184646606445})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.544040203094482})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.274247169494629})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 5.257519721984863})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 6.4832611083984375})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.849008560180664})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.964397430419922})
store['active_learning_steps'][5]['training']['best_epoch']=8
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.2209, 'crossentropy': 5.165765625}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 2.524433135986328})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 2.8272457122802734})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 2.8309035301208496})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.033531665802002})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 2.9128167629241943})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 3.259890079498291})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.142282724380493})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 3.224921226501465})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 3.103099822998047})
store['active_learning_steps'][5]['eval_training']['best_epoch']=6
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 27609], ['id', 38974], ['id', 44105], ['id', 6868], ['id', 46514]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6844693362311826, 1.2581851496956127, 1.759462254527536, 2.1383160132850296, 2.469374467511861]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 4.89243221282959})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 4.722956657409668})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 7.684271812438965})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.67702317237854})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 4.638705253601074})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.1994, 'crossentropy': 4.961075}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 3.0115184783935547})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 2.8112823963165283})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 2.9447007179260254})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 3.072392463684082})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 14191], ['id', 43296], ['id', 2960], ['ood', 58625], ['id', 26943]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4511273607278442, 0.8608397709883744, 1.2526842822110078, 1.5949369586859907, 1.8954706623492203]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 4.543670654296875})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 5.959392547607422})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 6.612491607666016})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 4.535520553588867})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 5.394885063171387})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.851348400115967})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.1997, 'crossentropy': 6.418627734375}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 2.996155023574829})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 3.329087734222412})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 3.0926294326782227})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 3.2867722511291504})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 3.8862791061401367})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 44844], ['id', 38651], ['id', 246], ['id', 16338], ['id', 29890]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6522247672719921, 1.2257016871226958, 1.736956429974438, 2.1761616359559426, 2.5221615578125416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 6.11437463760376})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 6.077466011047363})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 4.92268705368042})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 5.0243682861328125})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.664318084716797})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 3.7314491271972656})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 5.1207733154296875})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.0015411376953125})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 5.076753616333008})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.2475, 'crossentropy': 3.879937109375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 2.517982006072998})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 2.3444931507110596})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 2.257093906402588})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 2.6184568405151367})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.3581182956695557})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 2.299191474914551})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 2.501122236251831})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.417342185974121})
store['active_learning_steps'][8]['eval_training']['best_epoch']=6
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 32182], ['ood', 39125], ['id', 35827], ['id', 7633], ['id', 38225]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6124384388586936, 1.1092928887211544, 1.5400023550826476, 1.9159213116555582, 2.231411328190628]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 4.428112030029297})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.567436695098877})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.7476980686187744})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.21324348449707})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.1834, 'crossentropy': 4.533010546875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 2.6564245223999023})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 3.2735514640808105})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 2.9198169708251953})
store['active_learning_steps'][9]['eval_training']['best_epoch']=1
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 7758], ['id', 7189], ['id', 13883], ['id', 10517], ['id', 27111]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7701495793593398, 1.3071734747775419, 1.7254456212191074, 2.058276237572308, 2.3535708486639475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 4.523638725280762})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 6.17579984664917})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 4.445230007171631})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.951752662658691})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.72634744644165})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.290802955627441})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 5.612014293670654})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 4.337034225463867})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 8.544593811035156})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.231, 'crossentropy': 5.34159140625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 2.583385944366455})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 2.5134623050689697})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 2.876251697540283})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 3.0408849716186523})
store['active_learning_steps'][10]['eval_training']['best_epoch']=1
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 2012], ['id', 577], ['id', 42224], ['id', 35826], ['id', 17715]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5642000547890997, 1.1219187843092557, 1.58743984712628, 1.978707617341116, 2.310670972436067]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 3.311814785003662})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.740229845046997})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 4.368422508239746})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.012043476104736})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 5.233058929443359})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 4.927460670471191})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.29886531829834})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.11317777633667})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.2497, 'crossentropy': 5.266292578125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 2.7379820346832275})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 2.6270904541015625})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 2.769913673400879})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 2.8986191749572754})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 2.7340221405029297})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 2.8455491065979004})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.9157609939575195})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 34315], ['id', 19470], ['id', 2229], ['id', 13081], ['id', 110]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6279273915156771, 1.1387249291669903, 1.5619619614228117, 1.939839506504402, 2.2439020370048324]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 4.833502769470215})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 3.5091488361358643})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.297351360321045})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 4.392535209655762})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 4.527827262878418})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.528101921081543})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 5.358570098876953})
store['active_learning_steps'][12]['training']['best_epoch']=4
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.2835, 'crossentropy': 4.63249921875}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 2.320181369781494})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 2.395704984664917})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 2.708728075027466})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 2.451651096343994})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.310546875, 'crossentropy': 2.477447986602783})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 2.667450189590454})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 2601], ['id', 5948], ['id', 1496], ['id', 23449], ['id', 14948]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5700525512358487, 1.0765342682215149, 1.4742964506868743, 1.8241156317096925, 2.117827996348515]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.4304654598236084})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 3.7709250450134277})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 4.42364501953125})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.658901214599609})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.2421, 'crossentropy': 3.543024609375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.0364115238189697})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 2.9110500812530518})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 2.9271931648254395})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 3235], ['id', 4396], ['id', 39753], ['id', 36449], ['id', 41406]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.46977292702159357, 0.9084891490392282, 1.2546750577825923, 1.5569776914372717, 1.798519575791314]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 3.9053025245666504})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 3.879305362701416})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 3.8986620903015137})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 5.595549583435059})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 3.9055771827697754})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 4.2463250160217285})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 4.565913200378418})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 5.939399719238281})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 5.191768646240234})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 4.891761779785156})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.2592, 'crossentropy': 4.86255859375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.4348225593566895})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 2.4775781631469727})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 2.8715121746063232})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 2.423478126525879})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 2.7610716819763184})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.6788582801818848})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.7625679969787598})
store['active_learning_steps'][14]['eval_training']['best_epoch']=4
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 31889], ['id', 36093], ['id', 25823], ['id', 23118], ['id', 36686]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5241741312753825, 0.9645498868865707, 1.3659572488759917, 1.6906667297497542, 1.9802607565529495]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.231344699859619})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.652520179748535})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.31655216217041})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.693618297576904})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.4691691398620605})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 4.396256446838379})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 5.117762565612793})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 4.940173149108887})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 5.8624420166015625})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.2612, 'crossentropy': 4.53323828125}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 2.7041540145874023})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.3733038902282715})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.6427173614501953})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.6393675804138184})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 2.4493465423583984})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.665146827697754})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.700813055038452})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 2.5910239219665527})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 15076], ['id', 673], ['id', 25530], ['id', 16538], ['id', 8938]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7162216113698425, 1.229671686558858, 1.6660245408381096, 2.0375837467853977, 2.3622143894299397]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 3.313581943511963})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 5.51534366607666})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 3.438546895980835})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.804248094558716})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 5.88810920715332})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 5.789806842803955})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 4.7039690017700195})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.617926597595215})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 5.203503608703613})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 5.617072105407715})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.2684, 'crossentropy': 4.833716015625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 2.446699619293213})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 2.5264339447021484})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 2.463008165359497})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.5562491416931152})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 2.7665257453918457})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.6309051513671875})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.6240644454956055})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 2.978656053543091})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 2.7852890491485596})
store['active_learning_steps'][16]['eval_training']['best_epoch']=8
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 4275], ['id', 37886], ['ood', 58219], ['id', 2324], ['ood', 39412]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6383903395713446, 1.1195068537436965, 1.5873577004261512, 1.9593159947824574, 2.2954511736275514]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.4423751831054688})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.03176212310791})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 4.532924652099609})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 4.188237190246582})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 4.253792762756348})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 3.818284511566162})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 6.089458465576172})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 5.213791370391846})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 4.887543678283691})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.2638, 'crossentropy': 3.744598828125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 2.3804125785827637})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 2.3735568523406982})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 2.4622693061828613})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 2.471332550048828})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 2.3836541175842285})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 2.3355259895324707})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 2.593212366104126})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 2.5948030948638916})
store['active_learning_steps'][17]['eval_training']['best_epoch']=6
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 24450], ['id', 7709], ['id', 33626], ['id', 48813], ['id', 12412]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4634383147144385, 0.9101683527354427, 1.3067657344153671, 1.6531284873250174, 1.9652684454089258]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 3.2314634323120117})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 4.57280158996582})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.907524108886719})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 6.430768013000488})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.635593414306641})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.018311500549316})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.2698, 'crossentropy': 5.044448828125}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.4881443977355957})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 3.0902113914489746})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 2.5509145259857178})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 2.737091064453125})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.6460347175598145})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 18465], ['id', 20046], ['id', 39757], ['id', 33068], ['id', 43886]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5968350951097467, 1.0201061621126284, 1.4150239718244362, 1.7381985429944358, 2.0134480916192032]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.2229766845703125})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.04539155960083})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 4.045910835266113})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 4.317436695098877})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 4.743846893310547})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 3.963730812072754})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.872261047363281})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.694684982299805})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.271, 'crossentropy': 4.92440859375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 2.5163052082061768})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.506622314453125})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.5077648162841797})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 2.4481985569000244})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 2.5568182468414307})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 2.794451951980591})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 3.0627756118774414})
store['active_learning_steps'][19]['eval_training']['best_epoch']=7
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 11124], ['id', 17607], ['id', 43664], ['id', 11121], ['id', 10586]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6155392732465423, 1.1514716990026987, 1.582810251169183, 1.9155580595694026, 2.1992429139793854]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 3.8224234580993652})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 4.445029258728027})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 4.827386856079102})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 4.155740737915039})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 4.880449295043945})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.869683742523193})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.653120040893555})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 5.704126358032227})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 4.4386186599731445})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 5.166536331176758})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 5.306103706359863})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.972563743591309})
store['active_learning_steps'][20]['training']['best_epoch']=9
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.2619, 'crossentropy': 4.749233203125}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 2.493116855621338})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 2.222257137298584})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 2.8972840309143066})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.8367843627929688})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 2.6013479232788086})
store['active_learning_steps'][20]['eval_training']['best_epoch']=2
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 22594], ['id', 18259], ['id', 22322], ['id', 42377], ['id', 36178]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5387220901203943, 1.055235995995854, 1.5289853210854036, 1.954459533941515, 2.3083682801920293]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.266336441040039})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 3.1081326007843018})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 3.116311550140381})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.018925189971924})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 4.053895950317383})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 4.7934770584106445})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.2787, 'crossentropy': 3.2245564453125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 2.26896071434021})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 2.2822370529174805})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 2.3453288078308105})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 2.25727915763855})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 2.3491740226745605})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 2297], ['id', 30101], ['id', 22508], ['id', 28995], ['id', 25186]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.3990669056684225, 0.714006073899677, 0.9869355988092381, 1.2311788701573452, 1.4564812460321406]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 3.195258855819702})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 2.6078720092773438})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 3.477431297302246})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 5.0754899978637695})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 4.6457014083862305})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 6.197335720062256})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 3.7360117435455322})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 5.198386192321777})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 4.276859283447266})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 5.149958610534668})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.2726, 'crossentropy': 3.57443984375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 2.185875415802002})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 2.4587645530700684})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 2.2776854038238525})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.3859429359436035})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.4364700317382812})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 2.649550199508667})
store['active_learning_steps'][22]['eval_training']['best_epoch']=3
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 38061], ['id', 10478], ['id', 2316], ['id', 25067], ['id', 25325]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5569154009744599, 1.0337107791024644, 1.4447023101352237, 1.7990761671094022, 2.1013003415816645]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.175232410430908})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 4.118579864501953})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 3.5639686584472656})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 3.7485718727111816})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.524406433105469})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 4.644194602966309})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 4.655793190002441})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.660859107971191})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 6.2642412185668945})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 4.3227386474609375})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 4.9085693359375})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 4.158985614776611})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 5.211434364318848})
store['active_learning_steps'][23]['training']['best_epoch']=10
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.2969, 'crossentropy': 4.442428125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 2.611395835876465})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 2.3063175678253174})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 2.4958651065826416})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.30078125, 'crossentropy': 2.4223904609680176})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 2.75258731842041})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 2.574087142944336})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.3125, 'crossentropy': 2.509843349456787})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 2.552438497543335})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 2.736143112182617})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 2.674307346343994})
store['active_learning_steps'][23]['eval_training']['best_epoch']=7
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 26074], ['id', 16131], ['id', 1946], ['id', 44494], ['id', 10583]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5808477311912481, 1.1328440730160918, 1.5929451098459744, 1.9360722698418176, 2.2351435091895855]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 2.7296392917633057})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 4.190855979919434})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 4.100536346435547})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 3.8307833671569824})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 3.18917179107666})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 4.322523593902588})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 4.315853595733643})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.318359375, 'crossentropy': 4.031667232513428})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 4.391253471374512})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 4.921576499938965})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.30078125, 'crossentropy': 4.0056610107421875})
store['active_learning_steps'][24]['training']['best_epoch']=8
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.3123, 'crossentropy': 4.058821875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 2.2881689071655273})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 2.256382465362549})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 2.321981430053711})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.33984375, 'crossentropy': 2.215955972671509})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.333984375, 'crossentropy': 2.290726661682129})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.32421875, 'crossentropy': 2.410372257232666})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.337890625, 'crossentropy': 2.4534356594085693})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 24400], ['id', 6170], ['id', 7851], ['id', 31443], ['id', 47720]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5481493980929104, 1.0011197394154823, 1.390899990496988, 1.7400228167961895, 2.044381816061037]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 2.7758264541625977})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 3.3177647590637207})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 3.6565256118774414})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 3.8429479598999023})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 4.109666347503662})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 3.431471824645996})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 4.02428674697876})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.2839, 'crossentropy': 4.068589453125}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 2.877980947494507})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 2.2456719875335693})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 2.445633888244629})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 2.515350818634033})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 2.4843058586120605})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.3291015625, 'crossentropy': 2.3032944202423096})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 31544], ['id', 2726], ['id', 7544], ['id', 17533], ['id', 24353]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.49683391740977784, 0.9049866646514614, 1.2555656297069797, 1.580114686281209, 1.8674887959823945]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 2.894587278366089})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 3.0174248218536377})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 4.359533309936523})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.056221008300781})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 4.74346923828125})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 4.474179267883301})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 4.234375953674316})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 4.346621513366699})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.3067, 'crossentropy': 4.85115859375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 2.370777130126953})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 2.860671281814575})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 2.3442530632019043})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 2.484520196914673})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 2.863271951675415})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.721769332885742})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 2.649719715118408})
store['active_learning_steps'][26]['eval_training']['best_epoch']=5
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 34642], ['id', 34046], ['id', 28333], ['id', 26271], ['id', 15774]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6668576863259814, 1.1183307313907727, 1.547613352093653, 1.9309642198434913, 2.26241932303577]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 2.798905849456787})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.090145587921143})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 3.5192034244537354})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 3.7968978881835938})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 4.92718505859375})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 3.213517665863037})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 6.298898696899414})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.2974, 'crossentropy': 3.71770546875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 2.2129530906677246})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.268505334854126})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.642423152923584})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 2.361663341522217})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 2.522642135620117})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 2.2626898288726807})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 27500], ['id', 39451], ['ood', 20033], ['id', 28735], ['id', 40038]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.473111284934167, 0.8897419925978141, 1.2415884282306298, 1.5616748251207717, 1.8523086837502234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 2.474733352661133})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 2.74757981300354})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.31640625, 'crossentropy': 3.3209400177001953})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 4.82391357421875})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 4.106400012969971})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 4.004251480102539})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.3006, 'crossentropy': 3.287655859375}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 2.6176095008850098})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 2.300199508666992})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.2557168006896973})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 2.513749122619629})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 2.6023800373077393})
store['active_learning_steps'][28]['eval_training']['best_epoch']=5
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 24970], ['id', 35669], ['id', 14715], ['id', 48925], ['id', 26214]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.35807368919469806, 0.6915159148399554, 0.9677842661310643, 1.2232977697930085, 1.4590020202253289]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 2.391125202178955})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 3.0285606384277344})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 3.1432909965515137})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 3.523097038269043})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.30859375, 'crossentropy': 4.4349365234375})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 4.222857475280762})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 4.227358818054199})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 4.965399265289307})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.3134, 'crossentropy': 4.366716796875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 2.3523101806640625})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.3134765625, 'crossentropy': 2.04349422454834})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 2.762789487838745})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 3.000288963317871})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.3212890625, 'crossentropy': 2.583005428314209})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.322265625, 'crossentropy': 2.4743452072143555})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 2.4831955432891846})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 1062], ['id', 21082], ['id', 35386], ['id', 11103], ['id', 22737]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6403701309701677, 1.1017583083013611, 1.4911979341165984, 1.827161598719223, 2.1181959632905514]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 2.5502731800079346})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 2.7481236457824707})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 2.732677936553955})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.017709255218506})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 3.295292615890503})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 3.222809314727783})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.8557872772216797})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 4.415622711181641})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.2585, 'crossentropy': 3.440053515625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 2.302962064743042})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 2.21612286567688})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.5359058380126953})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 2.2385048866271973})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 2.286294460296631})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 2.3886184692382812})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 2.4353270530700684})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 36782], ['id', 19467], ['id', 37767], ['id', 1338], ['id', 32425]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.3952332762690538, 0.738478182256145, 1.058019656230703, 1.3358369443885767, 1.6006822494974289]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.480006694793701})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 3.675069808959961})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 2.9825658798217773})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 3.516176223754883})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 3.674010753631592})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 3.747641086578369})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 4.13217830657959})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.710870742797852})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 4.952033042907715})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.3001, 'crossentropy': 3.816016796875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 2.3958637714385986})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.6488215923309326})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 2.470676898956299})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 2.3750743865966797})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 2.531254768371582})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 2.4484167098999023})
store['active_learning_steps'][31]['eval_training']['best_epoch']=3
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 47113], ['id', 8947], ['id', 7024], ['id', 22705], ['id', 26441]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5088250180964107, 0.9422466761080595, 1.3325653040636354, 1.6403252187336488, 1.9175369246408742]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 2.4744787216186523})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 2.8212273120880127})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.6058847904205322})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 3.306475877761841})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 4.268000602722168})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 4.00686502456665})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 3.622098922729492})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.3118, 'crossentropy': 3.143291015625}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.222477674484253})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 2.4823899269104004})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 2.346919536590576})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.383913516998291})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 2.2389631271362305})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 2.325456380844116})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 15436], ['id', 16739], ['id', 45246], ['id', 24573], ['id', 40356]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4276333838992987, 0.7975454173703462, 1.15071009810227, 1.4484686074216926, 1.699014298354375]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 2.5751633644104004})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 3.7931342124938965})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 2.9711859226226807})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 2.8769023418426514})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 3.752216339111328})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.3095703125, 'crossentropy': 3.742340564727783})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 4.7394514083862305})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 4.082197189331055})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 5.204771995544434})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.3246, 'crossentropy': 3.72464140625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 2.21728515625})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 2.1910033226013184})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 2.5028252601623535})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 2.3348989486694336})
store['active_learning_steps'][33]['eval_training']['best_epoch']=1
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 622], ['id', 6137], ['id', 37971], ['id', 35343], ['id', 37951]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.46395135622673167, 0.8998944414039785, 1.3026116629576285, 1.6547929312922243, 1.962248317821424]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 2.994480609893799})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.2321417331695557})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.9989030361175537})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 3.3437023162841797})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 3.1829607486724854})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 3.1684751510620117})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 3.5300168991088867})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.314453125, 'crossentropy': 3.317594051361084})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.3125, 'crossentropy': 3.740212917327881})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 5.598407745361328})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 4.232850074768066})
store['active_learning_steps'][34]['training']['best_epoch']=8
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.3164, 'crossentropy': 3.4381875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 2.4228827953338623})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 2.2337417602539062})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.314453125, 'crossentropy': 2.2603843212127686})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 2.7950022220611572})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 2.342968463897705})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 2.270451545715332})
store['active_learning_steps'][34]['eval_training']['best_epoch']=3
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 46933], ['id', 5905], ['ood', 8608], ['id', 22530], ['id', 5254]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.49592671961432006, 0.9066986629084313, 1.2926315158438042, 1.6357035648574083, 1.9278007733113798]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 2.6527209281921387})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 2.2763895988464355})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 2.3231892585754395})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 3.898463726043701})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 3.866507053375244})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 3.1393113136291504})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.3427734375, 'crossentropy': 3.235783100128174})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 5.0271501541137695})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.314453125, 'crossentropy': 3.8306069374084473})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.3291015625, 'crossentropy': 4.162691116333008})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.3331, 'crossentropy': 3.2502150390625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 2.9584033489227295})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 2.3727564811706543})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.316802501678467})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.3154296875, 'crossentropy': 2.4666852951049805})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 2.182220935821533})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.31640625, 'crossentropy': 2.2414777278900146})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.3359375, 'crossentropy': 2.1500511169433594})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.3486328125, 'crossentropy': 2.282461166381836})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.3623046875, 'crossentropy': 2.2953391075134277})
store['active_learning_steps'][35]['eval_training']['best_epoch']=9
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 54863], ['id', 47654], ['id', 33845], ['id', 11994], ['id', 33866]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.48742071991924374, 0.9578436185874017, 1.3567383577144954, 1.693204495421174, 1.9936971663610041]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 2.7443130016326904})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.613187789916992})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 3.0488550662994385})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 4.339969635009766})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 4.156983852386475})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.2588491439819336})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 5.381900787353516})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 3.8166146278381348})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.2978, 'crossentropy': 4.05531015625}
