store = {}
store['timestamp']=1621618175
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=22']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=22
store['worker_id']=22
store['num_workers']=24
store['config']={'seed': 1258, 'uniform_ood': False, 'id_dataset_name': 'CIFAR-10', 'ood_dataset_name': 'SVHN', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node) + ('SVHN (Train, seed=0, 73257 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'CIFAR-10 (Test)'"}
store['initial_training_set_indices']=[12980, 44617, 6984, 21168, 33976, 35571, 33058, 43729, 26944, 24745, 66, 14046, 46542, 39478, 6000, 5915, 39360, 20774, 27084, 44464]
store['evaluation_set_indices']=[3812, 42704, 6729, 38942, 48125, 16968, 5652, 4045, 10740, 19606, 37062, 15768, 44824, 47581, 19482, 4628, 25290, 27933, 27441, 5508, 35131, 18717, 43561, 37318, 8187, 37590, 45717, 1493, 5924, 19803, 23554, 6460, 2962, 36049, 18273, 11023, 27366, 39007, 5305, 46743, 15798, 44136, 20072, 20717, 1152, 8194, 36500, 17618, 35054, 18973, 45734, 16753, 6410, 28807, 8902, 20957, 6625, 41155, 1332, 47376, 36719, 11500, 36383, 7417, 30371, 19517, 33334, 27185, 29033, 42916, 39943, 34789, 18504, 7348, 6096, 28402, 10058, 12011, 34663, 1618, 17887, 41306, 1467, 28071, 12667, 38339, 44920, 44374, 14769, 31145, 21575, 16685, 24836, 48736, 21176, 26844, 45671, 22164, 42503, 10770, 27020, 30182, 37164, 33354, 47307, 17878, 26665, 40819, 14805, 201, 47956, 44739, 8060, 45495, 8139, 27034, 40800, 21802, 18878, 8672, 41175, 48917, 23272, 9952, 23154, 37915, 18669, 18159, 13468, 14436, 16099, 8128, 33349, 31445, 7202, 21948, 10215, 34670, 538, 40015, 17530, 11133, 6028, 12100, 21106, 5614, 30720, 34210, 39322, 40006, 31808, 24717, 34090, 17381, 18164, 17668, 16984, 37856, 41017, 43216, 46788, 26334, 6887, 40485, 39838, 1931, 47231, 37148, 801, 14067, 31951, 7105, 34561, 18698, 45258, 21399, 18558, 26959, 17240, 30502, 39056, 47625, 18880, 37323, 26204, 21788, 1674, 47188, 10526, 25980, 27994, 19871, 22250, 38761, 7182, 14241, 235, 37616, 39973, 35218, 46446, 33361, 39076, 38899, 15578, 36667, 5551, 23088, 32496, 5705, 23255, 25559, 11975, 44032, 45743, 23571, 30475, 15184, 41327, 15827, 33432, 37357, 40250, 16421, 2561, 8533, 25715, 17074, 36811, 30099, 44174, 8029, 1480, 43701, 10198, 38802, 13200, 31615, 28252, 17879, 18749, 16580, 19178, 48034, 4365, 4796, 46033, 47538, 7188, 45076, 13569, 28392, 19457, 41335, 4474, 23022, 11289, 25103, 35813, 40336, 12008, 36695, 28598, 12671, 48831, 18364, 9890, 11804, 37612, 31396, 10683, 31008, 36360, 15312, 26328, 41353, 34761, 4398, 46637, 13891, 32787, 22410, 26463, 4503, 31374, 26143, 7765, 27551, 15340, 16182, 7868, 42518, 34516, 8244, 13037, 39992, 14300, 48188, 42511, 2963, 28224, 28657, 5474, 19682, 682, 25867, 47518, 36303, 18452, 34447, 24821, 36157, 48089, 25120, 44689, 6509, 1852, 17387, 19405, 39441, 42197, 14298, 16443, 1151, 9775, 10834, 44482, 10445, 41434, 37644, 5702, 29159, 17097, 28308, 42161, 29973, 38602, 4592, 24411, 38792, 25200, 28299, 5522, 4441, 4065, 12187, 32012, 41361, 36098, 25224, 27204, 29536, 18785, 28218, 42361, 10437, 8978, 44209, 7804, 35232, 3041, 23251, 41265, 28139, 41350, 18536, 37181, 25352, 16787, 27537, 29568, 45681, 33891, 35667, 31031, 5795, 23494, 7658, 26711, 35750, 34571, 4852, 29601, 14492, 5318, 26987, 11839, 533, 29565, 16424, 43853, 34375, 26710, 37956, 34492, 46294, 12920, 7945, 29669, 14520, 36081, 14478, 37173, 19188, 40253, 23549, 741, 34309, 11001, 6995, 10899, 36881, 7002, 19049, 13388, 40737, 9210, 22684, 43970, 7048, 46803, 45248, 4726, 40534, 23790, 47216, 8585, 7880, 25042, 306, 11939, 45003, 12905, 4052, 45391, 28968, 19408, 6012, 7814, 27790, 10979, 2005, 32156, 16025, 23706, 8236, 24750, 39229, 6968, 7599, 32427, 48001, 12257, 6899, 36229, 19760, 30468, 32347, 15232, 17555, 34373, 1157, 22434, 38137, 3717, 38235, 41506, 10786, 3175, 48043, 24171, 29368, 39765, 16373, 22973, 42399, 32908, 35630, 28508, 29334, 37539, 45770, 29181, 10946, 18072, 18511, 47354, 31444, 42643, 4078, 45028, 45610, 35405, 33751, 7967, 4701, 13378, 48105, 22116, 20599, 45454, 7325, 11304, 12289, 46114, 8359, 41073, 22751, 19402, 8483, 45656, 5604, 9134, 35979, 19757, 43627, 35248, 23566, 727, 34909, 43560, 2888, 12158, 48248, 2094, 47190, 15295, 27629, 15047, 4402, 32595, 6538, 13474, 11538, 10736, 29892, 29786, 1884, 45940, 2144, 37537, 5222, 26418, 10690, 19114, 30223, 17188, 41379, 46182, 20359, 32256, 43739, 41935, 16411, 15933, 22295, 940, 8665, 1154, 32089, 46513, 17506, 39407, 6187, 7878, 37671, 25414, 16789, 37546, 44170, 9921, 22033, 33690, 23656, 5226, 1631, 8671, 45821, 34099, 40039, 31342, 35231, 29621, 31899, 1023, 17082, 38261, 26917, 31921, 5241, 37282, 45513, 46687, 18915, 10796, 8986, 31711, 2185, 29316, 45090, 13383, 5741, 7930, 39306, 13675, 38034, 29826, 48781, 21746, 39559, 31318, 19965, 25443, 45862, 30730, 9611, 43077, 23902, 9541, 38859, 13973, 27923, 25754, 38295, 39261, 15442, 40254, 28002, 23139, 44524, 11458, 10297, 25299, 13617, 28750, 1835, 29505, 23873, 45073, 34640, 5831, 29115, 26568, 6588, 31067, 15001, 4887, 27814, 17283, 23813, 43511, 14398, 13500, 7428, 11090, 11751, 36607, 9712, 43583, 45864, 39972, 14617, 3431, 26470, 33191, 18204, 24481, 28879, 43889, 15015, 36437, 12660, 37650, 405, 36212, 42818, 10677, 15723, 24514, 35518, 42654, 44052, 10218, 37297, 34741, 40715, 37290, 29931, 29774, 25075, 12136, 44466, 25236, 7096, 26190, 14575, 41698, 9068, 24101, 3379, 19906, 15856, 38317, 20799, 17172, 5987, 140, 11530, 38636, 9116, 11151, 25071, 182, 31603, 21547, 47739, 13909, 624, 25621, 30173, 37807, 7053, 30625, 10450, 22316, 23965, 5028, 37725, 1675, 45751, 19683, 26061, 34327, 38096, 30828, 438, 46574, 9121, 4859, 15563, 33935, 39481, 48048, 37730, 35947, 18461, 22658, 35939, 3507, 16223, 5279, 9615, 13583, 28557, 36129, 19326, 23956, 31469, 3397, 36813, 4416, 48955, 27367, 9692, 41380, 27998, 33372, 24467, 24186, 47802, 16612, 46008, 3943, 48514, 42699, 37077, 17401, 39288, 44878, 31226, 14334, 44847, 7473, 42669, 32658, 40101, 11309, 853, 12919, 41501, 26725, 3843, 41314, 16050, 39323, 5916, 19945, 17950, 48824, 8856, 12778, 28765, 13275, 34339, 8883, 36161, 41767, 44449, 7357, 3967, 41737, 3432, 27375, 5603, 1739, 2418, 23760, 26549, 2676, 11659, 40405, 46217, 5207, 28673, 12645, 45982, 48103, 21541, 33384, 28830, 46313, 2540, 17302, 42509, 2321, 40265, 21290, 35387, 48490, 11327, 16529, 40097, 16839, 12570, 17132, 18289, 20343, 22077, 21098, 5426, 8478, 1923, 4941, 48459, 34289, 38039, 44848, 20094, 25546, 19669, 32606, 16624, 28652, 11887, 22863, 48068, 9574, 39941, 2068, 28297, 7225, 41330, 47575, 30080, 25197, 25710, 18030, 16190, 21185, 46949, 1377, 47189, 30166, 28575, 12032, 14160, 11813, 48219, 39348, 42953, 46300, 5559, 15360, 14665, 25279, 42955, 43707, 10089, 10928, 16650, 18156, 4140, 2816, 45019, 25339, 16628, 3925, 25879, 43725, 33970, 17789, 20083, 8873, 41315, 45472, 40526, 4589, 44440, 3184, 4581, 16953, 7585, 45975, 28441, 10956, 22017, 21698, 2107, 44107, 45868, 30293, 15530, 26848, 45705, 811, 22587, 28712, 16591, 45100, 41182, 1225, 40805, 3915, 6545, 8556, 26652, 29708, 24040, 676, 8243, 42597, 17603, 3208, 38902, 15447, 8826, 14791, 38670, 37596, 42980, 17743, 44094, 23778, 32296, 43347, 20210, 6487, 33150, 5095, 35163, 3681, 42450, 21707, 13663, 37987, 13359, 10158, 24531, 21817, 39213, 29424, 38798, 32466, 37354, 27218, 12293, 4133, 14755, 38826, 23328, 48318, 22137, 28379, 35441, 1910, 31964, 26833, 13669, 7484, 43359, 48803, 6853, 47906, 25522, 42533, 16633, 38444, 39544, 13401, 36560, 47222, 1732, 10624, 45339, 24754, 9680, 47728, 4309, 20076, 32836]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 8.59104061126709})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 9.513998031616211})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 10.138608932495117})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 9.616283416748047})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 11.059825897216797})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.1958, 'crossentropy': 9.313296875}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 55778], ['id', 22706], ['ood', 3159], ['ood', 9636], ['id', 39107]], 'labels': [-1, 2, -1, -1, 0], 'scores': [0.7928454937037057, 1.4599621804580387, 1.9788579331060823, 2.4402462569017747, 2.8442379406265967]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 11.810140609741211})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 9.83502197265625})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 8.307861328125})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 9.121260643005371})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 8.412742614746094})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 8.919914245605469})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 9.290948867797852})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 8.628547668457031})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 10.470958709716797})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 9.875804901123047})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 10.67093563079834})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 9.286359786987305})
store['active_learning_steps'][1]['training']['best_epoch']=9
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.2037, 'crossentropy': 10.6994921875}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 36871], ['ood', 3280], ['ood', 58448], ['id', 40013], ['id', 45559]], 'labels': [0, -1, -1, 7, 9], 'scores': [0.8477510462931477, 1.667106760090145, 2.3759582257375325, 2.9117478730110875, 3.349823214338402]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 9.099348068237305})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 9.6892671585083})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 9.007662773132324})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 9.625102996826172})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 10.271337509155273})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 10.672012329101562})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 11.829263687133789})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 10.949953079223633})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 11.603588104248047})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 12.179769515991211})
store['active_learning_steps'][2]['training']['best_epoch']=7
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.189, 'crossentropy': 11.58520625}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 43536], ['ood', 66291], ['id', 19157], ['ood', 15599], ['ood', 19230]], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.8317051625839464, 1.606848692796281, 2.2958587983314565, 2.880753107141823, 3.3514957896240114]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 8.716222763061523})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 9.071758270263672})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 9.798025131225586})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 10.145942687988281})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 10.865503311157227})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.1694, 'crossentropy': 9.82086953125}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 47669], ['ood', 1907], ['ood', 62463], ['id', 34958], ['ood', 10586]], 'labels': [7, -1, -1, 8, -1], 'scores': [0.7378946257795014, 1.400951148000793, 1.9531102258302413, 2.3960875564591806, 2.7930628675328038]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 8.588951110839844})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 7.538678169250488})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 7.483832359313965})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 8.994037628173828})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 13.472757339477539})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 9.290983200073242})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 9.925134658813477})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 9.99600601196289})
store['active_learning_steps'][4]['training']['best_epoch']=5
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.2003, 'crossentropy': 13.4216359375}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 57101], ['id', 21853], ['ood', 4493], ['id', 29564], ['id', 12090]], 'labels': [-1, 0, -1, 6, 5], 'scores': [0.8078568719377084, 1.512898188366484, 2.1412918202143385, 2.703265931095161, 3.119379733527481]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 10.142767906188965})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 10.945138931274414})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 8.048239707946777})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 8.381088256835938})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 9.140277862548828})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 12.028909683227539})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.1897, 'crossentropy': 8.57680390625}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 986], ['ood', 1782], ['ood', 37865], ['id', 15539], ['id', 33659]], 'labels': [-1, -1, -1, 3, 1], 'scores': [0.7191227506528264, 1.403012978573969, 1.940763803487087, 2.4212798711402623, 2.8378364403304985]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 7.862453937530518})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 7.211068153381348})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 7.44285774230957})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 9.041023254394531})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 9.375049591064453})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 10.37493896484375})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.217, 'crossentropy': 8.006675}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 10805], ['ood', 45332], ['id', 39895], ['ood', 36628], ['ood', 35149]], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.7647772981616612, 1.411682027416465, 1.9997765200616926, 2.532210418456331, 2.9992377487470234]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 9.507091522216797})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 7.284292221069336})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 8.278451919555664})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 7.087033271789551})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 7.850571632385254})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 9.889992713928223})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 8.643167495727539})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 8.318475723266602})
store['active_learning_steps'][7]['training']['best_epoch']=5
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.2052, 'crossentropy': 8.4548046875}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 19995], ['ood', 57289], ['ood', 22006], ['ood', 51803], ['ood', 69622]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.8058443752731865, 1.5623952205289404, 2.154554251684459, 2.6688733634297312, 3.0922017776709207]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 7.540178298950195})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 8.22700309753418})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 8.914918899536133})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 7.759670257568359})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 8.501387596130371})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 8.3634033203125})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 8.616819381713867})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 7.775128364562988})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 8.466495513916016})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 10.276021003723145})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 8.11156177520752})
store['active_learning_steps'][8]['training']['best_epoch']=8
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.1957, 'crossentropy': 7.897809375}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 13691], ['ood', 28380], ['id', 23072], ['ood', 46422], ['ood', 55727]], 'labels': [-1, -1, 1, -1, -1], 'scores': [0.842557436049781, 1.490362215923029, 2.105258372975074, 2.636832858112653, 3.0834147623527173]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 8.17317008972168})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 6.732071876525879})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 8.143253326416016})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 8.225728034973145})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 11.52027702331543})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 8.786314010620117})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 9.34286880493164})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.2018, 'crossentropy': 8.6602296875}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 33447], ['ood', 59028], ['ood', 5449], ['id', 27202], ['id', 16576]], 'labels': [-1, -1, -1, 3, 1], 'scores': [0.722916056690756, 1.4157213136684534, 1.9729561925502463, 2.481248829543272, 2.9104803056215145]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 8.545269012451172})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 7.702541351318359})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 6.993237495422363})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 7.626224994659424})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 9.004417419433594})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 8.228082656860352})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 7.957821846008301})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 7.713045120239258})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.1983, 'crossentropy': 9.30880078125}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 58417], ['id', 26733], ['id', 42214], ['ood', 4412], ['ood', 6373]], 'labels': [-1, 8, 3, -1, -1], 'scores': [0.7469204702093, 1.3966423968244284, 2.002351149577583, 2.5136261664776507, 2.8928019663883777]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 7.172321319580078})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 6.074464797973633})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 7.261599540710449})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 10.580188751220703})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 7.049066543579102})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 8.323793411254883})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 6.692294597625732})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 7.438887596130371})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 8.492183685302734})
store['active_learning_steps'][11]['training']['best_epoch']=6
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.2155, 'crossentropy': 8.300803125}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 23679], ['ood', 22824], ['id', 8427], ['ood', 13159], ['ood', 66807]], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.8671978445003592, 1.6230963911484717, 2.198610262083151, 2.7192238487903584, 3.1525264655099363]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 8.450939178466797})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 7.714720726013184})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 7.36390495300293})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 7.6567182540893555})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 6.430086135864258})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 8.819332122802734})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 8.477973937988281})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 8.305265426635742})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.2151, 'crossentropy': 6.8803359375}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 477], ['ood', 25871], ['id', 41160], ['id', 41885], ['id', 5449]], 'labels': [0, -1, 4, 4, 8], 'scores': [0.6060429476037066, 1.1216454791665158, 1.6098288969730108, 2.029316177251107, 2.405404478071665]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 7.790099620819092})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 6.124383926391602})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 7.570465087890625})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 8.007832527160645})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 7.980374813079834})
store['active_learning_steps'][13]['training']['best_epoch']=2
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.204, 'crossentropy': 6.290191015625}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 53232], ['id', 23320], ['id', 7738], ['id', 25187], ['id', 13273]], 'labels': [-1, 7, 8, 4, 0], 'scores': [0.6883094129371947, 1.2969337508814656, 1.8206652953692632, 2.2689069602142435, 2.6728048131287245]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 5.968274116516113})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 9.550350189208984})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 9.327564239501953})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 10.17801284790039})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 7.565724849700928})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 8.503656387329102})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 8.597285270690918})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 7.988673210144043})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.2055, 'crossentropy': 8.3787375}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 67632], ['id', 32052], ['ood', 61321], ['id', 45311], ['id', 30384]], 'labels': [-1, 0, -1, 8, 2], 'scores': [0.8033670578507204, 1.4452585084523975, 2.006625865568024, 2.470836044398399, 2.8643699977725596]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 5.684671401977539})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 5.942914009094238})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 7.249523162841797})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 7.258701324462891})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.2162, 'crossentropy': 6.060303515625}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 47776], ['ood', 68383], ['ood', 50440], ['id', 7652], ['ood', 30679]], 'labels': [-1, -1, -1, 4, -1], 'scores': [0.5989020990705323, 1.0403346703445444, 1.4478861610308646, 1.8212491568332752, 2.1628108140550735]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 5.843206882476807})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 7.315016269683838})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 6.283994674682617})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 8.326942443847656})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 7.757176399230957})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 8.075849533081055})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 8.529504776000977})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 8.811561584472656})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 8.407224655151367})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 8.851716995239258})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.2135, 'crossentropy': 8.66570703125}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 563], ['id', 46794], ['id', 20069], ['id', 39777], ['id', 15572]], 'labels': [-1, 4, 3, 4, 1], 'scores': [0.6919039613101148, 1.3415855807128718, 1.928001922459086, 2.4444770172461965, 2.8755646706544473]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 6.352054595947266})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 5.715102195739746})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 7.922616958618164})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 7.783867835998535})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 6.681119441986084})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 9.442750930786133})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 8.726333618164062})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 8.876920700073242})
store['active_learning_steps'][17]['training']['best_epoch']=5
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.2382, 'crossentropy': 6.86165625}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 2854], ['ood', 19448], ['id', 48946], ['ood', 39442], ['id', 11149]], 'labels': [8, -1, 7, -1, 3], 'scores': [0.777878256541896, 1.3342917099166063, 1.8323406835264913, 2.2877427309019485, 2.6798906024715405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 6.884126663208008})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 7.346848487854004})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 7.10653018951416})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 7.670805931091309})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 7.928768157958984})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 7.650986671447754})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 8.986236572265625})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 9.025315284729004})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.2255, 'crossentropy': 8.25390390625}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 17411], ['id', 24918], ['ood', 48187], ['id', 25100], ['id', 21559]], 'labels': [-1, 6, -1, 0, 0], 'scores': [0.6118132968999961, 1.1849887858969845, 1.7135895743538403, 2.1956489505040633, 2.609564874768121]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.052658557891846})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 7.24446964263916})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 8.675975799560547})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 7.277632713317871})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 7.696983337402344})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 6.876969814300537})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 10.625255584716797})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 7.340811729431152})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 10.300613403320312})
store['active_learning_steps'][19]['training']['best_epoch']=6
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.2314, 'crossentropy': 6.78093984375}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 34323], ['ood', 32110], ['ood', 31309], ['id', 39852], ['id', 12373]], 'labels': [1, -1, -1, 4, 9], 'scores': [0.6394044974656488, 1.2444292740127514, 1.814897775801402, 2.3235235143300983, 2.7597273798714417]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 4.136322021484375})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.937759876251221})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 6.185788154602051})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 6.810391426086426})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.2228, 'crossentropy': 4.23325234375}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 23226], ['id', 39320], ['ood', 63426], ['ood', 51305], ['id', 37236]], 'labels': [-1, 8, -1, -1, 0], 'scores': [0.5003604472297147, 0.9112158047916756, 1.2346608253739264, 1.5302879868808317, 1.8171882966326205]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 6.581371307373047})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.559144020080566})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 6.338309288024902})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 6.290101051330566})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 7.392426013946533})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 7.484217643737793})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 8.018133163452148})
store['active_learning_steps'][21]['training']['best_epoch']=4
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.2367, 'crossentropy': 6.263303125}
store['active_learning_steps'][21]['acquisition']={'indices': [['ood', 58606], ['id', 17698], ['ood', 56653], ['id', 43646], ['id', 28642]], 'labels': [-1, 6, -1, 0, 9], 'scores': [0.59195596050255, 1.1412058050214302, 1.6102176979727556, 2.0562824114081284, 2.4527413681054977]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.471736431121826})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.9572672843933105})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 8.183151245117188})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 6.7767510414123535})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 7.332765579223633})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 7.085599899291992})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 7.259078025817871})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 7.7056660652160645})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.2282, 'crossentropy': 7.6886671875}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 10289], ['ood', 61496], ['ood', 16414], ['ood', 43579], ['ood', 26377]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.5911231585414698, 1.1431050171833057, 1.6248521612405011, 2.071854200641681, 2.455968577050207]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.024136543273926})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 7.1077189445495605})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 6.773989677429199})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 6.847366809844971})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 7.49530553817749})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 8.45379638671875})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 7.451048374176025})
store['active_learning_steps'][23]['training']['best_epoch']=4
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.2421, 'crossentropy': 6.97594609375}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 42321], ['ood', 43639], ['id', 38213], ['ood', 30480], ['id', 35628]], 'labels': [-1, -1, 7, -1, 7], 'scores': [0.8582091244407564, 1.4441484436319763, 1.9224419600684928, 2.350976249202276, 2.744350506875646]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.656839370727539})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 6.326446533203125})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 6.8883466720581055})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 6.540759563446045})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 7.734574317932129})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 7.418684959411621})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.212, 'crossentropy': 7.12778125}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 53702], ['ood', 35040], ['id', 26935], ['ood', 22335], ['ood', 67794]], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.7376600065922267, 1.2730594863561446, 1.7658880432842823, 2.2028417756427148, 2.59170859067346]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 4.678419589996338})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.729536056518555})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 6.292327404022217})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 7.798938751220703})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 6.343760967254639})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 6.794564247131348})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.2286, 'crossentropy': 6.678271875}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 38161], ['ood', 14032], ['ood', 43675], ['id', 23104], ['ood', 38942]], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.774324806887374, 1.2560740966939203, 1.7167812705121746, 2.123045979214517, 2.4882411280435734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 4.260123252868652})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 6.036566734313965})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 6.790699005126953})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 7.993896484375})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 7.283750534057617})
store['active_learning_steps'][26]['training']['best_epoch']=2
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.2106, 'crossentropy': 6.37967421875}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 18248], ['ood', 14135], ['ood', 54898], ['id', 6848], ['id', 10396]], 'labels': [-1, -1, -1, 9, 8], 'scores': [0.6782692552420131, 1.1024360987205855, 1.480535423866336, 1.8436485171006218, 2.1805338856785834]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 4.975476264953613})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.5785675048828125})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 6.315068244934082})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 7.37054443359375})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.2193, 'crossentropy': 5.036465625}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 16585], ['id', 41082], ['ood', 68287], ['ood', 2628], ['id', 2090]], 'labels': [4, 0, -1, -1, 6], 'scores': [0.4518626632792062, 0.7761664406604507, 1.0697290206078138, 1.3502154434712237, 1.6201874959060314]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 11.424825668334961})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.998333930969238})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 6.722615718841553})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 6.632281303405762})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 7.618037700653076})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 6.736125946044922})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 7.149849891662598})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 7.570062160491943})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 6.439831733703613})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 7.412186145782471})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 6.755382537841797})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 7.666289329528809})
store['active_learning_steps'][28]['training']['best_epoch']=9
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.2386, 'crossentropy': 6.72542734375}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 73110], ['id', 4784], ['id', 19910], ['ood', 18459], ['ood', 37062]], 'labels': [-1, 8, 2, -1, -1], 'scores': [0.659353136504294, 1.25064526039947, 1.7497740084118805, 2.2066460359102287, 2.6232798864181053]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 4.400018692016602})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 6.637110710144043})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 7.141419410705566})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 6.244282245635986})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 7.535943031311035})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 8.332701683044434})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 8.68233871459961})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 7.890689373016357})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 7.112327575683594})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 6.148409843444824})
store['active_learning_steps'][29]['training']['best_epoch']=7
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.2293, 'crossentropy': 9.145371875}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 17434], ['id', 34547], ['id', 43294], ['id', 17229], ['id', 16139]], 'labels': [-1, 1, 4, 8, 7], 'scores': [0.6892636321270402, 1.3092009488800045, 1.8744343527869551, 2.3509858316461694, 2.775065914427498]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.338177680969238})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 6.360886096954346})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 7.447211265563965})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.872518539428711})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 7.191984176635742})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 6.628639221191406})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 9.466497421264648})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 7.814631462097168})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 8.1945161819458})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 7.598483085632324})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 7.25025749206543})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 7.22182559967041})
store['active_learning_steps'][30]['training']['best_epoch']=9
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.2341, 'crossentropy': 8.01438359375}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 38060], ['ood', 20426], ['id', 46838], ['id', 33410], ['id', 42774]], 'labels': [3, -1, 9, 8, 1], 'scores': [0.614363639301736, 1.1640833855767654, 1.6935067090619729, 2.1675543062192926, 2.579463518395735]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 4.370323181152344})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 7.926981449127197})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 7.899140357971191})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 8.048498153686523})
store['active_learning_steps'][31]['training']['best_epoch']=1
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.2117, 'crossentropy': 4.60368984375}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 61921], ['ood', 36856], ['id', 48121], ['ood', 55901], ['ood', 30480]], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.46789242973395373, 0.8776940560908506, 1.2547864385369678, 1.5913726908970283, 1.8897570791941742]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 4.6649627685546875})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.820189952850342})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 6.205137252807617})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 8.920219421386719})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 5.779598236083984})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.2175, 'crossentropy': 6.29608984375}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 16190], ['ood', 4018], ['id', 40874], ['id', 13058], ['id', 40184]], 'labels': [-1, -1, 0, 4, 8], 'scores': [0.5770191023061524, 1.066641112154739, 1.4806524917065538, 1.8706285537755214, 2.232980933387932]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.3291826248168945})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 4.986208915710449})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 5.736032485961914})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 6.505492687225342})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 7.333996772766113})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.2336, 'crossentropy': 5.26697421875}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 61668], ['id', 8812], ['id', 27695], ['ood', 73110], ['ood', 29707]], 'labels': [-1, 6, 0, -1, -1], 'scores': [0.7697675467861853, 1.2840088237770448, 1.695078154660238, 2.0798515210416237, 2.4144347385122717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 4.467560291290283})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 5.783210754394531})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 6.547781944274902})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 6.189294338226318})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 6.947081089019775})
store['active_learning_steps'][34]['training']['best_epoch']=2
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.2023, 'crossentropy': 5.8403125}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 43238], ['id', 7520], ['id', 21679], ['id', 44129], ['id', 45330]], 'labels': [0, 0, 0, 9, 7], 'scores': [0.517524915148253, 0.9556806939069977, 1.3302725590004387, 1.6871189167394203, 2.0227409500657494]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.225732326507568})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.91768741607666})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 5.939336776733398})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 7.706439971923828})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 5.5765533447265625})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 7.885433197021484})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.2318, 'crossentropy': 6.02457421875}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 40393], ['ood', 43032], ['id', 41339], ['id', 5725], ['ood', 61701]], 'labels': [-1, -1, 9, 6, -1], 'scores': [0.5599908041131783, 1.066939766119679, 1.5457554460757432, 1.962822727621977, 2.330313222181367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 4.5259222984313965})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 4.360792636871338})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 6.477818489074707})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 5.886648178100586})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 6.963496208190918})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 6.814846992492676})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 8.137025833129883})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 6.0296478271484375})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.2266, 'crossentropy': 7.00300390625}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 27078], ['id', 23399], ['ood', 10440], ['id', 32945], ['ood', 22519]], 'labels': [-1, 5, -1, 5, -1], 'scores': [0.829312740628487, 1.4428654822947364, 2.029896494830047, 2.5053405051226836, 2.9133679198971505]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 5.268976211547852})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 7.600498199462891})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.687557220458984})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 7.560201168060303})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 6.3788909912109375})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 5.9365553855896})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 6.937285423278809})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 6.468258857727051})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 5.930434226989746})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 7.015746593475342})
store['active_learning_steps'][37]['training']['best_epoch']=7
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.2677, 'crossentropy': 6.97108203125}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 7009], ['ood', 52613], ['id', 5772], ['id', 37408], ['id', 5851]], 'labels': [7, -1, 1, 7, 0], 'scores': [0.6763864154783261, 1.2460651139985055, 1.7458734774482814, 2.195747789962013, 2.6071557239183623]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 4.7485456466674805})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 5.993196487426758})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 7.234477519989014})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 5.809497833251953})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 7.302484035491943})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.236, 'crossentropy': 6.283023046875}
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 65233], ['id', 26230], ['id', 19798], ['id', 9717], ['ood', 67313]], 'labels': [-1, 6, 3, 0, -1], 'scores': [0.8165014615610051, 1.354379023213108, 1.7712028334125236, 2.1685808930707493, 2.509861518039079]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.897576332092285})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.019640922546387})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 4.382232666015625})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 5.477721214294434})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 7.214143753051758})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 8.368021965026855})
store['active_learning_steps'][39]['training']['best_epoch']=3
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.258, 'crossentropy': 4.601780859375}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 57286], ['ood', 3597], ['id', 36919], ['ood', 58447], ['id', 4490]], 'labels': [-1, -1, 8, -1, 9], 'scores': [0.46161480537631716, 0.8852148613305282, 1.2825617266554867, 1.6669125877111375, 2.018852736666565]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 5.284191608428955})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.492964744567871})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 7.435311317443848})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 4.718866348266602})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 5.739322662353516})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 7.1749091148376465})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 7.068051338195801})
store['active_learning_steps'][40]['training']['best_epoch']=4
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.2518, 'crossentropy': 4.802128515625}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 25614], ['ood', 57288], ['ood', 31013], ['ood', 16096], ['ood', 66791]], 'labels': [3, -1, -1, -1, -1], 'scores': [0.6062132356720531, 1.1467147794150692, 1.629441443966405, 2.0318370027284534, 2.4011064728831233]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 4.1986188888549805})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 4.611665725708008})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 6.678752422332764})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 6.597481727600098})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 5.2678422927856445})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 6.734040260314941})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 6.546855926513672})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 6.437082767486572})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 6.347896575927734})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 7.416409492492676})
store['active_learning_steps'][41]['training']['best_epoch']=7
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.2553, 'crossentropy': 6.5663578125}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 40287], ['id', 20103], ['ood', 40338], ['id', 37153], ['ood', 15772]], 'labels': [-1, 1, -1, 2, -1], 'scores': [0.7374455699955462, 1.3089461041077977, 1.8407449948954557, 2.311693790229528, 2.6976487936102256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.676547050476074})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 6.5816144943237305})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.279961585998535})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 5.647724628448486})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 6.036465644836426})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 6.603515625})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 6.7804765701293945})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 6.385764122009277})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 9.645662307739258})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.2449, 'crossentropy': 6.5950453125}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 17839], ['id', 43084], ['ood', 35251], ['id', 29941], ['id', 45051]], 'labels': [-1, 0, -1, 6, 5], 'scores': [0.6708531802863849, 1.2495921479129586, 1.7723129397316573, 2.2666655941063114, 2.6607966893618666]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 3.777522087097168})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 4.134784698486328})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.314388275146484})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 6.006424427032471})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 5.921359062194824})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 6.836780071258545})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 7.050159454345703})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.2447, 'crossentropy': 6.28659140625}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 4891], ['ood', 29855], ['id', 14890], ['ood', 21299], ['id', 31704]], 'labels': [-1, -1, 1, -1, 8], 'scores': [0.4902323202791232, 0.9372830059597557, 1.348647557702896, 1.716024404571871, 2.052797405827315]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 3.6409242153167725})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 5.700117111206055})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 6.0463714599609375})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 5.006499290466309})
store['active_learning_steps'][44]['training']['best_epoch']=1
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.2421, 'crossentropy': 3.680565234375}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 46969], ['id', 35650], ['ood', 12332], ['ood', 26970], ['ood', 71473]], 'labels': [-1, 1, -1, -1, -1], 'scores': [0.486590526584872, 0.763765558466722, 1.0339130372743934, 1.294905339208512, 1.5073389601460718]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 3.868180274963379})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.245381832122803})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 5.499992370605469})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 7.605642795562744})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 6.224583625793457})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 8.079696655273438})
store['active_learning_steps'][45]['training']['best_epoch']=3
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.2693, 'crossentropy': 5.544115234375}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 33301], ['id', 43069], ['id', 34218], ['ood', 22930], ['id', 26118]], 'labels': [8, 8, 2, -1, 1], 'scores': [0.5597619025076814, 1.0930545783193004, 1.5530210255190546, 1.970316201345577, 2.3078268525064454]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 3.615311622619629})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.9350404739379883})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.453041076660156})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 5.306324481964111})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.695498466491699})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 6.692962646484375})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 8.082164764404297})
store['active_learning_steps'][46]['training']['best_epoch']=4
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.2765, 'crossentropy': 5.677521484375}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 10328], ['ood', 14190], ['ood', 25423], ['ood', 50209], ['id', 36864]], 'labels': [6, -1, -1, -1, 2], 'scores': [0.6132596526195169, 1.1225336280993568, 1.5865921005145993, 2.0053379558229505, 2.3484730102749065]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.7183592319488525})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.323178768157959})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 5.662108898162842})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 5.285902500152588})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 7.314308166503906})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.2462, 'crossentropy': 4.397665625}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 47189], ['ood', 19262], ['id', 41734], ['id', 5476], ['id', 14760]], 'labels': [-1, -1, 0, 4, 1], 'scores': [0.44116237529204283, 0.8429528240375026, 1.2181754220253254, 1.5747743665918446, 1.8852210319766627]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 4.241419792175293})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 5.5546159744262695})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.084798336029053})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.984956741333008})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 5.069726943969727})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 5.504910469055176})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 6.474649906158447})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 7.3830647468566895})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 7.374177932739258})
store['active_learning_steps'][48]['training']['best_epoch']=6
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.2779, 'crossentropy': 5.628534375}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 18039], ['id', 4724], ['id', 22302], ['ood', 65355], ['ood', 29555]], 'labels': [-1, 1, 9, -1, -1], 'scores': [0.6685033908755296, 1.2369129390781586, 1.7823498173441412, 2.262220469417243, 2.6548303560557738]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 3.532433032989502})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.483949661254883})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 5.537845134735107})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 5.140314102172852})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 4.771345138549805})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 7.053063869476318})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.381125450134277})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 6.584124565124512})
store['active_learning_steps'][49]['training']['best_epoch']=5
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.2799, 'crossentropy': 4.76724296875}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 12130], ['ood', 62047], ['ood', 40255], ['ood', 66815], ['id', 44839]], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.6389509006027041, 1.1553375216696398, 1.609690086321125, 2.0109616514065154, 2.34845698198734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 5.039748191833496})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.411818504333496})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 4.387951850891113})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 5.468112945556641})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 6.661928653717041})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 5.994551658630371})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 6.415277481079102})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 6.400391101837158})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 5.415399551391602})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 7.825416564941406})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 5.707583427429199})
store['active_learning_steps'][50]['training']['best_epoch']=8
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.3075, 'crossentropy': 6.415568359375}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 50603], ['ood', 40258], ['id', 44865], ['id', 38195], ['id', 33762]], 'labels': [-1, -1, 5, 2, 7], 'scores': [0.6699596536757708, 1.2765864802660936, 1.8142979386103697, 2.2873742247345934, 2.652197132449853]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 4.343660354614258})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.494350433349609})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 4.688159942626953})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 5.37090539932251})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 7.050380229949951})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 7.5007829666137695})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.2807, 'crossentropy': 4.550241015625}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 24228], ['id', 41345], ['id', 42115], ['id', 42440], ['id', 14203]], 'labels': [0, 3, 2, 0, 1], 'scores': [0.5780206551274523, 1.0627238296786006, 1.5014387378484821, 1.883345466816805, 2.202727240874072]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.235548973083496})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.368320465087891})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 4.709827423095703})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 5.8404340744018555})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 6.13430118560791})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 6.517581939697266})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 6.965261459350586})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 6.38515567779541})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 6.8877272605896})
store['active_learning_steps'][52]['training']['best_epoch']=6
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.2841, 'crossentropy': 6.194575390625}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 45781], ['id', 12413], ['ood', 65578], ['id', 17971], ['id', 26460]], 'labels': [7, 0, -1, 7, 7], 'scores': [0.6356015741950016, 1.1582436239971128, 1.6279793608012545, 2.0588833570320872, 2.431163752027567]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 2.716346502304077})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.791474342346191})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 4.809256553649902})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 5.418169975280762})
store['active_learning_steps'][53]['training']['best_epoch']=1
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.2695, 'crossentropy': 2.6947564453125}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 56601], ['ood', 6906], ['ood', 8062], ['ood', 63262], ['id', 27836]], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.576218537351187, 0.9617696462608447, 1.2762460308935974, 1.5464633535167085, 1.8057886812168311]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 3.1078810691833496})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 4.355318069458008})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 4.591092109680176})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 5.345098972320557})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 6.551346778869629})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 6.650254249572754})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 6.214422225952148})
store['active_learning_steps'][54]['training']['best_epoch']=4
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.2704, 'crossentropy': 4.9926453125}
