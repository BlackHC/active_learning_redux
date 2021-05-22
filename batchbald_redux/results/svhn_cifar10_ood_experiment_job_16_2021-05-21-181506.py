store = {}
store['timestamp']=1621617306
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=16']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=16
store['worker_id']=16
store['num_workers']=24
store['config']={'seed': 1252, 'uniform_ood': True, 'id_dataset_name': 'CIFAR-10', 'ood_dataset_name': 'SVHN', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node | one_hot_targets{'num_classes': 10}) + ('SVHN (Train, seed=0, 73257 samples)' | uniform_targets{'num_classes': 10})", 'test': "'CIFAR-10 (Test)'"}
store['initial_training_set_indices']=[12980, 44617, 6984, 21168, 33976, 35571, 33058, 43729, 26944, 24745, 66, 14046, 46542, 39478, 6000, 5915, 39360, 20774, 27084, 44464]
store['evaluation_set_indices']=[3812, 42704, 6729, 38942, 48125, 16968, 5652, 4045, 10740, 19606, 37062, 15768, 44824, 47581, 19482, 4628, 25290, 27933, 27441, 5508, 35131, 18717, 43561, 37318, 8187, 37590, 45717, 1493, 5924, 19803, 23554, 6460, 2962, 36049, 18273, 11023, 27366, 39007, 5305, 46743, 15798, 44136, 20072, 20717, 1152, 8194, 36500, 17618, 35054, 18973, 45734, 16753, 6410, 28807, 8902, 20957, 6625, 41155, 1332, 47376, 36719, 11500, 36383, 7417, 30371, 19517, 33334, 27185, 29033, 42916, 39943, 34789, 18504, 7348, 6096, 28402, 10058, 12011, 34663, 1618, 17887, 41306, 1467, 28071, 12667, 38339, 44920, 44374, 14769, 31145, 21575, 16685, 24836, 48736, 21176, 26844, 45671, 22164, 42503, 10770, 27020, 30182, 37164, 33354, 47307, 17878, 26665, 40819, 14805, 201, 47956, 44739, 8060, 45495, 8139, 27034, 40800, 21802, 18878, 8672, 41175, 48917, 23272, 9952, 23154, 37915, 18669, 18159, 13468, 14436, 16099, 8128, 33349, 31445, 7202, 21948, 10215, 34670, 538, 40015, 17530, 11133, 6028, 12100, 21106, 5614, 30720, 34210, 39322, 40006, 31808, 24717, 34090, 17381, 18164, 17668, 16984, 37856, 41017, 43216, 46788, 26334, 6887, 40485, 39838, 1931, 47231, 37148, 801, 14067, 31951, 7105, 34561, 18698, 45258, 21399, 18558, 26959, 17240, 30502, 39056, 47625, 18880, 37323, 26204, 21788, 1674, 47188, 10526, 25980, 27994, 19871, 22250, 38761, 7182, 14241, 235, 37616, 39973, 35218, 46446, 33361, 39076, 38899, 15578, 36667, 5551, 23088, 32496, 5705, 23255, 25559, 11975, 44032, 45743, 23571, 30475, 15184, 41327, 15827, 33432, 37357, 40250, 16421, 2561, 8533, 25715, 17074, 36811, 30099, 44174, 8029, 1480, 43701, 10198, 38802, 13200, 31615, 28252, 17879, 18749, 16580, 19178, 48034, 4365, 4796, 46033, 47538, 7188, 45076, 13569, 28392, 19457, 41335, 4474, 23022, 11289, 25103, 35813, 40336, 12008, 36695, 28598, 12671, 48831, 18364, 9890, 11804, 37612, 31396, 10683, 31008, 36360, 15312, 26328, 41353, 34761, 4398, 46637, 13891, 32787, 22410, 26463, 4503, 31374, 26143, 7765, 27551, 15340, 16182, 7868, 42518, 34516, 8244, 13037, 39992, 14300, 48188, 42511, 2963, 28224, 28657, 5474, 19682, 682, 25867, 47518, 36303, 18452, 34447, 24821, 36157, 48089, 25120, 44689, 6509, 1852, 17387, 19405, 39441, 42197, 14298, 16443, 1151, 9775, 10834, 44482, 10445, 41434, 37644, 5702, 29159, 17097, 28308, 42161, 29973, 38602, 4592, 24411, 38792, 25200, 28299, 5522, 4441, 4065, 12187, 32012, 41361, 36098, 25224, 27204, 29536, 18785, 28218, 42361, 10437, 8978, 44209, 7804, 35232, 3041, 23251, 41265, 28139, 41350, 18536, 37181, 25352, 16787, 27537, 29568, 45681, 33891, 35667, 31031, 5795, 23494, 7658, 26711, 35750, 34571, 4852, 29601, 14492, 5318, 26987, 11839, 533, 29565, 16424, 43853, 34375, 26710, 37956, 34492, 46294, 12920, 7945, 29669, 14520, 36081, 14478, 37173, 19188, 40253, 23549, 741, 34309, 11001, 6995, 10899, 36881, 7002, 19049, 13388, 40737, 9210, 22684, 43970, 7048, 46803, 45248, 4726, 40534, 23790, 47216, 8585, 7880, 25042, 306, 11939, 45003, 12905, 4052, 45391, 28968, 19408, 6012, 7814, 27790, 10979, 2005, 32156, 16025, 23706, 8236, 24750, 39229, 6968, 7599, 32427, 48001, 12257, 6899, 36229, 19760, 30468, 32347, 15232, 17555, 34373, 1157, 22434, 38137, 3717, 38235, 41506, 10786, 3175, 48043, 24171, 29368, 39765, 16373, 22973, 42399, 32908, 35630, 28508, 29334, 37539, 45770, 29181, 10946, 18072, 18511, 47354, 31444, 42643, 4078, 45028, 45610, 35405, 33751, 7967, 4701, 13378, 48105, 22116, 20599, 45454, 7325, 11304, 12289, 46114, 8359, 41073, 22751, 19402, 8483, 45656, 5604, 9134, 35979, 19757, 43627, 35248, 23566, 727, 34909, 43560, 2888, 12158, 48248, 2094, 47190, 15295, 27629, 15047, 4402, 32595, 6538, 13474, 11538, 10736, 29892, 29786, 1884, 45940, 2144, 37537, 5222, 26418, 10690, 19114, 30223, 17188, 41379, 46182, 20359, 32256, 43739, 41935, 16411, 15933, 22295, 940, 8665, 1154, 32089, 46513, 17506, 39407, 6187, 7878, 37671, 25414, 16789, 37546, 44170, 9921, 22033, 33690, 23656, 5226, 1631, 8671, 45821, 34099, 40039, 31342, 35231, 29621, 31899, 1023, 17082, 38261, 26917, 31921, 5241, 37282, 45513, 46687, 18915, 10796, 8986, 31711, 2185, 29316, 45090, 13383, 5741, 7930, 39306, 13675, 38034, 29826, 48781, 21746, 39559, 31318, 19965, 25443, 45862, 30730, 9611, 43077, 23902, 9541, 38859, 13973, 27923, 25754, 38295, 39261, 15442, 40254, 28002, 23139, 44524, 11458, 10297, 25299, 13617, 28750, 1835, 29505, 23873, 45073, 34640, 5831, 29115, 26568, 6588, 31067, 15001, 4887, 27814, 17283, 23813, 43511, 14398, 13500, 7428, 11090, 11751, 36607, 9712, 43583, 45864, 39972, 14617, 3431, 26470, 33191, 18204, 24481, 28879, 43889, 15015, 36437, 12660, 37650, 405, 36212, 42818, 10677, 15723, 24514, 35518, 42654, 44052, 10218, 37297, 34741, 40715, 37290, 29931, 29774, 25075, 12136, 44466, 25236, 7096, 26190, 14575, 41698, 9068, 24101, 3379, 19906, 15856, 38317, 20799, 17172, 5987, 140, 11530, 38636, 9116, 11151, 25071, 182, 31603, 21547, 47739, 13909, 624, 25621, 30173, 37807, 7053, 30625, 10450, 22316, 23965, 5028, 37725, 1675, 45751, 19683, 26061, 34327, 38096, 30828, 438, 46574, 9121, 4859, 15563, 33935, 39481, 48048, 37730, 35947, 18461, 22658, 35939, 3507, 16223, 5279, 9615, 13583, 28557, 36129, 19326, 23956, 31469, 3397, 36813, 4416, 48955, 27367, 9692, 41380, 27998, 33372, 24467, 24186, 47802, 16612, 46008, 3943, 48514, 42699, 37077, 17401, 39288, 44878, 31226, 14334, 44847, 7473, 42669, 32658, 40101, 11309, 853, 12919, 41501, 26725, 3843, 41314, 16050, 39323, 5916, 19945, 17950, 48824, 8856, 12778, 28765, 13275, 34339, 8883, 36161, 41767, 44449, 7357, 3967, 41737, 3432, 27375, 5603, 1739, 2418, 23760, 26549, 2676, 11659, 40405, 46217, 5207, 28673, 12645, 45982, 48103, 21541, 33384, 28830, 46313, 2540, 17302, 42509, 2321, 40265, 21290, 35387, 48490, 11327, 16529, 40097, 16839, 12570, 17132, 18289, 20343, 22077, 21098, 5426, 8478, 1923, 4941, 48459, 34289, 38039, 44848, 20094, 25546, 19669, 32606, 16624, 28652, 11887, 22863, 48068, 9574, 39941, 2068, 28297, 7225, 41330, 47575, 30080, 25197, 25710, 18030, 16190, 21185, 46949, 1377, 47189, 30166, 28575, 12032, 14160, 11813, 48219, 39348, 42953, 46300, 5559, 15360, 14665, 25279, 42955, 43707, 10089, 10928, 16650, 18156, 4140, 2816, 45019, 25339, 16628, 3925, 25879, 43725, 33970, 17789, 20083, 8873, 41315, 45472, 40526, 4589, 44440, 3184, 4581, 16953, 7585, 45975, 28441, 10956, 22017, 21698, 2107, 44107, 45868, 30293, 15530, 26848, 45705, 811, 22587, 28712, 16591, 45100, 41182, 1225, 40805, 3915, 6545, 8556, 26652, 29708, 24040, 676, 8243, 42597, 17603, 3208, 38902, 15447, 8826, 14791, 38670, 37596, 42980, 17743, 44094, 23778, 32296, 43347, 20210, 6487, 33150, 5095, 35163, 3681, 42450, 21707, 13663, 37987, 13359, 10158, 24531, 21817, 39213, 29424, 38798, 32466, 37354, 27218, 12293, 4133, 14755, 38826, 23328, 48318, 22137, 28379, 35441, 1910, 31964, 26833, 13669, 7484, 43359, 48803, 6853, 47906, 25522, 42533, 16633, 38444, 39544, 13401, 36560, 47222, 1732, 10624, 45339, 24754, 9680, 47728, 4309, 20076, 32836]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 9.552142143249512})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 10.14071273803711})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 11.115730285644531})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 9.052614212036133})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 10.763328552246094})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 10.241353988647461})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 11.621959686279297})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.1822, 'crossentropy': 9.3896453125}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 4.107209205627441})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 3.7565436363220215})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 4.146817207336426})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 4.3508710861206055})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 15952], ['id', 46601], ['ood', 32566], ['id', 42965], ['id', 1504]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6300787161482029, 1.1897350722584887, 1.598464769584559, 1.9629587853797825, 2.2621863602962398]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 7.802016258239746})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 10.085748672485352})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 7.278385639190674})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 11.267366409301758})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.1788, 'crossentropy': 8.357828125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 3.49825119972229})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 3.5943498611450195})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 3.289335250854492})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 18340], ['ood', 62776], ['id', 38561], ['id', 6470], ['id', 46680]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.811652549021824, 1.4728889003544126, 2.045392591047188, 2.513703390205384, 2.90866551738287]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 6.233710765838623})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.977725982666016})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 9.246383666992188})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 10.732690811157227})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 7.4695234298706055})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.1967, 'crossentropy': 5.95206640625}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 3.319708824157715})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 3.653461456298828})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 3.550130844116211})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 3.4976513385772705})
store['active_learning_steps'][2]['eval_training']['best_epoch']=4
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 10541], ['id', 2616], ['id', 12913], ['id', 11825], ['id', 23175]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.47846250858591066, 0.9297069590311287, 1.2778037498346713, 1.5877535343589342, 1.8808937380940707]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 13.26701545715332})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 9.769214630126953})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 9.27204418182373})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 8.882196426391602})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 8.167344093322754})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 8.434514045715332})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 8.78874397277832})
store['active_learning_steps'][3]['training']['best_epoch']=4
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.2004, 'crossentropy': 9.0921765625}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 3.5232205390930176})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 3.589651107788086})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.444445848464966})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.7082033157348633})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 3.6661734580993652})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.8316240310668945})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 16637], ['id', 11473], ['id', 16625], ['ood', 3159], ['id', 41946]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.7018294001485985, 1.3436996991485932, 1.8446289857854001, 2.2656282749631544, 2.632648276658477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 7.703049182891846})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 7.223284721374512})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 6.583264350891113})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 7.682616233825684})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 9.794157028198242})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 7.0612287521362305})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 7.7382001876831055})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 7.8173136711120605})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 8.632555961608887})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 8.689350128173828})
store['active_learning_steps'][4]['training']['best_epoch']=7
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.2075, 'crossentropy': 7.91685546875}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 3.687081813812256})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 3.4472179412841797})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.4470043182373047})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 3.5210182666778564})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 3.6320433616638184})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 3.8146581649780273})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 4.083516597747803})
store['active_learning_steps'][4]['eval_training']['best_epoch']=4
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 1853], ['id', 41581], ['id', 31765], ['id', 20371], ['id', 5021]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5585417931883538, 1.0935815815449157, 1.57963530009108, 2.028034333101131, 2.3920526410359653]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 4.917762756347656})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 5.5794196128845215})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 4.993101119995117})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 6.560559272766113})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 6.954845428466797})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.2302, 'crossentropy': 5.64145078125}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 2.9934451580047607})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 2.929810047149658})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 2.824352502822876})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.4920849800109863})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 55468], ['ood', 46112], ['id', 39627], ['id', 6682], ['id', 48135]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6153218040526559, 1.1174916397220511, 1.5974750724949782, 1.9800416658247775, 2.3191670868441223]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 8.970598220825195})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 6.113397598266602})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.704217910766602})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 6.369332313537598})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 5.02944278717041})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.97728967666626})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 11.476934432983398})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 5.604727745056152})
store['active_learning_steps'][6]['training']['best_epoch']=5
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.2393, 'crossentropy': 5.2315546875}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 2.8503940105438232})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 2.611976146697998})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.005606174468994})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 2.7003002166748047})
store['active_learning_steps'][6]['eval_training']['best_epoch']=1
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 6929], ['id', 22679], ['id', 32920], ['id', 21542], ['id', 5649]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6115251810276956, 1.1594626104467336, 1.5944268869584235, 1.9664579585978395, 2.2966037175083844]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 11.507625579833984})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 7.373260021209717})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 6.1787919998168945})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 5.336483955383301})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.523657321929932})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 5.256537914276123})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 6.3088226318359375})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 6.3210554122924805})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 7.508644104003906})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 6.4624834060668945})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 6.291095733642578})
store['active_learning_steps'][7]['training']['best_epoch']=8
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.2572, 'crossentropy': 6.388183203125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 2.577068328857422})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 2.4656918048858643})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 2.8700366020202637})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 3.1535816192626953})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 2.7181882858276367})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 3.0446627140045166})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 3.248383045196533})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 3.1489951610565186})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 3.347050428390503})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 3.2263357639312744})
store['active_learning_steps'][7]['eval_training']['best_epoch']=10
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 5473], ['id', 31846], ['ood', 65197], ['id', 43566], ['id', 36010]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7180312731347258, 1.3007705615988647, 1.7813017445386001, 2.2081633183563003, 2.5652139848277775]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.448342323303223})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 6.880191326141357})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 5.213709354400635})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 5.760679721832275})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 7.0504231452941895})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 5.124677658081055})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 7.216245651245117})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 5.7515058517456055})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 5.011445045471191})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 5.5192413330078125})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 5.445570945739746})
store['active_learning_steps'][8]['training']['best_epoch']=8
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.2349, 'crossentropy': 5.812559375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 2.8886024951934814})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.0092267990112305})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 2.9231696128845215})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 3.386162281036377})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 3.1596322059631348})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.942045211791992})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 3.0481441020965576})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 3.103262424468994})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 3.2244925498962402})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 2.993399143218994})
store['active_learning_steps'][8]['eval_training']['best_epoch']=7
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 35120], ['id', 47996], ['id', 27820], ['id', 38785], ['id', 23660]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6305005071988301, 1.2303070734748056, 1.6957203354233306, 2.096440824344917, 2.4217630134001267]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 5.07345724105835})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 8.534730911254883})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 5.219552993774414})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.8592753410339355})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 5.323260307312012})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 6.414350509643555})
store['active_learning_steps'][9]['training']['best_epoch']=3
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.2498, 'crossentropy': 5.445616015625}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 2.60085391998291})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 2.945112466812134})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 2.9768941402435303})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 2.69903826713562})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 3.089919090270996})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 28965], ['id', 4876], ['id', 32747], ['ood', 32013], ['id', 29067]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5616537533853176, 1.0224357143462433, 1.448868014269462, 1.8229679344762229, 2.1482589252507074]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 6.917087078094482})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 5.718390464782715})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 5.228756904602051})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 4.91652774810791})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 5.380982398986816})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.2677, 'crossentropy': 5.988487109375}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 4.576714038848877})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 2.8804194927215576})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 2.6654210090637207})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 3.012674331665039})
store['active_learning_steps'][10]['eval_training']['best_epoch']=3
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 38360], ['id', 13414], ['id', 20613], ['id', 38509], ['ood', 70189]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5814742481539766, 1.101755256198992, 1.5299382871739278, 1.8832990218118244, 2.2009969713196353]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 3.855703115463257})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 4.081560134887695})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 4.181159019470215})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 5.596681594848633})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.2493, 'crossentropy': 3.8014171875}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 2.4198288917541504})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 2.5238780975341797})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 2.808335781097412})
store['active_learning_steps'][11]['eval_training']['best_epoch']=2
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 45538], ['id', 23910], ['id', 20651], ['ood', 52416], ['id', 655]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5601929700981605, 1.0689744598325142, 1.4788336887866809, 1.8403556290580765, 2.1424021960216306]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 3.981194257736206})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 3.9109201431274414})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.451485633850098})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 5.836493015289307})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 5.130613327026367})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 5.393655776977539})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 5.36601448059082})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 5.688262939453125})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 5.228409767150879})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 4.90524959564209})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 5.048142433166504})
store['active_learning_steps'][12]['training']['best_epoch']=8
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.2591, 'crossentropy': 5.7860484375}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 2.65378999710083})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 2.3893885612487793})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 2.6563990116119385})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.57249116897583})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 2.9330806732177734})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 2.7748005390167236})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 3.020418643951416})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 1672], ['id', 6227], ['ood', 60007], ['id', 30477], ['id', 3680]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6364918996991817, 1.183645505237667, 1.6507396382054864, 2.0478737680460313, 2.377567968640931]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 3.262624502182007})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 4.482767581939697})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 4.256741523742676})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 5.9635419845581055})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 5.677092552185059})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 4.790402412414551})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.2616, 'crossentropy': 4.5416375}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 2.995105743408203})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 2.3449249267578125})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 2.457958936691284})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.5861024856567383})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 2.4465041160583496})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 12092], ['id', 24839], ['id', 42952], ['id', 33918], ['id', 4256]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4235496886699286, 0.8261591699282427, 1.1778217028059816, 1.4803722986883292, 1.7635299587746882]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 3.332916736602783})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 4.590723037719727})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 5.291341781616211})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.3154296875, 'crossentropy': 4.989346504211426})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 4.155606269836426})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 4.949323654174805})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 5.180995464324951})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.2864, 'crossentropy': 5.088355859375}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.2707395553588867})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 2.8084375858306885})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 3.2782163619995117})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 2.403470039367676})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 3.1380786895751953})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.3115234375, 'crossentropy': 2.5892443656921387})
store['active_learning_steps'][14]['eval_training']['best_epoch']=6
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 24557], ['id', 3121], ['id', 39513], ['id', 32425], ['id', 45798]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6058967679808538, 1.1707981963141059, 1.5935371136154606, 1.9401036044139182, 2.248917385546285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 3.799013137817383})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 3.833909749984741})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.414935111999512})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 4.637591361999512})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 4.4828691482543945})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.567741870880127})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 5.4928388595581055})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 4.194387435913086})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 5.814919471740723})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.199090003967285})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 4.691989898681641})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 5.817614555358887})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 5.384072303771973})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 5.5462236404418945})
store['active_learning_steps'][15]['training']['best_epoch']=11
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.2549, 'crossentropy': 4.8932421875}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 2.9658873081207275})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.957916021347046})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 3.234715461730957})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 3.0410239696502686})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 2.8102688789367676})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 3.1930108070373535})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 2.930434226989746})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 3.1121912002563477})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 3.0232114791870117})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 3.0558483600616455})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 2.974191188812256})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 3.268833637237549})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 3.0739731788635254})
store['active_learning_steps'][15]['eval_training']['best_epoch']=11
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 33813], ['id', 16639], ['ood', 23311], ['id', 30578], ['id', 21936]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5124758311682518, 0.9840920134938036, 1.4337212378042552, 1.7817259539338028, 2.1054473765593]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 2.8021740913391113})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 4.321653366088867})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.166172504425049})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 5.114714622497559})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 4.633152008056641})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 5.646060943603516})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 4.694211006164551})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 7.043675422668457})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 5.135787010192871})
store['active_learning_steps'][16]['training']['best_epoch']=6
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.2707, 'crossentropy': 5.471162890625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 2.5854268074035645})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 2.7595407962799072})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 2.892587900161743})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 2.6619396209716797})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.373422861099243})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 2.8427014350891113})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 3.036547899246216})
store['active_learning_steps'][16]['eval_training']['best_epoch']=4
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 46470], ['id', 28649], ['id', 9706], ['id', 1220], ['id', 11909]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5819376349690208, 1.105569497102247, 1.5686463965214137, 1.9609766428059228, 2.2961162867752396]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.0479464530944824})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 3.551654815673828})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 5.0197954177856445})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 4.558370113372803})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 4.859533786773682})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.879027843475342})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.2683, 'crossentropy': 5.186211328125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 3.516758918762207})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 2.8035974502563477})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 3.023332118988037})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 2.805476665496826})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 3.3356447219848633})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 16245], ['id', 43361], ['id', 14399], ['id', 33493], ['id', 8401]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5764098541083745, 1.0545827406155461, 1.508067221959644, 1.843900821230898, 2.146158987169624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 5.547489166259766})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.837799072265625})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 4.256107330322266})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 5.395118713378906})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 4.344475746154785})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 4.87114143371582})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 4.960365295410156})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.3125, 'crossentropy': 5.288718223571777})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 4.535911560058594})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 4.891980171203613})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 4.526750564575195})
store['active_learning_steps'][18]['training']['best_epoch']=8
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.2794, 'crossentropy': 5.418971875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 2.594574451446533})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 2.4585018157958984})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.9763870239257812})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 2.6089160442352295})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 2.698153495788574})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 2.7362287044525146})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 2.7636141777038574})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 2.87331223487854})
store['active_learning_steps'][18]['eval_training']['best_epoch']=5
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 16559], ['id', 17620], ['id', 7516], ['id', 7456], ['id', 40025]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6334960441679831, 1.2102011532391104, 1.7191979841538885, 2.15413033539812, 2.515421781502993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.24271821975708})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 3.6154298782348633})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.367401599884033})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 4.479449272155762})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 5.012085437774658})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 4.895734786987305})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.360688209533691})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 5.295289993286133})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 4.40707540512085})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 5.846940517425537})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 5.235072135925293})
store['active_learning_steps'][19]['training']['best_epoch']=8
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.2736, 'crossentropy': 5.25691328125}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 2.2564496994018555})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 2.823256015777588})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 2.8089213371276855})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 2.7516708374023438})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.5961594581604004})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 2.8212122917175293})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 2.750377655029297})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 2.649251937866211})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 3.2729549407958984})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 48973], ['id', 27959], ['id', 5297], ['id', 10839], ['id', 31873]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7380947640448754, 1.374153997964707, 1.8127442587760836, 2.186046416806776, 2.516299094622635]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 3.4595885276794434})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 4.592514991760254})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 3.7883808612823486})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 3.732822895050049})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 4.903392314910889})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.059600830078125})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 5.4589996337890625})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 5.191897869110107})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.2673, 'crossentropy': 4.90798515625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 2.355524778366089})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 2.53680682182312})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.577484130859375})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.6005213260650635})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 2.536926746368408})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 2.656160354614258})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 2.7163267135620117})
store['active_learning_steps'][20]['eval_training']['best_epoch']=7
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 17819], ['id', 6282], ['id', 47180], ['id', 9589], ['id', 9579]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5599925913321856, 1.06058939877726, 1.4319611749345382, 1.7731245667952957, 2.061983864535855]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 3.061217784881592})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 4.673125267028809})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 3.3242218494415283})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 5.814654350280762})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.221684455871582})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 4.729427814483643})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 4.4130353927612305})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 4.816258430480957})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 5.193357467651367})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.2784, 'crossentropy': 4.5943546875}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 2.3466949462890625})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 2.713599681854248})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 2.6190357208251953})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 2.360572338104248})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 2.635772943496704})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.6395177841186523})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.7397561073303223})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 2.667782783508301})
store['active_learning_steps'][21]['eval_training']['best_epoch']=8
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 14883], ['id', 22229], ['id', 48192], ['id', 15366], ['id', 36724]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6153159908444357, 1.0933978247461176, 1.5571730247968374, 1.8988501996235068, 2.1876074189644257]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 3.8277978897094727})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 3.9492087364196777})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 3.6021900177001953})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.969581604003906})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 4.948285102844238})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 4.144073486328125})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 5.336225509643555})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 4.304043769836426})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 4.802884101867676})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 4.777780532836914})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 6.387202262878418})
store['active_learning_steps'][22]['training']['best_epoch']=8
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.3018, 'crossentropy': 4.29855859375}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 2.2882637977600098})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 2.3839035034179688})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.2910728454589844})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 3.061587333679199})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.3212890625, 'crossentropy': 2.539694309234619})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 2.601019859313965})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.3115234375, 'crossentropy': 2.8263356685638428})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 2.9794750213623047})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 21856], ['ood', 63309], ['id', 16081], ['id', 40975], ['id', 42613]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5968948095371414, 1.1288172552828728, 1.5816130238568746, 1.9723430166158362, 2.2901884314487813]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 2.8048250675201416})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 3.3202877044677734})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 4.666826248168945})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.214450836181641})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 4.858716011047363})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 4.383865833282471})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 5.3360915184021})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.3125, 'crossentropy': 4.82431697845459})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 4.591684341430664})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 4.4650373458862305})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 4.101528167724609})
store['active_learning_steps'][23]['training']['best_epoch']=8
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.3084, 'crossentropy': 5.0154734375}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 2.268017530441284})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 2.3252973556518555})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 2.785820484161377})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 2.3381810188293457})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.3203125, 'crossentropy': 2.4298295974731445})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.322265625, 'crossentropy': 2.5943965911865234})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.3154296875, 'crossentropy': 2.503159761428833})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.30859375, 'crossentropy': 2.48160982131958})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.30859375, 'crossentropy': 2.570962429046631})
store['active_learning_steps'][23]['eval_training']['best_epoch']=6
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 16562], ['id', 33648], ['id', 15341], ['id', 33930], ['id', 15589]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5766739034089619, 1.1124368384559347, 1.5516979994457882, 1.945526230936104, 2.3037690208877857]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 3.1390089988708496})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 4.363540172576904})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.3134765625, 'crossentropy': 3.93679141998291})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 4.61642599105835})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 3.8850183486938477})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 4.001023769378662})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.2949, 'crossentropy': 3.9645}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 2.705045223236084})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 2.6089789867401123})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 2.8371009826660156})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 2.4342856407165527})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 2.482017755508423})
store['active_learning_steps'][24]['eval_training']['best_epoch']=5
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 10197], ['id', 32654], ['id', 46164], ['id', 739], ['id', 8812]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4931193962257463, 0.9559666468648662, 1.3007876007062165, 1.6096116540556795, 1.8882202695745622]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 3.0715126991271973})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 3.175175905227661})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 4.108290195465088})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 4.742926597595215})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.318359375, 'crossentropy': 4.018394470214844})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.3173828125, 'crossentropy': 4.215007781982422})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.3134765625, 'crossentropy': 5.064393043518066})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.3203125, 'crossentropy': 4.8426337242126465})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.314453125, 'crossentropy': 5.910722732543945})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 5.055502891540527})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 4.596963882446289})
store['active_learning_steps'][25]['training']['best_epoch']=8
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.3165, 'crossentropy': 4.84216640625}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 2.8712663650512695})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.407196283340454})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 2.3430018424987793})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.4466500282287598})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.31640625, 'crossentropy': 2.3582892417907715})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 2.837233066558838})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 2.768141746520996})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 2.641317129135132})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 6687], ['id', 40671], ['ood', 51617], ['id', 6065], ['id', 26796]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5340191846254108, 1.0452146508453435, 1.511967724820316, 1.916866112081193, 2.259905274616181]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.275490760803223})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 4.318535804748535})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 3.588372230529785})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 3.6745853424072266})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 4.789617538452148})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 3.984618663787842})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 5.0776472091674805})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.31640625, 'crossentropy': 4.3443603515625})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 4.702502250671387})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.3076171875, 'crossentropy': 4.525166988372803})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 4.861490249633789})
store['active_learning_steps'][26]['training']['best_epoch']=8
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.3058, 'crossentropy': 4.33941015625}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 2.16817045211792})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 2.3520524501800537})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 2.623755931854248})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.3154296875, 'crossentropy': 2.4829750061035156})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 2.5919833183288574})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 2.7347981929779053})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 2.6718411445617676})
store['active_learning_steps'][26]['eval_training']['best_epoch']=4
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 39685], ['id', 20564], ['id', 47458], ['id', 41866], ['id', 9489]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4701902739335879, 0.9086521534879353, 1.3202289672264866, 1.683867704809543, 2.0164095362464405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 2.6518120765686035})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 3.708937644958496})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 2.981217622756958})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 3.8841357231140137})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.3154296875, 'crossentropy': 4.017230033874512})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 4.608192443847656})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 4.722475051879883})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.314453125, 'crossentropy': 4.395656108856201})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.3052, 'crossentropy': 4.256355859375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 2.378615140914917})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 2.3864095211029053})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 2.6781511306762695})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 2.4817402362823486})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 2.8174350261688232})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.3193359375, 'crossentropy': 2.497281551361084})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.3699452877044678})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 21523], ['id', 33237], ['id', 41787], ['id', 20880], ['id', 36654]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5305100066640106, 0.9657075724611093, 1.3536669499893788, 1.6856275857769099, 1.975134893198284]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 2.704890251159668})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 4.677839279174805})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.3173828125, 'crossentropy': 3.2029151916503906})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 4.071619987487793})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 3.5258123874664307})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 4.800307273864746})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.3116, 'crossentropy': 3.178281640625}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 2.4821596145629883})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 2.278076648712158})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.558712959289551})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 2.4969277381896973})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 2.4702303409576416})
store['active_learning_steps'][28]['eval_training']['best_epoch']=2
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 18605], ['id', 37767], ['id', 28109], ['id', 17070], ['id', 43105]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5061987809335965, 0.9265061668964902, 1.3012863635374332, 1.6043688472016098, 1.8671577027167858]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 2.670701503753662})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 3.13297700881958})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 3.722914218902588})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.3076171875, 'crossentropy': 3.3934614658355713})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 4.954651355743408})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 4.334167003631592})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.3076171875, 'crossentropy': 4.269874572753906})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.3062, 'crossentropy': 3.60112890625}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 2.550748586654663})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.3125, 'crossentropy': 2.2221250534057617})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.3291015625, 'crossentropy': 2.247131109237671})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 2.5213077068328857})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.3095703125, 'crossentropy': 2.3476438522338867})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.3115234375, 'crossentropy': 2.3944482803344727})
store['active_learning_steps'][29]['eval_training']['best_epoch']=3
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 48137], ['id', 10969], ['id', 46476], ['id', 23916], ['id', 31284]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.36486876378540584, 0.7152918735094181, 0.995458010944962, 1.2553514143766318, 1.4961797579847618]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.442152976989746})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.728940725326538})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 4.305573463439941})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 3.1341495513916016})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 4.11269474029541})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 4.4580078125})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 4.553252220153809})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 4.582100868225098})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.2954, 'crossentropy': 4.016981640625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.638123035430908})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 2.6144471168518066})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 2.472959518432617})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 2.3960440158843994})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 2.799532651901245})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 2.7174272537231445})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.8777530193328857})
store['active_learning_steps'][30]['eval_training']['best_epoch']=5
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 3725], ['id', 20835], ['id', 30942], ['id', 45002], ['id', 42702]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5119521902879932, 0.9753778583732098, 1.3572973777534059, 1.6932083158731057, 2.000355695973732]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 2.4571404457092285})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 3.662104845046997})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 3.0741844177246094})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 4.445760726928711})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 3.693391799926758})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 4.792971611022949})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 3.3585352897644043})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 4.58288049697876})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 4.739145278930664})
store['active_learning_steps'][31]['training']['best_epoch']=6
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.3001, 'crossentropy': 4.558941796875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 2.4941697120666504})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 2.360055446624756})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 2.286153793334961})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 2.347926616668701})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 2.5149755477905273})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 2.6004691123962402})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.30859375, 'crossentropy': 2.518627643585205})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 2.801379442214966})
store['active_learning_steps'][31]['eval_training']['best_epoch']=7
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 21472], ['id', 22804], ['id', 11674], ['id', 7299], ['id', 22898]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.47117357500410306, 0.8498068100775811, 1.2164685806594462, 1.5563998964771661, 1.8467732220551722]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 2.63287353515625})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 3.8958587646484375})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 3.611506938934326})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.3154296875, 'crossentropy': 3.062347412109375})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 3.390399932861328})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 4.624176979064941})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 4.69028377532959})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.3018, 'crossentropy': 3.1767892578125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 2.4051666259765625})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.254305839538574})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 2.353804588317871})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 2.4056684970855713})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.3125, 'crossentropy': 2.2194318771362305})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 2.321884870529175})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 12110], ['id', 44614], ['ood', 23540], ['id', 2635], ['id', 42928]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.4320930871698362, 0.8210090687493627, 1.1284121587710092, 1.4049711147127821, 1.6509634487914306]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 2.633472442626953})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 3.0192484855651855})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 3.655503988265991})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 3.3850648403167725})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 4.060410499572754})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.328125, 'crossentropy': 3.9648191928863525})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 5.561236381530762})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 5.9521002769470215})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 4.234472274780273})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.3133, 'crossentropy': 3.96690390625}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 2.238680839538574})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 2.297865867614746})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.30859375, 'crossentropy': 2.618074417114258})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.306640625, 'crossentropy': 2.484400510787964})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 2.532045364379883})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.310546875, 'crossentropy': 2.434035301208496})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 2.5256576538085938})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.310546875, 'crossentropy': 2.455110549926758})
store['active_learning_steps'][33]['eval_training']['best_epoch']=6
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 31361], ['id', 459], ['ood', 12130], ['id', 4389], ['id', 15576]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.49499942338189207, 0.9214624809771461, 1.2848457792213246, 1.6194882090132334, 1.9142055718835636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 2.9200191497802734})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.46657395362854})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.684049129486084})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 2.9929494857788086})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 4.105950355529785})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 3.392411231994629})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 4.587515354156494})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 4.370423793792725})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.3115234375, 'crossentropy': 4.180506706237793})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.922788619995117})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.3115234375, 'crossentropy': 4.859259128570557})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 4.016705513000488})
store['active_learning_steps'][34]['training']['best_epoch']=9
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.3005, 'crossentropy': 4.1876046875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 2.333941698074341})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 2.3802084922790527})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 2.272657632827759})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 2.305785894393921})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 2.874889850616455})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 2.697913646697998})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 2.468343496322632})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.310546875, 'crossentropy': 2.507962226867676})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 2.6013689041137695})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 2.602814197540283})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.656050682067871})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 43065], ['id', 45190], ['id', 22607], ['id', 3572], ['id', 42286]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5154159516812132, 0.9254229480355334, 1.2993160684360632, 1.6509165520117017, 1.9422161829761198]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.093743324279785})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 3.0072274208068848})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 3.754157066345215})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 4.192136287689209})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 3.378065586090088})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2822265625, 'crossentropy': 4.364394664764404})
store['active_learning_steps'][35]['training']['best_epoch']=3
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.301, 'crossentropy': 3.506953515625}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 2.4007785320281982})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.6357786655426025})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.6052186489105225})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 2.846445083618164})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 2.7265748977661133})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 21235], ['id', 32697], ['id', 24627], ['id', 36576], ['id', 3753]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5160550592098128, 0.8215327644977806, 1.1129795817692316, 1.3701522828616848, 1.5970355226563688]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 2.601484775543213})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 2.9137673377990723})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.8315324783325195})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 3.409952163696289})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 4.337873458862305})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 3.8237252235412598})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 4.321193695068359})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 3.872598648071289})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.3115234375, 'crossentropy': 4.4800214767456055})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.30078125, 'crossentropy': 4.544798374176025})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 4.440333366394043})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 7.0038042068481445})
store['active_learning_steps'][36]['training']['best_epoch']=9
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.3177, 'crossentropy': 4.251712890625}
