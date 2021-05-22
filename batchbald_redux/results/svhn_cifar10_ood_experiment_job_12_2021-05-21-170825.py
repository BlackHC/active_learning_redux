store = {}
store['timestamp']=1621613305
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=12']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=12
store['worker_id']=12
store['num_workers']=24
store['config']={'seed': 1247, 'uniform_ood': True, 'id_dataset_name': 'CIFAR-10', 'ood_dataset_name': 'SVHN', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node | one_hot_targets{'num_classes': 10}) + ('SVHN (Train, seed=0, 73257 samples)' | uniform_targets{'num_classes': 10})", 'test': "'CIFAR-10 (Test)'"}
store['initial_training_set_indices']=[12980, 44617, 6984, 21168, 33976, 35571, 33058, 43729, 26944, 24745, 66, 14046, 46542, 39478, 6000, 5915, 39360, 20774, 27084, 44464]
store['evaluation_set_indices']=[3812, 42704, 6729, 38942, 48125, 16968, 5652, 4045, 10740, 19606, 37062, 15768, 44824, 47581, 19482, 4628, 25290, 27933, 27441, 5508, 35131, 18717, 43561, 37318, 8187, 37590, 45717, 1493, 5924, 19803, 23554, 6460, 2962, 36049, 18273, 11023, 27366, 39007, 5305, 46743, 15798, 44136, 20072, 20717, 1152, 8194, 36500, 17618, 35054, 18973, 45734, 16753, 6410, 28807, 8902, 20957, 6625, 41155, 1332, 47376, 36719, 11500, 36383, 7417, 30371, 19517, 33334, 27185, 29033, 42916, 39943, 34789, 18504, 7348, 6096, 28402, 10058, 12011, 34663, 1618, 17887, 41306, 1467, 28071, 12667, 38339, 44920, 44374, 14769, 31145, 21575, 16685, 24836, 48736, 21176, 26844, 45671, 22164, 42503, 10770, 27020, 30182, 37164, 33354, 47307, 17878, 26665, 40819, 14805, 201, 47956, 44739, 8060, 45495, 8139, 27034, 40800, 21802, 18878, 8672, 41175, 48917, 23272, 9952, 23154, 37915, 18669, 18159, 13468, 14436, 16099, 8128, 33349, 31445, 7202, 21948, 10215, 34670, 538, 40015, 17530, 11133, 6028, 12100, 21106, 5614, 30720, 34210, 39322, 40006, 31808, 24717, 34090, 17381, 18164, 17668, 16984, 37856, 41017, 43216, 46788, 26334, 6887, 40485, 39838, 1931, 47231, 37148, 801, 14067, 31951, 7105, 34561, 18698, 45258, 21399, 18558, 26959, 17240, 30502, 39056, 47625, 18880, 37323, 26204, 21788, 1674, 47188, 10526, 25980, 27994, 19871, 22250, 38761, 7182, 14241, 235, 37616, 39973, 35218, 46446, 33361, 39076, 38899, 15578, 36667, 5551, 23088, 32496, 5705, 23255, 25559, 11975, 44032, 45743, 23571, 30475, 15184, 41327, 15827, 33432, 37357, 40250, 16421, 2561, 8533, 25715, 17074, 36811, 30099, 44174, 8029, 1480, 43701, 10198, 38802, 13200, 31615, 28252, 17879, 18749, 16580, 19178, 48034, 4365, 4796, 46033, 47538, 7188, 45076, 13569, 28392, 19457, 41335, 4474, 23022, 11289, 25103, 35813, 40336, 12008, 36695, 28598, 12671, 48831, 18364, 9890, 11804, 37612, 31396, 10683, 31008, 36360, 15312, 26328, 41353, 34761, 4398, 46637, 13891, 32787, 22410, 26463, 4503, 31374, 26143, 7765, 27551, 15340, 16182, 7868, 42518, 34516, 8244, 13037, 39992, 14300, 48188, 42511, 2963, 28224, 28657, 5474, 19682, 682, 25867, 47518, 36303, 18452, 34447, 24821, 36157, 48089, 25120, 44689, 6509, 1852, 17387, 19405, 39441, 42197, 14298, 16443, 1151, 9775, 10834, 44482, 10445, 41434, 37644, 5702, 29159, 17097, 28308, 42161, 29973, 38602, 4592, 24411, 38792, 25200, 28299, 5522, 4441, 4065, 12187, 32012, 41361, 36098, 25224, 27204, 29536, 18785, 28218, 42361, 10437, 8978, 44209, 7804, 35232, 3041, 23251, 41265, 28139, 41350, 18536, 37181, 25352, 16787, 27537, 29568, 45681, 33891, 35667, 31031, 5795, 23494, 7658, 26711, 35750, 34571, 4852, 29601, 14492, 5318, 26987, 11839, 533, 29565, 16424, 43853, 34375, 26710, 37956, 34492, 46294, 12920, 7945, 29669, 14520, 36081, 14478, 37173, 19188, 40253, 23549, 741, 34309, 11001, 6995, 10899, 36881, 7002, 19049, 13388, 40737, 9210, 22684, 43970, 7048, 46803, 45248, 4726, 40534, 23790, 47216, 8585, 7880, 25042, 306, 11939, 45003, 12905, 4052, 45391, 28968, 19408, 6012, 7814, 27790, 10979, 2005, 32156, 16025, 23706, 8236, 24750, 39229, 6968, 7599, 32427, 48001, 12257, 6899, 36229, 19760, 30468, 32347, 15232, 17555, 34373, 1157, 22434, 38137, 3717, 38235, 41506, 10786, 3175, 48043, 24171, 29368, 39765, 16373, 22973, 42399, 32908, 35630, 28508, 29334, 37539, 45770, 29181, 10946, 18072, 18511, 47354, 31444, 42643, 4078, 45028, 45610, 35405, 33751, 7967, 4701, 13378, 48105, 22116, 20599, 45454, 7325, 11304, 12289, 46114, 8359, 41073, 22751, 19402, 8483, 45656, 5604, 9134, 35979, 19757, 43627, 35248, 23566, 727, 34909, 43560, 2888, 12158, 48248, 2094, 47190, 15295, 27629, 15047, 4402, 32595, 6538, 13474, 11538, 10736, 29892, 29786, 1884, 45940, 2144, 37537, 5222, 26418, 10690, 19114, 30223, 17188, 41379, 46182, 20359, 32256, 43739, 41935, 16411, 15933, 22295, 940, 8665, 1154, 32089, 46513, 17506, 39407, 6187, 7878, 37671, 25414, 16789, 37546, 44170, 9921, 22033, 33690, 23656, 5226, 1631, 8671, 45821, 34099, 40039, 31342, 35231, 29621, 31899, 1023, 17082, 38261, 26917, 31921, 5241, 37282, 45513, 46687, 18915, 10796, 8986, 31711, 2185, 29316, 45090, 13383, 5741, 7930, 39306, 13675, 38034, 29826, 48781, 21746, 39559, 31318, 19965, 25443, 45862, 30730, 9611, 43077, 23902, 9541, 38859, 13973, 27923, 25754, 38295, 39261, 15442, 40254, 28002, 23139, 44524, 11458, 10297, 25299, 13617, 28750, 1835, 29505, 23873, 45073, 34640, 5831, 29115, 26568, 6588, 31067, 15001, 4887, 27814, 17283, 23813, 43511, 14398, 13500, 7428, 11090, 11751, 36607, 9712, 43583, 45864, 39972, 14617, 3431, 26470, 33191, 18204, 24481, 28879, 43889, 15015, 36437, 12660, 37650, 405, 36212, 42818, 10677, 15723, 24514, 35518, 42654, 44052, 10218, 37297, 34741, 40715, 37290, 29931, 29774, 25075, 12136, 44466, 25236, 7096, 26190, 14575, 41698, 9068, 24101, 3379, 19906, 15856, 38317, 20799, 17172, 5987, 140, 11530, 38636, 9116, 11151, 25071, 182, 31603, 21547, 47739, 13909, 624, 25621, 30173, 37807, 7053, 30625, 10450, 22316, 23965, 5028, 37725, 1675, 45751, 19683, 26061, 34327, 38096, 30828, 438, 46574, 9121, 4859, 15563, 33935, 39481, 48048, 37730, 35947, 18461, 22658, 35939, 3507, 16223, 5279, 9615, 13583, 28557, 36129, 19326, 23956, 31469, 3397, 36813, 4416, 48955, 27367, 9692, 41380, 27998, 33372, 24467, 24186, 47802, 16612, 46008, 3943, 48514, 42699, 37077, 17401, 39288, 44878, 31226, 14334, 44847, 7473, 42669, 32658, 40101, 11309, 853, 12919, 41501, 26725, 3843, 41314, 16050, 39323, 5916, 19945, 17950, 48824, 8856, 12778, 28765, 13275, 34339, 8883, 36161, 41767, 44449, 7357, 3967, 41737, 3432, 27375, 5603, 1739, 2418, 23760, 26549, 2676, 11659, 40405, 46217, 5207, 28673, 12645, 45982, 48103, 21541, 33384, 28830, 46313, 2540, 17302, 42509, 2321, 40265, 21290, 35387, 48490, 11327, 16529, 40097, 16839, 12570, 17132, 18289, 20343, 22077, 21098, 5426, 8478, 1923, 4941, 48459, 34289, 38039, 44848, 20094, 25546, 19669, 32606, 16624, 28652, 11887, 22863, 48068, 9574, 39941, 2068, 28297, 7225, 41330, 47575, 30080, 25197, 25710, 18030, 16190, 21185, 46949, 1377, 47189, 30166, 28575, 12032, 14160, 11813, 48219, 39348, 42953, 46300, 5559, 15360, 14665, 25279, 42955, 43707, 10089, 10928, 16650, 18156, 4140, 2816, 45019, 25339, 16628, 3925, 25879, 43725, 33970, 17789, 20083, 8873, 41315, 45472, 40526, 4589, 44440, 3184, 4581, 16953, 7585, 45975, 28441, 10956, 22017, 21698, 2107, 44107, 45868, 30293, 15530, 26848, 45705, 811, 22587, 28712, 16591, 45100, 41182, 1225, 40805, 3915, 6545, 8556, 26652, 29708, 24040, 676, 8243, 42597, 17603, 3208, 38902, 15447, 8826, 14791, 38670, 37596, 42980, 17743, 44094, 23778, 32296, 43347, 20210, 6487, 33150, 5095, 35163, 3681, 42450, 21707, 13663, 37987, 13359, 10158, 24531, 21817, 39213, 29424, 38798, 32466, 37354, 27218, 12293, 4133, 14755, 38826, 23328, 48318, 22137, 28379, 35441, 1910, 31964, 26833, 13669, 7484, 43359, 48803, 6853, 47906, 25522, 42533, 16633, 38444, 39544, 13401, 36560, 47222, 1732, 10624, 45339, 24754, 9680, 47728, 4309, 20076, 32836]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 11.774261474609375})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 11.583006858825684})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 12.158781051635742})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 10.094687461853027})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 11.212566375732422})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 12.9017333984375})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 10.997697830200195})
store['active_learning_steps'][0]['training']['best_epoch']=4
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.1789, 'crossentropy': 10.592109375}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 27836], ['id', 10597], ['id', 13879], ['ood', 22632], ['ood', 50597]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.9804270958422652, 1.6392554398402917, 2.242066513876589, 2.713062484661613, 3.1268344217648982]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 9.009071350097656})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 8.003692626953125})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 8.586494445800781})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 8.902830123901367})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.1626, 'crossentropy': 9.4136734375}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 10157], ['ood', 32748], ['ood', 64128], ['id', 15314], ['id', 27251]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8748121910496658, 1.5396795504443959, 2.0315554220070315, 2.457565878337764, 2.8051299817083377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 5.728903770446777})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.63420295715332})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 6.081517696380615})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 6.172025680541992})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 8.440101623535156})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 8.022686004638672})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 6.739950656890869})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 7.546526908874512})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 6.890430450439453})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 7.584232330322266})
store['active_learning_steps'][2]['training']['best_epoch']=7
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.2004, 'crossentropy': 6.74186796875}
store['active_learning_steps'][2]['acquisition']={'indices': [['ood', 53587], ['ood', 51543], ['ood', 50203], ['ood', 6217], ['id', 31765]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6944684140498885, 1.3343711783488623, 1.8425680381409872, 2.3229159988137056, 2.751400941412218]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 5.020049095153809})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 6.113016128540039})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.349987030029297})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 7.307782173156738})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.1842, 'crossentropy': 5.110587890625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 42], ['id', 28180], ['id', 33989], ['id', 1388], ['id', 32666]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5912562166246986, 1.1456477747587641, 1.6316213916636984, 2.0476341708278625, 2.4180640987936206]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 4.509530067443848})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.770774841308594})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 4.92188024520874})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.926077842712402})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 8.162393569946289})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 6.480159759521484})
store['active_learning_steps'][4]['training']['best_epoch']=3
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.2164, 'crossentropy': 4.95805703125}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 38685], ['id', 14873], ['id', 44347], ['id', 41752], ['id', 26945]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7213243042381483, 1.309200078721676, 1.868511616201551, 2.3145939821314947, 2.7115651274120722]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 4.536771774291992})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 4.059128284454346})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 7.198744773864746})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 5.304646968841553})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 6.131831169128418})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 7.100438117980957})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 7.543632507324219})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 5.567312240600586})
store['active_learning_steps'][5]['training']['best_epoch']=5
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.1935, 'crossentropy': 6.55635}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 41244], ['id', 48808], ['id', 40569], ['id', 12749], ['id', 2032]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7939470826035642, 1.448317125552249, 1.999466002091829, 2.492126032534973, 2.904399398982086]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 6.301372528076172})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 5.680951118469238})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 4.751666069030762})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 6.699599266052246})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 4.294965744018555})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 7.408415794372559})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.700502395629883})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 4.707733154296875})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 6.320291519165039})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 6.218872547149658})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 7.424545764923096})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 5.499996185302734})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 6.21830940246582})
store['active_learning_steps'][6]['training']['best_epoch']=10
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.1845, 'crossentropy': 6.5707546875}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 10564], ['id', 43972], ['id', 1936], ['id', 46964], ['id', 19847]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.7769976674910473, 1.3825112279644278, 1.9272507507374694, 2.410420101745853, 2.828196948224794]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 3.2525784969329834})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.849553346633911})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 4.2609100341796875})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 4.939841270446777})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 6.851442337036133})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 6.322381496429443})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 5.293119430541992})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.2079, 'crossentropy': 5.1351109375}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 24328], ['id', 31874], ['id', 13674], ['ood', 44588], ['id', 20061]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6627763708127877, 1.209808385244412, 1.6740012647165736, 2.093761259073956, 2.4805369823830006]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 4.058644771575928})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 6.785260200500488})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 6.172696113586426})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 6.352603912353516})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.185674667358398})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.802854537963867})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 6.179202079772949})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 5.580293655395508})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 5.845296859741211})
store['active_learning_steps'][8]['training']['best_epoch']=6
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.2141, 'crossentropy': 5.005328515625}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 23887], ['id', 45646], ['id', 32308], ['id', 14262], ['id', 37233]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6010939521970398, 1.1531318585138126, 1.6747082361647827, 2.1341299572411545, 2.554502616577751]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 3.280829429626465})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 6.69420051574707})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 6.804987907409668})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.873581886291504})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 6.137853622436523})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.939669609069824})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 6.013097763061523})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 6.9835405349731445})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 8.936758041381836})
store['active_learning_steps'][9]['training']['best_epoch']=6
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.1857, 'crossentropy': 6.252575}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 25760], ['id', 16266], ['id', 32489], ['id', 10921], ['id', 19379]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6986461393132111, 1.2951691058440193, 1.8012754253292345, 2.261777056801943, 2.6635160347032585]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.303479194641113})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 4.472875118255615})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.943758010864258})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 5.292158126831055})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 5.2812042236328125})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 6.554633140563965})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.76347541809082})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 6.364791393280029})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 5.980395317077637})
store['active_learning_steps'][10]['training']['best_epoch']=6
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.214, 'crossentropy': 6.113733984375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 6967], ['ood', 62502], ['ood', 10517], ['id', 4819], ['ood', 66280]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6601136076210239, 1.2064088001000828, 1.6936455449794345, 2.1286376136063234, 2.507203334537861]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 2.992189884185791})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 3.922477960586548})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 4.05394172668457})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.579996109008789})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.2006, 'crossentropy': 3.0483572265625}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 45538], ['id', 31353], ['ood', 13197], ['id', 22741], ['ood', 10557]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5353816100298144, 0.9590153133100512, 1.2995451137479073, 1.5849350957251538, 1.8194304897162636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 3.172520399093628})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 3.1965177059173584})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 4.709502220153809})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.913604736328125})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 4.481532096862793})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.465544700622559})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.416229248046875})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.64533805847168})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.2136, 'crossentropy': 4.260853125}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 41965], ['id', 44677], ['id', 23900], ['id', 39487], ['id', 23560]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.57579543076556, 1.1013190846794587, 1.5718842712013714, 2.0140745600364784, 2.3954564293668668]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 5.0326828956604})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 4.380563735961914})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 4.218703746795654})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.179329872131348})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.256133079528809})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 4.709036827087402})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 4.9575629234313965})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.37125301361084})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 6.209299564361572})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 5.675090789794922})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 4.338702201843262})
store['active_learning_steps'][13]['training']['best_epoch']=8
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.2094, 'crossentropy': 5.61924609375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 30898], ['id', 41622], ['id', 2203], ['id', 3710], ['id', 39619]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6424020236142283, 1.1600508070622952, 1.6521843367397695, 2.0999532899609914, 2.4825827223889227]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 4.1877031326293945})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 4.936100959777832})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 3.991389513015747})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.0072340965271})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 5.195636749267578})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 4.6497344970703125})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.2217, 'crossentropy': 4.14621171875}
store['active_learning_steps'][14]['acquisition']={'indices': [['ood', 72837], ['id', 33717], ['id', 23564], ['id', 37283], ['id', 21745]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5731578164419953, 1.0818487101089724, 1.5419127407974655, 1.945557000389229, 2.2991663724820803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 3.2838685512542725})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.347414016723633})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.87900972366333})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 3.496403217315674})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 4.623514175415039})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 5.360528945922852})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 5.123919486999512})
store['active_learning_steps'][15]['training']['best_epoch']=4
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.218, 'crossentropy': 3.578128125}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 46199], ['id', 27935], ['id', 18350], ['id', 44991], ['id', 33504]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5818319134631782, 1.1032238405378525, 1.582733495709407, 1.9896530366365237, 2.377100411567218]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 2.877380609512329})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 3.309770107269287})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 4.058969497680664})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 4.03586483001709})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.305760383605957})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 4.842299461364746})
store['active_learning_steps'][16]['training']['best_epoch']=3
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.2219, 'crossentropy': 4.2040046875}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 4068], ['id', 9855], ['id', 26895], ['id', 18307], ['ood', 65885]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.4727649875785074, 0.9122192158772964, 1.3172847213967667, 1.67866012744196, 1.9862514829044589]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 2.9648571014404297})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 3.7095842361450195})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 3.2948145866394043})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 4.566802978515625})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 4.628228187561035})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.587014675140381})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.211396217346191})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.060969352722168})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 5.715144157409668})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.448528289794922})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 6.063549518585205})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.627569198608398})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.126886367797852})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 4.568848609924316})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 4.816563129425049})
store['active_learning_steps'][17]['training']['best_epoch']=12
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.25, 'crossentropy': 4.4738546875}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 48655], ['id', 43983], ['id', 14356], ['id', 47113], ['id', 38503]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.717261083330798, 1.2464149811567728, 1.7273374651625542, 2.152340353407503, 2.5443905610562645]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.006367206573486})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 7.448452949523926})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 3.411804437637329})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 4.1105146408081055})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 4.269012451171875})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 5.065817832946777})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 4.57942533493042})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 5.863690376281738})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 4.607880115509033})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 4.838256359100342})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 5.384055137634277})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.873172760009766})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.997148036956787})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.51188850402832})
store['active_learning_steps'][18]['training']['best_epoch']=11
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.25, 'crossentropy': 5.2798859375}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 18875], ['id', 28420], ['id', 8294], ['id', 17663], ['id', 8927]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7099776521915881, 1.3807457886110273, 1.9345183429788886, 2.4060427856989275, 2.819852666001899]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 3.823965549468994})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 3.1410446166992188})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 4.083003044128418})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 3.531268835067749})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.485783100128174})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.872494697570801})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 5.353128433227539})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.495067596435547})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.239, 'crossentropy': 4.53832890625}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 3785], ['id', 17823], ['id', 26094], ['id', 38803], ['id', 8423]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5439262385150783, 1.06398848660654, 1.521509173165323, 1.93902545008231, 2.3233965958569556]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 2.9941060543060303})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 4.251601696014404})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 3.735236167907715})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 4.636573791503906})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 4.107847213745117})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.665903091430664})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.166258811950684})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 5.495651721954346})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.2434, 'crossentropy': 4.220330859375}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 6134], ['id', 17449], ['id', 12087], ['id', 17021], ['id', 29404]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5263784471497037, 1.0349502179976704, 1.4640894729270189, 1.8688890915828775, 2.2331735701329407]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 2.8974175453186035})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 2.6309356689453125})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.2297005653381348})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 4.062258243560791})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 3.8656582832336426})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 4.163811683654785})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.565814018249512})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 4.792844295501709})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 4.6045756340026855})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 4.492120742797852})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 4.7024312019348145})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 4.879624843597412})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 4.215773582458496})
store['active_learning_steps'][21]['training']['best_epoch']=10
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.2842, 'crossentropy': 4.60929765625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 34942], ['id', 10653], ['id', 19597], ['id', 6196], ['ood', 59650]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6111518975097827, 1.192406850183438, 1.677239322313424, 2.113629014197096, 2.5238687845218983]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 2.601454734802246})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 2.506923198699951})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 3.1627395153045654})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 5.967119216918945})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.302401304244995})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.467555999755859})
store['active_learning_steps'][22]['training']['best_epoch']=3
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.2562, 'crossentropy': 3.422018359375}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 28704], ['id', 30451], ['id', 7845], ['id', 46236], ['id', 42660]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.46502764310824074, 0.7946475294212361, 1.094568295810011, 1.3881954631198097, 1.664787936183365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.698140859603882})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 3.421527862548828})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 5.426957130432129})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 3.2722620964050293})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 3.816377639770508})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.012947082519531})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 4.290035247802734})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 4.8183488845825195})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 4.479334831237793})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 4.297403335571289})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 4.347752571105957})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 5.193800449371338})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 5.027293682098389})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 5.870598793029785})
store['active_learning_steps'][23]['training']['best_epoch']=11
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.262, 'crossentropy': 4.3564}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 2606], ['id', 35835], ['id', 44964], ['id', 4444], ['id', 42576]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.59195284238587, 1.1277398277881843, 1.6004854566173998, 2.0302384652156746, 2.3987272938181174]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 2.645493984222412})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 2.59682035446167})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 3.9551069736480713})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 3.7698373794555664})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 3.7891573905944824})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 5.316300392150879})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 4.506732940673828})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 4.367288589477539})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 4.593109130859375})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.591118812561035})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 4.82858943939209})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.386929512023926})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.226655960083008})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 4.418342590332031})
store['active_learning_steps'][24]['training']['best_epoch']=11
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.2824, 'crossentropy': 4.886745703125}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 27878], ['id', 27117], ['id', 14420], ['id', 5991], ['id', 30652]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.7755276351438263, 1.5401724375371568, 2.0724040477521903, 2.507507486895224, 2.8955200517194397]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 2.360772132873535})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 3.2119317054748535})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 3.0620312690734863})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 4.061500549316406})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 3.768282413482666})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.0783538818359375})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.219403266906738})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.529977798461914})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 5.048240661621094})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 5.11058235168457})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 5.084023952484131})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 4.751735687255859})
store['active_learning_steps'][25]['training']['best_epoch']=9
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.2522, 'crossentropy': 5.1721015625}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 2498], ['ood', 17054], ['id', 13217], ['id', 13712], ['id', 17465]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7105598266894215, 1.2901969717093795, 1.804392954546962, 2.2573011253691577, 2.6644714395354816]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 2.254781723022461})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 2.745853900909424})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.331179141998291})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.957552433013916})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.2427, 'crossentropy': 2.297478515625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 37767], ['id', 23445], ['id', 39513], ['id', 34578], ['id', 10949]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.42751743195847247, 0.7550805181965154, 1.0111131549411017, 1.242386183645702, 1.4330340017450407]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 2.77815580368042})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 3.1533894538879395})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 3.2242836952209473})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 2.7154202461242676})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 4.821863174438477})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.3212890625, 'crossentropy': 3.52121639251709})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 3.3738508224487305})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 4.181342124938965})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 3.7560877799987793})
store['active_learning_steps'][27]['training']['best_epoch']=6
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.294, 'crossentropy': 3.599348046875}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 43056], ['id', 10207], ['id', 7905], ['id', 20545], ['id', 4969]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.43363689260414073, 0.8146419625454033, 1.1890214459927737, 1.5335069389431482, 1.861053838357419]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 2.9360976219177246})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 3.15432071685791})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 2.487366199493408})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.387077808380127})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 3.9748573303222656})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 4.620092391967773})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 3.37035870552063})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 4.092658996582031})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.548253059387207})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 3.7674951553344727})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 4.742246627807617})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 4.4270148277282715})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 4.73721981048584})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 4.773204803466797})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 5.112938404083252})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 4.675518989562988})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 5.0247578620910645})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.58868932723999})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 4.122303485870361})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 4.825806617736816})
store['active_learning_steps'][28]['training']['best_epoch']=17
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.2785, 'crossentropy': 5.18987890625}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 13175], ['id', 3607], ['id', 685], ['id', 42207], ['id', 36538]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6031045254341034, 1.1459767237540253, 1.6595393513140761, 2.145614854812502, 2.56430062594955]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 2.1867756843566895})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 2.3229146003723145})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.723353862762451})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 3.1063148975372314})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 3.4630320072174072})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 3.2027223110198975})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 4.259395599365234})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.2599, 'crossentropy': 3.1393318359375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 30084], ['id', 38909], ['id', 24466], ['id', 40145], ['id', 35362]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.45536918936238413, 0.797359507908669, 1.1184251738168811, 1.4136168189172906, 1.6992911971845732]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 2.558072566986084})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 2.964268207550049})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 3.038970947265625})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 3.0378527641296387})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 3.7995901107788086})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 3.4303200244903564})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 3.1784942150115967})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.2772, 'crossentropy': 3.1779869140625}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 36626], ['id', 40112], ['id', 37436], ['id', 17904], ['id', 42760]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.38932749915234344, 0.7470319998062922, 1.0668517599798313, 1.3755313831282567, 1.6621837322900408]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 2.3482959270477295})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 4.794220924377441})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.2933554649353027})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 3.7175445556640625})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 3.38185453414917})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.976221084594727})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 3.784735679626465})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 4.619197368621826})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 3.8123488426208496})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 4.192505359649658})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 4.110721588134766})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 3.7885708808898926})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 4.540058135986328})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 3.9970908164978027})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 4.173550605773926})
store['active_learning_steps'][31]['training']['best_epoch']=12
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.2969, 'crossentropy': 4.016896484375}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 20160], ['id', 31690], ['id', 11578], ['id', 29506], ['id', 21035]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5246951124563497, 1.036882884088476, 1.5043824334131806, 1.9155782278745939, 2.2843080570471654]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 2.7511587142944336})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 2.7684988975524902})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 3.1771559715270996})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 2.980675458908081})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.3095703125, 'crossentropy': 3.4385037422180176})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 3.7707133293151855})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 3.631666421890259})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.3251953125, 'crossentropy': 3.6565873622894287})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 3.613780975341797})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 4.474885940551758})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 4.176562309265137})
store['active_learning_steps'][32]['training']['best_epoch']=8
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.3111, 'crossentropy': 3.671665625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 5203], ['id', 26042], ['id', 3267], ['id', 47987], ['id', 41949]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6358824958747897, 1.1641169486395793, 1.6142808684897103, 1.986353022605904, 2.3344152345564666]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.030999660491943})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 2.566401481628418})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 3.7133560180664062})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 3.2517080307006836})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 3.1041512489318848})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 4.061888694763184})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 3.756226062774658})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 4.279211044311523})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.293, 'crossentropy': 3.08158984375}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 18498], ['id', 47215], ['ood', 15375], ['ood', 39778], ['id', 40441]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5203499055568659, 1.007966165637074, 1.4453619042454147, 1.820047496997911, 2.162767880695129]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 2.1565089225769043})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 2.661585569381714})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 2.654245376586914})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 4.019284248352051})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 3.229205846786499})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 3.2867650985717773})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 4.257207870483398})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 3.836308479309082})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.2827, 'crossentropy': 3.29163515625}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 30227], ['id', 24921], ['id', 37160], ['id', 40243], ['id', 36824]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4234546759400466, 0.8205209173557342, 1.1407299294368576, 1.4401352264338616, 1.7049191107309856]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 2.7484493255615234})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.936849594116211})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.9570374488830566})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 3.0602869987487793})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 3.9364757537841797})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 4.111424446105957})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 4.081733703613281})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.2871, 'crossentropy': 3.093847265625}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 41728], ['id', 11948], ['id', 38045], ['id', 4370], ['id', 7386]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.4108316585156847, 0.7293969615414526, 1.010674604823795, 1.2640693204830686, 1.5090568803754572]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 2.3990695476531982})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 3.168504238128662})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.28125, 'crossentropy': 2.775167465209961})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.3203125, 'crossentropy': 2.777676582336426})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2978515625, 'crossentropy': 3.2217276096343994})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 3.6125144958496094})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.3056640625, 'crossentropy': 3.465975284576416})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.3146, 'crossentropy': 2.9610357421875}
