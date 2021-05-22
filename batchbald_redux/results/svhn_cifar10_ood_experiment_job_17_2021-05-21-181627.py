store = {}
store['timestamp']=1621617387
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=17']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=17
store['worker_id']=17
store['num_workers']=24
store['config']={'seed': 1253, 'uniform_ood': True, 'id_dataset_name': 'SVHN', 'ood_dataset_name': 'CIFAR-10', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node | one_hot_targets{'num_classes': 10}) + ('CIFAR-10 (Train, seed=0, 50000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'SVHN (Test)'"}
store['initial_training_set_indices']=[38482, 18819, 58066, 14663, 39799, 53509, 12901, 26100, 61523, 67745, 57808, 69963, 69909, 45371, 37280, 48685, 26877, 52249, 66762, 14073]
store['evaluation_set_indices']=[9356, 52217, 13204, 15153, 14643, 13323, 68768, 23207, 25999, 62719, 62312, 67969, 24256, 39281, 37692, 459, 50826, 51277, 57053, 2584, 51764, 14758, 22887, 43685, 53675, 71612, 55166, 16551, 62820, 4535, 12102, 2976, 62920, 41178, 65425, 24347, 41886, 15904, 4242, 38591, 69801, 8821, 58682, 26825, 58891, 26239, 12097, 25295, 62111, 31755, 35768, 26368, 42500, 34271, 27190, 19058, 51104, 6911, 30075, 67867, 33661, 68699, 33542, 20892, 66108, 65071, 38221, 28545, 4922, 712, 69652, 9859, 30961, 51019, 29978, 24859, 3266, 17700, 8635, 6353, 5221, 42961, 38139, 71930, 52654, 10503, 21854, 36516, 30504, 22436, 45904, 30936, 48527, 39826, 3646, 58802, 10195, 14513, 6465, 6942, 57592, 56379, 26009, 61985, 2559, 12661, 12013, 46596, 22602, 4480, 17051, 33111, 8443, 71520, 63570, 69611, 25877, 35431, 68255, 42429, 25233, 38864, 11350, 35991, 55649, 57177, 7278, 4769, 20349, 2614, 44954, 59941, 37367, 65209, 17027, 19532, 53043, 65575, 20118, 14547, 5357, 36375, 13466, 33485, 25546, 9095, 13754, 12356, 31308, 21474, 7790, 60533, 72158, 29121, 42063, 39774, 8251, 53403, 49392, 11194, 9155, 41513, 66798, 65593, 59814, 15932, 37576, 11589, 53361, 63564, 23612, 39344, 15174, 35048, 32969, 69692, 25106, 48838, 47004, 4184, 853, 45864, 56849, 67982, 15528, 22376, 35245, 45656, 59597, 66590, 54076, 16022, 11813, 65618, 9234, 51953, 9766, 41955, 44395, 39226, 40025, 41050, 18973, 65107, 47464, 33366, 60380, 2486, 33728, 17384, 20252, 502, 5733, 4780, 8085, 20338, 65499, 16532, 46969, 7202, 65103, 41400, 26582, 27643, 8071, 55598, 37396, 44808, 26291, 28417, 36402, 28726, 22517, 69815, 36383, 23607, 23033, 27971, 2408, 2278, 41478, 44310, 22574, 36584, 20402, 39412, 4629, 15386, 62095, 71458, 33017, 16110, 17249, 12926, 3490, 47863, 57175, 70171, 64841, 69552, 16738, 53687, 49215, 68777, 42356, 44008, 58581, 4015, 25552, 6585, 63976, 21856, 22022, 55859, 646, 40666, 20229, 54017, 19316, 47715, 63714, 56139, 20095, 56198, 49498, 71125, 37745, 28370, 447, 16265, 16217, 31553, 42330, 39800, 4708, 41610, 26365, 29555, 39014, 12058, 57716, 30264, 19834, 44802, 28557, 41674, 58223, 69197, 20831, 68939, 58071, 61613, 908, 66783, 49048, 8901, 8366, 43877, 27035, 5594, 16712, 65988, 44267, 68598, 18916, 55473, 13995, 8035, 35402, 49125, 1977, 30455, 18722, 28193, 13172, 50182, 7501, 13256, 30190, 3792, 2123, 1945, 578, 46527, 39552, 67117, 42833, 5445, 46094, 33919, 17401, 32440, 65698, 21803, 1135, 10541, 46967, 10104, 10938, 63683, 40034, 50634, 69388, 36184, 19463, 34004, 28951, 14855, 64729, 14756, 22150, 21459, 17111, 16346, 43426, 67098, 33904, 31401, 7659, 48749, 63155, 2295, 10885, 35729, 19327, 37233, 62037, 43673, 32598, 17664, 54682, 26311, 47139, 39399, 39716, 12071, 64933, 24857, 5906, 55259, 19820, 50768, 64273, 5453, 68989, 5148, 32502, 26332, 21086, 2537, 56917, 2572, 33746, 12667, 67185, 22625, 22488, 46950, 11323, 7732, 4099, 66265, 45874, 44873, 50645, 54736, 27587, 37633, 20063, 1608, 10391, 69839, 40026, 23753, 16692, 70616, 33037, 36107, 60644, 10024, 70725, 42517, 59766, 63776, 5240, 4298, 48682, 2647, 31850, 35911, 50647, 29464, 44634, 59672, 65002, 63792, 17766, 62198, 24020, 42922, 58463, 65717, 23905, 3709, 24462, 16997, 57309, 37223, 66400, 62492, 47056, 40814, 21985, 72066, 40550, 18131, 28968, 4841, 27091, 18456, 30336, 57899, 48912, 37103, 49194, 47247, 54365, 28077, 55585, 49073, 62608, 17950, 33176, 69058, 59000, 33429, 19825, 69851, 24553, 14100, 52015, 34854, 8384, 22221, 35886, 67782, 48319, 56320, 19629, 42327, 58156, 24662, 57555, 36936, 69589, 3895, 49861, 58546, 37408, 20865, 9547, 2308, 60654, 64334, 29058, 57610, 3713, 22067, 67083, 55907, 60300, 36206, 2137, 31864, 59454, 62125, 3472, 61684, 53364, 19002, 5961, 5119, 54575, 21647, 10117, 2063, 45076, 7655, 17649, 16183, 34516, 22281, 64009, 1482, 45897, 16054, 26453, 54529, 22123, 51161, 56473, 51275, 58255, 30056, 58472, 25031, 45022, 19772, 18227, 61247, 64229, 33494, 42705, 32892, 7643, 6554, 38114, 71630, 50256, 48460, 12647, 41199, 26273, 45698, 52378, 67419, 39957, 34025, 21810, 36037, 46937, 32002, 68859, 22312, 38228, 49463, 32134, 43593, 12976, 48518, 29540, 49660, 65445, 20048, 50377, 55745, 48666, 34187, 14797, 1090, 9866, 49432, 16623, 66209, 29260, 52431, 20003, 17847, 51378, 16023, 68062, 44305, 16631, 27731, 24784, 39156, 11115, 28872, 68835, 23709, 69182, 55249, 51867, 58062, 15447, 54267, 22358, 11689, 32422, 17668, 70285, 14630, 66794, 3930, 48981, 53416, 52758, 259, 46199, 29534, 64541, 17082, 44746, 25437, 49288, 43065, 30764, 38017, 51276, 30890, 65349, 52566, 50133, 43793, 30313, 16596, 24263, 5825, 59782, 46247, 12714, 31550, 66659, 56183, 15363, 28327, 17799, 7985, 57408, 63114, 5656, 45109, 8170, 71088, 44865, 5179, 33238, 67850, 59037, 70356, 57561, 5224, 54748, 48857, 57920, 64313, 61094, 24227, 27540, 48418, 49627, 5977, 47424, 49350, 2294, 51114, 31731, 68660, 48657, 47982, 5572, 67954, 72131, 38419, 5584, 43252, 9618, 23545, 33898, 68204, 52186, 24178, 19915, 6776, 31485, 32593, 19584, 19419, 27692, 8249, 34767, 43187, 21199, 9445, 58948, 11805, 31566, 23275, 48477, 70581, 468, 60975, 35599, 51011, 23731, 62929, 52127, 43105, 47132, 37098, 36682, 66718, 11836, 18937, 8353, 39475, 25066, 3810, 42035, 61047, 31409, 53353, 43799, 66218, 33732, 13353, 60944, 44114, 63746, 58818, 58308, 71199, 34872, 33651, 31320, 10155, 22562, 26256, 588, 650, 11367, 32284, 59309, 47102, 12778, 23277, 11903, 57880, 27145, 31297, 29703, 71945, 51586, 46004, 3819, 11022, 9807, 13278, 4765, 14868, 45323, 64881, 49532, 21786, 27694, 4261, 4225, 19091, 72034, 55698, 45428, 10685, 53402, 56253, 46547, 71757, 51782, 51907, 35547, 4933, 17159, 55552, 42654, 15891, 18290, 60649, 12688, 14180, 27824, 31768, 58640, 10644, 65690, 49127, 6096, 11685, 19904, 65825, 9756, 69122, 22560, 15354, 7212, 69075, 32862, 40238, 51753, 2289, 15439, 32940, 48616, 33630, 61582, 59003, 31277, 69455, 15225, 6524, 12255, 35631, 19799, 939, 19052, 51599, 33349, 15648, 53478, 48461, 57688, 16560, 29049, 42225, 52412, 16140, 40390, 32570, 24745, 64558, 36783, 6915, 47728, 965, 11449, 5116, 5323, 60583, 65003, 49946, 14668, 41788, 22684, 41248, 57017, 35386, 56663, 11333, 6235, 14545, 57849, 48023, 18451, 52781, 55872, 12166, 65210, 42135, 45704, 22159, 13433, 43848, 57952, 67211, 13469, 11047, 5020, 42097, 20945, 63525, 38029, 4448, 12645, 67581, 29111, 8657, 67780, 64513, 18251, 17888, 32040, 59868, 23404, 9423, 1799, 42360, 38722, 2521, 70901, 20614, 58004, 61052, 52510, 1767, 18118, 63984, 8997, 7359, 57822, 51575, 1154, 20732, 22093, 36091, 65675, 30482, 18517, 58191, 41454, 56022, 42315, 16818, 29430, 51625, 52715, 19267, 60460, 50887, 71829, 53823, 20360, 60961, 45356, 39961, 39474, 66779, 32959, 45573, 36984, 2876, 30770, 34908, 12101, 10839, 42028, 42187, 29776, 30785, 65134, 31096, 13346, 32978, 29254, 50953, 33172, 13798, 22658, 32286, 20308, 15277, 9517, 18525, 14838, 14280, 35505, 71679, 35497, 51264, 15149, 15077, 19660, 2980, 11973, 61547, 51033, 60741, 11385, 19913, 68557, 23524, 68591, 9114]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1005859375, 'crossentropy': 19.93238067626953})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1015625, 'crossentropy': 12.139759063720703})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1083984375, 'crossentropy': 8.714908599853516})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1064453125, 'crossentropy': 13.179631233215332})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1005859375, 'crossentropy': 9.62379264831543})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.103515625, 'crossentropy': 10.519475936889648})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.10805931161647203, 'crossentropy': 8.15623439420713}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.095703125, 'crossentropy': 4.262972831726074})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.087890625, 'crossentropy': 5.47929573059082})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.099609375, 'crossentropy': 5.104036331176758})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.0908203125, 'crossentropy': 5.022164344787598})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.09765625, 'crossentropy': 5.413016319274902})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 33264], ['ood', 32304], ['id', 6965], ['id', 33465], ['id', 26098]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6928858156000693, 1.322754210485713, 1.83678281890103, 2.298834345912233, 2.683377575113914]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.107421875, 'crossentropy': 7.261017799377441})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 7.770479679107666})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1005859375, 'crossentropy': 9.163244247436523})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.0986328125, 'crossentropy': 24.434314727783203})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 8.471977233886719})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 8.92813491821289})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 8.75503921508789})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 9.90035343170166})
store['active_learning_steps'][1]['training']['best_epoch']=5
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.1333358942839582, 'crossentropy': 9.10908869372311}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1279296875, 'crossentropy': 4.457847595214844})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 4.38865852355957})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 4.5901899337768555})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 5.2765607833862305})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 4.9861931800842285})
store['active_learning_steps'][1]['eval_training']['best_epoch']=2
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 41894], ['id', 67270], ['id', 21399], ['id', 59694], ['id', 52608]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5872683859897834, 1.0987820963011616, 1.5418957531149768, 1.9444811175482135, 2.297412919960829]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 6.966980934143066})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.107421875, 'crossentropy': 8.116044998168945})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 7.835786819458008})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1103515625, 'crossentropy': 8.13869857788086})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.11021051014136447, 'crossentropy': 7.526235138483405}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1005859375, 'crossentropy': 4.099861145019531})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.1005859375, 'crossentropy': 4.559012413024902})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 3.800604820251465})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 28416], ['id', 34238], ['id', 12678], ['id', 15202], ['id', 43828]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7390000274720253, 1.273021013455014, 1.7349145295843353, 2.1205369318775205, 2.433256464705103]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 10.067100524902344})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 18.09018325805664})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 7.56015157699585})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.11328125, 'crossentropy': 8.53325080871582})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.11528119237861094, 'crossentropy': 10.696584972341734}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 5.209200859069824})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1279296875, 'crossentropy': 5.006219863891602})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 5.276826858520508})
store['active_learning_steps'][3]['eval_training']['best_epoch']=1
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 26062], ['id', 5011], ['id', 8425], ['id', 48579], ['id', 59142]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7048062804151785, 1.31693719150248, 1.7869083892881745, 2.2024676110370844, 2.5625583556078197]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 9.672048568725586})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 8.52914047241211})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 11.029316902160645})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 8.105781555175781})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.12342501536570374, 'crossentropy': 11.445347312922557}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 4.690895080566406})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 5.791630744934082})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 6.390841960906982})
store['active_learning_steps'][4]['eval_training']['best_epoch']=1
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 14294], ['ood', 48832], ['id', 17537], ['ood', 26544], ['id', 63471]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0594386683478842, 1.638108077150417, 2.0747777043209314, 2.431003483067326, 2.7089929364081753]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 6.797184944152832})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 5.9654622077941895})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 5.633472442626953})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 6.183083534240723})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 8.228346824645996})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 6.284948348999023})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.11328125, 'crossentropy': 6.778360366821289})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.12876459741856178, 'crossentropy': 6.161000763483405}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 3.6600828170776367})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 4.532362937927246})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 3.854193687438965})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 3.8532750606536865})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 3.9035024642944336})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 14619], ['id', 41263], ['id', 2657], ['id', 8994], ['id', 401]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5092605580721761, 0.9790881046667548, 1.3729410788219862, 1.728264895287948, 2.0453045630604927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 7.767271995544434})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 6.637535095214844})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 8.851471900939941})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 7.33907413482666})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.11973724646588814, 'crossentropy': 7.878433874654272}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1015625, 'crossentropy': 5.268259525299072})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 4.670839309692383})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 4.336189270019531})
store['active_learning_steps'][6]['eval_training']['best_epoch']=3
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 3297], ['id', 56993], ['id', 24592], ['id', 34560], ['id', 36556]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6446482371007269, 1.0878321720717001, 1.465751712143077, 1.7962168669911054, 2.082141466203553]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 6.201440811157227})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 5.506002426147461})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 6.323875427246094})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 6.055666446685791})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 5.654767036437988})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.1413260602335587, 'crossentropy': 4.827091716445144}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 3.403139114379883})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 2.9144701957702637})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 3.220302104949951})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 3.437227725982666})
store['active_learning_steps'][7]['eval_training']['best_epoch']=2
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 16477], ['id', 16593], ['id', 32041], ['id', 62558], ['ood', 27613]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5825585426323132, 1.081897376885287, 1.5064119556031592, 1.8871747917378379, 2.210797273440021]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 5.405066013336182})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 5.009000778198242})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1298828125, 'crossentropy': 5.352750778198242})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 6.511709690093994})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.13663952059004303, 'crossentropy': 5.641764823102336}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 3.7622275352478027})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 3.8219103813171387})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 4.382610321044922})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 2687], ['id', 37351], ['id', 28865], ['id', 65453], ['id', 29621]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.48829643665090616, 0.9055024042423665, 1.2786362324650176, 1.6224078594183737, 1.9276309485043779]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1279296875, 'crossentropy': 6.264726638793945})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 5.832553863525391})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 7.12990665435791})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 5.949393272399902})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 5.915942192077637})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 7.7850117683410645})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 6.882091522216797})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.12004456054087277, 'crossentropy': 5.970504451252305}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.111328125, 'crossentropy': 3.233431577682495})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 3.797180652618408})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 3.8806238174438477})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 3.713132858276367})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 3.6158676147460938})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 3.9220495223999023})
store['active_learning_steps'][9]['eval_training']['best_epoch']=5
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 71159], ['id', 22383], ['id', 54951], ['id', 67196], ['id', 54070]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5313004447736591, 0.9866885922893127, 1.4270536399049134, 1.7904188353610913, 2.0910118697972067]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 5.700421333312988})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 4.927407264709473})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 5.665192604064941})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1279296875, 'crossentropy': 5.593456268310547})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.13272126613398894, 'crossentropy': 5.440726197564536}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 3.4920191764831543})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 4.008928298950195})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 3.9911012649536133})
store['active_learning_steps'][10]['eval_training']['best_epoch']=2
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 41209], ['id', 63345], ['id', 20623], ['id', 36229], ['id', 69755]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6601517852166684, 1.1938708296543021, 1.6547890116442026, 1.9966553473990412, 2.2929902522943304]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 6.153952598571777})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 5.672065258026123})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 5.944326400756836})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 5.614302635192871})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.14051936078672403, 'crossentropy': 5.218446287261831}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 3.6199445724487305})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 4.015927314758301})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 3.8603906631469727})
store['active_learning_steps'][11]['eval_training']['best_epoch']=2
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 30921], ['id', 42316], ['id', 28039], ['id', 11656], ['id', 23717]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4042909296711361, 0.7954492484367899, 1.1559434645096367, 1.4651491066773454, 1.7299859778292603]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 5.560234069824219})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 6.063434600830078})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 6.572020053863525})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 4.988174915313721})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 5.290205001831055})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 5.488585948944092})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 5.525065898895264})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 7.226266384124756})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 5.56191873550415})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 6.007152557373047})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 5.736282825469971})
store['active_learning_steps'][12]['training']['best_epoch']=8
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.14044253226797787, 'crossentropy': 6.996506103065458}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 3.6323843002319336})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 3.362936019897461})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 4.264310836791992})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 4.2642130851745605})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 3.92889404296875})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 4.332913875579834})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 4.17820930480957})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 38020], ['id', 629], ['id', 21705], ['id', 21133], ['id', 59532]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6332102897326564, 1.1786704948387534, 1.6498085181874984, 2.049786416008412, 2.4013320618679064]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 4.440446853637695})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 5.026880264282227})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 5.932130813598633})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 5.5113019943237305})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 5.800055027008057})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 5.074280738830566})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 4.89904260635376})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 6.199921607971191})
store['active_learning_steps'][13]['training']['best_epoch']=5
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.14405347264904733, 'crossentropy': 5.704208402158882}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 3.47963809967041})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 3.8254141807556152})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 3.6616015434265137})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 3.3489418029785156})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 3.621229648590088})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 3.4639697074890137})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 3.8632102012634277})
store['active_learning_steps'][13]['eval_training']['best_epoch']=4
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 37845], ['id', 4172], ['id', 39145], ['id', 68756], ['ood', 23497]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6136724743683333, 1.1099631767068074, 1.5855874470401652, 2.0153901791329467, 2.361681022520063]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 6.682839870452881})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 4.899716377258301})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 5.594318389892578})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 5.546026229858398})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.14889366933005532, 'crossentropy': 5.072341853295944}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 4.662130355834961})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 4.608176231384277})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 4.500507354736328})
store['active_learning_steps'][14]['eval_training']['best_epoch']=1
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 428], ['id', 46720], ['id', 39632], ['id', 8474], ['id', 22133]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4960242523840679, 0.9390992325522198, 1.2969083320928845, 1.6092617609380078, 1.9034988417086671]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 5.48114538192749})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 6.723099708557129})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 7.241789817810059})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 6.324745178222656})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 5.426356792449951})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 5.86295223236084})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 5.941988945007324})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 7.339059829711914})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 6.344278335571289})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 6.779669761657715})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 6.380521774291992})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 6.45496129989624})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 6.670802116394043})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 6.744505882263184})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 6.637073516845703})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 6.982453346252441})
store['active_learning_steps'][15]['training']['best_epoch']=13
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.15135218192993238, 'crossentropy': 6.31930712680547}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 3.472609519958496})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 3.859449625015259})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 4.035512924194336})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 4.173919677734375})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 4.073071002960205})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 4.222829818725586})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 3.9592761993408203})
store['active_learning_steps'][15]['eval_training']['best_epoch']=4
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 9565], ['id', 32516], ['id', 42273], ['id', 60548], ['id', 12370]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.594843426769247, 1.1133051197849035, 1.5750949376585481, 2.0110498232694796, 2.3451863366311674]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.435081481933594})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 5.181522369384766})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 5.449521064758301})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 5.503957748413086})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.17217271051014135, 'crossentropy': 5.6781449273970495}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 3.8492870330810547})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 4.017328262329102})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 3.9126644134521484})
store['active_learning_steps'][16]['eval_training']['best_epoch']=1
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 63938], ['id', 66973], ['id', 460], ['id', 71554], ['id', 6869]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5684159538438405, 1.0674735491794627, 1.4637772241562192, 1.8071543295790606, 2.0941908998657333]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 7.567751884460449})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 4.468433856964111})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 4.725612640380859})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 6.05593204498291})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 4.759034156799316})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 5.6691575050354})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.319026947021484})
store['active_learning_steps'][17]['training']['best_epoch']=4
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.18588660110633068, 'crossentropy': 5.785407143131531}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 3.1732096672058105})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 3.7416391372680664})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 4.000151634216309})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 3.7102761268615723})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.910372734069824})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 3.702476978302002})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 32588], ['id', 7816], ['id', 55588], ['id', 2078], ['id', 7483]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6809847506644788, 1.214927148271784, 1.6798263867607015, 2.0261866222083755, 2.3132713899523636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 5.329514503479004})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 5.367968559265137})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 4.980620384216309})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 5.088067054748535})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.798800468444824})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 6.0584564208984375})
store['active_learning_steps'][18]['training']['best_epoch']=3
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.17793484941610327, 'crossentropy': 4.614851432851875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 3.223736524581909})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 3.6968014240264893})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 3.6902618408203125})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 3.382312536239624})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 3.495426654815674})
store['active_learning_steps'][18]['eval_training']['best_epoch']=4
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 2291], ['id', 15626], ['id', 12115], ['id', 38213], ['id', 32726]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.46801994413145653, 0.8801698873516974, 1.255087577455865, 1.5908211595595443, 1.8925144022470217]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 5.625990390777588})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 5.421187400817871})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 5.009427547454834})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 4.275411605834961})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 6.557894706726074})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 5.468271732330322})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.932129383087158})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.161339889366933, 'crossentropy': 4.141904975126767}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 2.8276138305664062})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 2.970292568206787})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 3.206569194793701})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 3.1703262329101562})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.326317310333252})
store['active_learning_steps'][19]['eval_training']['best_epoch']=2
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 49597], ['id', 28655], ['id', 30207], ['id', 69124], ['id', 38002]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4922664808465289, 0.9267909184611574, 1.30940211079835, 1.673423217529034, 1.9982966079095839]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 4.393736839294434})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 5.556659698486328})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 6.0546369552612305})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.046644687652588})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 5.8893585205078125})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.17985556238475722, 'crossentropy': 4.882713463237554}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 3.9053518772125244})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 3.6185314655303955})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 3.671276569366455})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 3.837803840637207})
store['active_learning_steps'][20]['eval_training']['best_epoch']=3
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 5037], ['id', 2843], ['ood', 47400], ['id', 68798], ['id', 37431]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5415623442505468, 1.0439767566588913, 1.4115216363470582, 1.7410686089708962, 2.0480813411496808]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 5.49846887588501})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 5.204407691955566})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 4.537690162658691})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 4.8485517501831055})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 5.089756011962891})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 4.828269958496094})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 4.979159832000732})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.23989200592041})
store['active_learning_steps'][21]['training']['best_epoch']=5
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.18139213275968039, 'crossentropy': 4.575694097649047}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 3.81473445892334})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 3.811163902282715})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 3.6299843788146973})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 3.3984527587890625})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 3.3186140060424805})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 3.30121111869812})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 3.331695318222046})
store['active_learning_steps'][21]['eval_training']['best_epoch']=6
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 11579], ['id', 5976], ['id', 56071], ['id', 54540], ['id', 59015]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6312937572393915, 1.1082549823528356, 1.553712518828656, 1.9250805607821544, 2.27196200933264]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 4.098614692687988})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 4.31934928894043})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 6.36860466003418})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 5.251217842102051})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 5.404371738433838})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 4.603078842163086})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 4.606419563293457})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 4.942136287689209})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 5.815128326416016})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.753002166748047})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.18442685925015365, 'crossentropy': 4.353862853891364}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 3.7259387969970703})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.0952322483062744})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 3.0956318378448486})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 3.113903522491455})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.027151584625244})
store['active_learning_steps'][22]['eval_training']['best_epoch']=2
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 6392], ['id', 18767], ['id', 27718], ['id', 4254], ['id', 58693]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5620142208255721, 1.0006148152497754, 1.4089532492603771, 1.7732320838851257, 2.10329496290079]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 5.0073041915893555})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.236863136291504})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 6.112841606140137})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.715585708618164})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.128986358642578})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 5.58599328994751})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 5.244324684143066})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.102461814880371})
store['active_learning_steps'][23]['training']['best_epoch']=5
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.1713660110633067, 'crossentropy': 5.087119338698525}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 3.165348529815674})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 3.1732752323150635})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 3.170492172241211})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.10111665725708})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.0572400093078613})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.058647632598877})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.2663464546203613})
store['active_learning_steps'][23]['eval_training']['best_epoch']=7
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 47051], ['id', 19853], ['id', 58551], ['id', 38936], ['ood', 10095]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5556251947572953, 1.0443595058537118, 1.4919629525287053, 1.866857795382379, 2.202691459130846]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 4.397936820983887})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 4.411421775817871})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.544206619262695})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 4.307522773742676})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 4.483313083648682})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 4.629141807556152})
store['active_learning_steps'][24]['training']['best_epoch']=3
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.20597725875845113, 'crossentropy': 4.992216610805931}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 3.260924816131592})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 2.712076187133789})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.913681983947754})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 3.1565160751342773})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 3.310220241546631})
store['active_learning_steps'][24]['eval_training']['best_epoch']=3
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 11741], ['id', 18808], ['id', 7341], ['id', 55787], ['id', 39288]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5583076275952765, 1.043415430163297, 1.4905721862069878, 1.8874414425776322, 2.2021594162889855]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 5.12263822555542})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 4.657950401306152})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 4.354358673095703})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 4.848021030426025})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.80222225189209})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 5.77842378616333})
store['active_learning_steps'][25]['training']['best_epoch']=3
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.20559311616472034, 'crossentropy': 4.0809679553050096}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 2.9073355197906494})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 2.7363414764404297})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 2.9019577503204346})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 3.1549768447875977})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 3.4012768268585205})
store['active_learning_steps'][25]['eval_training']['best_epoch']=5
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 14719], ['id', 52648], ['id', 6599], ['id', 10446], ['id', 32690]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4199026562537037, 0.8313935722126905, 1.198645281186769, 1.5077302814580134, 1.7846248570528882]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 4.495030403137207})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.7914299964904785})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 4.495722770690918})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 4.524718761444092})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 4.525362968444824})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 4.689579010009766})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.716068267822266})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 4.725237846374512})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 4.980580806732178})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 4.88548469543457})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 7.287500858306885})
store['active_learning_steps'][26]['training']['best_epoch']=8
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.22687461585740626, 'crossentropy': 4.442111211681777}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.070591688156128})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.5046353340148926})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 3.0910186767578125})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.146904468536377})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 3.1587376594543457})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.947556972503662})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 3.1294965744018555})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.912992477416992})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 3.1435227394104004})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.0311083793640137})
store['active_learning_steps'][26]['eval_training']['best_epoch']=8
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 40696], ['id', 12080], ['id', 54587], ['id', 58232], ['id', 13871]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5208510925194288, 1.0205713797106826, 1.44144841381075, 1.7972779735593551, 2.1251056222659734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 4.661794662475586})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 4.0273332595825195})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.648641586303711})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 4.623713493347168})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.35599422454834})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.545022964477539})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 4.402096748352051})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.5600433349609375})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 4.3366594314575195})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 4.597007751464844})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 4.65230655670166})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 4.674817085266113})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 4.713900566101074})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 4.744131565093994})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 4.987987518310547})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 4.778131484985352})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 5.293727397918701})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 4.078483581542969})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 4.6493120193481445})
store['active_learning_steps'][27]['training']['best_epoch']=16
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.24085740626920712, 'crossentropy': 4.1103182501344495}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 2.739696502685547})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.689453601837158})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 3.1488466262817383})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 2.8420145511627197})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 3.0122132301330566})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 2.8994081020355225})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 2.928621768951416})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 2.7385897636413574})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 2.9062790870666504})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 2.7905173301696777})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 2.7979347705841064})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.871899366378784})
store['active_learning_steps'][27]['eval_training']['best_epoch']=9
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 31157], ['id', 69099], ['id', 41113], ['id', 33552], ['id', 2631]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6748359987628889, 1.2842713953031715, 1.7554690086809976, 2.1716725718132386, 2.517139475907377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 4.39735221862793})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 4.5848212242126465})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.555743217468262})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.03474235534668})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 6.257158279418945})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 4.520409107208252})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 4.645147323608398})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 5.670374870300293})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 5.0506086349487305})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 4.912487030029297})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.542680740356445})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 4.63484001159668})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.762999534606934})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 4.887460708618164})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.909976482391357})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.997438430786133})
store['active_learning_steps'][28]['training']['best_epoch']=13
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.2362476951444376, 'crossentropy': 4.460882879724954}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 2.9013895988464355})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 2.88430118560791})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 2.960538387298584})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 2.9280343055725098})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.117558240890503})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 3.1146726608276367})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.887876510620117})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 2.711181640625})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 2.8821280002593994})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 2.951951026916504})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 2.8316593170166016})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2744140625, 'crossentropy': 2.795787811279297})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.887876510620117})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 2.8969478607177734})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 2.8677921295166016})
store['active_learning_steps'][28]['eval_training']['best_epoch']=12
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 69745], ['id', 53481], ['id', 40874], ['id', 72098], ['id', 63064]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5751434717804792, 1.0712314982999112, 1.5505916899539176, 1.9636220373270596, 2.3319799879307084]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 4.4856109619140625})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 3.7032177448272705})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 4.173677444458008})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 5.381854057312012})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 4.512880325317383})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 5.053742408752441})
store['active_learning_steps'][29]['training']['best_epoch']=3
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.2027120467117394, 'crossentropy': 3.792679142497695}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 2.796609401702881})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 3.094290256500244})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 2.785818576812744})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.076012134552002})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 2.8786983489990234})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 18013], ['id', 44892], ['id', 65277], ['id', 15926], ['id', 57225]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.46940561479710186, 0.8738148944201427, 1.2404124524279703, 1.5841784722461902, 1.8684375049944926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.131045341491699})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 4.010912895202637})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 4.685236930847168})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 4.431117057800293})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.875012397766113})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 5.064424514770508})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 4.879863262176514})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 4.771263122558594})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 5.149265766143799})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 4.829140663146973})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 4.949188232421875})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 5.216876029968262})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 5.091646194458008})
store['active_learning_steps'][30]['training']['best_epoch']=10
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.25253534111862325, 'crossentropy': 4.357336043139213}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 2.752856731414795})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.0509281158447266})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.26953125, 'crossentropy': 2.643702268600464})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.8542230129241943})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 3.0693211555480957})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 3.0104947090148926})
store['active_learning_steps'][30]['eval_training']['best_epoch']=3
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 47513], ['id', 4036], ['id', 2388], ['id', 55142], ['id', 45825]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5387299730657655, 1.0686967457216636, 1.4803370057400098, 1.8471818441450267, 2.168899347921923]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 4.709511756896973})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 5.074956893920898})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 4.799377918243408})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.147773742675781})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 5.054508686065674})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.562962055206299})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 4.321975231170654})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.057007789611816})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 5.69031286239624})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 6.14279842376709})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 5.699680328369141})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 6.029703140258789})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 5.128602981567383})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.450361251831055})
store['active_learning_steps'][31]['training']['best_epoch']=11
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.19272433927473878, 'crossentropy': 5.444115655731408}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 3.4799506664276123})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 3.6969923973083496})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.404928684234619})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.388730049133301})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 3.1889612674713135})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.38889741897583})
store['active_learning_steps'][31]['eval_training']['best_epoch']=3
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 24310], ['id', 57988], ['id', 24118], ['id', 40892], ['id', 38449]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6346835282751035, 1.1223685972405355, 1.5647828787313482, 1.9676731471622837, 2.311520814582833]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 4.879846572875977})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 4.734957695007324})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 5.0192413330078125})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 4.864269256591797})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 5.688389778137207})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.5776262283325195})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 5.206574440002441})
store['active_learning_steps'][32]['training']['best_epoch']=4
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.21093269821757837, 'crossentropy': 4.700902675072987}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.1946234703063965})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 3.1146082878112793})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.180363893508911})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 3.116122245788574})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 3.2367560863494873})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 3.0059399604797363})
store['active_learning_steps'][32]['eval_training']['best_epoch']=4
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 56972], ['id', 14937], ['id', 68172], ['id', 31931], ['id', 6700]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6108168439765314, 1.1140743028578064, 1.527335113940583, 1.8763788743609187, 2.1782859081889407]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 4.3925909996032715})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.179056167602539})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 4.766413688659668})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 5.672231674194336})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 4.385651588439941})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 4.612727165222168})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.988641738891602})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 4.731928825378418})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 4.330324649810791})
store['active_learning_steps'][33]['training']['best_epoch']=6
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.24861708666256915, 'crossentropy': 4.399630442820375}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.3238768577575684})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 3.220128297805786})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 3.182440757751465})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 3.0721850395202637})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 3.0655741691589355})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 3.1483347415924072})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.9598546028137207})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 3.036139488220215})
store['active_learning_steps'][33]['eval_training']['best_epoch']=8
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 57415], ['id', 56596], ['id', 30671], ['id', 43835], ['id', 63752]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6991003415299027, 1.2030648809704863, 1.6845391476339762, 2.0992089429339353, 2.3880651190670736]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 4.065338611602783})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 4.1216535568237305})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 4.451886177062988})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.186123371124268})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.710942268371582})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 4.795454978942871})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.294970989227295})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 4.486286163330078})
store['active_learning_steps'][34]['training']['best_epoch']=5
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.23943607867240319, 'crossentropy': 4.353112275276582}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 2.6130809783935547})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 2.7786998748779297})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 2.756722927093506})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 2.973031520843506})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 2.880523204803467})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 2.964789867401123})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 2.91508150100708})
store['active_learning_steps'][34]['eval_training']['best_epoch']=7
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 44450], ['id', 65783], ['id', 3273], ['id', 47437], ['id', 57532]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5429799489746434, 1.0208273534174501, 1.4317290377126173, 1.7902970301594157, 2.097788357053699]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 4.045961380004883})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 3.8238840103149414})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 4.154825687408447})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 5.41505241394043})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 4.473421096801758})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.833208084106445})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2646484375, 'crossentropy': 4.286971569061279})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 5.884747505187988})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 4.750147819519043})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 4.0506181716918945})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 4.31784725189209})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 4.702310562133789})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 4.24725341796875})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.147111892700195})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 4.149198532104492})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2919921875, 'crossentropy': 4.31238317489624})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.33622407913208})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.29296875, 'crossentropy': 4.132546901702881})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.298828125, 'crossentropy': 4.326781272888184})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 4.259305953979492})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 4.224376678466797})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 4.200797080993652})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.302734375, 'crossentropy': 4.382018089294434})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.3017578125, 'crossentropy': 4.283288955688477})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 4.201339244842529})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2998046875, 'crossentropy': 4.396734237670898})
store['active_learning_steps'][35]['training']['best_epoch']=23
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.2628303626306085, 'crossentropy': 4.378860633066995}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 2.635953426361084})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 2.5069081783294678})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 2.5632340908050537})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 2.579575538635254})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 2.8115992546081543})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.828371047973633})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 2.5966501235961914})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2841796875, 'crossentropy': 2.697600841522217})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.291015625, 'crossentropy': 2.8323283195495605})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2939453125, 'crossentropy': 2.62992525100708})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.283203125, 'crossentropy': 2.6451058387756348})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 2.764228343963623})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.279296875, 'crossentropy': 2.6240296363830566})
store['active_learning_steps'][35]['eval_training']['best_epoch']=10
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 69920], ['id', 24093], ['id', 28952], ['id', 28913], ['id', 13544]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6371803059205801, 1.1757287499997635, 1.6617175468875116, 2.0995327710382297, 2.4812128162077536]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 4.40425968170166})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.952056407928467})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.147855758666992})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 3.9227254390716553})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 4.061203956604004})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 3.9815268516540527})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 4.085002899169922})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 4.268110275268555})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 4.358525276184082})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 4.331428527832031})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 4.398045539855957})
store['active_learning_steps'][36]['training']['best_epoch']=8
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.24834818684695759, 'crossentropy': 4.136508972130454}
