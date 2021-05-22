store = {}
store['timestamp']=1621608536
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=5']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=5
store['worker_id']=5
store['num_workers']=24
store['config']={'seed': 1239, 'uniform_ood': True, 'id_dataset_name': 'SVHN', 'ood_dataset_name': 'CIFAR-10', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node | one_hot_targets{'num_classes': 10}) + ('CIFAR-10 (Train, seed=0, 50000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'SVHN (Test)'"}
store['initial_training_set_indices']=[38482, 18819, 58066, 14663, 39799, 53509, 12901, 26100, 61523, 67745, 57808, 69963, 69909, 45371, 37280, 48685, 26877, 52249, 66762, 14073]
store['evaluation_set_indices']=[9356, 52217, 13204, 15153, 14643, 13323, 68768, 23207, 25999, 62719, 62312, 67969, 24256, 39281, 37692, 459, 50826, 51277, 57053, 2584, 51764, 14758, 22887, 43685, 53675, 71612, 55166, 16551, 62820, 4535, 12102, 2976, 62920, 41178, 65425, 24347, 41886, 15904, 4242, 38591, 69801, 8821, 58682, 26825, 58891, 26239, 12097, 25295, 62111, 31755, 35768, 26368, 42500, 34271, 27190, 19058, 51104, 6911, 30075, 67867, 33661, 68699, 33542, 20892, 66108, 65071, 38221, 28545, 4922, 712, 69652, 9859, 30961, 51019, 29978, 24859, 3266, 17700, 8635, 6353, 5221, 42961, 38139, 71930, 52654, 10503, 21854, 36516, 30504, 22436, 45904, 30936, 48527, 39826, 3646, 58802, 10195, 14513, 6465, 6942, 57592, 56379, 26009, 61985, 2559, 12661, 12013, 46596, 22602, 4480, 17051, 33111, 8443, 71520, 63570, 69611, 25877, 35431, 68255, 42429, 25233, 38864, 11350, 35991, 55649, 57177, 7278, 4769, 20349, 2614, 44954, 59941, 37367, 65209, 17027, 19532, 53043, 65575, 20118, 14547, 5357, 36375, 13466, 33485, 25546, 9095, 13754, 12356, 31308, 21474, 7790, 60533, 72158, 29121, 42063, 39774, 8251, 53403, 49392, 11194, 9155, 41513, 66798, 65593, 59814, 15932, 37576, 11589, 53361, 63564, 23612, 39344, 15174, 35048, 32969, 69692, 25106, 48838, 47004, 4184, 853, 45864, 56849, 67982, 15528, 22376, 35245, 45656, 59597, 66590, 54076, 16022, 11813, 65618, 9234, 51953, 9766, 41955, 44395, 39226, 40025, 41050, 18973, 65107, 47464, 33366, 60380, 2486, 33728, 17384, 20252, 502, 5733, 4780, 8085, 20338, 65499, 16532, 46969, 7202, 65103, 41400, 26582, 27643, 8071, 55598, 37396, 44808, 26291, 28417, 36402, 28726, 22517, 69815, 36383, 23607, 23033, 27971, 2408, 2278, 41478, 44310, 22574, 36584, 20402, 39412, 4629, 15386, 62095, 71458, 33017, 16110, 17249, 12926, 3490, 47863, 57175, 70171, 64841, 69552, 16738, 53687, 49215, 68777, 42356, 44008, 58581, 4015, 25552, 6585, 63976, 21856, 22022, 55859, 646, 40666, 20229, 54017, 19316, 47715, 63714, 56139, 20095, 56198, 49498, 71125, 37745, 28370, 447, 16265, 16217, 31553, 42330, 39800, 4708, 41610, 26365, 29555, 39014, 12058, 57716, 30264, 19834, 44802, 28557, 41674, 58223, 69197, 20831, 68939, 58071, 61613, 908, 66783, 49048, 8901, 8366, 43877, 27035, 5594, 16712, 65988, 44267, 68598, 18916, 55473, 13995, 8035, 35402, 49125, 1977, 30455, 18722, 28193, 13172, 50182, 7501, 13256, 30190, 3792, 2123, 1945, 578, 46527, 39552, 67117, 42833, 5445, 46094, 33919, 17401, 32440, 65698, 21803, 1135, 10541, 46967, 10104, 10938, 63683, 40034, 50634, 69388, 36184, 19463, 34004, 28951, 14855, 64729, 14756, 22150, 21459, 17111, 16346, 43426, 67098, 33904, 31401, 7659, 48749, 63155, 2295, 10885, 35729, 19327, 37233, 62037, 43673, 32598, 17664, 54682, 26311, 47139, 39399, 39716, 12071, 64933, 24857, 5906, 55259, 19820, 50768, 64273, 5453, 68989, 5148, 32502, 26332, 21086, 2537, 56917, 2572, 33746, 12667, 67185, 22625, 22488, 46950, 11323, 7732, 4099, 66265, 45874, 44873, 50645, 54736, 27587, 37633, 20063, 1608, 10391, 69839, 40026, 23753, 16692, 70616, 33037, 36107, 60644, 10024, 70725, 42517, 59766, 63776, 5240, 4298, 48682, 2647, 31850, 35911, 50647, 29464, 44634, 59672, 65002, 63792, 17766, 62198, 24020, 42922, 58463, 65717, 23905, 3709, 24462, 16997, 57309, 37223, 66400, 62492, 47056, 40814, 21985, 72066, 40550, 18131, 28968, 4841, 27091, 18456, 30336, 57899, 48912, 37103, 49194, 47247, 54365, 28077, 55585, 49073, 62608, 17950, 33176, 69058, 59000, 33429, 19825, 69851, 24553, 14100, 52015, 34854, 8384, 22221, 35886, 67782, 48319, 56320, 19629, 42327, 58156, 24662, 57555, 36936, 69589, 3895, 49861, 58546, 37408, 20865, 9547, 2308, 60654, 64334, 29058, 57610, 3713, 22067, 67083, 55907, 60300, 36206, 2137, 31864, 59454, 62125, 3472, 61684, 53364, 19002, 5961, 5119, 54575, 21647, 10117, 2063, 45076, 7655, 17649, 16183, 34516, 22281, 64009, 1482, 45897, 16054, 26453, 54529, 22123, 51161, 56473, 51275, 58255, 30056, 58472, 25031, 45022, 19772, 18227, 61247, 64229, 33494, 42705, 32892, 7643, 6554, 38114, 71630, 50256, 48460, 12647, 41199, 26273, 45698, 52378, 67419, 39957, 34025, 21810, 36037, 46937, 32002, 68859, 22312, 38228, 49463, 32134, 43593, 12976, 48518, 29540, 49660, 65445, 20048, 50377, 55745, 48666, 34187, 14797, 1090, 9866, 49432, 16623, 66209, 29260, 52431, 20003, 17847, 51378, 16023, 68062, 44305, 16631, 27731, 24784, 39156, 11115, 28872, 68835, 23709, 69182, 55249, 51867, 58062, 15447, 54267, 22358, 11689, 32422, 17668, 70285, 14630, 66794, 3930, 48981, 53416, 52758, 259, 46199, 29534, 64541, 17082, 44746, 25437, 49288, 43065, 30764, 38017, 51276, 30890, 65349, 52566, 50133, 43793, 30313, 16596, 24263, 5825, 59782, 46247, 12714, 31550, 66659, 56183, 15363, 28327, 17799, 7985, 57408, 63114, 5656, 45109, 8170, 71088, 44865, 5179, 33238, 67850, 59037, 70356, 57561, 5224, 54748, 48857, 57920, 64313, 61094, 24227, 27540, 48418, 49627, 5977, 47424, 49350, 2294, 51114, 31731, 68660, 48657, 47982, 5572, 67954, 72131, 38419, 5584, 43252, 9618, 23545, 33898, 68204, 52186, 24178, 19915, 6776, 31485, 32593, 19584, 19419, 27692, 8249, 34767, 43187, 21199, 9445, 58948, 11805, 31566, 23275, 48477, 70581, 468, 60975, 35599, 51011, 23731, 62929, 52127, 43105, 47132, 37098, 36682, 66718, 11836, 18937, 8353, 39475, 25066, 3810, 42035, 61047, 31409, 53353, 43799, 66218, 33732, 13353, 60944, 44114, 63746, 58818, 58308, 71199, 34872, 33651, 31320, 10155, 22562, 26256, 588, 650, 11367, 32284, 59309, 47102, 12778, 23277, 11903, 57880, 27145, 31297, 29703, 71945, 51586, 46004, 3819, 11022, 9807, 13278, 4765, 14868, 45323, 64881, 49532, 21786, 27694, 4261, 4225, 19091, 72034, 55698, 45428, 10685, 53402, 56253, 46547, 71757, 51782, 51907, 35547, 4933, 17159, 55552, 42654, 15891, 18290, 60649, 12688, 14180, 27824, 31768, 58640, 10644, 65690, 49127, 6096, 11685, 19904, 65825, 9756, 69122, 22560, 15354, 7212, 69075, 32862, 40238, 51753, 2289, 15439, 32940, 48616, 33630, 61582, 59003, 31277, 69455, 15225, 6524, 12255, 35631, 19799, 939, 19052, 51599, 33349, 15648, 53478, 48461, 57688, 16560, 29049, 42225, 52412, 16140, 40390, 32570, 24745, 64558, 36783, 6915, 47728, 965, 11449, 5116, 5323, 60583, 65003, 49946, 14668, 41788, 22684, 41248, 57017, 35386, 56663, 11333, 6235, 14545, 57849, 48023, 18451, 52781, 55872, 12166, 65210, 42135, 45704, 22159, 13433, 43848, 57952, 67211, 13469, 11047, 5020, 42097, 20945, 63525, 38029, 4448, 12645, 67581, 29111, 8657, 67780, 64513, 18251, 17888, 32040, 59868, 23404, 9423, 1799, 42360, 38722, 2521, 70901, 20614, 58004, 61052, 52510, 1767, 18118, 63984, 8997, 7359, 57822, 51575, 1154, 20732, 22093, 36091, 65675, 30482, 18517, 58191, 41454, 56022, 42315, 16818, 29430, 51625, 52715, 19267, 60460, 50887, 71829, 53823, 20360, 60961, 45356, 39961, 39474, 66779, 32959, 45573, 36984, 2876, 30770, 34908, 12101, 10839, 42028, 42187, 29776, 30785, 65134, 31096, 13346, 32978, 29254, 50953, 33172, 13798, 22658, 32286, 20308, 15277, 9517, 18525, 14838, 14280, 35505, 71679, 35497, 51264, 15149, 15077, 19660, 2980, 11973, 61547, 51033, 60741, 11385, 19913, 68557, 23524, 68591, 9114]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.0927734375, 'crossentropy': 10.70887279510498})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 7.886605262756348})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1025390625, 'crossentropy': 11.20225715637207})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 10.14535903930664})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1103515625, 'crossentropy': 9.734682083129883})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.0942301782421635, 'crossentropy': 8.113882673248309}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 70220], ['id', 56472], ['id', 61020], ['id', 17162], ['id', 61597]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.680691150539491, 1.2354367232644181, 1.7565366871417245, 2.211554856463824, 2.605388664916786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.099609375, 'crossentropy': 9.791297912597656})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.0986328125, 'crossentropy': 7.5982232093811035})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.10546875, 'crossentropy': 8.208192825317383})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.095703125, 'crossentropy': 8.438673973083496})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1025390625, 'crossentropy': 8.765641212463379})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.10546875, 'crossentropy': 8.669160842895508})
store['active_learning_steps'][1]['training']['best_epoch']=3
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.10068377381684081, 'crossentropy': 8.113927689958512}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 21], ['id', 0], ['id', 1], ['id', 2], ['id', 3]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [nan, nan, nan, nan, nan]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1123046875, 'crossentropy': 8.095148086547852})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 8.733575820922852})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1064453125, 'crossentropy': 8.618911743164062})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1171875, 'crossentropy': 8.198678016662598})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 8.38904094696045})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 7.882741928100586})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1171875, 'crossentropy': 7.744558334350586})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 7.909853935241699})
store['active_learning_steps'][2]['training']['best_epoch']=5
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.1160878918254456, 'crossentropy': 8.392588929010449}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 62579], ['ood', 48259], ['id', 25858], ['id', 36975], ['id', 68869]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.9102186168669018, 1.546246392485699, 2.0699480379098407, 2.5565769248832364, 2.959533939722931]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.0966796875, 'crossentropy': 6.676157474517822})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.11328125, 'crossentropy': 10.581624984741211})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.0947265625, 'crossentropy': 9.586440086364746})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 8.893220901489258})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 8.156913757324219})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 8.393911361694336})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 7.695103645324707})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 7.8230695724487305})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 7.89424991607666})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1298828125, 'crossentropy': 8.401287078857422})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 8.352959632873535})
store['active_learning_steps'][3]['training']['best_epoch']=8
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.11989090350338046, 'crossentropy': 7.238003346842348}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 3152], ['id', 10634], ['id', 28676], ['id', 69989], ['id', 63528]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7560662782316272, 1.4446595739457173, 2.049921081780792, 2.5796363168218743, 2.960005531210655]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.0888671875, 'crossentropy': 6.867160797119141})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 8.545476913452148})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1171875, 'crossentropy': 7.4058451652526855})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.109375, 'crossentropy': 8.353862762451172})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 8.556035995483398})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 7.3055901527404785})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1044921875, 'crossentropy': 7.910496711730957})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 9.002742767333984})
store['active_learning_steps'][4]['training']['best_epoch']=5
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.1263060848186847, 'crossentropy': 7.7267179577059}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 67318], ['id', 25568], ['id', 27413], ['id', 17030], ['id', 71382]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9292268469004119, 1.726946823060111, 2.4434019274128147, 3.0462449843337467, 3.4279638043336123]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 7.330322265625})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 7.289566993713379})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.109375, 'crossentropy': 8.747406005859375})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 7.681618690490723})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1171875, 'crossentropy': 10.089818954467773})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 7.163740158081055})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 7.338374614715576})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.131299938537185, 'crossentropy': 8.031811208320528}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 19557], ['id', 48026], ['id', 17063], ['id', 44761], ['id', 37865]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7776375732083922, 1.412303579357589, 1.974882999011049, 2.467146117237008, 2.890852035442512]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 7.487125396728516})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 6.849926948547363})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 5.813849449157715})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 7.839158058166504})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 6.38878059387207})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.14601259987707438, 'crossentropy': 6.30717782440842}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 8643], ['id', 39490], ['id', 51919], ['id', 23827], ['id', 37639]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7120834580827187, 1.2791095190550816, 1.7706578720307187, 2.2115042241673724, 2.5804760613696196]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.0986328125, 'crossentropy': 6.17506217956543})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 9.544455528259277})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 5.454875946044922})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 5.977247714996338})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1279296875, 'crossentropy': 6.022461891174316})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 6.164710998535156})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.14432237246465887, 'crossentropy': 5.314631391172403}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 23313], ['id', 58260], ['id', 69731], ['id', 58000], ['id', 28316]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5764900728309006, 1.1070397213953167, 1.5813530372144537, 1.9738166044484426, 2.323551662436847]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1015625, 'crossentropy': 7.771055221557617})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 5.798537254333496})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 6.248325347900391})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 7.04747200012207})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 6.288393974304199})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 5.328639507293701})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 6.7241692543029785})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 6.711855888366699})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 6.672340393066406})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 7.198310375213623})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 6.567714691162109})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 6.490418434143066})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 6.765981674194336})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 6.546745300292969})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 6.895876407623291})
store['active_learning_steps'][8]['training']['best_epoch']=12
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.15665334972341732, 'crossentropy': 6.748653100030731}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 52128], ['id', 33952], ['ood', 41757], ['id', 35221], ['id', 30648]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6561642861393175, 1.2266929980101504, 1.7588032436223084, 2.213692798857175, 2.625059722378767]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.103515625, 'crossentropy': 6.614874839782715})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 6.8394317626953125})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 6.157259464263916})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 6.678530693054199})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 6.5546770095825195})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 6.76544189453125})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 6.728539943695068})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 6.973557949066162})
store['active_learning_steps'][9]['training']['best_epoch']=5
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.13179932390903504, 'crossentropy': 6.523906274008912}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 27672], ['id', 23909], ['id', 12145], ['id', 66914], ['id', 29355]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.604390817248742, 1.1643326120684927, 1.6134128233971383, 2.052600515614431, 2.445273167271516]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 5.929455757141113})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 4.763619422912598})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 6.5648980140686035})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 5.846949577331543})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.14970036877688997, 'crossentropy': 5.446490137138906}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 15584], ['id', 15973], ['id', 8713], ['id', 62878], ['id', 26772]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6218320072669083, 1.223313871287727, 1.724980766615634, 2.195930571185958, 2.5603668310941288]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 5.478794097900391})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 6.122406482696533})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 7.593214511871338})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 6.04337215423584})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 6.960319995880127})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 7.219633102416992})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 6.978520393371582})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 6.87141227722168})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 6.60698938369751})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 8.666924476623535})
store['active_learning_steps'][11]['training']['best_epoch']=7
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.14436078672403196, 'crossentropy': 7.837631328749231}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 67018], ['id', 38245], ['id', 12873], ['id', 18524], ['id', 13254]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.738017269280369, 1.4349804092001515, 2.0466296151997465, 2.5992624003933917, 3.039178942158614]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 7.039491653442383})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 5.583760738372803})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 5.6112446784973145})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 5.369217872619629})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 5.604687213897705})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.1470497848801475, 'crossentropy': 5.2926668379302395}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 11436], ['id', 41500], ['ood', 20286], ['id', 11086], ['id', 69747]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4972735846368508, 0.9565700810382629, 1.3958552436397063, 1.7944207281461164, 2.170656720573831]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 5.67415714263916})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 6.4618635177612305})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 5.477838516235352})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 7.570940017700195})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.15108328211432084, 'crossentropy': 5.189210634987708}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 24865], ['id', 25810], ['id', 17306], ['id', 44211], ['id', 65625]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5751023126275379, 1.104901081401382, 1.5970550980058165, 2.0631252338313937, 2.458020977942038]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 7.230037689208984})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.32388973236084})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 5.885722637176514})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 7.213064193725586})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 7.834774494171143})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 6.805298328399658})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 6.469539642333984})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.16445144437615242, 'crossentropy': 6.191166761101721}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 5208], ['id', 26991], ['id', 63408], ['id', 27617], ['id', 16155]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8418928227015181, 1.6134817986746963, 2.2291636627317795, 2.7193696166308756, 3.109316537820808]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 4.954619407653809})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 5.817654609680176})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 5.402009963989258})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 4.8090057373046875})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.952335357666016})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 6.88861083984375})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 6.714426040649414})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 5.9497175216674805})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.17393976644130302, 'crossentropy': 6.111606028157652}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 69120], ['id', 61619], ['id', 41191], ['id', 58315], ['id', 40633]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7054891702749466, 1.2704861129765206, 1.7708657698906975, 2.2129850847536936, 2.5827765456357845]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 4.8892974853515625})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 4.992551803588867})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 5.904449939727783})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.119067192077637})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.16206976029502151, 'crossentropy': 4.757637535053012}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 56766], ['id', 2233], ['id', 33627], ['id', 25439], ['id', 12772]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6766806935909462, 1.308827614840772, 1.8112453825733006, 2.256095265229992, 2.636911541330626]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.744828224182129})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 7.04152250289917})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 5.354050636291504})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 6.045680522918701})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 7.086258888244629})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 6.326818466186523})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 7.1612324714660645})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.14904732636754764, 'crossentropy': 5.633832878764597}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 28029], ['id', 17188], ['id', 52376], ['id', 59001], ['id', 20623]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7604808511451631, 1.4465162351443892, 2.031694381891182, 2.520659360428785, 2.9403480231912837]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 4.401327133178711})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 5.477860450744629})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 6.308753967285156})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 7.453131675720215})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.815114974975586})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 6.078692436218262})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 5.4789018630981445})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.000310897827148})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.480915069580078})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 5.41970157623291})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 5.527431488037109})
store['active_learning_steps'][18]['training']['best_epoch']=8
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.21331438229870928, 'crossentropy': 5.679444409764905}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 62633], ['id', 6302], ['id', 37001], ['id', 22729], ['id', 24599]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6343969961226659, 1.1948650645409145, 1.704409675039214, 2.186337261067269, 2.593667532518298]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 6.05099630355835})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 4.187215805053711})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.311629295349121})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 7.069799423217773})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 7.174454689025879})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 5.478115081787109})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.777728080749512})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.5700578689575195})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 5.979647159576416})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.975532531738281})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 5.241938591003418})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 5.938103675842285})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 6.674652099609375})
store['active_learning_steps'][19]['training']['best_epoch']=10
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.18377381684081132, 'crossentropy': 5.37182842271051}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 27504], ['id', 32554], ['id', 60204], ['id', 50205], ['id', 61880]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5882452527056632, 1.136068659363172, 1.6109620755267988, 2.0451812886669662, 2.4311800203519596]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 4.780291557312012})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 4.594741344451904})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.4485979080200195})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 5.282810211181641})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.682325839996338})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 5.729704856872559})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 4.727381706237793})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.21584972341733252, 'crossentropy': 5.189486137254149}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 16465], ['id', 33304], ['id', 19099], ['id', 32527], ['id', 40618]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6452766649858588, 1.2376277691889213, 1.780392587031864, 2.2177043082677654, 2.608916872252326]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 5.288760662078857})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 5.537006378173828})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 6.7624664306640625})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 4.926489353179932})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 6.560480117797852})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 4.821440696716309})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 4.449179649353027})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 5.924372673034668})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.1845036877688998, 'crossentropy': 6.998923200291949}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 55643], ['id', 50773], ['id', 27549], ['id', 49706], ['id', 16813]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7505230527602071, 1.345150845936868, 1.8461290449950756, 2.319964877536309, 2.7285590788602336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.092367172241211})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.448599815368652})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 4.9983015060424805})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 5.56057071685791})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.17113552550706823, 'crossentropy': 5.498587075522434}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 45534], ['id', 71986], ['id', 51209], ['id', 56675], ['id', 10991]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5284996204926224, 0.98752678425695, 1.4049266619467833, 1.7636605180346345, 2.0407448595440423]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 5.565640449523926})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 4.387813568115234})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 5.74669075012207})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 5.462480545043945})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 6.174142837524414})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.8577165603637695})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.56064510345459})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.348658561706543})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.884726524353027})
store['active_learning_steps'][23]['training']['best_epoch']=6
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.22987092808850645, 'crossentropy': 4.537868656845421}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 26847], ['id', 56077], ['id', 64651], ['ood', 11543], ['id', 20977]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5957844803197299, 1.127915362405357, 1.6416113429648949, 2.101020525446069, 2.510858004256799]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 4.502917766571045})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.191624164581299})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.5794782638549805})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 4.676881790161133})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 4.494290351867676})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 4.763416290283203})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.0060834884643555})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 4.094535827636719})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.19522126613398894, 'crossentropy': 4.289352407613706}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 31153], ['id', 70783], ['id', 24743], ['id', 69114], ['id', 72055]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6510835036180715, 1.2566233019500288, 1.7512677958323506, 2.206601509958962, 2.6179894358646507]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 4.384405136108398})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 5.371921539306641})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.874240875244141})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 5.034859657287598})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 5.363739967346191})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.602686882019043})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.387979030609131})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 5.744845867156982})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 4.743878364562988})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 4.632017612457275})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.022300720214844})
store['active_learning_steps'][25]['training']['best_epoch']=8
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.2203441917639828, 'crossentropy': 5.792693847956361}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 40642], ['id', 8021], ['id', 30629], ['id', 46549], ['ood', 12334]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6987842887331526, 1.2953884141791407, 1.8047513039268255, 2.288883223300447, 2.6973570352814686]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 5.2375688552856445})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.517818927764893})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 5.412961959838867})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 5.401618003845215})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 5.250818252563477})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 4.748960494995117})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 4.846150875091553})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 4.7181854248046875})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.298947334289551})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 5.335505485534668})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.18166103257529195, 'crossentropy': 4.722313222668254}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 450], ['id', 33484], ['id', 25522], ['id', 16517], ['id', 63403]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6341091875876481, 1.2177350536927052, 1.7375602353403954, 2.2231853459533992, 2.6642500204666906]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 5.474704742431641})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 4.898878574371338})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 4.365684509277344})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 4.282768249511719})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.14565372467041})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.2718048095703125})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 4.471678733825684})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 4.326404571533203})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.465945243835449})
store['active_learning_steps'][27]['training']['best_epoch']=6
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.20905039950829749, 'crossentropy': 4.198064221438998}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 47138], ['id', 43328], ['ood', 18341], ['id', 67767], ['id', 26893]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5786650603653496, 1.1354244774648379, 1.646768762643358, 2.0863838797117715, 2.4809256610353483]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 4.247744083404541})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 4.983954429626465})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 4.88271427154541})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 5.576228618621826})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.64907169342041})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 4.859638214111328})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 4.601008415222168})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 4.701478004455566})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 4.371676445007324})
store['active_learning_steps'][28]['training']['best_epoch']=6
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.21043331284572833, 'crossentropy': 4.298951770897357}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 40040], ['id', 30131], ['id', 64515], ['id', 29208], ['id', 116]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6848078589858262, 1.2469888757241683, 1.7502982319472231, 2.1971669905233213, 2.6058159973070456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 5.367686748504639})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 4.710275650024414})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.808886528015137})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 5.327805042266846})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.17463122311001844, 'crossentropy': 5.404021372733559}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 15531], ['id', 8918], ['id', 69613], ['id', 4671], ['id', 14460]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7312004489692994, 1.3609485657784988, 1.8650482624768405, 2.284864661448962, 2.650123436680955]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 4.062999248504639})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 4.828710079193115})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 4.210394859313965})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 4.853713512420654})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.760927200317383})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 6.265815734863281})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 4.609117031097412})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 5.308280944824219})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 5.187755584716797})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.448835372924805})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 4.747657775878906})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 4.980688095092773})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.228633880615234})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 5.168615341186523})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.213724613189697})
store['active_learning_steps'][30]['training']['best_epoch']=12
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.21631069452980947, 'crossentropy': 4.8856977710126}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 9150], ['id', 12044], ['id', 9045], ['id', 64182], ['id', 59136]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6771975686750449, 1.30472077235108, 1.867403067090299, 2.374538122007685, 2.795924488014803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 6.498959064483643})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 4.644512176513672})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 4.435291290283203})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 5.545585632324219})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 4.678954124450684})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.915603160858154})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.21546558082360173, 'crossentropy': 4.349869571584972}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 67748], ['id', 51822], ['id', 54374], ['id', 64237], ['id', 27442]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6525027736748495, 1.2744065429430464, 1.790531474221388, 2.254183285762112, 2.6322021449004174]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 3.4673471450805664})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 5.163675308227539})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 4.579952716827393})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 5.01003360748291})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 4.863353729248047})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.520608901977539})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 5.388270378112793})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 7.16363000869751})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 6.984687805175781})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 4.457356929779053})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.297469139099121})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.6632184982299805})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 4.8126349449157715})
store['active_learning_steps'][32]['training']['best_epoch']=10
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.22318684695759067, 'crossentropy': 4.051413584722649}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 69368], ['id', 64435], ['id', 45060], ['id', 29891], ['id', 17487]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5692191761550014, 1.0869798854127763, 1.5570632566241525, 2.0008347477308126, 2.41435661176172]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.239339828491211})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 4.733351707458496})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 5.142396450042725})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 4.338611602783203})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.3918304443359375})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.307779312133789})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 5.068899631500244})
store['active_learning_steps'][33]['training']['best_epoch']=4
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.22499231714812537, 'crossentropy': 4.062636550687615}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 66524], ['id', 38093], ['id', 71671], ['id', 60363], ['id', 14626]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.574633115049267, 1.1228697674515367, 1.6220772677796154, 2.054739192879161, 2.4130949797405314]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 3.8063907623291016})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 4.731827735900879})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 4.247823715209961})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 4.471419334411621})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.30096435546875})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 4.783655643463135})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 4.91261100769043})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 3.8911709785461426})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 4.21938943862915})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 5.5619001388549805})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 4.314140319824219})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 3.9551944732666016})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 3.9180779457092285})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 3.6955549716949463})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 4.593313217163086})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 4.544635772705078})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.749428749084473})
store['active_learning_steps'][34]['training']['best_epoch']=14
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.25311155500921945, 'crossentropy': 3.7333009012945606}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 49889], ['id', 1240], ['id', 35945], ['id', 29867], ['id', 6635]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7116869420424743, 1.3372874904028782, 1.9156757969651714, 2.371012318518085, 2.771486617844957]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 3.702974796295166})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 4.895482063293457})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 5.342000961303711})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 4.103854179382324})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 4.578372955322266})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 4.032711982727051})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.7194976806640625})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.778494834899902})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.19902427781192378, 'crossentropy': 4.400266378879841}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 9572], ['id', 9338], ['id', 48168], ['id', 24996], ['id', 23212]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7749818148741578, 1.3256752265832148, 1.8114787928941758, 2.253044144666111, 2.6433719767783614]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 3.1027822494506836})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 5.047560214996338})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 4.616269111633301})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.796605110168457})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.299433708190918})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.673364639282227})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 4.381054878234863})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.068243980407715})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 5.363498687744141})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.548576354980469})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 4.95722770690918})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 7.277832984924316})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 5.358827590942383})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 4.855831146240234})
store['active_learning_steps'][36]['training']['best_epoch']=11
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.2377458512599877, 'crossentropy': 4.496569126459742}
