store = {}
store['timestamp']=1621608587
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=6']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=6
store['worker_id']=6
store['num_workers']=24
store['config']={'seed': 1240, 'uniform_ood': False, 'id_dataset_name': 'CIFAR-10', 'ood_dataset_name': 'SVHN', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node) + ('SVHN (Train, seed=0, 73257 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'CIFAR-10 (Test)'"}
store['initial_training_set_indices']=[12980, 44617, 6984, 21168, 33976, 35571, 33058, 43729, 26944, 24745, 66, 14046, 46542, 39478, 6000, 5915, 39360, 20774, 27084, 44464]
store['evaluation_set_indices']=[3812, 42704, 6729, 38942, 48125, 16968, 5652, 4045, 10740, 19606, 37062, 15768, 44824, 47581, 19482, 4628, 25290, 27933, 27441, 5508, 35131, 18717, 43561, 37318, 8187, 37590, 45717, 1493, 5924, 19803, 23554, 6460, 2962, 36049, 18273, 11023, 27366, 39007, 5305, 46743, 15798, 44136, 20072, 20717, 1152, 8194, 36500, 17618, 35054, 18973, 45734, 16753, 6410, 28807, 8902, 20957, 6625, 41155, 1332, 47376, 36719, 11500, 36383, 7417, 30371, 19517, 33334, 27185, 29033, 42916, 39943, 34789, 18504, 7348, 6096, 28402, 10058, 12011, 34663, 1618, 17887, 41306, 1467, 28071, 12667, 38339, 44920, 44374, 14769, 31145, 21575, 16685, 24836, 48736, 21176, 26844, 45671, 22164, 42503, 10770, 27020, 30182, 37164, 33354, 47307, 17878, 26665, 40819, 14805, 201, 47956, 44739, 8060, 45495, 8139, 27034, 40800, 21802, 18878, 8672, 41175, 48917, 23272, 9952, 23154, 37915, 18669, 18159, 13468, 14436, 16099, 8128, 33349, 31445, 7202, 21948, 10215, 34670, 538, 40015, 17530, 11133, 6028, 12100, 21106, 5614, 30720, 34210, 39322, 40006, 31808, 24717, 34090, 17381, 18164, 17668, 16984, 37856, 41017, 43216, 46788, 26334, 6887, 40485, 39838, 1931, 47231, 37148, 801, 14067, 31951, 7105, 34561, 18698, 45258, 21399, 18558, 26959, 17240, 30502, 39056, 47625, 18880, 37323, 26204, 21788, 1674, 47188, 10526, 25980, 27994, 19871, 22250, 38761, 7182, 14241, 235, 37616, 39973, 35218, 46446, 33361, 39076, 38899, 15578, 36667, 5551, 23088, 32496, 5705, 23255, 25559, 11975, 44032, 45743, 23571, 30475, 15184, 41327, 15827, 33432, 37357, 40250, 16421, 2561, 8533, 25715, 17074, 36811, 30099, 44174, 8029, 1480, 43701, 10198, 38802, 13200, 31615, 28252, 17879, 18749, 16580, 19178, 48034, 4365, 4796, 46033, 47538, 7188, 45076, 13569, 28392, 19457, 41335, 4474, 23022, 11289, 25103, 35813, 40336, 12008, 36695, 28598, 12671, 48831, 18364, 9890, 11804, 37612, 31396, 10683, 31008, 36360, 15312, 26328, 41353, 34761, 4398, 46637, 13891, 32787, 22410, 26463, 4503, 31374, 26143, 7765, 27551, 15340, 16182, 7868, 42518, 34516, 8244, 13037, 39992, 14300, 48188, 42511, 2963, 28224, 28657, 5474, 19682, 682, 25867, 47518, 36303, 18452, 34447, 24821, 36157, 48089, 25120, 44689, 6509, 1852, 17387, 19405, 39441, 42197, 14298, 16443, 1151, 9775, 10834, 44482, 10445, 41434, 37644, 5702, 29159, 17097, 28308, 42161, 29973, 38602, 4592, 24411, 38792, 25200, 28299, 5522, 4441, 4065, 12187, 32012, 41361, 36098, 25224, 27204, 29536, 18785, 28218, 42361, 10437, 8978, 44209, 7804, 35232, 3041, 23251, 41265, 28139, 41350, 18536, 37181, 25352, 16787, 27537, 29568, 45681, 33891, 35667, 31031, 5795, 23494, 7658, 26711, 35750, 34571, 4852, 29601, 14492, 5318, 26987, 11839, 533, 29565, 16424, 43853, 34375, 26710, 37956, 34492, 46294, 12920, 7945, 29669, 14520, 36081, 14478, 37173, 19188, 40253, 23549, 741, 34309, 11001, 6995, 10899, 36881, 7002, 19049, 13388, 40737, 9210, 22684, 43970, 7048, 46803, 45248, 4726, 40534, 23790, 47216, 8585, 7880, 25042, 306, 11939, 45003, 12905, 4052, 45391, 28968, 19408, 6012, 7814, 27790, 10979, 2005, 32156, 16025, 23706, 8236, 24750, 39229, 6968, 7599, 32427, 48001, 12257, 6899, 36229, 19760, 30468, 32347, 15232, 17555, 34373, 1157, 22434, 38137, 3717, 38235, 41506, 10786, 3175, 48043, 24171, 29368, 39765, 16373, 22973, 42399, 32908, 35630, 28508, 29334, 37539, 45770, 29181, 10946, 18072, 18511, 47354, 31444, 42643, 4078, 45028, 45610, 35405, 33751, 7967, 4701, 13378, 48105, 22116, 20599, 45454, 7325, 11304, 12289, 46114, 8359, 41073, 22751, 19402, 8483, 45656, 5604, 9134, 35979, 19757, 43627, 35248, 23566, 727, 34909, 43560, 2888, 12158, 48248, 2094, 47190, 15295, 27629, 15047, 4402, 32595, 6538, 13474, 11538, 10736, 29892, 29786, 1884, 45940, 2144, 37537, 5222, 26418, 10690, 19114, 30223, 17188, 41379, 46182, 20359, 32256, 43739, 41935, 16411, 15933, 22295, 940, 8665, 1154, 32089, 46513, 17506, 39407, 6187, 7878, 37671, 25414, 16789, 37546, 44170, 9921, 22033, 33690, 23656, 5226, 1631, 8671, 45821, 34099, 40039, 31342, 35231, 29621, 31899, 1023, 17082, 38261, 26917, 31921, 5241, 37282, 45513, 46687, 18915, 10796, 8986, 31711, 2185, 29316, 45090, 13383, 5741, 7930, 39306, 13675, 38034, 29826, 48781, 21746, 39559, 31318, 19965, 25443, 45862, 30730, 9611, 43077, 23902, 9541, 38859, 13973, 27923, 25754, 38295, 39261, 15442, 40254, 28002, 23139, 44524, 11458, 10297, 25299, 13617, 28750, 1835, 29505, 23873, 45073, 34640, 5831, 29115, 26568, 6588, 31067, 15001, 4887, 27814, 17283, 23813, 43511, 14398, 13500, 7428, 11090, 11751, 36607, 9712, 43583, 45864, 39972, 14617, 3431, 26470, 33191, 18204, 24481, 28879, 43889, 15015, 36437, 12660, 37650, 405, 36212, 42818, 10677, 15723, 24514, 35518, 42654, 44052, 10218, 37297, 34741, 40715, 37290, 29931, 29774, 25075, 12136, 44466, 25236, 7096, 26190, 14575, 41698, 9068, 24101, 3379, 19906, 15856, 38317, 20799, 17172, 5987, 140, 11530, 38636, 9116, 11151, 25071, 182, 31603, 21547, 47739, 13909, 624, 25621, 30173, 37807, 7053, 30625, 10450, 22316, 23965, 5028, 37725, 1675, 45751, 19683, 26061, 34327, 38096, 30828, 438, 46574, 9121, 4859, 15563, 33935, 39481, 48048, 37730, 35947, 18461, 22658, 35939, 3507, 16223, 5279, 9615, 13583, 28557, 36129, 19326, 23956, 31469, 3397, 36813, 4416, 48955, 27367, 9692, 41380, 27998, 33372, 24467, 24186, 47802, 16612, 46008, 3943, 48514, 42699, 37077, 17401, 39288, 44878, 31226, 14334, 44847, 7473, 42669, 32658, 40101, 11309, 853, 12919, 41501, 26725, 3843, 41314, 16050, 39323, 5916, 19945, 17950, 48824, 8856, 12778, 28765, 13275, 34339, 8883, 36161, 41767, 44449, 7357, 3967, 41737, 3432, 27375, 5603, 1739, 2418, 23760, 26549, 2676, 11659, 40405, 46217, 5207, 28673, 12645, 45982, 48103, 21541, 33384, 28830, 46313, 2540, 17302, 42509, 2321, 40265, 21290, 35387, 48490, 11327, 16529, 40097, 16839, 12570, 17132, 18289, 20343, 22077, 21098, 5426, 8478, 1923, 4941, 48459, 34289, 38039, 44848, 20094, 25546, 19669, 32606, 16624, 28652, 11887, 22863, 48068, 9574, 39941, 2068, 28297, 7225, 41330, 47575, 30080, 25197, 25710, 18030, 16190, 21185, 46949, 1377, 47189, 30166, 28575, 12032, 14160, 11813, 48219, 39348, 42953, 46300, 5559, 15360, 14665, 25279, 42955, 43707, 10089, 10928, 16650, 18156, 4140, 2816, 45019, 25339, 16628, 3925, 25879, 43725, 33970, 17789, 20083, 8873, 41315, 45472, 40526, 4589, 44440, 3184, 4581, 16953, 7585, 45975, 28441, 10956, 22017, 21698, 2107, 44107, 45868, 30293, 15530, 26848, 45705, 811, 22587, 28712, 16591, 45100, 41182, 1225, 40805, 3915, 6545, 8556, 26652, 29708, 24040, 676, 8243, 42597, 17603, 3208, 38902, 15447, 8826, 14791, 38670, 37596, 42980, 17743, 44094, 23778, 32296, 43347, 20210, 6487, 33150, 5095, 35163, 3681, 42450, 21707, 13663, 37987, 13359, 10158, 24531, 21817, 39213, 29424, 38798, 32466, 37354, 27218, 12293, 4133, 14755, 38826, 23328, 48318, 22137, 28379, 35441, 1910, 31964, 26833, 13669, 7484, 43359, 48803, 6853, 47906, 25522, 42533, 16633, 38444, 39544, 13401, 36560, 47222, 1732, 10624, 45339, 24754, 9680, 47728, 4309, 20076, 32836]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 8.87523078918457})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 10.227948188781738})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 10.48641300201416})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 10.853032112121582})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 9.964035034179688})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 10.59389877319336})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 18.80776596069336})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 11.9730224609375})
store['active_learning_steps'][0]['training']['best_epoch']=5
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.1799, 'crossentropy': 9.91656484375}
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 35860], ['ood', 25650], ['ood', 22392], ['ood', 6321], ['ood', 66673]], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.7386895675549767, 1.3945272422259563, 1.9538153587841136, 2.468930301869798, 2.9125890782887147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 12.007969856262207})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 10.245782852172852})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 12.812002182006836})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 9.494433403015137})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.1802, 'crossentropy': 12.362003125}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 9660], ['id', 30960], ['id', 20386], ['ood', 40947], ['id', 44730]], 'labels': [-1, 0, 2, -1, 4], 'scores': [0.8364558309501331, 1.5831882927959033, 2.171319374723427, 2.665922983421975, 3.0828164045932356]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 10.579822540283203})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 9.217364311218262})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 10.048428535461426})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 9.830835342407227})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 11.256501197814941})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.1901, 'crossentropy': 9.128159375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 37459], ['id', 16683], ['ood', 70760], ['id', 11438], ['id', 28333]], 'labels': [1, 9, -1, 9, 9], 'scores': [0.7954961757361625, 1.3874471060564222, 1.9233803271255745, 2.3877121820110467, 2.7851898322446385]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 9.287854194641113})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 7.996237754821777})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 10.282578468322754})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 9.126480102539062})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 8.564050674438477})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 9.073192596435547})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 8.721010208129883})
store['active_learning_steps'][3]['training']['best_epoch']=4
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.214, 'crossentropy': 9.20791796875}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 42899], ['ood', 2212], ['ood', 20215], ['id', 21237], ['ood', 45907]], 'labels': [3, -1, -1, 0, -1], 'scores': [0.7961725149637235, 1.4920208958939187, 2.139005904530302, 2.698143192406146, 3.1443228574891666]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 7.958312511444092})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 8.237515449523926})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 8.474809646606445})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 8.966135025024414})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 8.558950424194336})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 8.743658065795898})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 8.73004150390625})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 8.955146789550781})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 9.57339096069336})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 9.885692596435547})
store['active_learning_steps'][4]['training']['best_epoch']=7
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.1946, 'crossentropy': 9.12409296875}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 12108], ['id', 13714], ['id', 42129], ['id', 40330], ['id', 35827]], 'labels': [2, 8, 2, 0, 2], 'scores': [0.7096006485767821, 1.3378988858547722, 1.912530308384183, 2.438368959355955, 2.8937149836673726]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 7.657637596130371})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 7.124640464782715})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 8.793867111206055})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 8.162556648254395})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 10.270050048828125})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.1773, 'crossentropy': 7.37963828125}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 67386], ['ood', 41848], ['ood', 49456], ['ood', 33445], ['id', 38060]], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.6215705292390665, 1.165112975825477, 1.6768481282565175, 2.1328168554857934, 2.545910509088376]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 7.306128978729248})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 7.365647792816162})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 8.63129711151123})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 8.932031631469727})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.1847, 'crossentropy': 7.67683359375}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 48980], ['ood', 46242], ['ood', 47537], ['id', 27272], ['ood', 54976]], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.7385817028980286, 1.2591000685311053, 1.7087175821866776, 2.0654073156430686, 2.3845606288943237]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 9.863195419311523})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 8.571945190429688})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 8.510238647460938})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 6.727747917175293})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 8.735459327697754})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 9.65081787109375})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 9.834915161132812})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.1995, 'crossentropy': 6.84218203125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 25064], ['id', 5646], ['id', 42433], ['ood', 60570], ['ood', 70099]], 'labels': [6, 1, 4, -1, -1], 'scores': [0.644330865823628, 1.2591430530255288, 1.8284431877272072, 2.3313062417798136, 2.7647085954449224]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 8.03855037689209})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 8.304003715515137})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 9.300079345703125})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 9.090707778930664})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 10.337503433227539})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.2072, 'crossentropy': 8.61328125}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 62928], ['id', 8237], ['ood', 71222], ['ood', 23540], ['ood', 20508]], 'labels': [-1, 7, -1, -1, -1], 'scores': [0.7204893581544094, 1.3746886170878274, 1.9660849184298939, 2.5000631670381823, 2.9256499026357634]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 5.781258583068848})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 7.123650074005127})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 7.5656232833862305})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 8.758749961853027})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 10.076700210571289})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 8.365519523620605})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 7.893673419952393})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.2239, 'crossentropy': 9.3731515625}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 13489], ['ood', 20633], ['id', 1619], ['ood', 34588], ['id', 15493]], 'labels': [8, -1, 7, -1, 2], 'scores': [0.6304982277447071, 1.2128361253337645, 1.6911419868541686, 2.1365499332183706, 2.5237192495910428]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 6.033660888671875})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 8.662267684936523})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 7.672666549682617})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 7.122344970703125})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.2237, 'crossentropy': 6.1135515625}
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 16450], ['ood', 65303], ['ood', 21606], ['id', 26069], ['id', 32143]], 'labels': [-1, -1, -1, 8, 0], 'scores': [0.7102653656442257, 1.3456599546786348, 1.9050375321568964, 2.280666336126311, 2.6163697758103313]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 6.701024055480957})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 6.496743202209473})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 9.013447761535645})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 6.984002590179443})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 8.226734161376953})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 8.478199005126953})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 9.345699310302734})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 7.0088043212890625})
store['active_learning_steps'][11]['training']['best_epoch']=5
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.2257, 'crossentropy': 8.21234296875}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 11054], ['ood', 26761], ['ood', 29787], ['id', 37388], ['id', 41417]], 'labels': [-1, -1, -1, 7, 4], 'scores': [0.6334650375355004, 1.188906717797602, 1.7201752472362264, 2.1738360724585153, 2.5886340741927025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 5.641862392425537})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 7.1037678718566895})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 7.077357292175293})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 8.362234115600586})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 7.168463230133057})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 7.468967914581299})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.2262, 'crossentropy': 7.461240625}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 15098], ['ood', 32], ['ood', 69130], ['id', 14614], ['id', 32260]], 'labels': [0, -1, -1, 4, 0], 'scores': [0.592854741741432, 1.1685291627591572, 1.6675120199754239, 2.123635811370109, 2.499531530700337]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 8.018213272094727})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 7.752266883850098})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 6.798720836639404})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 8.863710403442383})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 9.028589248657227})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 7.15737771987915})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 7.266172409057617})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.2124, 'crossentropy': 9.4782640625}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 61752], ['id', 10748], ['id', 26516], ['ood', 47888], ['ood', 64040]], 'labels': [-1, 7, 4, -1, -1], 'scores': [0.6210093420374663, 1.1769815717654364, 1.6669761235699503, 2.1210349356144658, 2.53013754467488]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.024186611175537})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 6.5870161056518555})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 10.06773567199707})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 6.541801452636719})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.2263, 'crossentropy': 5.399784375}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 36095], ['ood', 16294], ['ood', 32937], ['id', 28364], ['id', 17156]], 'labels': [2, -1, -1, 3, 4], 'scores': [0.564445630972346, 1.0592324181367925, 1.4749535268700016, 1.844733290497702, 2.1870473167975817]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 6.655322074890137})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 7.663819313049316})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 7.545894145965576})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 7.818483352661133})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 6.250509738922119})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.2095, 'crossentropy': 7.98233984375}
store['active_learning_steps'][15]['acquisition']={'indices': [['ood', 6701], ['id', 10273], ['ood', 67348], ['id', 48795], ['ood', 55245]], 'labels': [-1, 8, -1, 9, -1], 'scores': [0.6587511617102206, 1.247109710306015, 1.7220066881299632, 2.1582150409807115, 2.506677869898539]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 5.523743629455566})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 6.254474639892578})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 7.1450700759887695})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 7.583895683288574})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 7.051758766174316})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 7.247698783874512})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 7.852675437927246})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.216, 'crossentropy': 7.53196328125}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 24953], ['id', 33520], ['id', 17293], ['ood', 58350], ['ood', 52868]], 'labels': [-1, 8, 5, -1, -1], 'scores': [0.8471764572155194, 1.4982788070461268, 2.0862671769071444, 2.533776116729422, 2.910082654613113]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 7.411321640014648})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.632071495056152})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 6.449858665466309})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 7.326220512390137})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.2118, 'crossentropy': 7.60202734375}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 12308], ['id', 10328], ['ood', 31477], ['id', 34578], ['id', 29872]], 'labels': [3, 6, -1, 0, 0], 'scores': [0.5430077217269833, 1.0286227967925723, 1.446149550491957, 1.8321593238466019, 2.1778470750249266]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.526636123657227})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 6.740412712097168})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 5.603592872619629})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 7.010129451751709})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 7.084397315979004})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 6.877723693847656})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 7.347712516784668})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.2162, 'crossentropy': 7.1942640625}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 14777], ['id', 36378], ['id', 48834], ['ood', 26810], ['ood', 28332]], 'labels': [8, 8, 7, -1, -1], 'scores': [0.6293403691872355, 1.1908292944565062, 1.674586684814786, 2.092185234299718, 2.4741415896811327]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 9.161280632019043})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 8.019124984741211})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 6.390066146850586})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 7.55612325668335})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 8.001176834106445})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 9.737836837768555})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 8.027024269104004})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 8.828054428100586})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 6.602396011352539})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 8.140024185180664})
store['active_learning_steps'][19]['training']['best_epoch']=7
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.2313, 'crossentropy': 8.51501484375}
store['active_learning_steps'][19]['acquisition']={'indices': [['ood', 56306], ['id', 34963], ['ood', 57554], ['ood', 52501], ['id', 39158]], 'labels': [-1, 1, -1, -1, 3], 'scores': [0.7612160393662575, 1.4068987167343936, 2.0015798800772595, 2.547048439196524, 3.003329805102238]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 5.041172504425049})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 5.4237189292907715})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 5.2195234298706055})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 6.03815221786499})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 6.270557880401611})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 11.722029685974121})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.739922523498535})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 7.815333843231201})
store['active_learning_steps'][20]['training']['best_epoch']=5
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.2145, 'crossentropy': 6.6221796875}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 37537], ['id', 37695], ['id', 1343], ['ood', 30053], ['ood', 5114]], 'labels': [-1, 1, 9, -1, -1], 'scores': [0.7178348031219042, 1.2896308770448246, 1.7998511925592444, 2.2326802569771447, 2.6093260083259464]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 12.271425247192383})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 6.978044509887695})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 7.167149066925049})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.789793968200684})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.5355544090271})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 6.180347442626953})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 6.310431480407715})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 8.45345687866211})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 8.515813827514648})
store['active_learning_steps'][21]['training']['best_epoch']=6
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.2216, 'crossentropy': 6.421308203125}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 34482], ['id', 39679], ['ood', 27299], ['id', 6338], ['ood', 592]], 'labels': [8, 8, -1, 3, -1], 'scores': [0.7468676262641338, 1.3579350042868006, 1.895811444974501, 2.3622419193952027, 2.730516057156718]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.173123836517334})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 5.533945560455322})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 6.085504531860352})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 6.469059467315674})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 6.321601867675781})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 6.945267677307129})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 6.892388343811035})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 7.459342002868652})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 6.988018989562988})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 8.222638130187988})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 8.684321403503418})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 6.370230197906494})
store['active_learning_steps'][22]['training']['best_epoch']=9
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.26, 'crossentropy': 7.11160234375}
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 63055], ['ood', 46069], ['id', 37412], ['ood', 59587], ['ood', 56248]], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.7164015771640453, 1.2770001593081144, 1.792293602435278, 2.2559552749701437, 2.659003310267135]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.928260803222656})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 6.3972578048706055})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.510919570922852})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 7.222498893737793})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.923122406005859})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 9.174406051635742})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.2256, 'crossentropy': 5.72427734375}
store['active_learning_steps'][23]['acquisition']={'indices': [['ood', 61670], ['ood', 24003], ['id', 34759], ['id', 38267], ['id', 46858]], 'labels': [-1, -1, 6, 1, 6], 'scores': [0.5704331504471818, 1.0990973610955033, 1.5465251664295154, 1.9409522512995174, 2.285879869594388]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.491279602050781})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.301923751831055})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 5.438503265380859})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 6.728453636169434})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 6.621601581573486})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 7.683884620666504})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.2303, 'crossentropy': 5.6272015625}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 44986], ['ood', 48529], ['id', 26179], ['id', 1234], ['id', 19793]], 'labels': [1, -1, 2, 8, 7], 'scores': [0.5774456168380242, 1.0657882149516302, 1.495259214175324, 1.8672360486442434, 2.213140202308308]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 6.7920708656311035})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.560457229614258})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 6.708152770996094})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 8.369806289672852})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 7.680744171142578})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 7.064878940582275})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 7.909111976623535})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 6.382152557373047})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 6.9733734130859375})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 7.926334381103516})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 8.701932907104492})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 7.309130668640137})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 8.127595901489258})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 7.414150238037109})
store['active_learning_steps'][25]['training']['best_epoch']=11
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.2429, 'crossentropy': 8.63690078125}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 21918], ['ood', 72315], ['id', 14153], ['id', 22421], ['id', 12367]], 'labels': [-1, -1, 9, 0, 8], 'scores': [0.9789092649784004, 1.6099464716676155, 2.186343448847272, 2.6748504295411966, 3.088399822842919]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.064260005950928})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 5.278223991394043})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.646905899047852})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 5.34096622467041})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 8.067541122436523})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 7.702610969543457})
store['active_learning_steps'][26]['training']['best_epoch']=3
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.2414, 'crossentropy': 5.620085546875}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 11336], ['id', 31622], ['id', 17516], ['ood', 62957], ['ood', 7718]], 'labels': [6, 0, 2, -1, -1], 'scores': [0.5415994350474123, 1.0721965624744358, 1.576669937241412, 1.9858933856729415, 2.3692590029597023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 4.010534763336182})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 6.937277317047119})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 6.686834335327148})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 4.878426551818848})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 6.998464584350586})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 7.516619682312012})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 6.839930057525635})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.2458, 'crossentropy': 5.188115234375}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 3619], ['ood', 23811], ['id', 5464], ['id', 22665], ['id', 24742]], 'labels': [4, -1, 7, 1, 1], 'scores': [0.6219226996038154, 1.1241273277370376, 1.5781411604744129, 1.9844249172811885, 2.336258487479996]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 4.399028778076172})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 5.99105167388916})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 6.867645740509033})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 7.039620399475098})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 8.514265060424805})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 7.217806816101074})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 9.028861999511719})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.2487, 'crossentropy': 7.17521171875}
store['active_learning_steps'][28]['acquisition']={'indices': [['ood', 39926], ['id', 14701], ['ood', 52824], ['id', 41318], ['id', 41199]], 'labels': [-1, 0, -1, 3, 6], 'scores': [0.6687926617613937, 1.3158566909315503, 1.8779703995810566, 2.346943700362523, 2.770379522316116]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 4.487842559814453})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 5.052639961242676})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 5.41343879699707})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 7.177463531494141})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 5.714943885803223})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 6.348154544830322})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 6.374472618103027})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 6.1689910888671875})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 8.145286560058594})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 7.172645092010498})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 6.959314346313477})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.2552, 'crossentropy': 6.11407734375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 28936], ['ood', 11718], ['id', 14902], ['ood', 3704], ['ood', 43954]], 'labels': [5, -1, 3, -1, -1], 'scores': [0.7774047752035185, 1.3464359433060067, 1.8791702272710964, 2.2998875338077216, 2.6887596313511004]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 6.077530384063721})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 4.935493469238281})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 6.531834125518799})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 6.230119705200195})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 7.751962661743164})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 6.2238664627075195})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.2354, 'crossentropy': 6.37817265625}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 40966], ['id', 8536], ['ood', 15728], ['ood', 46069], ['id', 13154]], 'labels': [-1, 4, -1, -1, 3], 'scores': [0.5470678258920461, 1.0536030287267604, 1.5094842540376323, 1.925515504743169, 2.2800898167088217]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 4.577496528625488})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 4.726050853729248})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 6.146018028259277})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 6.142901420593262})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 5.871117115020752})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 6.215707302093506})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 6.169942855834961})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 7.916900634765625})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.2578, 'crossentropy': 5.8293875}
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 27679], ['ood', 4518], ['id', 34194], ['id', 26747], ['ood', 33783]], 'labels': [-1, -1, 1, 5, -1], 'scores': [0.6848643234277398, 1.267485329773172, 1.8108984939889723, 2.2792106554792664, 2.6664364287866933]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 4.9757513999938965})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 4.677611351013184})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.81328821182251})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 6.516985893249512})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 6.252407550811768})
store['active_learning_steps'][32]['training']['best_epoch']=2
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.2375, 'crossentropy': 4.645476953125}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 57101], ['id', 40894], ['id', 19324], ['ood', 64186], ['id', 46680]], 'labels': [-1, 6, 9, -1, 3], 'scores': [0.6241237844592595, 1.099739040701769, 1.5376950668698655, 1.9396869877149499, 2.3006010194143522]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.406714916229248})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 4.854678153991699})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 5.500901222229004})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 5.413540840148926})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 6.095400810241699})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 7.166971206665039})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 8.03683853149414})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 6.792712211608887})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 7.614683151245117})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 7.749502182006836})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 8.147468566894531})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 6.8716864585876465})
store['active_learning_steps'][33]['training']['best_epoch']=9
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.2546, 'crossentropy': 7.5823203125}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 35271], ['ood', 18135], ['ood', 2117], ['ood', 45238], ['id', 15753]], 'labels': [0, -1, -1, -1, 6], 'scores': [0.6408851181481756, 1.2401401966835444, 1.7694281377368961, 2.241244864458759, 2.656474243172365]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 4.314464569091797})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 4.718398094177246})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.284236907958984})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 6.0723876953125})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 4.69595193862915})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 5.303529739379883})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 7.331528663635254})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.2561, 'crossentropy': 6.3506203125}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 32820], ['id', 34722], ['ood', 48980], ['ood', 60611], ['ood', 66298]], 'labels': [4, 7, -1, -1, -1], 'scores': [0.5466629677667172, 1.066958518414515, 1.5528367899208764, 1.9662845431422102, 2.3466095704774457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 6.361242294311523})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 3.949817180633545})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 5.204358100891113})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 6.427194118499756})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 6.481394290924072})
store['active_learning_steps'][35]['training']['best_epoch']=2
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.2653, 'crossentropy': 4.124664453125}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 56758], ['id', 36213], ['ood', 56306], ['id', 37767], ['id', 22806]], 'labels': [-1, 8, -1, 0, 6], 'scores': [0.5991609433343854, 1.0500262669300175, 1.486682098036344, 1.8849689494651471, 2.2579317886671966]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.123414039611816})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 4.076346397399902})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 4.710656642913818})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.7402520179748535})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 6.300556659698486})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.464090347290039})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 6.945972442626953})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.2377, 'crossentropy': 5.728255078125}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 44114], ['id', 45904], ['ood', 16190], ['id', 16690], ['id', 4252]], 'labels': [3, 0, -1, 4, 3], 'scores': [0.528952990924769, 1.001072545827705, 1.4423638769335207, 1.858083583901454, 2.2229433964557366]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 3.9631621837615967})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.9274492263793945})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.938568115234375})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.5062479972839355})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 6.641385555267334})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 5.905272006988525})
store['active_learning_steps'][37]['training']['best_epoch']=3
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.2499, 'crossentropy': 4.9363703125}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 18700], ['ood', 2118], ['ood', 32754], ['id', 5612], ['id', 27836]], 'labels': [5, -1, -1, 3, 0], 'scores': [0.5784822442547259, 1.0721539756901315, 1.506053151035136, 1.8956760936314945, 2.2376724420102168]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 4.117598056793213})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 3.8971142768859863})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 5.096940040588379})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 6.427370548248291})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 6.044974327087402})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 5.704256057739258})
store['active_learning_steps'][38]['training']['best_epoch']=3
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.2672, 'crossentropy': 5.2275953125}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 36949], ['ood', 6702], ['ood', 3750], ['id', 14088], ['ood', 19713]], 'labels': [6, -1, -1, 0, -1], 'scores': [0.619766966205546, 1.1774225382185817, 1.7124132176311595, 2.1317542235755784, 2.5114899608074035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 3.688880443572998})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.820508003234863})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 5.464101791381836})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 5.916707515716553})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 5.682049751281738})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 5.141772270202637})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 6.129275798797607})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.903583526611328})
store['active_learning_steps'][39]['training']['best_epoch']=5
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.2593, 'crossentropy': 5.42463828125}
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 69293], ['ood', 7302], ['ood', 33014], ['id', 10331], ['ood', 18236]], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.6710884494809994, 1.2043244997021847, 1.6640094961033363, 2.0988043865024313, 2.4852499390543423]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.0623207092285156})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 5.293522834777832})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 4.716790199279785})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 4.852593898773193})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 5.438947677612305})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 6.408396244049072})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.954626083374023})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 6.127996444702148})
store['active_learning_steps'][40]['training']['best_epoch']=5
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.2542, 'crossentropy': 5.45351484375}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 49673], ['id', 45162], ['ood', 4664], ['ood', 61670], ['ood', 23433]], 'labels': [-1, 0, -1, -1, -1], 'scores': [0.6447343591694388, 1.2686770255825186, 1.7224677552641756, 2.153384970281982, 2.532090412579165]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.1362481117248535})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.02277946472168})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 4.0329766273498535})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 6.368730068206787})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 5.759061813354492})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 6.7334089279174805})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 6.204611778259277})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.2584, 'crossentropy': 6.4151546875}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 42764], ['id', 22396], ['id', 4034], ['ood', 25498], ['id', 26369]], 'labels': [-1, 2, 1, -1, 1], 'scores': [0.6186390104994088, 1.2089454241299853, 1.7327613338754118, 2.206239780043104, 2.6066524548544656]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 3.879401206970215})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.122661113739014})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 4.572619438171387})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 4.840036392211914})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 5.155340194702148})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.30859375, 'crossentropy': 5.256379127502441})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 6.656429290771484})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 7.234992027282715})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 5.528563499450684})
store['active_learning_steps'][42]['training']['best_epoch']=6
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.2812, 'crossentropy': 5.388183203125}
store['active_learning_steps'][42]['acquisition']={'indices': [['ood', 36401], ['id', 42841], ['id', 167], ['ood', 64279], ['ood', 14912]], 'labels': [-1, 8, 0, -1, -1], 'scores': [0.700859270458039, 1.2877869819160908, 1.7913771488421926, 2.2355154263697568, 2.6421416757730487]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.708026885986328})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 4.254087448120117})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 5.062335014343262})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 5.492959976196289})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 5.058747291564941})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2705078125, 'crossentropy': 5.4177565574646})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 4.925078392028809})
store['active_learning_steps'][43]['training']['best_epoch']=4
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.2632, 'crossentropy': 5.528710546875}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 11683], ['ood', 54539], ['ood', 8320], ['ood', 70358], ['id', 1696]], 'labels': [2, -1, -1, -1, 6], 'scores': [0.6450372614840774, 1.2180605659784716, 1.6912499626956423, 2.1221267151119445, 2.516242966319558]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.2528176307678223})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 4.251883506774902})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 6.223645210266113})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 5.370461463928223})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.930935859680176})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.2626, 'crossentropy': 4.376203515625}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 59167], ['ood', 32551], ['ood', 71309], ['id', 5725], ['id', 36373]], 'labels': [-1, -1, -1, 6, 8], 'scores': [0.4515562318119284, 0.868210810651231, 1.2190955217655999, 1.542798705746769, 1.854797257006231]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 3.064466953277588})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.832901954650879})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.9966020584106445})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 5.760676860809326})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 6.017477035522461})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 5.9898681640625})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 6.260663986206055})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 6.026158332824707})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 6.2375264167785645})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 5.762497901916504})
store['active_learning_steps'][45]['training']['best_epoch']=7
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.2646, 'crossentropy': 6.1137}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 31370], ['id', 35215], ['id', 48410], ['id', 47642], ['ood', 50950]], 'labels': [-1, 6, 1, 5, -1], 'scores': [0.6780516588189875, 1.2008620537462886, 1.6891753207927507, 2.1431289121883257, 2.544381257376256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 4.030584812164307})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 3.863095760345459})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 4.945975303649902})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 5.948494911193848})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.257081031799316})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.505923271179199})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 5.984105110168457})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 7.040113925933838})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 6.946648597717285})
store['active_learning_steps'][46]['training']['best_epoch']=6
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.2488, 'crossentropy': 5.710359765625}
store['active_learning_steps'][46]['acquisition']={'indices': [['ood', 50108], ['ood', 39955], ['ood', 38388], ['id', 38928], ['ood', 72915]], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.7718543323563494, 1.3689581526364316, 1.8960886862020576, 2.3704002596154012, 2.7840414174212516]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 2.9840753078460693})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.5236687660217285})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 5.562910556793213})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.548214435577393})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 6.307667255401611})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 5.067898750305176})
store['active_learning_steps'][47]['training']['best_epoch']=3
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.2585, 'crossentropy': 5.504773046875}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 60052], ['ood', 52811], ['ood', 65340], ['id', 16238], ['id', 27787]], 'labels': [-1, -1, -1, 3, 1], 'scores': [0.7000441198040281, 1.189898886326688, 1.6502105199670773, 2.0854475203742737, 2.4624001960110027]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.6834826469421387})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 4.466256618499756})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 4.330972194671631})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 5.041451454162598})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 5.579494953155518})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 6.843256950378418})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 5.709856986999512})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 5.814538955688477})
store['active_learning_steps'][48]['training']['best_epoch']=5
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.2809, 'crossentropy': 5.776268359375}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 62386], ['id', 42932], ['ood', 20529], ['id', 38978], ['ood', 24263]], 'labels': [-1, 0, -1, 3, -1], 'scores': [0.6800313264440185, 1.2846371952861397, 1.8250757849871135, 2.2382193566078783, 2.6268438214315255]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 2.997360944747925})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 5.136669158935547})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 4.678750514984131})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 4.800223350524902})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.275390625, 'crossentropy': 6.017134189605713})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 5.031699180603027})
store['active_learning_steps'][49]['training']['best_epoch']=3
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.2776, 'crossentropy': 4.67143125}
store['active_learning_steps'][49]['acquisition']={'indices': [['ood', 54976], ['id', 13296], ['id', 42550], ['id', 33695], ['id', 21999]], 'labels': [-1, 3, 9, 7, 0], 'scores': [0.6798865511156933, 1.251238508610383, 1.7439509167433562, 2.177399856274496, 2.566202760555039]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 3.763911724090576})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 4.573159217834473})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 5.734550476074219})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 5.097173690795898})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 5.672503471374512})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 5.522859573364258})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 6.413579940795898})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 5.7169413566589355})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.2506, 'crossentropy': 5.751551953125}
store['active_learning_steps'][50]['acquisition']={'indices': [['ood', 11008], ['ood', 70184], ['id', 22943], ['ood', 6992], ['id', 15833]], 'labels': [-1, -1, 8, -1, 0], 'scores': [0.6667463058974374, 1.21735178026819, 1.7217788059311534, 2.1641461936245108, 2.5344786308042266]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.5577731132507324})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 4.121921539306641})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 4.708483695983887})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.4727630615234375})
store['active_learning_steps'][51]['training']['best_epoch']=1
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.2581, 'crossentropy': 2.6493572265625}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 69362], ['ood', 7817], ['ood', 25957], ['ood', 13148], ['id', 40924]], 'labels': [-1, -1, -1, -1, 4], 'scores': [0.3111846631945876, 0.5573443625252112, 0.794211892048426, 1.0176255200666908, 1.2260652760043858]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 4.587348937988281})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 3.7441225051879883})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 3.9151418209075928})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 4.774591445922852})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 6.006901741027832})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 5.9398722648620605})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 6.271195411682129})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 6.56241512298584})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 7.440056800842285})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 6.4435834884643555})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 5.8727707862854})
store['active_learning_steps'][52]['training']['best_epoch']=8
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.2909, 'crossentropy': 6.72509296875}
store['active_learning_steps'][52]['acquisition']={'indices': [['ood', 56067], ['ood', 66278], ['id', 43506], ['ood', 15939], ['ood', 34569]], 'labels': [-1, -1, 9, -1, -1], 'scores': [0.8020425915078264, 1.4806629247385956, 2.069030279828933, 2.5680062246433586, 2.9866900311742626]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 3.980544090270996})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 3.6453194618225098})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 7.271157741546631})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 4.963350772857666})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.613852500915527})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 5.423045635223389})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 5.094805717468262})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 7.194981098175049})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 5.911293029785156})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 6.9248199462890625})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 6.1238017082214355})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 7.384678840637207})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 6.0268874168396})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 5.593186378479004})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 7.070752143859863})
store['active_learning_steps'][53]['training']['best_epoch']=12
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.279, 'crossentropy': 7.10114140625}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 65802], ['ood', 62328], ['ood', 71157], ['id', 7621], ['ood', 4330]], 'labels': [-1, -1, -1, 0, -1], 'scores': [0.7359043920348167, 1.3364219078950152, 1.8529174575744256, 2.3176949644787133, 2.71645746216777]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 3.750760316848755})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 4.253487586975098})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 6.264885902404785})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 6.036835193634033})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 5.024514198303223})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 5.7411370277404785})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 5.324122428894043})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.3046875, 'crossentropy': 5.182125568389893})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 6.194251537322998})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 6.384896278381348})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.2724609375, 'crossentropy': 6.495477676391602})
store['active_learning_steps'][54]['training']['best_epoch']=8
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.2957, 'crossentropy': 5.31990859375}
