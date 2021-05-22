store = {}
store['timestamp']=1621617447
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=18']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=18
store['worker_id']=18
store['num_workers']=24
store['config']={'seed': 1254, 'uniform_ood': False, 'id_dataset_name': 'CIFAR-10', 'ood_dataset_name': 'SVHN', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node) + ('SVHN (Train, seed=0, 73257 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'CIFAR-10 (Test)'"}
store['initial_training_set_indices']=[12980, 44617, 6984, 21168, 33976, 35571, 33058, 43729, 26944, 24745, 66, 14046, 46542, 39478, 6000, 5915, 39360, 20774, 27084, 44464]
store['evaluation_set_indices']=[3812, 42704, 6729, 38942, 48125, 16968, 5652, 4045, 10740, 19606, 37062, 15768, 44824, 47581, 19482, 4628, 25290, 27933, 27441, 5508, 35131, 18717, 43561, 37318, 8187, 37590, 45717, 1493, 5924, 19803, 23554, 6460, 2962, 36049, 18273, 11023, 27366, 39007, 5305, 46743, 15798, 44136, 20072, 20717, 1152, 8194, 36500, 17618, 35054, 18973, 45734, 16753, 6410, 28807, 8902, 20957, 6625, 41155, 1332, 47376, 36719, 11500, 36383, 7417, 30371, 19517, 33334, 27185, 29033, 42916, 39943, 34789, 18504, 7348, 6096, 28402, 10058, 12011, 34663, 1618, 17887, 41306, 1467, 28071, 12667, 38339, 44920, 44374, 14769, 31145, 21575, 16685, 24836, 48736, 21176, 26844, 45671, 22164, 42503, 10770, 27020, 30182, 37164, 33354, 47307, 17878, 26665, 40819, 14805, 201, 47956, 44739, 8060, 45495, 8139, 27034, 40800, 21802, 18878, 8672, 41175, 48917, 23272, 9952, 23154, 37915, 18669, 18159, 13468, 14436, 16099, 8128, 33349, 31445, 7202, 21948, 10215, 34670, 538, 40015, 17530, 11133, 6028, 12100, 21106, 5614, 30720, 34210, 39322, 40006, 31808, 24717, 34090, 17381, 18164, 17668, 16984, 37856, 41017, 43216, 46788, 26334, 6887, 40485, 39838, 1931, 47231, 37148, 801, 14067, 31951, 7105, 34561, 18698, 45258, 21399, 18558, 26959, 17240, 30502, 39056, 47625, 18880, 37323, 26204, 21788, 1674, 47188, 10526, 25980, 27994, 19871, 22250, 38761, 7182, 14241, 235, 37616, 39973, 35218, 46446, 33361, 39076, 38899, 15578, 36667, 5551, 23088, 32496, 5705, 23255, 25559, 11975, 44032, 45743, 23571, 30475, 15184, 41327, 15827, 33432, 37357, 40250, 16421, 2561, 8533, 25715, 17074, 36811, 30099, 44174, 8029, 1480, 43701, 10198, 38802, 13200, 31615, 28252, 17879, 18749, 16580, 19178, 48034, 4365, 4796, 46033, 47538, 7188, 45076, 13569, 28392, 19457, 41335, 4474, 23022, 11289, 25103, 35813, 40336, 12008, 36695, 28598, 12671, 48831, 18364, 9890, 11804, 37612, 31396, 10683, 31008, 36360, 15312, 26328, 41353, 34761, 4398, 46637, 13891, 32787, 22410, 26463, 4503, 31374, 26143, 7765, 27551, 15340, 16182, 7868, 42518, 34516, 8244, 13037, 39992, 14300, 48188, 42511, 2963, 28224, 28657, 5474, 19682, 682, 25867, 47518, 36303, 18452, 34447, 24821, 36157, 48089, 25120, 44689, 6509, 1852, 17387, 19405, 39441, 42197, 14298, 16443, 1151, 9775, 10834, 44482, 10445, 41434, 37644, 5702, 29159, 17097, 28308, 42161, 29973, 38602, 4592, 24411, 38792, 25200, 28299, 5522, 4441, 4065, 12187, 32012, 41361, 36098, 25224, 27204, 29536, 18785, 28218, 42361, 10437, 8978, 44209, 7804, 35232, 3041, 23251, 41265, 28139, 41350, 18536, 37181, 25352, 16787, 27537, 29568, 45681, 33891, 35667, 31031, 5795, 23494, 7658, 26711, 35750, 34571, 4852, 29601, 14492, 5318, 26987, 11839, 533, 29565, 16424, 43853, 34375, 26710, 37956, 34492, 46294, 12920, 7945, 29669, 14520, 36081, 14478, 37173, 19188, 40253, 23549, 741, 34309, 11001, 6995, 10899, 36881, 7002, 19049, 13388, 40737, 9210, 22684, 43970, 7048, 46803, 45248, 4726, 40534, 23790, 47216, 8585, 7880, 25042, 306, 11939, 45003, 12905, 4052, 45391, 28968, 19408, 6012, 7814, 27790, 10979, 2005, 32156, 16025, 23706, 8236, 24750, 39229, 6968, 7599, 32427, 48001, 12257, 6899, 36229, 19760, 30468, 32347, 15232, 17555, 34373, 1157, 22434, 38137, 3717, 38235, 41506, 10786, 3175, 48043, 24171, 29368, 39765, 16373, 22973, 42399, 32908, 35630, 28508, 29334, 37539, 45770, 29181, 10946, 18072, 18511, 47354, 31444, 42643, 4078, 45028, 45610, 35405, 33751, 7967, 4701, 13378, 48105, 22116, 20599, 45454, 7325, 11304, 12289, 46114, 8359, 41073, 22751, 19402, 8483, 45656, 5604, 9134, 35979, 19757, 43627, 35248, 23566, 727, 34909, 43560, 2888, 12158, 48248, 2094, 47190, 15295, 27629, 15047, 4402, 32595, 6538, 13474, 11538, 10736, 29892, 29786, 1884, 45940, 2144, 37537, 5222, 26418, 10690, 19114, 30223, 17188, 41379, 46182, 20359, 32256, 43739, 41935, 16411, 15933, 22295, 940, 8665, 1154, 32089, 46513, 17506, 39407, 6187, 7878, 37671, 25414, 16789, 37546, 44170, 9921, 22033, 33690, 23656, 5226, 1631, 8671, 45821, 34099, 40039, 31342, 35231, 29621, 31899, 1023, 17082, 38261, 26917, 31921, 5241, 37282, 45513, 46687, 18915, 10796, 8986, 31711, 2185, 29316, 45090, 13383, 5741, 7930, 39306, 13675, 38034, 29826, 48781, 21746, 39559, 31318, 19965, 25443, 45862, 30730, 9611, 43077, 23902, 9541, 38859, 13973, 27923, 25754, 38295, 39261, 15442, 40254, 28002, 23139, 44524, 11458, 10297, 25299, 13617, 28750, 1835, 29505, 23873, 45073, 34640, 5831, 29115, 26568, 6588, 31067, 15001, 4887, 27814, 17283, 23813, 43511, 14398, 13500, 7428, 11090, 11751, 36607, 9712, 43583, 45864, 39972, 14617, 3431, 26470, 33191, 18204, 24481, 28879, 43889, 15015, 36437, 12660, 37650, 405, 36212, 42818, 10677, 15723, 24514, 35518, 42654, 44052, 10218, 37297, 34741, 40715, 37290, 29931, 29774, 25075, 12136, 44466, 25236, 7096, 26190, 14575, 41698, 9068, 24101, 3379, 19906, 15856, 38317, 20799, 17172, 5987, 140, 11530, 38636, 9116, 11151, 25071, 182, 31603, 21547, 47739, 13909, 624, 25621, 30173, 37807, 7053, 30625, 10450, 22316, 23965, 5028, 37725, 1675, 45751, 19683, 26061, 34327, 38096, 30828, 438, 46574, 9121, 4859, 15563, 33935, 39481, 48048, 37730, 35947, 18461, 22658, 35939, 3507, 16223, 5279, 9615, 13583, 28557, 36129, 19326, 23956, 31469, 3397, 36813, 4416, 48955, 27367, 9692, 41380, 27998, 33372, 24467, 24186, 47802, 16612, 46008, 3943, 48514, 42699, 37077, 17401, 39288, 44878, 31226, 14334, 44847, 7473, 42669, 32658, 40101, 11309, 853, 12919, 41501, 26725, 3843, 41314, 16050, 39323, 5916, 19945, 17950, 48824, 8856, 12778, 28765, 13275, 34339, 8883, 36161, 41767, 44449, 7357, 3967, 41737, 3432, 27375, 5603, 1739, 2418, 23760, 26549, 2676, 11659, 40405, 46217, 5207, 28673, 12645, 45982, 48103, 21541, 33384, 28830, 46313, 2540, 17302, 42509, 2321, 40265, 21290, 35387, 48490, 11327, 16529, 40097, 16839, 12570, 17132, 18289, 20343, 22077, 21098, 5426, 8478, 1923, 4941, 48459, 34289, 38039, 44848, 20094, 25546, 19669, 32606, 16624, 28652, 11887, 22863, 48068, 9574, 39941, 2068, 28297, 7225, 41330, 47575, 30080, 25197, 25710, 18030, 16190, 21185, 46949, 1377, 47189, 30166, 28575, 12032, 14160, 11813, 48219, 39348, 42953, 46300, 5559, 15360, 14665, 25279, 42955, 43707, 10089, 10928, 16650, 18156, 4140, 2816, 45019, 25339, 16628, 3925, 25879, 43725, 33970, 17789, 20083, 8873, 41315, 45472, 40526, 4589, 44440, 3184, 4581, 16953, 7585, 45975, 28441, 10956, 22017, 21698, 2107, 44107, 45868, 30293, 15530, 26848, 45705, 811, 22587, 28712, 16591, 45100, 41182, 1225, 40805, 3915, 6545, 8556, 26652, 29708, 24040, 676, 8243, 42597, 17603, 3208, 38902, 15447, 8826, 14791, 38670, 37596, 42980, 17743, 44094, 23778, 32296, 43347, 20210, 6487, 33150, 5095, 35163, 3681, 42450, 21707, 13663, 37987, 13359, 10158, 24531, 21817, 39213, 29424, 38798, 32466, 37354, 27218, 12293, 4133, 14755, 38826, 23328, 48318, 22137, 28379, 35441, 1910, 31964, 26833, 13669, 7484, 43359, 48803, 6853, 47906, 25522, 42533, 16633, 38444, 39544, 13401, 36560, 47222, 1732, 10624, 45339, 24754, 9680, 47728, 4309, 20076, 32836]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 12.199417114257812})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 10.372478485107422})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 9.631608963012695})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 10.012638092041016})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 10.574983596801758})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.2037, 'crossentropy': 10.2993328125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 3.8077611923217773})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 4.196352481842041})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 4.111441612243652})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 4.936849117279053})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 37116], ['ood', 17808], ['ood', 32151], ['id', 40689], ['id', 39998]], 'labels': [-1, -1, -1, 4, 6], 'scores': [0.8079976589600782, 1.4363963148416872, 1.9462666161919477, 2.3473532239291135, 2.6668922943718627]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 14.973114013671875})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 8.631731033325195})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 9.954360961914062})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 10.426169395446777})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 12.134349822998047})
store['active_learning_steps'][1]['training']['best_epoch']=2
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.1891, 'crossentropy': 8.923165625}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 3.3193297386169434})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 3.8786940574645996})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 3.6066741943359375})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.8327012062072754})
store['active_learning_steps'][1]['eval_training']['best_epoch']=4
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 3657], ['id', 43809], ['id', 36535], ['ood', 47469], ['id', 8606]], 'labels': [-1, 8, 5, -1, 0], 'scores': [0.6361335813429112, 1.1227110352487535, 1.5868752378780226, 1.9796917962133032, 2.3056132820846864]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 10.61620044708252})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 8.467437744140625})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 12.403289794921875})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 9.675333023071289})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 9.022148132324219})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 9.054435729980469})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 10.481225967407227})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 10.82650375366211})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 9.015804290771484})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 11.208673477172852})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 10.633831024169922})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 11.121681213378906})
store['active_learning_steps'][2]['training']['best_epoch']=9
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.2174, 'crossentropy': 9.27767421875}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 3.4400923252105713})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 4.392098426818848})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.5084333419799805})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.893364429473877})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 3.6248128414154053})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 4.15421724319458})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 19586], ['id', 2840], ['id', 341], ['ood', 4304], ['id', 17620]], 'labels': [-1, 9, 8, -1, 1], 'scores': [0.863881194580622, 1.5569474045471794, 2.178701790070902, 2.6010899593893564, 2.919517702278908]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 8.477336883544922})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 9.625330924987793})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 8.158651351928711})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 9.449217796325684})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.2032, 'crossentropy': 8.748953125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 4.159167289733887})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.7928404808044434})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 3.5453381538391113})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 23100], ['ood', 34218], ['id', 48345], ['id', 12199], ['ood', 54100]], 'labels': [2, -1, 3, 7, -1], 'scores': [0.844736186619168, 1.5828617224555508, 2.0306380853992643, 2.4179499067194286, 2.742012812382696]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 5.88950777053833})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 8.775684356689453})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 8.627634048461914})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 8.047612190246582})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 9.191094398498535})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 7.456722736358643})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 8.264198303222656})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.1968, 'crossentropy': 8.18540390625}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 4.096687316894531})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 4.013547897338867})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.902193307876587})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.6553990840911865})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 3.7715911865234375})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 3.7359800338745117})
store['active_learning_steps'][4]['eval_training']['best_epoch']=4
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 22788], ['id', 23908], ['ood', 55021], ['ood', 64387], ['id', 8016]], 'labels': [-1, 6, -1, -1, 4], 'scores': [0.6243632893677287, 1.1484729479140463, 1.6176887192109715, 2.035616095824664, 2.3696969204581775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.443559169769287})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 8.748771667480469})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 8.052678108215332})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 7.1394805908203125})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 8.16545295715332})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 8.306529998779297})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.2192, 'crossentropy': 7.9387609375}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 3.8940389156341553})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 3.7237708568573})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 4.005688190460205})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.771389961242676})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 3.6878304481506348})
store['active_learning_steps'][5]['eval_training']['best_epoch']=5
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 63723], ['ood', 72863], ['ood', 20252], ['ood', 22175], ['id', 35777]], 'labels': [-1, -1, -1, -1, 1], 'scores': [0.6800387700120618, 1.2823450751718846, 1.7968683862027952, 2.234550072819615, 2.582465969564579]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 14.530399322509766})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 10.084552764892578})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 8.33755874633789})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 8.924751281738281})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 7.976204872131348})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 8.168304443359375})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.2314, 'crossentropy': 8.5164671875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.835031747817993})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 3.35066556930542})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 3.96567702293396})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 4.323941707611084})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 3.9142494201660156})
store['active_learning_steps'][6]['eval_training']['best_epoch']=2
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 45958], ['ood', 33776], ['ood', 36436], ['id', 38932], ['ood', 22760]], 'labels': [2, -1, -1, 0, -1], 'scores': [0.5604258259025652, 1.095692212708882, 1.5755249921155916, 1.9836500352812285, 2.2980079795163295]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 6.588850498199463})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 8.790571212768555})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 6.716108322143555})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 6.94663143157959})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 7.61876106262207})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 8.101907730102539})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 10.291749954223633})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 6.638614654541016})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.2354, 'crossentropy': 7.8239765625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.451153516769409})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 3.9447200298309326})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.469827175140381})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 3.540147542953491})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.4826507568359375})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 3.837761878967285})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 3.7872543334960938})
store['active_learning_steps'][7]['eval_training']['best_epoch']=6
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 44910], ['id', 44154], ['id', 30525], ['ood', 26524], ['ood', 27299]], 'labels': [-1, 2, 4, -1, -1], 'scores': [0.5446938956875045, 1.0690009796716866, 1.5512909200183391, 1.9553691555305734, 2.3012087268212333]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 6.067960739135742})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 6.294795989990234})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 7.70026969909668})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 8.394916534423828})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 6.831853866577148})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 9.867374420166016})
store['active_learning_steps'][8]['training']['best_epoch']=3
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.222, 'crossentropy': 7.86384296875}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 3.1696839332580566})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 3.769190788269043})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.6764864921569824})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 3.802461624145508})
store['active_learning_steps'][8]['eval_training']['best_epoch']=1
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 59372], ['id', 48769], ['id', 34229], ['ood', 12126], ['id', 48677]], 'labels': [-1, 8, 2, -1, 6], 'scores': [0.5162020006646357, 0.9862337896482041, 1.426364707518796, 1.7974433610835003, 2.1464054341500987]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 6.5488739013671875})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 7.137679100036621})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 6.801753997802734})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 7.639559745788574})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 7.86197566986084})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 10.503223419189453})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 7.33352518081665})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 8.942558288574219})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 9.5947265625})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 8.569197654724121})
store['active_learning_steps'][9]['training']['best_epoch']=7
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.2307, 'crossentropy': 7.3370421875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 3.5086886882781982})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 3.267988920211792})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.0921363830566406})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 3.641443967819214})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 3.4461278915405273})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.769339084625244})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.512836456298828})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 3.864138126373291})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 27712], ['id', 21613], ['id', 27400], ['ood', 23345], ['ood', 30820]], 'labels': [3, 2, 3, -1, -1], 'scores': [0.7027640060424146, 1.3152986684300543, 1.8184119473613256, 2.250761550183321, 2.6125541117558013]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 7.561347961425781})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 7.1451416015625})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 7.238228797912598})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 6.864951133728027})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 7.19412899017334})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 6.947330951690674})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 6.412225723266602})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 6.161086082458496})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 8.577587127685547})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 7.288016319274902})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 9.18984603881836})
store['active_learning_steps'][10]['training']['best_epoch']=8
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.2579, 'crossentropy': 6.543589453125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 3.0997819900512695})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 2.8725767135620117})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.271501064300537})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.4333581924438477})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 3.2233943939208984})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 3.6698126792907715})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 3.542249917984009})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 3.522739887237549})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 3.7731199264526367})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 3.40148663520813})
store['active_learning_steps'][10]['eval_training']['best_epoch']=9
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 31621], ['id', 37514], ['id', 7104], ['ood', 30480], ['id', 42474]], 'labels': [0, 4, 7, -1, 7], 'scores': [0.5108400812731847, 0.9895534789917063, 1.435846893990572, 1.8530918233909865, 2.17562049626979]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.505871772766113})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 7.497798919677734})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 8.411441802978516})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 7.902811050415039})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.2248, 'crossentropy': 5.340867578125}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 3.3556392192840576})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.1136507987976074})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.2481768131256104})
store['active_learning_steps'][11]['eval_training']['best_epoch']=2
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 38660], ['id', 9530], ['ood', 63725], ['id', 37198], ['id', 21297]], 'labels': [2, 2, -1, 1, 5], 'scores': [0.6754903237320109, 1.1567539776457476, 1.502949537571304, 1.8023223592211686, 2.0605414042222048]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.169500350952148})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 6.273961544036865})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 6.50847053527832})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 6.036715507507324})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.2396, 'crossentropy': 5.427415234375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 2.9467577934265137})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 3.453808546066284})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 3.5774693489074707})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 47439], ['id', 35684], ['id', 28634], ['id', 17817], ['id', 37459]], 'labels': [3, 6, 3, 4, 1], 'scores': [0.5368651825708793, 0.9404864781028863, 1.2999050973803643, 1.6320282396197867, 1.89870127450442]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 7.779681205749512})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 6.947298526763916})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 7.3877339363098145})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 6.522525787353516})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 7.263283729553223})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 7.38316535949707})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 7.661277770996094})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 6.134472846984863})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 8.408990859985352})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 7.837959289550781})
store['active_learning_steps'][13]['training']['best_epoch']=7
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.2514, 'crossentropy': 7.7327078125}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.7001147270202637})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 4.517049789428711})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.773228168487549})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 3.7837977409362793})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.7760534286499023})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 4.027200698852539})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 3.750537395477295})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.947021961212158})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.155219554901123})
store['active_learning_steps'][13]['eval_training']['best_epoch']=7
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 35162], ['id', 9713], ['id', 27756], ['ood', 20591], ['ood', 23201]], 'labels': [-1, 1, 7, -1, -1], 'scores': [0.683771037982909, 1.3041760533039737, 1.7844107520700532, 2.210129213127944, 2.5425557818608877]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.562165260314941})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 5.753215789794922})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 7.670315742492676})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 7.5453267097473145})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 6.9813618659973145})
store['active_learning_steps'][14]['training']['best_epoch']=2
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.2467, 'crossentropy': 5.7420328125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 2.6519222259521484})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 2.874159336090088})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.2184908390045166})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.5456719398498535})
store['active_learning_steps'][14]['eval_training']['best_epoch']=1
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 57288], ['ood', 70771], ['id', 46616], ['id', 13782], ['id', 21309]], 'labels': [-1, -1, 6, 0, 1], 'scores': [0.5709710201804175, 1.057478616178945, 1.4498586678704957, 1.7575084866174375, 2.02798410961591]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 5.281474590301514})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 6.158873081207275})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 7.061298370361328})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 6.145973205566406})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 6.729016304016113})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 6.047065734863281})
store['active_learning_steps'][15]['training']['best_epoch']=3
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.2411, 'crossentropy': 6.9074875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 4.327150821685791})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 3.247333288192749})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 3.8381400108337402})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 3.7054595947265625})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 3.7948272228240967})
store['active_learning_steps'][15]['eval_training']['best_epoch']=5
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 9795], ['ood', 34868], ['id', 46808], ['ood', 23543], ['ood', 8632]], 'labels': [-1, -1, 1, -1, -1], 'scores': [0.575797512586768, 1.1261531141531491, 1.5363217589288252, 1.9101316485799171, 2.23648977303408]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 4.9890031814575195})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 7.041894435882568})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 8.170926094055176})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 7.266396999359131})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.2488, 'crossentropy': 5.029241796875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 2.833047866821289})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.834714412689209})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.0262722969055176})
store['active_learning_steps'][16]['eval_training']['best_epoch']=2
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 5782], ['id', 12341], ['id', 14719], ['id', 33613], ['ood', 37808]], 'labels': [7, 8, 0, 7, -1], 'scores': [0.5152220153042799, 0.987726114037554, 1.384611604340681, 1.7249785028861324, 2.0023124207582836]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 5.6601176261901855})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 6.059030055999756})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.708360195159912})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 8.686445236206055})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 6.783326625823975})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.2282, 'crossentropy': 6.061384765625}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 3.0796732902526855})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 3.72153902053833})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.8883190155029297})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 3.516909122467041})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 42576], ['id', 26319], ['id', 15277], ['ood', 20613], ['ood', 21520]], 'labels': [8, 4, 6, -1, -1], 'scores': [0.5473389857511691, 1.0035554573002543, 1.404508971311443, 1.7726630227456557, 2.0989842188828085]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 6.010749340057373})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.98718786239624})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 6.3001861572265625})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 6.943826675415039})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 6.9574995040893555})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 6.752552032470703})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 7.734066963195801})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.2448, 'crossentropy': 7.32540390625}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 3.083660125732422})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 3.4294538497924805})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.501056432723999})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.7258312702178955})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 3.554255485534668})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 3.898770809173584})
store['active_learning_steps'][18]['eval_training']['best_epoch']=5
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 27854], ['ood', 60407], ['id', 12394], ['ood', 10836], ['ood', 66763]], 'labels': [7, -1, 6, -1, -1], 'scores': [0.5345443093858635, 0.9901371732631987, 1.3898418348505066, 1.7305242307700133, 2.038229186883421]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 4.764778137207031})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 6.35483455657959})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 6.45712947845459})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 7.100933074951172})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.2361, 'crossentropy': 4.812574609375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.279773712158203})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 3.0638041496276855})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.3157031536102295})
store['active_learning_steps'][19]['eval_training']['best_epoch']=2
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 47271], ['id', 33233], ['ood', 56351], ['ood', 32112], ['ood', 51171]], 'labels': [-1, 6, -1, -1, -1], 'scores': [0.46675265887913453, 0.8575795287691251, 1.2184673811894609, 1.5423407599672254, 1.8343179669805352]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.229872703552246})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 6.561882019042969})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 5.747029781341553})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 7.365636825561523})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.954813003540039})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 6.892885208129883})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 7.043082237243652})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 6.455990791320801})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 7.934703826904297})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.2576, 'crossentropy': 6.998484375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 2.946545362472534})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 3.2395877838134766})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.795828342437744})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 3.5333056449890137})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 3.099323272705078})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 3.607511520385742})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.7067644596099854})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 3.3266947269439697})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 15131], ['id', 34399], ['id', 329], ['ood', 19744], ['ood', 29441]], 'labels': [1, 4, 9, -1, -1], 'scores': [0.5374028375465797, 1.0126422700809794, 1.4406309617122424, 1.8211013582580988, 2.1444858198044354]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.534478187561035})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.681654930114746})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 6.379007339477539})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 7.4007720947265625})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 6.63695764541626})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 7.765048503875732})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.2497, 'crossentropy': 6.684625}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 3.3330979347229004})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.862985134124756})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.470064640045166})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 3.546755790710449})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 3.277810573577881})
store['active_learning_steps'][21]['eval_training']['best_epoch']=3
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 9265], ['ood', 23811], ['id', 14203], ['ood', 50479], ['id', 31528]], 'labels': [8, -1, 1, -1, 0], 'scores': [0.6534560559786817, 1.1527479488368337, 1.5310427128924275, 1.8596182456689756, 2.1657709391160305]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 3.7637081146240234})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.859453201293945})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 7.314517021179199})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 7.058699607849121})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 6.594290733337402})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.2706, 'crossentropy': 4.821316015625}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 3.0203356742858887})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 3.1192996501922607})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 3.7101476192474365})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.059490919113159})
store['active_learning_steps'][22]['eval_training']['best_epoch']=2
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 22158], ['ood', 17700], ['id', 1092], ['id', 22450], ['id', 14979]], 'labels': [4, -1, 1, 0, 7], 'scores': [0.5745352986167993, 1.0701665896983301, 1.510609323039521, 1.8909665163622194, 2.2236583673367205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 5.462399482727051})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.505512714385986})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 6.093109607696533})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 6.032444000244141})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 6.711803436279297})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 6.481114387512207})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 8.200754165649414})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 7.0205488204956055})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.743839263916016})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 6.2325286865234375})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 6.464544296264648})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 8.034209251403809})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 9.165718078613281})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 6.84226655960083})
store['active_learning_steps'][23]['training']['best_epoch']=11
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.2729, 'crossentropy': 6.68337890625}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 2.904224395751953})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.3008604049682617})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 3.7837233543395996})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 3.0967445373535156})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 3.1548216342926025})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.4329209327697754})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 3.722346305847168})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 10981], ['id', 10909], ['ood', 645], ['id', 37378], ['id', 16285]], 'labels': [-1, 5, -1, 6, 2], 'scores': [0.5677129687053318, 1.0952214642284632, 1.603919572975525, 2.03100742927367, 2.3862086842520336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.6238250732421875})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 7.074859619140625})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 5.331215858459473})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 6.090252876281738})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.9806599617004395})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 7.054337501525879})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.2568, 'crossentropy': 5.444258984375}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 2.9893767833709717})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 2.930769443511963})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.8225789070129395})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.384824514389038})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 3.263429641723633})
store['active_learning_steps'][24]['eval_training']['best_epoch']=5
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 1356], ['ood', 57712], ['id', 42942], ['ood', 33707], ['ood', 53628]], 'labels': [-1, -1, 1, -1, -1], 'scores': [0.47802742288049, 0.9129278801914731, 1.2880898158086937, 1.6245170287686201, 1.9341468638499917]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 6.622903823852539})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 5.151053428649902})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.926898956298828})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 5.863420486450195})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 5.2234344482421875})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 5.630865097045898})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 6.84559440612793})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.2864, 'crossentropy': 6.088560546875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.6207375526428223})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.893983840942383})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.959805965423584})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 3.173104763031006})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 3.779569625854492})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 3.204451084136963})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 27714], ['ood', 31616], ['id', 42729], ['id', 25956], ['ood', 11962]], 'labels': [5, -1, 0, 7, -1], 'scores': [0.5562203808898011, 1.0670969476300773, 1.4963209250031648, 1.879669880829929, 2.2215634408318827]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 4.464347839355469})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.313105583190918})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.624872207641602})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 6.272525787353516})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 6.231474876403809})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.277, 'crossentropy': 4.265899609375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 2.952820301055908})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 3.043053150177002})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.9639697074890137})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 2.931868076324463})
store['active_learning_steps'][26]['eval_training']['best_epoch']=3
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 7209], ['id', 30116], ['ood', 34364], ['id', 7503], ['id', 25005]], 'labels': [6, 7, -1, 2, 6], 'scores': [0.46992469709702545, 0.8542288707086158, 1.2093175111132488, 1.518038981352499, 1.7950425994618548]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 4.456786155700684})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 5.651887893676758})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 6.157470703125})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 6.738192558288574})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 6.592006683349609})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.622725963592529})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 5.230622291564941})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 5.7749528884887695})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 6.0489091873168945})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 6.597601890563965})
store['active_learning_steps'][27]['training']['best_epoch']=7
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.2792, 'crossentropy': 5.165866796875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.071868419647217})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 2.7833328247070312})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 3.2466650009155273})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 2.852766513824463})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.3276619911193848})
store['active_learning_steps'][27]['eval_training']['best_epoch']=2
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 24696], ['id', 39513], ['id', 21782], ['ood', 44109], ['id', 40096]], 'labels': [-1, 0, 1, -1, 1], 'scores': [0.5168409153869331, 0.9899318635896793, 1.4054378121010114, 1.786396321972171, 2.119694707987091]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 3.958068370819092})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 4.8709611892700195})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.864943981170654})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 5.281811237335205})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 5.755168914794922})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 6.56499719619751})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 6.175623893737793})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 5.702118873596191})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 6.189699172973633})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 6.486424446105957})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 6.740332126617432})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.3069, 'crossentropy': 5.671989453125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.481074810028076})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 2.6503705978393555})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 3.9122183322906494})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 3.2440192699432373})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 3.135376453399658})
store['active_learning_steps'][28]['eval_training']['best_epoch']=2
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 20634], ['id', 31761], ['id', 9193], ['ood', 71191], ['id', 13240]], 'labels': [9, 8, 8, -1, 1], 'scores': [0.5431075129477791, 1.0278776242822376, 1.4908625073878108, 1.8837285099552306, 2.1291338446149863]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 5.0443620681762695})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 4.020733833312988})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 4.937171936035156})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 6.089412689208984})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.3115234375, 'crossentropy': 6.193658828735352})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 6.479504108428955})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 5.778388023376465})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 6.401645660400391})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.31, 'crossentropy': 6.264088671875}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 3.1437106132507324})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 2.683928966522217})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 3.2659034729003906})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 2.846208095550537})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 3.0478718280792236})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 3.2179036140441895})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 3.0758299827575684})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 49190], ['ood', 50603], ['id', 37180], ['ood', 29838], ['id', 34217]], 'labels': [-1, -1, 8, -1, 0], 'scores': [0.4779497744621629, 0.9027664171111738, 1.298219275942977, 1.6548387960679496, 1.9896654760113472]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 6.137579441070557})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 4.5448503494262695})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 5.6588945388793945})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 5.760829448699951})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 6.201724529266357})
store['active_learning_steps'][30]['training']['best_epoch']=2
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.271, 'crossentropy': 4.427544921875}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 2.7987489700317383})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.6227498054504395})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 2.931947946548462})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 3.1255197525024414})
store['active_learning_steps'][30]['eval_training']['best_epoch']=2
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 27707], ['id', 39676], ['id', 44593], ['ood', 65603], ['id', 35368]], 'labels': [0, 3, 0, -1, 4], 'scores': [0.5037376030676322, 0.9169295154649331, 1.2712445403770296, 1.5946731912772636, 1.8860602730788836]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 3.614741802215576})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 4.592624187469482})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 4.846538543701172})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 4.763761520385742})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 6.600429534912109})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 6.228909492492676})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 6.625776290893555})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.3195, 'crossentropy': 4.642218359375}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 2.920670747756958})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.613590955734253})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 3.3641741275787354})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 2.9329795837402344})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 2.718088150024414})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 2.7150392532348633})
store['active_learning_steps'][31]['eval_training']['best_epoch']=4
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 44299], ['id', 37483], ['ood', 24719], ['id', 16623], ['ood', 49903]], 'labels': [-1, 0, -1, 2, -1], 'scores': [0.5413956135344689, 0.9972925238491277, 1.4316221295108358, 1.839310660857381, 2.1693874282160275]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 2.9379658699035645})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 4.846071720123291})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 4.588095664978027})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 5.850399971008301})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.281, 'crossentropy': 3.0917966796875}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 2.522921085357666})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 2.361689805984497})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 2.2943246364593506})
store['active_learning_steps'][32]['eval_training']['best_epoch']=2
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 6613], ['id', 57], ['id', 12592], ['ood', 72699], ['ood', 66813]], 'labels': [5, 3, 8, -1, -1], 'scores': [0.269883122757137, 0.5219589021498847, 0.7505413001501999, 0.9588396369084045, 1.1614115217739913]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.538327217102051})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 4.569642543792725})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 4.390581130981445})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 6.291373252868652})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 5.682165145874023})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 6.691559314727783})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.310546875, 'crossentropy': 5.677905082702637})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.3251953125, 'crossentropy': 5.809940338134766})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 5.842500686645508})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 6.424988746643066})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.322265625, 'crossentropy': 5.953843116760254})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.2947, 'crossentropy': 5.8953203125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 2.722893476486206})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 2.551273822784424})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 3.01200532913208})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 2.6997857093811035})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 3.010280132293701})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 3.1056649684906006})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 3.2137556076049805})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.330078125, 'crossentropy': 3.066805839538574})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.3095703125, 'crossentropy': 3.3748092651367188})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.30078125, 'crossentropy': 3.2633895874023438})
store['active_learning_steps'][33]['eval_training']['best_epoch']=8
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 60408], ['ood', 55689], ['ood', 47783], ['id', 46323], ['id', 26131]], 'labels': [-1, -1, -1, 1, 0], 'scores': [0.5888985805236145, 1.1422817322232333, 1.6108919784403244, 2.0475644557915755, 2.3901627951818716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 3.7959468364715576})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 4.5559983253479})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 4.973168849945068})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 5.1091718673706055})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.2735, 'crossentropy': 3.920128515625}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 3.120368003845215})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 2.5562586784362793})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.8069469928741455})
store['active_learning_steps'][34]['eval_training']['best_epoch']=2
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 40821], ['id', 3235], ['id', 44940], ['id', 24079], ['id', 10328]], 'labels': [0, 9, 2, 7, 6], 'scores': [0.5899984753448542, 0.9943762742025983, 1.3048322755128972, 1.571199600289586, 1.7920667917985185]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.6841585636138916})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 4.009573936462402})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.3498616218566895})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.31086540222168})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 6.374824523925781})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 5.518353462219238})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 5.943820476531982})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.387678146362305})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 5.929652690887451})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 6.951630592346191})
store['active_learning_steps'][35]['training']['best_epoch']=7
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.2771, 'crossentropy': 6.19438046875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 2.7351465225219727})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 3.308323860168457})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 3.1945886611938477})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 3.2194173336029053})
store['active_learning_steps'][35]['eval_training']['best_epoch']=1
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 43573], ['id', 47031], ['id', 11415], ['id', 38094], ['id', 42367]], 'labels': [-1, 7, 7, 3, 0], 'scores': [0.5826463650900418, 1.1005316547094464, 1.5509888893710455, 1.9415199686650073, 2.2690773598552596]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 3.7310163974761963})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 5.482420921325684})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 8.290850639343262})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 5.854287147521973})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 5.088900566101074})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 6.287827014923096})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 6.064901828765869})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 5.890480041503906})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.3067, 'crossentropy': 5.3201125}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 3.7333531379699707})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 3.185981273651123})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.7291080951690674})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 2.84859561920166})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 3.1956686973571777})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 3.1146035194396973})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 3.3269739151000977})
store['active_learning_steps'][36]['eval_training']['best_epoch']=7
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 16494], ['id', 29670], ['id', 16949], ['id', 3577], ['ood', 3688]], 'labels': [9, 5, 1, 1, -1], 'scores': [0.5630003173457472, 1.0212023275837823, 1.4294874456146704, 1.7731898059367759, 2.0979365617658026]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 2.8907763957977295})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 4.797243118286133})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 4.809574127197266})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 5.61270809173584})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 5.583698272705078})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 5.966303825378418})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 5.706037521362305})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 7.900378227233887})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 7.310352802276611})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 5.789507865905762})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.3023, 'crossentropy': 5.484684765625}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 2.6698427200317383})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 2.599647045135498})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 2.841444730758667})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 3.018214702606201})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 3.103689670562744})
store['active_learning_steps'][37]['eval_training']['best_epoch']=2
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 8218], ['id', 38028], ['id', 10155], ['ood', 119], ['id', 37925]], 'labels': [5, 7, 8, -1, 4], 'scores': [0.5231327820573215, 1.0086397520898789, 1.482210689270293, 1.8706800275818454, 2.2169767696468297]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 3.313748359680176})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.371480941772461})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 4.358527183532715})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.165491104125977})
store['active_learning_steps'][38]['training']['best_epoch']=1
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.2669, 'crossentropy': 3.40300078125}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 2.846109390258789})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 3.0810022354125977})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 2.7506093978881836})
store['active_learning_steps'][38]['eval_training']['best_epoch']=3
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 10069], ['ood', 34791], ['ood', 30180], ['id', 3210], ['id', 12754]], 'labels': [0, -1, -1, 8, 1], 'scores': [0.4916087586788457, 0.8479543564869303, 1.1805376216526828, 1.472767128119619, 1.7030988855553169]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 2.9831387996673584})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 3.628631591796875})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 4.266785144805908})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 4.530673980712891})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.898094177246094})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 6.550037860870361})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 5.483833312988281})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.2981, 'crossentropy': 4.500135546875}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 2.632012128829956})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 2.9358179569244385})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 2.8377835750579834})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.908365249633789})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.721365451812744})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 3.5249838829040527})
store['active_learning_steps'][39]['eval_training']['best_epoch']=3
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 23134], ['id', 48640], ['id', 45798], ['ood', 37556], ['id', 43852]], 'labels': [1, 0, 7, -1, 1], 'scores': [0.48003504553159626, 0.8678503834824705, 1.2087506315530945, 1.5217407051171197, 1.8036931698834247]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 3.607266426086426})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.3115234375, 'crossentropy': 3.3422656059265137})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 4.697568416595459})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 5.808773040771484})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 6.108301162719727})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.2888, 'crossentropy': 3.56463046875}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.899864912033081})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.8130531311035156})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.456923007965088})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.6176393032073975})
store['active_learning_steps'][40]['eval_training']['best_epoch']=4
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 28671], ['id', 38873], ['id', 19665], ['ood', 25070], ['id', 4317]], 'labels': [0, 2, 1, -1, 7], 'scores': [0.39400808684753075, 0.6876363261904808, 0.9633443887994595, 1.1998148685595496, 1.4219674520173542]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.237351417541504})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 4.074886798858643})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 5.279726982116699})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 5.144168853759766})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.30078125, 'crossentropy': 5.095259666442871})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 5.1222944259643555})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 5.766040802001953})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.30859375, 'crossentropy': 5.270679473876953})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 5.560091972351074})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.310546875, 'crossentropy': 6.086514472961426})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.3359375, 'crossentropy': 5.94329833984375})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 6.535690784454346})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.326171875, 'crossentropy': 6.155144691467285})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 5.729297637939453})
store['active_learning_steps'][41]['training']['best_epoch']=11
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.322, 'crossentropy': 5.6860515625}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 2.69069766998291})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 2.5821070671081543})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 2.698030471801758})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 2.8090884685516357})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 3.5719902515411377})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.3203125, 'crossentropy': 2.896188735961914})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.3095703125, 'crossentropy': 3.197488784790039})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.33203125, 'crossentropy': 2.904480457305908})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.3193359375, 'crossentropy': 3.0679221153259277})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 3.4246230125427246})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.34765625, 'crossentropy': 2.9965457916259766})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.3125, 'crossentropy': 3.109866142272949})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.31640625, 'crossentropy': 3.330904722213745})
store['active_learning_steps'][41]['eval_training']['best_epoch']=11
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 29319], ['ood', 58188], ['ood', 61312], ['ood', 66755], ['id', 5446]], 'labels': [4, -1, -1, -1, 0], 'scores': [0.4712818352732805, 0.910402947535482, 1.3154234143410422, 1.6910523606816175, 2.0379329823358296]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 3.6017160415649414})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 3.3537299633026123})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 4.556380271911621})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 7.106194496154785})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 4.640561103820801})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 5.79900598526001})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 7.192671775817871})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 4.86106014251709})
store['active_learning_steps'][42]['training']['best_epoch']=5
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.3067, 'crossentropy': 4.67326015625}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 2.5953292846679688})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 3.2070305347442627})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.9566121101379395})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 3.2394251823425293})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 2.776942729949951})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 2.821974992752075})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 2.9853477478027344})
store['active_learning_steps'][42]['eval_training']['best_epoch']=5
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 26296], ['ood', 61387], ['id', 24968], ['id', 41124], ['id', 27706]], 'labels': [9, -1, 1, 1, 9], 'scores': [0.47955317992824487, 0.8964695497543524, 1.2802219535650434, 1.5909462025863328, 1.8743196747960935]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 3.602806568145752})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 4.515376567840576})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 4.828222274780273})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.3095703125, 'crossentropy': 5.13431453704834})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 5.155272483825684})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 4.9016642570495605})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 5.283411502838135})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.3189, 'crossentropy': 4.84563515625}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 2.5317704677581787})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 2.608025550842285})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 2.7059121131896973})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 2.8839025497436523})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 2.877445697784424})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 3.0421745777130127})
store['active_learning_steps'][43]['eval_training']['best_epoch']=5
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 26259], ['id', 3108], ['id', 18436], ['id', 11865], ['id', 6718]], 'labels': [3, 9, 9, 7, 1], 'scores': [0.5204601480932971, 0.955246048823748, 1.3148670593382823, 1.6376023466222733, 1.9387709425067277]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 3.9491615295410156})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 4.662510871887207})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 4.196572780609131})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 5.106322765350342})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 4.969378471374512})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 6.333721160888672})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 5.548120975494385})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 6.0848894119262695})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.30078125, 'crossentropy': 5.062344551086426})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.30859375, 'crossentropy': 5.63110876083374})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.32421875, 'crossentropy': 5.6701860427856445})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.30078125, 'crossentropy': 5.871598243713379})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.3154296875, 'crossentropy': 5.865200042724609})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.3095703125, 'crossentropy': 5.73392915725708})
store['active_learning_steps'][44]['training']['best_epoch']=11
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.3062, 'crossentropy': 5.714226171875}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.329122543334961})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 2.3736014366149902})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 2.484421968460083})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 2.717501401901245})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.314453125, 'crossentropy': 2.3471789360046387})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.31640625, 'crossentropy': 2.538426399230957})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 2.8022334575653076})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 2.907229423522949})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.30859375, 'crossentropy': 2.8027091026306152})
store['active_learning_steps'][44]['eval_training']['best_epoch']=6
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 49309], ['id', 4719], ['id', 45877], ['id', 17359], ['ood', 10981]], 'labels': [-1, 1, 7, 3, -1], 'scores': [0.5216916613307854, 1.0113953201458505, 1.4430995411920917, 1.8381626768226793, 2.187189389647732]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 2.8713653087615967})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 4.138766765594482})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 3.980714797973633})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 4.817037582397461})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 5.1549153327941895})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 5.813046932220459})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 5.7276129722595215})
store['active_learning_steps'][45]['training']['best_epoch']=4
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.2998, 'crossentropy': 4.63374296875}
store['active_learning_steps'][45]['eval_training']={}
store['active_learning_steps'][45]['eval_training']['epochs']=[]
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 3.0292720794677734})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.4859344959259033})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 2.5239009857177734})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 2.729961395263672})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.3095703125, 'crossentropy': 2.405366897583008})
store['active_learning_steps'][45]['eval_training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 2.9207887649536133})
store['active_learning_steps'][45]['eval_training']['best_epoch']=5
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 37165], ['id', 11355], ['id', 8958], ['ood', 11603], ['id', 19514]], 'labels': [7, 1, 1, -1, 4], 'scores': [0.4469717448471069, 0.8617424543551059, 1.2409257122475732, 1.539711656520863, 1.8185494321848044]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.4547910690307617})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 4.158692359924316})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 4.278172492980957})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.322265625, 'crossentropy': 4.050052165985107})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 4.654195785522461})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 6.13231086730957})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.3310546875, 'crossentropy': 4.82884407043457})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 6.009475231170654})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 5.594148635864258})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 5.399172782897949})
store['active_learning_steps'][46]['training']['best_epoch']=7
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.3292, 'crossentropy': 4.706716015625}
store['active_learning_steps'][46]['eval_training']={}
store['active_learning_steps'][46]['eval_training']['epochs']=[]
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 2.810826301574707})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 2.386380195617676})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.3095703125, 'crossentropy': 2.687324047088623})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.3154296875, 'crossentropy': 2.6495208740234375})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 2.801968574523926})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.32421875, 'crossentropy': 2.6928915977478027})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.3125, 'crossentropy': 2.973173141479492})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.3330078125, 'crossentropy': 2.671320676803589})
store['active_learning_steps'][46]['eval_training']['epochs'].append({'accuracy': 0.3173828125, 'crossentropy': 2.9404170513153076})
store['active_learning_steps'][46]['eval_training']['best_epoch']=8
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 17543], ['id', 44268], ['id', 24765], ['ood', 55370], ['ood', 5117]], 'labels': [-1, 0, 9, -1, -1], 'scores': [0.5258122689282116, 1.0367890283991321, 1.4771514235219905, 1.8302108558134185, 2.1563437146870688]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 5.357263088226318})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 4.037219524383545})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 5.153934955596924})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 4.611733436584473})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 4.571177005767822})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.330078125, 'crossentropy': 4.772612571716309})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 5.274666786193848})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.3173828125, 'crossentropy': 4.468077182769775})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.353515625, 'crossentropy': 5.141569137573242})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.328125, 'crossentropy': 6.056962490081787})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 5.787470817565918})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 5.554257869720459})
store['active_learning_steps'][47]['training']['best_epoch']=9
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.3382, 'crossentropy': 5.262018359375}
store['active_learning_steps'][47]['eval_training']={}
store['active_learning_steps'][47]['eval_training']['epochs']=[]
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 2.65018367767334})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.314453125, 'crossentropy': 2.5389814376831055})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.3115234375, 'crossentropy': 2.4617366790771484})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 3.1126627922058105})
store['active_learning_steps'][47]['eval_training']['epochs'].append({'accuracy': 0.3125, 'crossentropy': 2.466848373413086})
store['active_learning_steps'][47]['eval_training']['best_epoch']=2
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 18338], ['id', 46584], ['ood', 71423], ['id', 11488], ['id', 9582]], 'labels': [7, 0, -1, 4, 9], 'scores': [0.5630073189930322, 1.088832509398737, 1.565338271104178, 2.000735466045513, 2.342592226835512]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 2.9317569732666016})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 4.046443939208984})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.22184944152832})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 4.526551246643066})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 5.4928436279296875})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.879066467285156})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 4.910558223724365})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 6.009158134460449})
store['active_learning_steps'][48]['training']['best_epoch']=5
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.2996, 'crossentropy': 5.202651171875}
store['active_learning_steps'][48]['eval_training']={}
store['active_learning_steps'][48]['eval_training']['epochs']=[]
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 2.6867971420288086})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 3.4158072471618652})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 2.8310317993164062})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 3.009861469268799})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 2.701641082763672})
store['active_learning_steps'][48]['eval_training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 3.1582255363464355})
store['active_learning_steps'][48]['eval_training']['best_epoch']=3
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 40373], ['id', 27836], ['id', 46571], ['id', 44986], ['ood', 61680]], 'labels': [5, 0, 6, 1, -1], 'scores': [0.45095475741515156, 0.8809680412628929, 1.2572506465577038, 1.60702347053462, 1.9019777989213287]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 2.547898292541504})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 4.439425468444824})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 3.1140384674072266})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 4.907486438751221})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 4.900594711303711})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 5.801448345184326})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.3115, 'crossentropy': 3.118332421875}
store['active_learning_steps'][49]['eval_training']={}
store['active_learning_steps'][49]['eval_training']['epochs']=[]
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 2.2205798625946045})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 2.393860340118408})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 2.5820155143737793})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 2.4510905742645264})
store['active_learning_steps'][49]['eval_training']['epochs'].append({'accuracy': 0.3134765625, 'crossentropy': 2.4562158584594727})
store['active_learning_steps'][49]['eval_training']['best_epoch']=5
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 34468], ['id', 38035], ['id', 42504], ['id', 43191], ['ood', 67346]], 'labels': [9, 1, 8, 7, -1], 'scores': [0.3956686641494439, 0.7792247561132859, 1.0740297718837262, 1.3428731122019073, 1.5770233948266856]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 2.772663116455078})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 4.883232116699219})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 3.947413921356201})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.426369667053223})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 4.882149696350098})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 5.0119805335998535})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 5.782047271728516})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 5.459731101989746})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.3108, 'crossentropy': 4.584161328125}
store['active_learning_steps'][50]['eval_training']={}
store['active_learning_steps'][50]['eval_training']['epochs']=[]
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 2.517643451690674})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 2.549739122390747})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 2.959928035736084})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 3.048524856567383})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 3.1642041206359863})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.30078125, 'crossentropy': 2.9178504943847656})
store['active_learning_steps'][50]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 2.9682414531707764})
store['active_learning_steps'][50]['eval_training']['best_epoch']=6
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 36192], ['ood', 51172], ['ood', 40314], ['id', 12413], ['id', 14549]], 'labels': [4, -1, -1, 0, 6], 'scores': [0.4409809220913372, 0.8677645418902382, 1.2026347757973626, 1.5207635219409128, 1.797103169683969]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 2.9222381114959717})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 3.727879762649536})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 3.8759727478027344})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 4.609230995178223})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 3.665156841278076})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 6.373861312866211})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 5.566279411315918})
store['active_learning_steps'][51]['training']['best_epoch']=4
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.3101, 'crossentropy': 4.64881953125}
store['active_learning_steps'][51]['eval_training']={}
store['active_learning_steps'][51]['eval_training']['epochs']=[]
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 2.512078285217285})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 3.008970260620117})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 2.567676067352295})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 3.0368547439575195})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 2.745450735092163})
store['active_learning_steps'][51]['eval_training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 2.709115505218506})
store['active_learning_steps'][51]['eval_training']['best_epoch']=6
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 11769], ['id', 32370], ['id', 11583], ['id', 14437], ['id', 24738]], 'labels': [9, 1, 1, 4, 8], 'scores': [0.42093620970639123, 0.791863474432983, 1.1368079066103371, 1.4587702044784616, 1.7372655249777886]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.2814149856567383})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 3.1792242527008057})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 3.5937719345092773})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 4.2316694259643555})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 5.658435821533203})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 5.1724348068237305})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 5.194875717163086})
store['active_learning_steps'][52]['training']['best_epoch']=4
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.3023, 'crossentropy': 4.17089140625}
store['active_learning_steps'][52]['eval_training']={}
store['active_learning_steps'][52]['eval_training']['epochs']=[]
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 3.1088476181030273})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 2.460954189300537})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.8690004348754883})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 2.7255120277404785})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 2.5786266326904297})
store['active_learning_steps'][52]['eval_training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 3.2710697650909424})
store['active_learning_steps'][52]['eval_training']['best_epoch']=5
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 13072], ['ood', 66673], ['id', 1076], ['ood', 22504], ['id', 6709]], 'labels': [8, -1, 9, -1, 4], 'scores': [0.46601347286815553, 0.874627434542389, 1.2111853415725902, 1.5159236397178368, 1.7983467234859027]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 3.3301048278808594})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 3.60174560546875})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.113241672515869})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 4.714115142822266})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 4.42177152633667})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.3232421875, 'crossentropy': 4.638887405395508})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 4.785916328430176})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 5.934788703918457})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 6.056300163269043})
store['active_learning_steps'][53]['training']['best_epoch']=6
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.3313, 'crossentropy': 4.331859765625}
store['active_learning_steps'][53]['eval_training']={}
store['active_learning_steps'][53]['eval_training']['epochs']=[]
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 2.506152629852295})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.310546875, 'crossentropy': 2.2210693359375})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 2.5990190505981445})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 2.4475631713867188})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.333984375, 'crossentropy': 2.6351776123046875})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 2.743337631225586})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.3193359375, 'crossentropy': 2.77864408493042})
store['active_learning_steps'][53]['eval_training']['epochs'].append({'accuracy': 0.326171875, 'crossentropy': 2.668626308441162})
store['active_learning_steps'][53]['eval_training']['best_epoch']=5
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 33665], ['ood', 22071], ['id', 29737], ['ood', 11603], ['id', 35020]], 'labels': [1, -1, 3, -1, 7], 'scores': [0.4606862637454635, 0.9042512403150595, 1.319841781330139, 1.687106180918568, 1.9721001768051996]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 2.978386163711548})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 3.538163423538208})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 3.6061227321624756})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 4.234628200531006})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 3.957989454269409})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 4.634000778198242})
store['active_learning_steps'][54]['training']['best_epoch']=3
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.2996, 'crossentropy': 3.533831640625}
