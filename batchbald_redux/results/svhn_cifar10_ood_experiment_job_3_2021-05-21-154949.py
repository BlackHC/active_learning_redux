store = {}
store['timestamp']=1621608589
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=3']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=3
store['worker_id']=3
store['num_workers']=24
store['config']={'seed': 1237, 'uniform_ood': False, 'id_dataset_name': 'SVHN', 'ood_dataset_name': 'CIFAR-10', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node) + ('CIFAR-10 (Train, seed=0, 50000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'SVHN (Test)'"}
store['initial_training_set_indices']=[38482, 18819, 58066, 14663, 39799, 53509, 12901, 26100, 61523, 67745, 57808, 69963, 69909, 45371, 37280, 48685, 26877, 52249, 66762, 14073]
store['evaluation_set_indices']=[9356, 52217, 13204, 15153, 14643, 13323, 68768, 23207, 25999, 62719, 62312, 67969, 24256, 39281, 37692, 459, 50826, 51277, 57053, 2584, 51764, 14758, 22887, 43685, 53675, 71612, 55166, 16551, 62820, 4535, 12102, 2976, 62920, 41178, 65425, 24347, 41886, 15904, 4242, 38591, 69801, 8821, 58682, 26825, 58891, 26239, 12097, 25295, 62111, 31755, 35768, 26368, 42500, 34271, 27190, 19058, 51104, 6911, 30075, 67867, 33661, 68699, 33542, 20892, 66108, 65071, 38221, 28545, 4922, 712, 69652, 9859, 30961, 51019, 29978, 24859, 3266, 17700, 8635, 6353, 5221, 42961, 38139, 71930, 52654, 10503, 21854, 36516, 30504, 22436, 45904, 30936, 48527, 39826, 3646, 58802, 10195, 14513, 6465, 6942, 57592, 56379, 26009, 61985, 2559, 12661, 12013, 46596, 22602, 4480, 17051, 33111, 8443, 71520, 63570, 69611, 25877, 35431, 68255, 42429, 25233, 38864, 11350, 35991, 55649, 57177, 7278, 4769, 20349, 2614, 44954, 59941, 37367, 65209, 17027, 19532, 53043, 65575, 20118, 14547, 5357, 36375, 13466, 33485, 25546, 9095, 13754, 12356, 31308, 21474, 7790, 60533, 72158, 29121, 42063, 39774, 8251, 53403, 49392, 11194, 9155, 41513, 66798, 65593, 59814, 15932, 37576, 11589, 53361, 63564, 23612, 39344, 15174, 35048, 32969, 69692, 25106, 48838, 47004, 4184, 853, 45864, 56849, 67982, 15528, 22376, 35245, 45656, 59597, 66590, 54076, 16022, 11813, 65618, 9234, 51953, 9766, 41955, 44395, 39226, 40025, 41050, 18973, 65107, 47464, 33366, 60380, 2486, 33728, 17384, 20252, 502, 5733, 4780, 8085, 20338, 65499, 16532, 46969, 7202, 65103, 41400, 26582, 27643, 8071, 55598, 37396, 44808, 26291, 28417, 36402, 28726, 22517, 69815, 36383, 23607, 23033, 27971, 2408, 2278, 41478, 44310, 22574, 36584, 20402, 39412, 4629, 15386, 62095, 71458, 33017, 16110, 17249, 12926, 3490, 47863, 57175, 70171, 64841, 69552, 16738, 53687, 49215, 68777, 42356, 44008, 58581, 4015, 25552, 6585, 63976, 21856, 22022, 55859, 646, 40666, 20229, 54017, 19316, 47715, 63714, 56139, 20095, 56198, 49498, 71125, 37745, 28370, 447, 16265, 16217, 31553, 42330, 39800, 4708, 41610, 26365, 29555, 39014, 12058, 57716, 30264, 19834, 44802, 28557, 41674, 58223, 69197, 20831, 68939, 58071, 61613, 908, 66783, 49048, 8901, 8366, 43877, 27035, 5594, 16712, 65988, 44267, 68598, 18916, 55473, 13995, 8035, 35402, 49125, 1977, 30455, 18722, 28193, 13172, 50182, 7501, 13256, 30190, 3792, 2123, 1945, 578, 46527, 39552, 67117, 42833, 5445, 46094, 33919, 17401, 32440, 65698, 21803, 1135, 10541, 46967, 10104, 10938, 63683, 40034, 50634, 69388, 36184, 19463, 34004, 28951, 14855, 64729, 14756, 22150, 21459, 17111, 16346, 43426, 67098, 33904, 31401, 7659, 48749, 63155, 2295, 10885, 35729, 19327, 37233, 62037, 43673, 32598, 17664, 54682, 26311, 47139, 39399, 39716, 12071, 64933, 24857, 5906, 55259, 19820, 50768, 64273, 5453, 68989, 5148, 32502, 26332, 21086, 2537, 56917, 2572, 33746, 12667, 67185, 22625, 22488, 46950, 11323, 7732, 4099, 66265, 45874, 44873, 50645, 54736, 27587, 37633, 20063, 1608, 10391, 69839, 40026, 23753, 16692, 70616, 33037, 36107, 60644, 10024, 70725, 42517, 59766, 63776, 5240, 4298, 48682, 2647, 31850, 35911, 50647, 29464, 44634, 59672, 65002, 63792, 17766, 62198, 24020, 42922, 58463, 65717, 23905, 3709, 24462, 16997, 57309, 37223, 66400, 62492, 47056, 40814, 21985, 72066, 40550, 18131, 28968, 4841, 27091, 18456, 30336, 57899, 48912, 37103, 49194, 47247, 54365, 28077, 55585, 49073, 62608, 17950, 33176, 69058, 59000, 33429, 19825, 69851, 24553, 14100, 52015, 34854, 8384, 22221, 35886, 67782, 48319, 56320, 19629, 42327, 58156, 24662, 57555, 36936, 69589, 3895, 49861, 58546, 37408, 20865, 9547, 2308, 60654, 64334, 29058, 57610, 3713, 22067, 67083, 55907, 60300, 36206, 2137, 31864, 59454, 62125, 3472, 61684, 53364, 19002, 5961, 5119, 54575, 21647, 10117, 2063, 45076, 7655, 17649, 16183, 34516, 22281, 64009, 1482, 45897, 16054, 26453, 54529, 22123, 51161, 56473, 51275, 58255, 30056, 58472, 25031, 45022, 19772, 18227, 61247, 64229, 33494, 42705, 32892, 7643, 6554, 38114, 71630, 50256, 48460, 12647, 41199, 26273, 45698, 52378, 67419, 39957, 34025, 21810, 36037, 46937, 32002, 68859, 22312, 38228, 49463, 32134, 43593, 12976, 48518, 29540, 49660, 65445, 20048, 50377, 55745, 48666, 34187, 14797, 1090, 9866, 49432, 16623, 66209, 29260, 52431, 20003, 17847, 51378, 16023, 68062, 44305, 16631, 27731, 24784, 39156, 11115, 28872, 68835, 23709, 69182, 55249, 51867, 58062, 15447, 54267, 22358, 11689, 32422, 17668, 70285, 14630, 66794, 3930, 48981, 53416, 52758, 259, 46199, 29534, 64541, 17082, 44746, 25437, 49288, 43065, 30764, 38017, 51276, 30890, 65349, 52566, 50133, 43793, 30313, 16596, 24263, 5825, 59782, 46247, 12714, 31550, 66659, 56183, 15363, 28327, 17799, 7985, 57408, 63114, 5656, 45109, 8170, 71088, 44865, 5179, 33238, 67850, 59037, 70356, 57561, 5224, 54748, 48857, 57920, 64313, 61094, 24227, 27540, 48418, 49627, 5977, 47424, 49350, 2294, 51114, 31731, 68660, 48657, 47982, 5572, 67954, 72131, 38419, 5584, 43252, 9618, 23545, 33898, 68204, 52186, 24178, 19915, 6776, 31485, 32593, 19584, 19419, 27692, 8249, 34767, 43187, 21199, 9445, 58948, 11805, 31566, 23275, 48477, 70581, 468, 60975, 35599, 51011, 23731, 62929, 52127, 43105, 47132, 37098, 36682, 66718, 11836, 18937, 8353, 39475, 25066, 3810, 42035, 61047, 31409, 53353, 43799, 66218, 33732, 13353, 60944, 44114, 63746, 58818, 58308, 71199, 34872, 33651, 31320, 10155, 22562, 26256, 588, 650, 11367, 32284, 59309, 47102, 12778, 23277, 11903, 57880, 27145, 31297, 29703, 71945, 51586, 46004, 3819, 11022, 9807, 13278, 4765, 14868, 45323, 64881, 49532, 21786, 27694, 4261, 4225, 19091, 72034, 55698, 45428, 10685, 53402, 56253, 46547, 71757, 51782, 51907, 35547, 4933, 17159, 55552, 42654, 15891, 18290, 60649, 12688, 14180, 27824, 31768, 58640, 10644, 65690, 49127, 6096, 11685, 19904, 65825, 9756, 69122, 22560, 15354, 7212, 69075, 32862, 40238, 51753, 2289, 15439, 32940, 48616, 33630, 61582, 59003, 31277, 69455, 15225, 6524, 12255, 35631, 19799, 939, 19052, 51599, 33349, 15648, 53478, 48461, 57688, 16560, 29049, 42225, 52412, 16140, 40390, 32570, 24745, 64558, 36783, 6915, 47728, 965, 11449, 5116, 5323, 60583, 65003, 49946, 14668, 41788, 22684, 41248, 57017, 35386, 56663, 11333, 6235, 14545, 57849, 48023, 18451, 52781, 55872, 12166, 65210, 42135, 45704, 22159, 13433, 43848, 57952, 67211, 13469, 11047, 5020, 42097, 20945, 63525, 38029, 4448, 12645, 67581, 29111, 8657, 67780, 64513, 18251, 17888, 32040, 59868, 23404, 9423, 1799, 42360, 38722, 2521, 70901, 20614, 58004, 61052, 52510, 1767, 18118, 63984, 8997, 7359, 57822, 51575, 1154, 20732, 22093, 36091, 65675, 30482, 18517, 58191, 41454, 56022, 42315, 16818, 29430, 51625, 52715, 19267, 60460, 50887, 71829, 53823, 20360, 60961, 45356, 39961, 39474, 66779, 32959, 45573, 36984, 2876, 30770, 34908, 12101, 10839, 42028, 42187, 29776, 30785, 65134, 31096, 13346, 32978, 29254, 50953, 33172, 13798, 22658, 32286, 20308, 15277, 9517, 18525, 14838, 14280, 35505, 71679, 35497, 51264, 15149, 15077, 19660, 2980, 11973, 61547, 51033, 60741, 11385, 19913, 68557, 23524, 68591, 9114]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 9.374654769897461})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1123046875, 'crossentropy': 9.028488159179688})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 9.273488998413086})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1171875, 'crossentropy': 9.545455932617188})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.1090580823601721, 'crossentropy': 9.979876330093731}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 4.336522102355957})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1044921875, 'crossentropy': 4.593088150024414})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1083984375, 'crossentropy': 5.395223617553711})
store['active_learning_steps'][0]['eval_training']['best_epoch']=1
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 66699], ['id', 41954], ['id', 52634], ['id', 17940], ['id', 15596]], 'labels': [6, 4, 2, 7, 2], 'scores': [0.612004829080341, 1.1061096486763176, 1.568860176503505, 1.9860786803936463, 2.3270591517703574]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 9.55389404296875})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1044921875, 'crossentropy': 8.695592880249023})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1123046875, 'crossentropy': 8.730117797851562})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.099609375, 'crossentropy': 10.968557357788086})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.10291180086047941, 'crossentropy': 9.91916079248617}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.0751953125, 'crossentropy': 4.936549186706543})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 4.266460418701172})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.103515625, 'crossentropy': 5.257636070251465})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 9652], ['id', 20969], ['id', 50662], ['ood', 10488], ['id', 38764]], 'labels': [1, 0, 1, -1, 0], 'scores': [0.922857253387438, 1.6206114522376631, 2.2067766903679003, 2.6637318746995815, 2.9799301474769733]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 8.014286041259766})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 7.754585266113281})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 7.918570518493652})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 8.083984375})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 8.377105712890625})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 8.37978744506836})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.12062077443146896, 'crossentropy': 8.252326463583282}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1044921875, 'crossentropy': 4.663535118103027})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 4.499638557434082})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 5.169255256652832})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 5.147150039672852})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 5.124096870422363})
store['active_learning_steps'][2]['eval_training']['best_epoch']=4
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 64631], ['id', 39896], ['id', 54970], ['id', 35857], ['id', 60344]], 'labels': [7, 9, 8, 9, 3], 'scores': [0.5826569462933311, 1.0832430148451762, 1.495897022423013, 1.868374429759831, 2.194445239903632]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.11328125, 'crossentropy': 9.316497802734375})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.11328125, 'crossentropy': 8.367183685302734})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 8.799701690673828})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 9.419897079467773})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 7.173298358917236})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 7.386068344116211})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.12450061462814997, 'crossentropy': 8.50486960759834}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 4.5668816566467285})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 4.848756790161133})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 4.831195831298828})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 4.967596054077148})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 4.617862224578857})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 4266], ['id', 41744], ['id', 9194], ['ood', 19397], ['id', 50831]], 'labels': [0, 6, 1, -1, 0], 'scores': [0.534469994790677, 1.0020940433674226, 1.4038203821653141, 1.743952602381196, 2.0654855241841923]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 7.299091339111328})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1103515625, 'crossentropy': 7.590386390686035})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 7.72718620300293})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 7.703728675842285})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.1250384142593731, 'crossentropy': 7.6569576626843885}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.103515625, 'crossentropy': 3.4922266006469727})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.103515625, 'crossentropy': 3.894975185394287})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.111328125, 'crossentropy': 4.604238986968994})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 55153], ['id', 13218], ['id', 69344], ['id', 11148], ['id', 11573]], 'labels': [1, 2, 3, 9, 2], 'scores': [0.6244283265252273, 1.1756871325814724, 1.6268562344565356, 1.9793216607391226, 2.2887088941252856]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.109375, 'crossentropy': 8.178201675415039})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 6.705548286437988})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1298828125, 'crossentropy': 8.214151382446289})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 8.082658767700195})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 9.014055252075195})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 8.828638076782227})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.12791948371235404, 'crossentropy': 7.689935704133374}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 3.7451553344726562})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1123046875, 'crossentropy': 3.993438243865967})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 4.951226234436035})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 4.499970436096191})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 4.114213943481445})
store['active_learning_steps'][5]['eval_training']['best_epoch']=5
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 28304], ['id', 51468], ['id', 68497], ['id', 47020], ['ood', 38202]], 'labels': [1, 1, 8, 5, -1], 'scores': [0.6270765264472551, 1.1251101392865017, 1.585149567903077, 2.0122370560447793, 2.326177619428868]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 6.443085670471191})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 6.57127046585083})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 9.738138198852539})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 7.343492031097412})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.13114628149969268, 'crossentropy': 6.512082485018439}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 4.034431457519531})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 3.847242832183838})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 4.059031009674072})
store['active_learning_steps'][6]['eval_training']['best_epoch']=1
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 65089], ['id', 70262], ['id', 47963], ['id', 35299], ['id', 49514]], 'labels': [8, 5, 6, 9, 1], 'scores': [0.7033022924762995, 1.1746184943502782, 1.5899705554111105, 1.9840236479250395, 2.2924177721594714]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 7.7710466384887695})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 5.520256042480469})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 6.095146656036377})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 8.005008697509766})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 7.3684210777282715})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1123046875, 'crossentropy': 6.099307060241699})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 6.149196624755859})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.1407882606023356, 'crossentropy': 7.542156648547941}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 3.151608467102051})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 3.522289276123047})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 3.9491472244262695})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 4.419727802276611})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 4.333512306213379})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 16739], ['id', 35247], ['id', 39683], ['id', 3117], ['id', 22900]], 'labels': [7, 8, 5, 7, 3], 'scores': [0.5894461889102376, 1.1537245524845146, 1.5654834955727441, 1.9432433608019064, 2.247708524266475]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 9.084144592285156})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 6.463542938232422})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 6.962003231048584})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.095703125, 'crossentropy': 7.831081390380859})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.10598494161032575, 'crossentropy': 10.84747618315919}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 4.987296104431152})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.1103515625, 'crossentropy': 4.991372108459473})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.1025390625, 'crossentropy': 4.876861572265625})
store['active_learning_steps'][8]['eval_training']['best_epoch']=1
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 5502], ['id', 23306], ['id', 32800], ['id', 15835], ['ood', 3530]], 'labels': [1, 8, 5, 4, -1], 'scores': [0.7635453356671393, 1.2902108629788545, 1.7442557272149615, 2.147974718063474, 2.5027382657633925]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 5.420342445373535})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 5.715945243835449})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 5.3178253173828125})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1123046875, 'crossentropy': 6.913384437561035})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.14213275968039335, 'crossentropy': 5.11704764808697}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 3.803987979888916})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 3.9672622680664062})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 3.9325156211853027})
store['active_learning_steps'][9]['eval_training']['best_epoch']=1
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 14608], ['id', 11933], ['id', 30799], ['id', 32330], ['id', 16958]], 'labels': [-1, 1, 1, 1, 9], 'scores': [0.4897567081801901, 0.9261626896845296, 1.3166622097796976, 1.6733137666652311, 1.9658978167802301]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 6.485949516296387})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 6.200841426849365})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 5.249290466308594})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 5.566618919372559})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 6.556376934051514})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 6.422720909118652})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 6.589320182800293})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 6.739200592041016})
store['active_learning_steps'][10]['training']['best_epoch']=5
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.14985402581438229, 'crossentropy': 6.633174434350031}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 3.4995596408843994})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 4.237403869628906})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 4.396679401397705})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 4.073897361755371})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 4.05762243270874})
store['active_learning_steps'][10]['eval_training']['best_epoch']=2
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 27020], ['id', 3276], ['id', 63816], ['id', 66059], ['id', 48593]], 'labels': [0, 1, 2, 5, 9], 'scores': [0.4518274778326589, 0.876553961439468, 1.2691018302192605, 1.5962524277268089, 1.8844251337167695]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 5.614952087402344})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 6.647785186767578})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 5.8464155197143555})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1298828125, 'crossentropy': 7.126663684844971})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 6.3757829666137695})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 6.752562522888184})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 6.794842720031738})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 6.794626235961914})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 6.480082988739014})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 7.0010528564453125})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 6.954864501953125})
store['active_learning_steps'][11]['training']['best_epoch']=8
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.15400276582667485, 'crossentropy': 6.740724156807007}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 3.2860679626464844})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 3.9301650524139404})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 3.4569408893585205})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 3.9855620861053467})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 3.9591474533081055})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 3.797041654586792})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 6228], ['id', 6021], ['id', 24580], ['id', 15771], ['id', 16188]], 'labels': [9, 2, 1, 8, 2], 'scores': [0.5623896779940245, 1.028428164442325, 1.4653583721359689, 1.870010689939266, 2.208468230940193]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 5.639900207519531})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 5.940122127532959})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 6.7400712966918945})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 7.621034622192383})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.14916256914566686, 'crossentropy': 5.5555272117009835}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 3.734802484512329})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 4.364967346191406})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 3.793095588684082})
store['active_learning_steps'][12]['eval_training']['best_epoch']=2
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 18895], ['id', 12687], ['ood', 20710], ['id', 58887], ['ood', 28068]], 'labels': [1, 1, -1, 1, -1], 'scores': [0.5761437689000339, 1.0170090899809567, 1.4022669449092107, 1.7431226423509287, 2.03697513357678]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 6.527831077575684})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 6.15032958984375})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 5.2496843338012695})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 6.564184188842773})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 6.162674903869629})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 5.4331560134887695})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 5.817670822143555})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 5.9988532066345215})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 6.2188825607299805})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 6.201661109924316})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 6.20468282699585})
store['active_learning_steps'][13]['training']['best_epoch']=8
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.15108328211432084, 'crossentropy': 5.989290824754149}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 3.3053908348083496})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 3.273623466491699})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 3.4875411987304688})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 3.845292329788208})
store['active_learning_steps'][13]['eval_training']['best_epoch']=1
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 7662], ['id', 4602], ['id', 53695], ['id', 43809], ['id', 34681]], 'labels': [-1, 5, 3, 1, 1], 'scores': [0.5330510853728245, 1.026193883183232, 1.4768506099651106, 1.8605537046604192, 2.1975435539383454]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 4.960108757019043})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 6.017809867858887})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 6.3129072189331055})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 5.8085737228393555})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 6.1493120193481445})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 6.2160844802856445})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 6.57078742980957})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 7.2845458984375})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.13272126613398894, 'crossentropy': 5.943179908381992}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 2.8901233673095703})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.1171875, 'crossentropy': 3.524416446685791})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 3.7775516510009766})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 4.054318428039551})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 3.7839467525482178})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 4.042927265167236})
store['active_learning_steps'][14]['eval_training']['best_epoch']=3
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 16290], ['id', 7859], ['id', 63671], ['id', 65306], ['id', 58934]], 'labels': [8, 1, 6, 5, 5], 'scores': [0.41569627533234943, 0.8155400904797381, 1.2002152908363377, 1.5451080112012603, 1.8548435973248374]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 6.410066604614258})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 5.944482803344727})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 5.88379430770874})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 5.968886852264404})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 6.621551513671875})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.892850875854492})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 6.296865940093994})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 5.725895881652832})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 7.58334493637085})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.14528272894898586, 'crossentropy': 6.033412002535341}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 3.2249410152435303})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 3.105691432952881})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 3.448211193084717})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 3.743824005126953})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 3.6321821212768555})
store['active_learning_steps'][15]['eval_training']['best_epoch']=2
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 66067], ['id', 24022], ['id', 7922], ['id', 44900], ['id', 3166]], 'labels': [6, 9, 5, 8, 1], 'scores': [0.5250611863618717, 0.9752283842389158, 1.4028853917358077, 1.743583785617865, 2.039218593922243]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 6.107210159301758})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 7.787698745727539})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 7.043879508972168})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 6.622358322143555})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 5.9040374755859375})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 6.7922210693359375})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 6.218839168548584})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 7.795772552490234})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 6.33631706237793})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 6.909809112548828})
store['active_learning_steps'][16]['training']['best_epoch']=7
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.1474339274738783, 'crossentropy': 6.358490271588813}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 3.558022975921631})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 4.099745273590088})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 3.5581161975860596})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 3.912020683288574})
store['active_learning_steps'][16]['eval_training']['best_epoch']=1
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 35041], ['id', 64969], ['id', 58974], ['id', 53575], ['id', 58415]], 'labels': [0, 6, 9, 2, 9], 'scores': [0.6270825567270326, 1.1362568608724264, 1.5764008508268632, 1.9741323653967946, 2.321166250144201]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 5.473907470703125})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 6.71938943862915})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 7.401918411254883})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 6.275136947631836})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 6.114037036895752})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 6.218583583831787})
store['active_learning_steps'][17]['training']['best_epoch']=3
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.14824062692071296, 'crossentropy': 7.345361598225261}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 3.6068203449249268})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 3.9270613193511963})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 4.0261077880859375})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 4.451691627502441})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 4.3235979080200195})
store['active_learning_steps'][17]['eval_training']['best_epoch']=5
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 68060], ['id', 30701], ['id', 32398], ['id', 28372], ['id', 25784]], 'labels': [8, 7, 9, 6, 9], 'scores': [0.748520379677249, 1.322187640338097, 1.7780843973988427, 2.160499831254354, 2.5014475024954224]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 6.089883804321289})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 6.286763668060303})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 5.8852620124816895})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 6.661299705505371})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 6.660829544067383})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 8.110715866088867})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.14136447449293177, 'crossentropy': 5.743392747387831}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 3.137712001800537})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 3.609628677368164})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 3.513397455215454})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 3.5802114009857178})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 3.734687328338623})
store['active_learning_steps'][18]['eval_training']['best_epoch']=2
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 39765], ['id', 63078], ['id', 10857], ['ood', 35063], ['id', 30670]], 'labels': [1, 9, 8, -1, 0], 'scores': [0.5243355041222088, 0.9369691978226166, 1.3239256510471953, 1.6715319268920221, 1.9944274242675193]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 5.876156806945801})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 5.038950443267822})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 5.558261394500732})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 5.66878080368042})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 7.071155548095703})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.1516979102642901, 'crossentropy': 4.855564785648433}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 3.0071916580200195})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 3.0122525691986084})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 3.362359046936035})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 3.3887557983398438})
store['active_learning_steps'][19]['eval_training']['best_epoch']=4
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 20780], ['ood', 40826], ['id', 32205], ['id', 71314], ['id', 45440]], 'labels': [1, -1, 1, 3, 8], 'scores': [0.4710126059079418, 0.8782060074587803, 1.2323379175694957, 1.556154483109637, 1.803526611390435]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 5.178735733032227})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 6.4378461837768555})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 5.0784711837768555})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 5.87138557434082})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.15238936693300553, 'crossentropy': 5.077662228219115}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 3.538719415664673})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 3.6836163997650146})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 3.4704933166503906})
store['active_learning_steps'][20]['eval_training']['best_epoch']=1
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 3286], ['id', 22290], ['id', 4494], ['id', 25743], ['id', 51447]], 'labels': [-1, 3, 9, 1, 6], 'scores': [0.438811116000561, 0.8332779978619107, 1.2190922254441077, 1.5431228944852853, 1.8399646008241035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.662989616394043})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 6.141914367675781})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 5.6382365226745605})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 6.349766254425049})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 5.640298843383789})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.17851106330669944, 'crossentropy': 6.287561942993239}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 3.899534225463867})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 4.031307697296143})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 4.008613109588623})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 3.699868679046631})
store['active_learning_steps'][21]['eval_training']['best_epoch']=4
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 65886], ['id', 17087], ['id', 24671], ['id', 5493], ['id', 32095]], 'labels': [1, 7, 2, 4, 1], 'scores': [0.4400731317872326, 0.8290500354473918, 1.1870758839009123, 1.5225365646729996, 1.8282821253557757]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 5.879225730895996})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.984251976013184})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 6.3552775382995605})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 6.064598083496094})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 5.862614154815674})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.15565457897971727, 'crossentropy': 6.046381016633374}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 3.196094512939453})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 3.538083553314209})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 3.4891929626464844})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 3.7780587673187256})
store['active_learning_steps'][22]['eval_training']['best_epoch']=4
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 22798], ['id', 2886], ['id', 8180], ['id', 37784], ['id', 54237]], 'labels': [-1, 0, 1, 9, 1], 'scores': [0.5024427511882761, 0.9652945394835953, 1.3678271225388852, 1.69348047293116, 1.993559309947364]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 6.693046569824219})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 5.738951683044434})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 6.116678714752197})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 6.043515205383301})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 5.887413501739502})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 5.87687873840332})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.16906115550092193, 'crossentropy': 5.545967463122311}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 3.3037848472595215})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 3.553982734680176})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 3.512669086456299})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 3.5649471282958984})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 3.687873601913452})
store['active_learning_steps'][23]['eval_training']['best_epoch']=4
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 61652], ['id', 58906], ['id', 20787], ['id', 35774], ['id', 56975]], 'labels': [1, 1, 1, 8, 7], 'scores': [0.5934900292603942, 1.1441415565292195, 1.5328295142961403, 1.8607411843828239, 2.1614677807301774]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 5.035294055938721})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 5.585379600524902})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 6.419287204742432})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 4.9608612060546875})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.003728866577148})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 5.846997261047363})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 6.211091995239258})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 6.370022296905518})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.1706361401352182, 'crossentropy': 4.958476886620313}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 3.3868894577026367})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 3.129380464553833})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 3.36037015914917})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 3.374398708343506})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 3.5121583938598633})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 3.476961612701416})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 3.530998706817627})
store['active_learning_steps'][24]['eval_training']['best_epoch']=4
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 1381], ['id', 63236], ['id', 32588], ['ood', 12149], ['id', 3357]], 'labels': [7, 1, 1, -1, 2], 'scores': [0.4852035145417386, 0.9248234713192882, 1.2906252838430534, 1.6385539534633944, 1.9218584861339338]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 6.315722465515137})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 4.840786933898926})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 7.032393455505371})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.533725261688232})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 6.53901481628418})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 6.056467056274414})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.2682271003723145})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 5.926976203918457})
store['active_learning_steps'][25]['training']['best_epoch']=5
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.16760141364474493, 'crossentropy': 6.848194649854026}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 3.277876615524292})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 3.9909496307373047})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 3.676661491394043})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 4.214293479919434})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.9522881507873535})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 4.025130748748779})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.9111428260803223})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 67793], ['id', 15211], ['id', 24652], ['ood', 39614], ['id', 70362]], 'labels': [4, 5, 6, -1, 0], 'scores': [0.5458748112628683, 1.0515359378429299, 1.5013588201540142, 1.8874356921091784, 2.2347203686322663]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 5.713844299316406})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 5.07913875579834})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 6.019903182983398})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 5.897201061248779})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.656425476074219})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 5.707195281982422})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 5.708067893981934})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.840248107910156})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.176359864781807, 'crossentropy': 5.357749596650277}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 3.5350356101989746})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 3.3168022632598877})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.1729423999786377})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 3.432361125946045})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 3.551624298095703})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.62141752243042})
store['active_learning_steps'][26]['eval_training']['best_epoch']=3
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 6571], ['id', 64357], ['id', 36227], ['id', 24421], ['id', 12238]], 'labels': [1, 3, 1, 1, 1], 'scores': [0.5589034576172858, 1.0742593412636143, 1.5285271693591183, 1.9058387435146917, 2.2409659039118104]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 5.106401443481445})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 5.210319995880127})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 6.044543743133545})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.5502166748046875})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 6.10833740234375})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 5.534628868103027})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 6.450863838195801})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 5.85740852355957})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.9160614013671875})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 6.329537391662598})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.9718427658081055})
store['active_learning_steps'][27]['training']['best_epoch']=8
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.20205900430239704, 'crossentropy': 5.648423094652735}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 2.946193218231201})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 3.159897804260254})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 3.8153610229492188})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.3487796783447266})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 3.6403443813323975})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.522456645965576})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.3077797889709473})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 3.6769509315490723})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.5641090869903564})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 3.758272647857666})
store['active_learning_steps'][27]['eval_training']['best_epoch']=7
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 16887], ['id', 13831], ['id', 53879], ['id', 38545], ['id', 62807]], 'labels': [5, 1, 0, 1, 3], 'scores': [0.5271908396332077, 1.0012060107446916, 1.417949637532094, 1.7831496493615102, 2.093605065973465]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 5.334958076477051})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 5.688650131225586})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 6.100716590881348})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 6.53039026260376})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 8.209335327148438})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 5.427903652191162})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 6.102623462677002})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.576138973236084})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.508646011352539})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 5.6776933670043945})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 6.271981716156006})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 6.3555097579956055})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.200137138366699})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 5.881666660308838})
store['active_learning_steps'][28]['training']['best_epoch']=11
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.1777043638598648, 'crossentropy': 6.07844011697142}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 3.146430015563965})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 3.131856918334961})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 3.585892915725708})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 3.7342782020568848})
store['active_learning_steps'][28]['eval_training']['best_epoch']=1
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 71086], ['id', 25631], ['id', 65874], ['id', 21523], ['id', 70675]], 'labels': [3, 0, 5, 4, 9], 'scores': [0.6084012759684174, 1.1456012784364744, 1.6285372282864063, 2.0183686773515532, 2.3662314276694936]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 5.38907527923584})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 6.006636619567871})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 5.671358585357666})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 6.057124614715576})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 7.33964729309082})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 5.969449520111084})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.14063460356484328, 'crossentropy': 5.949362203249846}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 3.0081911087036133})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 3.2876458168029785})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 3.7655246257781982})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 3.610978603363037})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 3.5600545406341553})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 62714], ['id', 2363], ['id', 33473], ['id', 69799], ['ood', 37485]], 'labels': [6, 9, 1, 1, -1], 'scores': [0.5586923724733566, 1.0139626863319042, 1.4403662907934645, 1.7991966582390981, 2.1319170948339297]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 5.092378616333008})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 6.030397415161133})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 5.224787712097168})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 6.104584693908691})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.638216018676758})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.8267107009887695})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.576969146728516})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.1750921942224954, 'crossentropy': 6.387492437192686}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 3.9852540493011475})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 3.4019622802734375})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 3.5691142082214355})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 3.505959987640381})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 3.768721103668213})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 3.585559368133545})
store['active_learning_steps'][30]['eval_training']['best_epoch']=3
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 24801], ['id', 64404], ['id', 42409], ['id', 8132], ['id', 56230]], 'labels': [4, 7, 4, 0, 0], 'scores': [0.6451519989802652, 1.083240664666869, 1.4966226067867294, 1.8610656723375916, 2.18377107752666]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 4.611481189727783})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 4.872586727142334})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.694579124450684})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 5.548299789428711})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.395811080932617})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.625554084777832})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 6.152757167816162})
store['active_learning_steps'][31]['training']['best_epoch']=4
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.19691149354640441, 'crossentropy': 5.6963172729717275}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 2.7542967796325684})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 3.0225753784179688})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.1605727672576904})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.418290615081787})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.0348477363586426})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.3800110816955566})
store['active_learning_steps'][31]['eval_training']['best_epoch']=5
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 9029], ['id', 34768], ['ood', 40757], ['id', 7226], ['id', 12988]], 'labels': [4, 3, -1, 2, 1], 'scores': [0.5168407993454733, 0.9619678792456341, 1.3248667407280927, 1.655778247246431, 1.9398640967107816]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 4.3015899658203125})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 5.375449180603027})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 5.7534685134887695})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 5.560151100158691})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 7.0435590744018555})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.2370686531066895})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 6.114975929260254})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 6.493934154510498})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 5.964184761047363})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.1654118008604794, 'crossentropy': 5.509986506991395}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 2.944444179534912})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 3.2726712226867676})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 3.334874391555786})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 3.3820571899414062})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 3.443758487701416})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 3.415480375289917})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 3.2715935707092285})
store['active_learning_steps'][32]['eval_training']['best_epoch']=4
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 19640], ['ood', 32771], ['id', 49668], ['id', 56434], ['ood', 47900]], 'labels': [6, -1, 8, 0, -1], 'scores': [0.5686137057077837, 1.000593177410654, 1.3822824906590307, 1.7249901153429665, 2.009718963798803]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 4.877309799194336})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 4.86752986907959})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 4.976984024047852})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.593260765075684})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 6.132932186126709})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 6.390352249145508})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 6.456491470336914})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 5.8381805419921875})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 6.30989933013916})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.19441456668715426, 'crossentropy': 6.183035542793485}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 3.1180310249328613})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 4.156170845031738})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 3.7800135612487793})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.734306812286377})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 3.5698118209838867})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 3.7598609924316406})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.7513279914855957})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.700072765350342})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 29365], ['id', 37526], ['id', 34881], ['id', 51293], ['id', 13406]], 'labels': [-1, 5, 1, 5, 9], 'scores': [0.5770951547405675, 1.1039874532914264, 1.5660590901853948, 1.97851722197795, 2.3344481227233285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 5.918891906738281})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.162007808685303})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.052330017089844})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 4.806272506713867})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 5.29481840133667})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 5.531654357910156})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 6.290753364562988})
store['active_learning_steps'][34]['training']['best_epoch']=4
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.20182851874615856, 'crossentropy': 4.782299189459128}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 2.7770168781280518})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 3.2471771240234375})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.1294445991516113})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 3.35383677482605})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 3.3328945636749268})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.100933074951172})
store['active_learning_steps'][34]['eval_training']['best_epoch']=6
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 13223], ['ood', 40154], ['id', 17534], ['id', 50344], ['id', 20625]], 'labels': [-1, -1, 1, 5, 4], 'scores': [0.5498758164635529, 0.9502312552361694, 1.3434244475583452, 1.685022028348861, 1.9750049724828767]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 4.666077613830566})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.4779534339904785})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 6.464695453643799})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 6.3514251708984375})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.0106377601623535})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 6.024200439453125})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.306258201599121})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.827029228210449})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 5.762097358703613})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.740154266357422})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 6.583943843841553})
store['active_learning_steps'][35]['training']['best_epoch']=8
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.20989551321450522, 'crossentropy': 6.194347941956054}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 2.7436208724975586})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 3.5281178951263428})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.222623348236084})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 3.245438575744629})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 3.41571044921875})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.3981330394744873})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 3.3335158824920654})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 3.2951557636260986})
store['active_learning_steps'][35]['eval_training']['best_epoch']=5
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 11983], ['id', 16433], ['id', 55739], ['id', 38410], ['ood', 43368]], 'labels': [2, 1, 3, 1, -1], 'scores': [0.5236042147517058, 1.0117920308601631, 1.4647949440120538, 1.8662151971637737, 2.2396821787248946]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 5.071690559387207})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 4.495068550109863})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.552847862243652})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 6.0642924308776855})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 4.918448448181152})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 5.008825302124023})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 5.425332069396973})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.563449859619141})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.789257049560547})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.2253764597418562, 'crossentropy': 5.097764290104487}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 2.6016297340393066})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 2.9198596477508545})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.057784080505371})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.0325350761413574})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 3.088243007659912})
store['active_learning_steps'][36]['eval_training']['best_epoch']=2
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 14277], ['id', 36916], ['ood', 15768], ['id', 35389], ['id', 18499]], 'labels': [-1, 3, -1, 4, 5], 'scores': [0.5239036170804305, 0.9698307606177088, 1.3694362210937974, 1.7407375963989864, 2.0748611038480433]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 4.706891059875488})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 5.183184623718262})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 6.374290466308594})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 6.161549091339111})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.670866012573242})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 6.04121208190918})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.574984550476074})
store['active_learning_steps'][37]['training']['best_epoch']=4
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.22722034419176398, 'crossentropy': 6.023625969960049}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 3.047227621078491})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 3.194340705871582})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.3086352348327637})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 3.6508352756500244})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 3.4643301963806152})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 3.7730631828308105})
store['active_learning_steps'][37]['eval_training']['best_epoch']=5
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 61203], ['id', 19186], ['id', 23617], ['id', 24546], ['id', 43868]], 'labels': [0, 2, 3, 4, 5], 'scores': [0.49893787576910476, 0.9207269657664705, 1.310182150565288, 1.669653096576111, 1.9633795397209974]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 4.57758903503418})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.432940483093262})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.598201751708984})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 5.270879745483398})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 6.125234603881836})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.114936351776123})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 5.235208511352539})
store['active_learning_steps'][38]['training']['best_epoch']=4
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.20889674247080517, 'crossentropy': 5.317258566379841}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 2.6178250312805176})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.0327563285827637})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 3.261735200881958})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 2.9710028171539307})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 2.9589476585388184})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 3.110118865966797})
store['active_learning_steps'][38]['eval_training']['best_epoch']=5
store['active_learning_steps'][38]['acquisition']={'indices': [['ood', 16567], ['id', 69687], ['id', 47898], ['ood', 24504], ['id', 18077]], 'labels': [-1, 1, 6, -1, 1], 'scores': [0.5377643094105568, 1.049852401105812, 1.475794373838528, 1.8582448963043052, 2.2152679380575466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.556879043579102})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 5.474100589752197})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 5.3346662521362305})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 6.5806169509887695})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.439243793487549})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.6823344230651855})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 5.710362911224365})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 5.645017623901367})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.771635055541992})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.871675968170166})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.975399017333984})
store['active_learning_steps'][39]['training']['best_epoch']=8
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.2294099569760295, 'crossentropy': 5.668342688806085}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 2.6833720207214355})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 2.721165657043457})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 3.0430259704589844})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.117391347885132})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 2.924276351928711})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 3.186269998550415})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 3.133737087249756})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 3.003389358520508})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 2.9176225662231445})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 3.0585379600524902})
store['active_learning_steps'][39]['eval_training']['best_epoch']=8
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 71544], ['id', 48891], ['ood', 17982], ['ood', 14277], ['id', 55834]], 'labels': [1, 5, -1, -1, 4], 'scores': [0.5067461763213783, 0.9827920711852496, 1.4482268214859628, 1.8542044782168245, 2.1836436316938426]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 4.721760272979736})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 6.283959865570068})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 5.19125509262085})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 6.3579301834106445})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.716236114501953})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.4982099533081055})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.310749053955078})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 5.395648956298828})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.392366409301758})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.602485656738281})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.81075382232666})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 5.944825172424316})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 6.171836853027344})
store['active_learning_steps'][40]['training']['best_epoch']=10
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.2132759680393362, 'crossentropy': 5.858774777197295}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 2.7659380435943604})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 2.7927777767181396})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 3.2438597679138184})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 2.9998087882995605})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.2175588607788086})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.270155429840088})
store['active_learning_steps'][40]['eval_training']['best_epoch']=3
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 72215], ['id', 45277], ['id', 8637], ['id', 57122], ['id', 40357]], 'labels': [3, 1, 3, 1, 1], 'scores': [0.6666168457353114, 1.256916465161032, 1.7947385110536942, 2.203966109234206, 2.58345072672857]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 4.649345397949219})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 4.479374885559082})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 4.512165069580078})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 5.644262790679932})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 6.281903266906738})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 4.649629592895508})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.912264823913574})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 5.106845855712891})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 5.4482221603393555})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.468027114868164})
store['active_learning_steps'][41]['training']['best_epoch']=7
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.2476183159188691, 'crossentropy': 4.920404454133374}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 2.4817237854003906})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 2.7681868076324463})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 2.888209819793701})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 3.3147075176239014})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 3.090230941772461})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 3.006812810897827})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 3.1261560916900635})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 2.8396337032318115})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.9004011154174805})
store['active_learning_steps'][41]['eval_training']['best_epoch']=7
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 64899], ['id', 44029], ['ood', 40427], ['id', 26768], ['id', 55089]], 'labels': [1, 1, -1, 1, 2], 'scores': [0.5548676215171602, 1.0446591572641917, 1.481033672557679, 1.855867383142665, 2.1906402156268565]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 4.477467060089111})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 4.908407211303711})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 5.075841903686523})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.307760238647461})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 6.219570159912109})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 5.301178455352783})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.527078628540039})
store['active_learning_steps'][42]['training']['best_epoch']=4
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.22287953288260604, 'crossentropy': 5.399675159419177}
