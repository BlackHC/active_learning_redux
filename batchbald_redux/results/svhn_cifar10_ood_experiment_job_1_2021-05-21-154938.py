store = {}
store['timestamp']=1621608578
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=1']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=1
store['worker_id']=1
store['num_workers']=24
store['config']={'seed': 1235, 'uniform_ood': True, 'id_dataset_name': 'SVHN', 'ood_dataset_name': 'CIFAR-10', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node | one_hot_targets{'num_classes': 10}) + ('CIFAR-10 (Train, seed=0, 50000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'SVHN (Test)'"}
store['initial_training_set_indices']=[38482, 18819, 58066, 14663, 39799, 53509, 12901, 26100, 61523, 67745, 57808, 69963, 69909, 45371, 37280, 48685, 26877, 52249, 66762, 14073]
store['evaluation_set_indices']=[9356, 52217, 13204, 15153, 14643, 13323, 68768, 23207, 25999, 62719, 62312, 67969, 24256, 39281, 37692, 459, 50826, 51277, 57053, 2584, 51764, 14758, 22887, 43685, 53675, 71612, 55166, 16551, 62820, 4535, 12102, 2976, 62920, 41178, 65425, 24347, 41886, 15904, 4242, 38591, 69801, 8821, 58682, 26825, 58891, 26239, 12097, 25295, 62111, 31755, 35768, 26368, 42500, 34271, 27190, 19058, 51104, 6911, 30075, 67867, 33661, 68699, 33542, 20892, 66108, 65071, 38221, 28545, 4922, 712, 69652, 9859, 30961, 51019, 29978, 24859, 3266, 17700, 8635, 6353, 5221, 42961, 38139, 71930, 52654, 10503, 21854, 36516, 30504, 22436, 45904, 30936, 48527, 39826, 3646, 58802, 10195, 14513, 6465, 6942, 57592, 56379, 26009, 61985, 2559, 12661, 12013, 46596, 22602, 4480, 17051, 33111, 8443, 71520, 63570, 69611, 25877, 35431, 68255, 42429, 25233, 38864, 11350, 35991, 55649, 57177, 7278, 4769, 20349, 2614, 44954, 59941, 37367, 65209, 17027, 19532, 53043, 65575, 20118, 14547, 5357, 36375, 13466, 33485, 25546, 9095, 13754, 12356, 31308, 21474, 7790, 60533, 72158, 29121, 42063, 39774, 8251, 53403, 49392, 11194, 9155, 41513, 66798, 65593, 59814, 15932, 37576, 11589, 53361, 63564, 23612, 39344, 15174, 35048, 32969, 69692, 25106, 48838, 47004, 4184, 853, 45864, 56849, 67982, 15528, 22376, 35245, 45656, 59597, 66590, 54076, 16022, 11813, 65618, 9234, 51953, 9766, 41955, 44395, 39226, 40025, 41050, 18973, 65107, 47464, 33366, 60380, 2486, 33728, 17384, 20252, 502, 5733, 4780, 8085, 20338, 65499, 16532, 46969, 7202, 65103, 41400, 26582, 27643, 8071, 55598, 37396, 44808, 26291, 28417, 36402, 28726, 22517, 69815, 36383, 23607, 23033, 27971, 2408, 2278, 41478, 44310, 22574, 36584, 20402, 39412, 4629, 15386, 62095, 71458, 33017, 16110, 17249, 12926, 3490, 47863, 57175, 70171, 64841, 69552, 16738, 53687, 49215, 68777, 42356, 44008, 58581, 4015, 25552, 6585, 63976, 21856, 22022, 55859, 646, 40666, 20229, 54017, 19316, 47715, 63714, 56139, 20095, 56198, 49498, 71125, 37745, 28370, 447, 16265, 16217, 31553, 42330, 39800, 4708, 41610, 26365, 29555, 39014, 12058, 57716, 30264, 19834, 44802, 28557, 41674, 58223, 69197, 20831, 68939, 58071, 61613, 908, 66783, 49048, 8901, 8366, 43877, 27035, 5594, 16712, 65988, 44267, 68598, 18916, 55473, 13995, 8035, 35402, 49125, 1977, 30455, 18722, 28193, 13172, 50182, 7501, 13256, 30190, 3792, 2123, 1945, 578, 46527, 39552, 67117, 42833, 5445, 46094, 33919, 17401, 32440, 65698, 21803, 1135, 10541, 46967, 10104, 10938, 63683, 40034, 50634, 69388, 36184, 19463, 34004, 28951, 14855, 64729, 14756, 22150, 21459, 17111, 16346, 43426, 67098, 33904, 31401, 7659, 48749, 63155, 2295, 10885, 35729, 19327, 37233, 62037, 43673, 32598, 17664, 54682, 26311, 47139, 39399, 39716, 12071, 64933, 24857, 5906, 55259, 19820, 50768, 64273, 5453, 68989, 5148, 32502, 26332, 21086, 2537, 56917, 2572, 33746, 12667, 67185, 22625, 22488, 46950, 11323, 7732, 4099, 66265, 45874, 44873, 50645, 54736, 27587, 37633, 20063, 1608, 10391, 69839, 40026, 23753, 16692, 70616, 33037, 36107, 60644, 10024, 70725, 42517, 59766, 63776, 5240, 4298, 48682, 2647, 31850, 35911, 50647, 29464, 44634, 59672, 65002, 63792, 17766, 62198, 24020, 42922, 58463, 65717, 23905, 3709, 24462, 16997, 57309, 37223, 66400, 62492, 47056, 40814, 21985, 72066, 40550, 18131, 28968, 4841, 27091, 18456, 30336, 57899, 48912, 37103, 49194, 47247, 54365, 28077, 55585, 49073, 62608, 17950, 33176, 69058, 59000, 33429, 19825, 69851, 24553, 14100, 52015, 34854, 8384, 22221, 35886, 67782, 48319, 56320, 19629, 42327, 58156, 24662, 57555, 36936, 69589, 3895, 49861, 58546, 37408, 20865, 9547, 2308, 60654, 64334, 29058, 57610, 3713, 22067, 67083, 55907, 60300, 36206, 2137, 31864, 59454, 62125, 3472, 61684, 53364, 19002, 5961, 5119, 54575, 21647, 10117, 2063, 45076, 7655, 17649, 16183, 34516, 22281, 64009, 1482, 45897, 16054, 26453, 54529, 22123, 51161, 56473, 51275, 58255, 30056, 58472, 25031, 45022, 19772, 18227, 61247, 64229, 33494, 42705, 32892, 7643, 6554, 38114, 71630, 50256, 48460, 12647, 41199, 26273, 45698, 52378, 67419, 39957, 34025, 21810, 36037, 46937, 32002, 68859, 22312, 38228, 49463, 32134, 43593, 12976, 48518, 29540, 49660, 65445, 20048, 50377, 55745, 48666, 34187, 14797, 1090, 9866, 49432, 16623, 66209, 29260, 52431, 20003, 17847, 51378, 16023, 68062, 44305, 16631, 27731, 24784, 39156, 11115, 28872, 68835, 23709, 69182, 55249, 51867, 58062, 15447, 54267, 22358, 11689, 32422, 17668, 70285, 14630, 66794, 3930, 48981, 53416, 52758, 259, 46199, 29534, 64541, 17082, 44746, 25437, 49288, 43065, 30764, 38017, 51276, 30890, 65349, 52566, 50133, 43793, 30313, 16596, 24263, 5825, 59782, 46247, 12714, 31550, 66659, 56183, 15363, 28327, 17799, 7985, 57408, 63114, 5656, 45109, 8170, 71088, 44865, 5179, 33238, 67850, 59037, 70356, 57561, 5224, 54748, 48857, 57920, 64313, 61094, 24227, 27540, 48418, 49627, 5977, 47424, 49350, 2294, 51114, 31731, 68660, 48657, 47982, 5572, 67954, 72131, 38419, 5584, 43252, 9618, 23545, 33898, 68204, 52186, 24178, 19915, 6776, 31485, 32593, 19584, 19419, 27692, 8249, 34767, 43187, 21199, 9445, 58948, 11805, 31566, 23275, 48477, 70581, 468, 60975, 35599, 51011, 23731, 62929, 52127, 43105, 47132, 37098, 36682, 66718, 11836, 18937, 8353, 39475, 25066, 3810, 42035, 61047, 31409, 53353, 43799, 66218, 33732, 13353, 60944, 44114, 63746, 58818, 58308, 71199, 34872, 33651, 31320, 10155, 22562, 26256, 588, 650, 11367, 32284, 59309, 47102, 12778, 23277, 11903, 57880, 27145, 31297, 29703, 71945, 51586, 46004, 3819, 11022, 9807, 13278, 4765, 14868, 45323, 64881, 49532, 21786, 27694, 4261, 4225, 19091, 72034, 55698, 45428, 10685, 53402, 56253, 46547, 71757, 51782, 51907, 35547, 4933, 17159, 55552, 42654, 15891, 18290, 60649, 12688, 14180, 27824, 31768, 58640, 10644, 65690, 49127, 6096, 11685, 19904, 65825, 9756, 69122, 22560, 15354, 7212, 69075, 32862, 40238, 51753, 2289, 15439, 32940, 48616, 33630, 61582, 59003, 31277, 69455, 15225, 6524, 12255, 35631, 19799, 939, 19052, 51599, 33349, 15648, 53478, 48461, 57688, 16560, 29049, 42225, 52412, 16140, 40390, 32570, 24745, 64558, 36783, 6915, 47728, 965, 11449, 5116, 5323, 60583, 65003, 49946, 14668, 41788, 22684, 41248, 57017, 35386, 56663, 11333, 6235, 14545, 57849, 48023, 18451, 52781, 55872, 12166, 65210, 42135, 45704, 22159, 13433, 43848, 57952, 67211, 13469, 11047, 5020, 42097, 20945, 63525, 38029, 4448, 12645, 67581, 29111, 8657, 67780, 64513, 18251, 17888, 32040, 59868, 23404, 9423, 1799, 42360, 38722, 2521, 70901, 20614, 58004, 61052, 52510, 1767, 18118, 63984, 8997, 7359, 57822, 51575, 1154, 20732, 22093, 36091, 65675, 30482, 18517, 58191, 41454, 56022, 42315, 16818, 29430, 51625, 52715, 19267, 60460, 50887, 71829, 53823, 20360, 60961, 45356, 39961, 39474, 66779, 32959, 45573, 36984, 2876, 30770, 34908, 12101, 10839, 42028, 42187, 29776, 30785, 65134, 31096, 13346, 32978, 29254, 50953, 33172, 13798, 22658, 32286, 20308, 15277, 9517, 18525, 14838, 14280, 35505, 71679, 35497, 51264, 15149, 15077, 19660, 2980, 11973, 61547, 51033, 60741, 11385, 19913, 68557, 23524, 68591, 9114]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.0966796875, 'crossentropy': 8.080072402954102})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 8.80338191986084})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 8.938344955444336})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 8.564973831176758})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 9.140113830566406})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 9.347457885742188})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 9.195541381835938})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 9.32646369934082})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 10.281549453735352})
store['active_learning_steps'][0]['training']['best_epoch']=6
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.10302704363859864, 'crossentropy': 9.499614056737862}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.09765625, 'crossentropy': 6.748357772827148})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1123046875, 'crossentropy': 5.555789947509766})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 5.894532203674316})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1083984375, 'crossentropy': 5.86686372756958})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 5.3677978515625})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 5.6485466957092285})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 5.545442581176758})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 5.744606971740723})
store['active_learning_steps'][0]['eval_training']['best_epoch']=8
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 45038], ['id', 38481], ['id', 21133], ['ood', 13401], ['ood', 13223]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6648110641274025, 1.169440032247923, 1.6136159322333081, 1.9884178614262724, 2.31953071536413]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 7.896793365478516})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1279296875, 'crossentropy': 7.308200836181641})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 7.462985515594482})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 8.194028854370117})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.12361708666256914, 'crossentropy': 7.9404296875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1279296875, 'crossentropy': 4.4249348640441895})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1171875, 'crossentropy': 4.935388565063477})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1279296875, 'crossentropy': 4.952259063720703})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 1227], ['id', 4227], ['id', 11098], ['id', 34634], ['id', 53027]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5983892527497718, 1.1101266812979076, 1.5625287848425549, 1.9614426290633302, 2.286040220919544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 9.302988052368164})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 8.062210083007812})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1123046875, 'crossentropy': 7.320322036743164})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 6.918469429016113})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 8.14042854309082})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.13733097725875845, 'crossentropy': 8.222281710971112}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 4.0623579025268555})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 4.226245880126953})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 4.294634819030762})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 4.479618072509766})
store['active_learning_steps'][2]['eval_training']['best_epoch']=4
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 64690], ['id', 7376], ['id', 15902], ['id', 63250], ['id', 52000]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.9086612617985306, 1.728795414394386, 2.351328796624735, 2.843809019181144, 3.1736670713184143]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 9.625041007995605})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 6.590256690979004})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 7.4626145362854})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 7.832497596740723})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 7.8259806632995605})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 7.723687171936035})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 8.115739822387695})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 7.944884777069092})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 8.116277694702148})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 8.395126342773438})
store['active_learning_steps'][3]['training']['best_epoch']=7
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.10967271051014137, 'crossentropy': 8.11728053453442}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.0986328125, 'crossentropy': 4.68573522567749})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 4.3635358810424805})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 4.4856462478637695})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 4.812920570373535})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 4.200499534606934})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 4.963446140289307})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 4.829667091369629})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1279296875, 'crossentropy': 4.336945533752441})
store['active_learning_steps'][3]['eval_training']['best_epoch']=5
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 46147], ['id', 61322], ['id', 29312], ['id', 2589], ['ood', 37379]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6394904438412468, 1.1960642533982435, 1.668165736080946, 2.0688549291113194, 2.4124134121590686]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 17.881336212158203})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 8.051970481872559})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.0908203125, 'crossentropy': 8.439998626708984})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 9.20877456665039})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 8.362794876098633})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 11.054357528686523})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 13.538005828857422})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 11.402616500854492})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 12.243072509765625})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 12.405174255371094})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 12.418163299560547})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 12.357114791870117})
store['active_learning_steps'][4]['training']['best_epoch']=9
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.12307928703134603, 'crossentropy': 11.65232814420713}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 4.32719612121582})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 4.391777992248535})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 5.460738182067871})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 5.629907608032227})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 5.864833831787109})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 5.91694450378418})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 6.25996208190918})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 5.029266357421875})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 5.773858070373535})
store['active_learning_steps'][4]['eval_training']['best_epoch']=6
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 37424], ['id', 30777], ['id', 50539], ['id', 26452], ['id', 1228]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.666994241087602, 1.2147352192350522, 1.6978025516249802, 2.1192859363333296, 2.47640066425305]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 5.2032246589660645})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 6.369229316711426})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 6.396857261657715})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 6.763533592224121})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 6.565528869628906})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 7.011697769165039})
store['active_learning_steps'][5]['training']['best_epoch']=3
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.12899508297480025, 'crossentropy': 6.248310372810387}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 3.7906360626220703})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 3.819303512573242})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 4.114139080047607})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 4.038748264312744})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 4.03884744644165})
store['active_learning_steps'][5]['eval_training']['best_epoch']=4
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 40844], ['id', 61024], ['id', 14230], ['id', 11528], ['id', 40362]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5099376879837525, 0.9959926596605961, 1.3905134057479218, 1.7602474660940954, 2.0542673975140255]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 5.222904205322266})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 5.772219657897949})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 6.723094940185547})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 7.294644355773926})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 11.002138137817383})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 9.265116691589355})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 8.625967979431152})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 10.517566680908203})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 12.140729904174805})
store['active_learning_steps'][6]['training']['best_epoch']=6
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.13952059004302397, 'crossentropy': 9.414989844230178}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 4.093317985534668})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 4.330901145935059})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 4.198784828186035})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 4.396646499633789})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 5.7566609382629395})
store['active_learning_steps'][6]['eval_training']['best_epoch']=2
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 6474], ['id', 65808], ['id', 39405], ['id', 49273], ['id', 25758]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.588946649597454, 1.1053937170217618, 1.4918171994629281, 1.838005430542779, 2.151318397230866]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1044921875, 'crossentropy': 6.754550457000732})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 6.20300817489624})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 5.561028480529785})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 7.497061729431152})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 7.554131984710693})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.13748463429625077, 'crossentropy': 5.847816509488322}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 3.8783135414123535})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 3.704472064971924})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1279296875, 'crossentropy': 4.082169055938721})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 4.109057426452637})
store['active_learning_steps'][7]['eval_training']['best_epoch']=4
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 63471], ['id', 29424], ['id', 63697], ['id', 37829], ['id', 8482]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.500761296572455, 0.9593685210825902, 1.36205677716775, 1.701066025923744, 1.9981400349444238]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 6.935715675354004})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 6.283840179443359})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 5.078721523284912})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 5.800202369689941})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 7.161260604858398})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 7.121991157531738})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 6.655961036682129})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.14585894283958206, 'crossentropy': 5.06170770590043}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 3.2320685386657715})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 3.6594972610473633})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 3.713223934173584})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 3.672116756439209})
store['active_learning_steps'][8]['eval_training']['best_epoch']=1
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 44952], ['id', 39363], ['id', 10111], ['id', 64082], ['id', 44499]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6473254630228084, 1.1976424015755693, 1.6938507970209242, 2.103769036752511, 2.434673952871692]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 5.377894878387451})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 5.119070053100586})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 6.573764324188232})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 6.053027153015137})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 6.7139105796813965})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.1696757836508912, 'crossentropy': 4.825672189516749}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 4.2314605712890625})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 3.932054042816162})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 3.606619358062744})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 3.803325891494751})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 60018], ['id', 8150], ['id', 70107], ['id', 42776], ['id', 29336]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5359172073272602, 1.0265458175129978, 1.430930190817762, 1.7871851814099218, 2.097225984632555]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 7.422574043273926})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 7.322248458862305})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 5.146660327911377})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 5.457119941711426})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.18020129071911495, 'crossentropy': 6.814596578249846}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 4.194787979125977})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 4.232935905456543})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 4.648958206176758})
store['active_learning_steps'][10]['eval_training']['best_epoch']=1
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 56434], ['id', 41974], ['id', 58287], ['id', 14199], ['id', 26196]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.839769559905301, 1.4353021911348314, 1.9587386069569486, 2.404898590729621, 2.7082438877929658]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1298828125, 'crossentropy': 5.786079406738281})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 5.516016960144043})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1279296875, 'crossentropy': 6.963951587677002})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 6.979963302612305})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 6.741056442260742})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.1609557467732022, 'crossentropy': 5.390216848494161}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 3.0882935523986816})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 3.6532042026519775})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 3.777489423751831})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 3.4024405479431152})
store['active_learning_steps'][11]['eval_training']['best_epoch']=2
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 68063], ['id', 31130], ['id', 31414], ['id', 57007], ['id', 60562]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.723709218716396, 1.2380444509203405, 1.6944341448917362, 2.069982508664543, 2.413660141605124]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 4.873829364776611})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 6.86605978012085})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 5.027239799499512})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 6.351238250732422})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.13275968039336203, 'crossentropy': 4.659145774911647}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 3.459980010986328})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 3.409571886062622})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 3.338855743408203})
store['active_learning_steps'][12]['eval_training']['best_epoch']=3
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 68765], ['id', 10651], ['id', 8599], ['id', 12916], ['id', 16086]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4328761405364544, 0.8462035186396559, 1.1584021462903693, 1.4406142980659982, 1.6952436371047348]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 4.566532135009766})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 7.019317626953125})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 8.28521728515625})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.401906967163086})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 5.547840118408203})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 7.354424476623535})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 7.872431755065918})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.16771665642286418, 'crossentropy': 5.041509608366626}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 3.2506914138793945})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 3.6170942783355713})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 3.606472969055176})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 3.82210111618042})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 3.4398021697998047})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 3.7111973762512207})
store['active_learning_steps'][13]['eval_training']['best_epoch']=6
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 71407], ['id', 48990], ['id', 3237], ['id', 26491], ['id', 57234]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5754436228115043, 0.9866626807832919, 1.3709512534961346, 1.7254693217610662, 2.03483736169915]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 6.507228374481201})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 5.646610260009766})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 6.247769355773926})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 7.100094795227051})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.16502765826674862, 'crossentropy': 6.528996763598648}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 4.150778770446777})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 4.053952217102051})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 4.616591453552246})
store['active_learning_steps'][14]['eval_training']['best_epoch']=1
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 24441], ['id', 53645], ['id', 55296], ['id', 67801], ['id', 60977]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5322786511883035, 1.0162571574729053, 1.4126513408818955, 1.7817294879876715, 2.074118543151367]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 7.172184944152832})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 5.951883316040039})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 4.949123382568359})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 7.561254501342773})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 6.721493244171143})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.14674247080516287, 'crossentropy': 6.023415891979103}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 3.815214157104492})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 3.9712836742401123})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 4.146549701690674})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 4.273891448974609})
store['active_learning_steps'][15]['eval_training']['best_epoch']=2
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 70220], ['id', 23975], ['id', 13749], ['ood', 46985], ['id', 62899]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5868129047930891, 1.0452737473608207, 1.4750198987647551, 1.862405369105283, 2.1925600401165033]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 6.399250507354736})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 7.428234577178955})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 5.820641994476318})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.798304557800293})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 5.191373825073242})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 6.296353816986084})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 6.245948314666748})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.16180086047940995, 'crossentropy': 5.444712877420098}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 3.8573336601257324})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 3.6051464080810547})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 3.6354756355285645})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 3.837477684020996})
store['active_learning_steps'][16]['eval_training']['best_epoch']=1
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 29157], ['id', 4602], ['id', 17998], ['id', 10100], ['id', 9380]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5362398644744657, 1.043729473244316, 1.514882060939287, 1.895317711656337, 2.2238488855734913]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 5.802733421325684})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 5.399932861328125})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 6.861703872680664})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 5.52937650680542})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 7.640802383422852})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 4.472437858581543})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 5.438277244567871})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.4150800704956055})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.9359846115112305})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.784128189086914})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.1924938537185003, 'crossentropy': 5.337672143899816}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 3.0920629501342773})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 3.46970534324646})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.4969329833984375})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 3.608076572418213})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.745779037475586})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.5222976207733154})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 3.745913028717041})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 3.6434988975524902})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 3.8521366119384766})
store['active_learning_steps'][17]['eval_training']['best_epoch']=9
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 9336], ['id', 32149], ['id', 44387], ['id', 65277], ['id', 23594]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5772583219544402, 1.035203415638624, 1.45308370867568, 1.8433262570973699, 2.164505179279172]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 6.061723232269287})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 5.202078819274902})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 5.267309188842773})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 6.717369079589844})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 5.292428970336914})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 5.467105388641357})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 7.271420478820801})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 6.540515899658203})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 6.268013000488281})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 6.866548538208008})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 6.531006813049316})
store['active_learning_steps'][18]['training']['best_epoch']=8
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.16087891825445605, 'crossentropy': 5.743067426628764}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 3.079561710357666})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 4.05711555480957})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 3.831084728240967})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 4.1242523193359375})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 3.528313159942627})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 3.916163444519043})
store['active_learning_steps'][18]['eval_training']['best_epoch']=3
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 55425], ['id', 4429], ['id', 62715], ['id', 64121], ['id', 18368]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6934894001190604, 1.2531113048291278, 1.6962859681134135, 2.0796220831891943, 2.3986749250148156]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 5.419579029083252})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 6.7575883865356445})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.414504051208496})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 5.359802722930908})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 5.4511189460754395})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 5.806002616882324})
store['active_learning_steps'][19]['training']['best_epoch']=3
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.17059772587584512, 'crossentropy': 5.169223815880454}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 3.3618674278259277})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 3.052031993865967})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 3.8238799571990967})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 3.414875030517578})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 3.465128183364868})
store['active_learning_steps'][19]['eval_training']['best_epoch']=5
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 17970], ['id', 58522], ['id', 45272], ['id', 33071], ['id', 18069]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.459760630605066, 0.8517350810710271, 1.1888931075207494, 1.5108821558466707, 1.7678960262422119]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 5.437197685241699})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 9.370403289794922})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 5.912033557891846})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 6.621070384979248})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.269157409667969})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 6.266628265380859})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.7645416259765625})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.577764511108398})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 6.095810890197754})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 6.124687194824219})
store['active_learning_steps'][20]['training']['best_epoch']=7
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.15569299323909036, 'crossentropy': 5.42675121004917}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 3.4818854331970215})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 3.2449378967285156})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 3.536743402481079})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 3.7418291568756104})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 3.8337900638580322})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 3.713501453399658})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 3.4043259620666504})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 3.6763951778411865})
store['active_learning_steps'][20]['eval_training']['best_epoch']=5
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 66932], ['id', 27676], ['id', 16064], ['id', 60192], ['id', 35836]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4898223708317184, 0.9320013644743173, 1.333527067252287, 1.7050139525431893, 2.0239021099923407]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 4.912356376647949})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 5.349703788757324})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 5.45497465133667})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 6.047825813293457})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 7.106158256530762})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 7.8356032371521})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 7.426825046539307})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 7.162932872772217})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.19479870928088505, 'crossentropy': 6.590621038529502}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 3.518843650817871})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 3.5174853801727295})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.188436985015869})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.5707590579986572})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 3.917590618133545})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.5317463874816895})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 3.7781481742858887})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 27684], ['id', 72049], ['id', 69647], ['id', 36372], ['id', 39317]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6918299883060994, 1.3048513792819088, 1.8369819944638475, 2.293237159814307, 2.636271188835526]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 4.606844902038574})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 5.2857489585876465})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 4.708312034606934})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 4.208511829376221})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 3.9381468296051025})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 4.887082099914551})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 4.993389129638672})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 4.936365127563477})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.1294355392456055})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 5.198882102966309})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.18016287645974186, 'crossentropy': 4.414054697103565}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 3.093264102935791})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 3.407498598098755})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 3.339548110961914})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.2463431358337402})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 3.2326765060424805})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 3.3347582817077637})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.237668991088867})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.3685150146484375})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 3.1657636165618896})
store['active_learning_steps'][22]['eval_training']['best_epoch']=8
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 33006], ['id', 66206], ['id', 57316], ['id', 40865], ['id', 842]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.571045523167315, 1.0393720025988875, 1.4816311969624048, 1.833925637067444, 2.125440728467405]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 5.4192304611206055})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 6.47032356262207})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 4.958279609680176})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 5.397522449493408})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 5.42923641204834})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 7.180704593658447})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 5.282687187194824})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 4.538976669311523})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.16652581438229871, 'crossentropy': 5.477085294061156}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 2.965709924697876})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 3.069258689880371})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.4085187911987305})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 3.43072509765625})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.3526878356933594})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 3.4761903285980225})
store['active_learning_steps'][23]['eval_training']['best_epoch']=3
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 56194], ['id', 154], ['id', 4796], ['id', 41884], ['id', 6792]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5307447577913671, 0.9588539369511517, 1.3267097319990144, 1.670938869771529, 1.9795900798121275]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 5.749692916870117})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 5.257870674133301})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 6.060565948486328})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 5.025592803955078})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.150321006774902})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 4.721261978149414})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.498455047607422})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 4.814242362976074})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.20536263060848187, 'crossentropy': 4.55229711268823}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 2.821300983428955})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 2.7059264183044434})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 2.9317522048950195})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 3.031778573989868})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 3.1449224948883057})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.159249782562256})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 3.0913119316101074})
store['active_learning_steps'][24]['eval_training']['best_epoch']=7
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 44526], ['id', 62970], ['id', 16200], ['id', 3833], ['id', 24141]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.607228158655622, 1.135573017044232, 1.5572896449983553, 1.9094198122683057, 2.2003564268138938]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 5.823850631713867})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 6.203112602233887})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 4.467721939086914})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 6.2928032875061035})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 4.989618301391602})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 4.277268409729004})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 4.797306060791016})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.780792713165283})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 4.842720031738281})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.2137956619262695})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.495521068572998})
store['active_learning_steps'][25]['training']['best_epoch']=8
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.20782114320835895, 'crossentropy': 4.947305239704979}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 3.0678603649139404})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.4563205242156982})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 3.321394443511963})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.3011984825134277})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 3.3104047775268555})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 3.309105634689331})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.384012222290039})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.2616608142852783})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 52964], ['id', 47098], ['id', 66214], ['id', 43809], ['id', 46273]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5448064496463254, 0.9897804857362007, 1.3890312420900637, 1.7459873184728942, 2.071444033462793]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 4.298810958862305})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 4.093557357788086})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 4.659649848937988})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 5.846503257751465})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 5.118385314941406})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 5.387269973754883})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.17189884185791})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 4.673559188842773})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 4.625223636627197})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 4.945757865905762})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 5.0242509841918945})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 5.099157333374023})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.1729936599731445})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 5.198637008666992})
store['active_learning_steps'][26]['training']['best_epoch']=11
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.22395513214505225, 'crossentropy': 4.964456906403657}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 2.7167673110961914})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 3.032351016998291})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 2.9230847358703613})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 2.9209651947021484})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 3.0905277729034424})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.1585230827331543})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 2.8840582370758057})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 2.7867751121520996})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 2.943363904953003})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 2.891396999359131})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.881681442260742})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.0520071983337402})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 2.9368414878845215})
store['active_learning_steps'][26]['eval_training']['best_epoch']=10
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 39043], ['id', 70735], ['id', 24929], ['id', 34587], ['id', 57965]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5653403486437727, 1.0509925123019022, 1.4276389061665706, 1.7828633740708257, 2.0732113388641515]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 4.807962894439697})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 4.570176124572754})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 4.974033832550049})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 6.2375006675720215})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 4.841581344604492})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.078941345214844})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.964705944061279})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 5.83425235748291})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.18580977258758452, 'crossentropy': 4.564481635583128}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 2.7185020446777344})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 2.8219399452209473})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 3.2292122840881348})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 3.3325796127319336})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 3.2641658782958984})
store['active_learning_steps'][27]['eval_training']['best_epoch']=2
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 58772], ['id', 71350], ['id', 32318], ['id', 54463], ['id', 44466]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.470028426371782, 0.8900497118177761, 1.2865755136093475, 1.6342710313714255, 1.9379536103771304]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 4.7795891761779785})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.4774065017700195})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 4.619978427886963})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 4.936184883117676})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 4.355125904083252})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 5.795395851135254})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.785556793212891})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 5.086390495300293})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 4.839451789855957})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 4.763234615325928})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 4.954554557800293})
store['active_learning_steps'][28]['training']['best_epoch']=8
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.20059926244622003, 'crossentropy': 5.28555359749539}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 2.957620143890381})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.071560859680176})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.053215503692627})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.10638689994812})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 2.9745495319366455})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.0088233947753906})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 3.228846549987793})
store['active_learning_steps'][28]['eval_training']['best_epoch']=4
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 12739], ['id', 29149], ['id', 1789], ['id', 65219], ['id', 7823]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5049653904445064, 0.9482123902121806, 1.3541086701190697, 1.7170379280227976, 2.0428163481608532]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 4.122173309326172})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 6.164698600769043})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 4.506622791290283})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.9607696533203125})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 5.088692665100098})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.081534385681152})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.35703182220459})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 6.422205924987793})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.17055931161647203, 'crossentropy': 4.8020906360441}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 3.0662600994110107})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 3.0714468955993652})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 2.9250683784484863})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.1306076049804688})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 3.0057873725891113})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.2076668739318848})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 3.078369140625})
store['active_learning_steps'][29]['eval_training']['best_epoch']=6
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 68567], ['id', 63603], ['id', 21874], ['id', 58872], ['id', 46189]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5442083951327414, 1.0654752682389534, 1.5116896940957596, 1.915655254425023, 2.2631721061064374]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 6.299219608306885})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 4.313173294067383})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 4.304332256317139})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 6.070669651031494})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.140928745269775})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.73214054107666})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.9484453201293945})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 4.669916152954102})
store['active_learning_steps'][30]['training']['best_epoch']=5
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.1960279655808236, 'crossentropy': 5.155208613437308}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 3.2188427448272705})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 3.0130577087402344})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 3.1921350955963135})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.3772428035736084})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.449455738067627})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 3.0424108505249023})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.244121551513672})
store['active_learning_steps'][30]['eval_training']['best_epoch']=7
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 33102], ['ood', 13170], ['id', 13857], ['ood', 31727], ['id', 65427]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6134121946723201, 1.1132273729576585, 1.5486536338122092, 1.936212014922173, 2.278831739858946]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.566866874694824})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 4.334116458892822})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 4.092519283294678})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.015484809875488})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 4.481843948364258})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.2574462890625})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.929439544677734})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 4.825952529907227})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 6.680179119110107})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 5.2687506675720215})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 4.236971855163574})
store['active_learning_steps'][31]['training']['best_epoch']=8
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.20582360172095882, 'crossentropy': 4.405633871293024}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 2.883772850036621})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 3.1375620365142822})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 2.914531946182251})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 3.0752594470977783})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 3.251521110534668})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 3.1597166061401367})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.099703311920166})
store['active_learning_steps'][31]['eval_training']['best_epoch']=4
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 16991], ['id', 62619], ['id', 34173], ['id', 10229], ['id', 66955]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5138056729653453, 0.9799106651757004, 1.420810499183092, 1.820969277230744, 2.1727344784000016]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 4.58728551864624})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 4.289140224456787})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.201957702636719})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 5.821639060974121})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 4.025423049926758})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 6.789464950561523})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.342470645904541})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.926048278808594})
store['active_learning_steps'][32]['training']['best_epoch']=5
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.22595267363245236, 'crossentropy': 3.985076060233559}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 2.922229528427124})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 2.6232943534851074})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 3.0726680755615234})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.0573086738586426})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 2.819045066833496})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 2.9854073524475098})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 2.7690353393554688})
store['active_learning_steps'][32]['eval_training']['best_epoch']=7
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 19745], ['id', 65625], ['id', 4431], ['id', 35518], ['id', 49290]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5542003365288056, 0.9444222451803075, 1.3114226879848507, 1.6386040640332, 1.9430447196465224]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 4.847885608673096})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.021167755126953})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 4.534631252288818})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 4.899112701416016})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.196303367614746})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 5.065035820007324})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.800891399383545})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.875201225280762})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 5.32965612411499})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.2279118008604794, 'crossentropy': 5.509577755262754}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 2.8316829204559326})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 3.047485828399658})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 3.103489398956299})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 2.9836745262145996})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 3.271500587463379})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 3.1724958419799805})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 3.194481611251831})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 3.15718674659729})
store['active_learning_steps'][33]['eval_training']['best_epoch']=8
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 16518], ['id', 58338], ['id', 39490], ['id', 63649], ['id', 27722]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6224029453832154, 1.0846408587161884, 1.5079901307009869, 1.9022090251110475, 2.214002543944303]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 4.276462554931641})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 4.098118782043457})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 4.671195030212402})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 5.146315574645996})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 4.931771278381348})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.979416847229004})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.378345966339111})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 5.573146820068359})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 5.031163692474365})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 4.650205612182617})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 5.13973331451416})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 5.029243469238281})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 4.469748497009277})
store['active_learning_steps'][34]['training']['best_epoch']=10
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.21485095267363244, 'crossentropy': 4.4405113178011675}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.246241331100464})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 3.1197304725646973})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 2.917917490005493})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 3.594393730163574})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.24513578414917})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 2.9992074966430664})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 2.90777587890625})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 2.8970956802368164})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 3.004595994949341})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 3.024160861968994})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 3.024690628051758})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 3.040867567062378})
store['active_learning_steps'][34]['eval_training']['best_epoch']=9
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 12341], ['id', 14312], ['id', 4569], ['id', 34544], ['id', 17041]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6446124132794179, 1.1395550134568344, 1.6162171464846584, 2.0351660120447344, 2.380673274916651]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 4.462283134460449})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 4.129144191741943})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 5.113340854644775})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 4.550417900085449})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 4.9148712158203125})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 5.065295696258545})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.049807548522949})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.124198913574219})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 5.315981864929199})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.4239959716796875})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.523988723754883})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 4.297113418579102})
store['active_learning_steps'][35]['training']['best_epoch']=9
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.22929471419791025, 'crossentropy': 5.026953905289644}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 2.519439697265625})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 2.6772541999816895})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.0210142135620117})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 3.3036208152770996})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.123347282409668})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 3.4327149391174316})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 3.169189929962158})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 3.173327684402466})
store['active_learning_steps'][35]['eval_training']['best_epoch']=5
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 17943], ['id', 66020], ['id', 41585], ['id', 33863], ['id', 42421]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5466242902483383, 1.03260107503609, 1.4520898942463853, 1.8212991378284005, 2.158174834336731]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 5.640593528747559})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 4.817315101623535})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 4.590660095214844})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.016458034515381})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.182499885559082})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 5.051105499267578})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 4.468008995056152})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.533574104309082})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 4.0569939613342285})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 4.6474175453186035})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.370274543762207})
store['active_learning_steps'][36]['training']['best_epoch']=8
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.23290565457897972, 'crossentropy': 4.623386601106331}
