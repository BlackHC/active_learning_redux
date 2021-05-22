store = {}
store['timestamp']=1621608535
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=11']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=11
store['worker_id']=11
store['num_workers']=24
store['config']={'seed': 1246, 'uniform_ood': False, 'id_dataset_name': 'SVHN', 'ood_dataset_name': 'CIFAR-10', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node) + ('CIFAR-10 (Train, seed=0, 50000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'SVHN (Test)'"}
store['initial_training_set_indices']=[38482, 18819, 58066, 14663, 39799, 53509, 12901, 26100, 61523, 67745, 57808, 69963, 69909, 45371, 37280, 48685, 26877, 52249, 66762, 14073]
store['evaluation_set_indices']=[9356, 52217, 13204, 15153, 14643, 13323, 68768, 23207, 25999, 62719, 62312, 67969, 24256, 39281, 37692, 459, 50826, 51277, 57053, 2584, 51764, 14758, 22887, 43685, 53675, 71612, 55166, 16551, 62820, 4535, 12102, 2976, 62920, 41178, 65425, 24347, 41886, 15904, 4242, 38591, 69801, 8821, 58682, 26825, 58891, 26239, 12097, 25295, 62111, 31755, 35768, 26368, 42500, 34271, 27190, 19058, 51104, 6911, 30075, 67867, 33661, 68699, 33542, 20892, 66108, 65071, 38221, 28545, 4922, 712, 69652, 9859, 30961, 51019, 29978, 24859, 3266, 17700, 8635, 6353, 5221, 42961, 38139, 71930, 52654, 10503, 21854, 36516, 30504, 22436, 45904, 30936, 48527, 39826, 3646, 58802, 10195, 14513, 6465, 6942, 57592, 56379, 26009, 61985, 2559, 12661, 12013, 46596, 22602, 4480, 17051, 33111, 8443, 71520, 63570, 69611, 25877, 35431, 68255, 42429, 25233, 38864, 11350, 35991, 55649, 57177, 7278, 4769, 20349, 2614, 44954, 59941, 37367, 65209, 17027, 19532, 53043, 65575, 20118, 14547, 5357, 36375, 13466, 33485, 25546, 9095, 13754, 12356, 31308, 21474, 7790, 60533, 72158, 29121, 42063, 39774, 8251, 53403, 49392, 11194, 9155, 41513, 66798, 65593, 59814, 15932, 37576, 11589, 53361, 63564, 23612, 39344, 15174, 35048, 32969, 69692, 25106, 48838, 47004, 4184, 853, 45864, 56849, 67982, 15528, 22376, 35245, 45656, 59597, 66590, 54076, 16022, 11813, 65618, 9234, 51953, 9766, 41955, 44395, 39226, 40025, 41050, 18973, 65107, 47464, 33366, 60380, 2486, 33728, 17384, 20252, 502, 5733, 4780, 8085, 20338, 65499, 16532, 46969, 7202, 65103, 41400, 26582, 27643, 8071, 55598, 37396, 44808, 26291, 28417, 36402, 28726, 22517, 69815, 36383, 23607, 23033, 27971, 2408, 2278, 41478, 44310, 22574, 36584, 20402, 39412, 4629, 15386, 62095, 71458, 33017, 16110, 17249, 12926, 3490, 47863, 57175, 70171, 64841, 69552, 16738, 53687, 49215, 68777, 42356, 44008, 58581, 4015, 25552, 6585, 63976, 21856, 22022, 55859, 646, 40666, 20229, 54017, 19316, 47715, 63714, 56139, 20095, 56198, 49498, 71125, 37745, 28370, 447, 16265, 16217, 31553, 42330, 39800, 4708, 41610, 26365, 29555, 39014, 12058, 57716, 30264, 19834, 44802, 28557, 41674, 58223, 69197, 20831, 68939, 58071, 61613, 908, 66783, 49048, 8901, 8366, 43877, 27035, 5594, 16712, 65988, 44267, 68598, 18916, 55473, 13995, 8035, 35402, 49125, 1977, 30455, 18722, 28193, 13172, 50182, 7501, 13256, 30190, 3792, 2123, 1945, 578, 46527, 39552, 67117, 42833, 5445, 46094, 33919, 17401, 32440, 65698, 21803, 1135, 10541, 46967, 10104, 10938, 63683, 40034, 50634, 69388, 36184, 19463, 34004, 28951, 14855, 64729, 14756, 22150, 21459, 17111, 16346, 43426, 67098, 33904, 31401, 7659, 48749, 63155, 2295, 10885, 35729, 19327, 37233, 62037, 43673, 32598, 17664, 54682, 26311, 47139, 39399, 39716, 12071, 64933, 24857, 5906, 55259, 19820, 50768, 64273, 5453, 68989, 5148, 32502, 26332, 21086, 2537, 56917, 2572, 33746, 12667, 67185, 22625, 22488, 46950, 11323, 7732, 4099, 66265, 45874, 44873, 50645, 54736, 27587, 37633, 20063, 1608, 10391, 69839, 40026, 23753, 16692, 70616, 33037, 36107, 60644, 10024, 70725, 42517, 59766, 63776, 5240, 4298, 48682, 2647, 31850, 35911, 50647, 29464, 44634, 59672, 65002, 63792, 17766, 62198, 24020, 42922, 58463, 65717, 23905, 3709, 24462, 16997, 57309, 37223, 66400, 62492, 47056, 40814, 21985, 72066, 40550, 18131, 28968, 4841, 27091, 18456, 30336, 57899, 48912, 37103, 49194, 47247, 54365, 28077, 55585, 49073, 62608, 17950, 33176, 69058, 59000, 33429, 19825, 69851, 24553, 14100, 52015, 34854, 8384, 22221, 35886, 67782, 48319, 56320, 19629, 42327, 58156, 24662, 57555, 36936, 69589, 3895, 49861, 58546, 37408, 20865, 9547, 2308, 60654, 64334, 29058, 57610, 3713, 22067, 67083, 55907, 60300, 36206, 2137, 31864, 59454, 62125, 3472, 61684, 53364, 19002, 5961, 5119, 54575, 21647, 10117, 2063, 45076, 7655, 17649, 16183, 34516, 22281, 64009, 1482, 45897, 16054, 26453, 54529, 22123, 51161, 56473, 51275, 58255, 30056, 58472, 25031, 45022, 19772, 18227, 61247, 64229, 33494, 42705, 32892, 7643, 6554, 38114, 71630, 50256, 48460, 12647, 41199, 26273, 45698, 52378, 67419, 39957, 34025, 21810, 36037, 46937, 32002, 68859, 22312, 38228, 49463, 32134, 43593, 12976, 48518, 29540, 49660, 65445, 20048, 50377, 55745, 48666, 34187, 14797, 1090, 9866, 49432, 16623, 66209, 29260, 52431, 20003, 17847, 51378, 16023, 68062, 44305, 16631, 27731, 24784, 39156, 11115, 28872, 68835, 23709, 69182, 55249, 51867, 58062, 15447, 54267, 22358, 11689, 32422, 17668, 70285, 14630, 66794, 3930, 48981, 53416, 52758, 259, 46199, 29534, 64541, 17082, 44746, 25437, 49288, 43065, 30764, 38017, 51276, 30890, 65349, 52566, 50133, 43793, 30313, 16596, 24263, 5825, 59782, 46247, 12714, 31550, 66659, 56183, 15363, 28327, 17799, 7985, 57408, 63114, 5656, 45109, 8170, 71088, 44865, 5179, 33238, 67850, 59037, 70356, 57561, 5224, 54748, 48857, 57920, 64313, 61094, 24227, 27540, 48418, 49627, 5977, 47424, 49350, 2294, 51114, 31731, 68660, 48657, 47982, 5572, 67954, 72131, 38419, 5584, 43252, 9618, 23545, 33898, 68204, 52186, 24178, 19915, 6776, 31485, 32593, 19584, 19419, 27692, 8249, 34767, 43187, 21199, 9445, 58948, 11805, 31566, 23275, 48477, 70581, 468, 60975, 35599, 51011, 23731, 62929, 52127, 43105, 47132, 37098, 36682, 66718, 11836, 18937, 8353, 39475, 25066, 3810, 42035, 61047, 31409, 53353, 43799, 66218, 33732, 13353, 60944, 44114, 63746, 58818, 58308, 71199, 34872, 33651, 31320, 10155, 22562, 26256, 588, 650, 11367, 32284, 59309, 47102, 12778, 23277, 11903, 57880, 27145, 31297, 29703, 71945, 51586, 46004, 3819, 11022, 9807, 13278, 4765, 14868, 45323, 64881, 49532, 21786, 27694, 4261, 4225, 19091, 72034, 55698, 45428, 10685, 53402, 56253, 46547, 71757, 51782, 51907, 35547, 4933, 17159, 55552, 42654, 15891, 18290, 60649, 12688, 14180, 27824, 31768, 58640, 10644, 65690, 49127, 6096, 11685, 19904, 65825, 9756, 69122, 22560, 15354, 7212, 69075, 32862, 40238, 51753, 2289, 15439, 32940, 48616, 33630, 61582, 59003, 31277, 69455, 15225, 6524, 12255, 35631, 19799, 939, 19052, 51599, 33349, 15648, 53478, 48461, 57688, 16560, 29049, 42225, 52412, 16140, 40390, 32570, 24745, 64558, 36783, 6915, 47728, 965, 11449, 5116, 5323, 60583, 65003, 49946, 14668, 41788, 22684, 41248, 57017, 35386, 56663, 11333, 6235, 14545, 57849, 48023, 18451, 52781, 55872, 12166, 65210, 42135, 45704, 22159, 13433, 43848, 57952, 67211, 13469, 11047, 5020, 42097, 20945, 63525, 38029, 4448, 12645, 67581, 29111, 8657, 67780, 64513, 18251, 17888, 32040, 59868, 23404, 9423, 1799, 42360, 38722, 2521, 70901, 20614, 58004, 61052, 52510, 1767, 18118, 63984, 8997, 7359, 57822, 51575, 1154, 20732, 22093, 36091, 65675, 30482, 18517, 58191, 41454, 56022, 42315, 16818, 29430, 51625, 52715, 19267, 60460, 50887, 71829, 53823, 20360, 60961, 45356, 39961, 39474, 66779, 32959, 45573, 36984, 2876, 30770, 34908, 12101, 10839, 42028, 42187, 29776, 30785, 65134, 31096, 13346, 32978, 29254, 50953, 33172, 13798, 22658, 32286, 20308, 15277, 9517, 18525, 14838, 14280, 35505, 71679, 35497, 51264, 15149, 15077, 19660, 2980, 11973, 61547, 51033, 60741, 11385, 19913, 68557, 23524, 68591, 9114]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.10546875, 'crossentropy': 13.192342758178711})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.095703125, 'crossentropy': 15.456306457519531})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 8.603362083435059})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 10.91840934753418})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 10.386819839477539})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 10.46560001373291})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 10.64501953125})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 11.26232624053955})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 10.98304557800293})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 11.024261474609375})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 11.770965576171875})
store['active_learning_steps'][0]['training']['best_epoch']=8
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.11086355255070682, 'crossentropy': 11.07015043984327}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 6.239193439483643})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 6.261960029602051})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.126953125, 'crossentropy': 5.085477352142334})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 5.644772529602051})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 6.029515743255615})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.10546875, 'crossentropy': 6.4550323486328125})
store['active_learning_steps'][0]['eval_training']['best_epoch']=3
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 39632], ['id', 50986], ['id', 16867], ['id', 37137], ['id', 63627]], 'labels': [0, 6, 2, 8, 9], 'scores': [0.6509356408761493, 1.124700008504451, 1.5226270655120597, 1.8980725599446924, 2.221240404819006]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.08984375, 'crossentropy': 10.764179229736328})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1025390625, 'crossentropy': 9.099937438964844})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1103515625, 'crossentropy': 8.869217872619629})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1171875, 'crossentropy': 9.032363891601562})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.107421875, 'crossentropy': 9.003016471862793})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.109375, 'crossentropy': 9.345865249633789})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.109375, 'crossentropy': 9.719829559326172})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.10671481253841426, 'crossentropy': 9.738665392593731}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1005859375, 'crossentropy': 4.614372253417969})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.109375, 'crossentropy': 4.422794342041016})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.09375, 'crossentropy': 5.4586501121521})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1103515625, 'crossentropy': 4.966721057891846})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 5.327524185180664})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 6.014759063720703})
store['active_learning_steps'][1]['eval_training']['best_epoch']=6
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 67006], ['ood', 31575], ['id', 4786], ['id', 57064], ['id', 31253]], 'labels': [1, -1, 7, 1, 4], 'scores': [0.6448042763217376, 1.1998737124715873, 1.6392248484428609, 2.036523213455685, 2.3411212504158683]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 8.49393081665039})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 7.698586940765381})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 7.251619338989258})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1015625, 'crossentropy': 8.57579231262207})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.1136677934849416, 'crossentropy': 8.119305686270744}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.099609375, 'crossentropy': 4.225168704986572})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.11328125, 'crossentropy': 4.203207969665527})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 4.2775678634643555})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 41200], ['id', 9518], ['id', 16278], ['id', 55765], ['id', 31440]], 'labels': [1, 1, 5, 7, 1], 'scores': [0.6186374647792787, 1.1765022801582594, 1.666306794789266, 2.057280226280612, 2.3812300442970464]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 6.865395545959473})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 7.925320625305176})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 7.549005508422852})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 8.743008613586426})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.119140625, 'crossentropy': 7.757768154144287})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 7.730370998382568})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.1275737553779963, 'crossentropy': 7.647426724800246}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 4.391013145446777})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 4.405364036560059})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 4.550001621246338})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 4.252159118652344})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 4.411287307739258})
store['active_learning_steps'][3]['eval_training']['best_epoch']=4
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 21281], ['id', 55161], ['id', 1142], ['id', 37225], ['ood', 10971]], 'labels': [9, 3, 5, 1, -1], 'scores': [0.5739086364771593, 1.0867969948157068, 1.5155450512665327, 1.9082121529222027, 2.2439764079050084]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 6.508065223693848})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 7.799120903015137})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 5.921857833862305})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 6.440364837646484})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.14386140135218192, 'crossentropy': 6.581262364589736}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 4.056948184967041})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 4.256067276000977})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 3.9452269077301025})
store['active_learning_steps'][4]['eval_training']['best_epoch']=1
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 43327], ['id', 60297], ['id', 15968], ['id', 45149], ['id', 63869]], 'labels': [-1, 8, 3, 0, 4], 'scores': [0.5473260410101033, 1.0596721113474574, 1.4756149783453685, 1.8378279617861377, 2.155573236538399]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 7.101532936096191})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 6.987245559692383})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1318359375, 'crossentropy': 8.47695541381836})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 6.07722282409668})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.13529502151198525, 'crossentropy': 6.325428799170252}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 3.7724971771240234})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 3.89212703704834})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 3.8966445922851562})
store['active_learning_steps'][5]['eval_training']['best_epoch']=1
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 33465], ['id', 28311], ['id', 49486], ['id', 38944], ['id', 28434]], 'labels': [1, 8, 3, 8, 1], 'scores': [1.0688747893369184, 1.5736346910516856, 2.0358000234292883, 2.3994535279449103, 2.7007590804171313]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 7.666874885559082})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 7.94450569152832})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 5.667056083679199})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 6.55863094329834})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 6.742396354675293})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 6.779117584228516})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.1357944068838353, 'crossentropy': 6.272145220305777}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 3.1734633445739746})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 3.335524082183838})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 4.024722099304199})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 3.3575258255004883})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 3.8389649391174316})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 10493], ['id', 46071], ['id', 44291], ['id', 53607], ['id', 6948]], 'labels': [-1, 0, 6, 6, 1], 'scores': [0.47209628005760307, 0.9243303902923046, 1.3183353235733288, 1.6551878193182787, 1.949723498804791]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.111328125, 'crossentropy': 9.881551742553711})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 6.9369730949401855})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 9.108892440795898})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 7.722951889038086})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 7.5617170333862305})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.16145513214505225, 'crossentropy': 7.245631578441918}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 4.300844192504883})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 4.657472610473633})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 4.346232891082764})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 4.610262393951416})
store['active_learning_steps'][7]['eval_training']['best_epoch']=1
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 51300], ['id', 14665], ['id', 34118], ['id', 29968], ['id', 44031]], 'labels': [1, 1, 5, 9, 4], 'scores': [0.576909955180676, 1.0070423411973541, 1.3480686690601074, 1.6662359366355854, 1.9616916430857927]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 6.682077407836914})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 6.663911819458008})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 5.686540603637695})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 8.34620475769043})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 5.716970920562744})
store['active_learning_steps'][8]['training']['best_epoch']=2
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.13859864781807008, 'crossentropy': 6.829764208474185}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 3.5504746437072754})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 3.8328402042388916})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 3.8811545372009277})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 4.002068042755127})
store['active_learning_steps'][8]['eval_training']['best_epoch']=2
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 11641], ['id', 32786], ['id', 70796], ['id', 6531], ['id', 17329]], 'labels': [2, 3, 9, 9, 1], 'scores': [0.48603627837627805, 0.9296416103652151, 1.3308608122026342, 1.6525217189971717, 1.9409426907848721]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 7.097338676452637})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 6.928323745727539})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 6.929244518280029})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 6.951800346374512})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 7.28179407119751})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 7.4019975662231445})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 7.36404275894165})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.13314382298709282, 'crossentropy': 7.672314963314382}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.111328125, 'crossentropy': 3.3417906761169434})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1171875, 'crossentropy': 3.5996954441070557})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 3.8224291801452637})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 4.650146484375})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1123046875, 'crossentropy': 4.2793779373168945})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 4.373106956481934})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 21980], ['id', 54135], ['id', 24929], ['id', 59255], ['ood', 25093]], 'labels': [2, 8, 5, 8, -1], 'scores': [0.5383391662089346, 1.0093032168151765, 1.4303908182453027, 1.7898311366395792, 2.089061207431574]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 6.899143218994141})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1064453125, 'crossentropy': 6.268669128417969})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 6.689513206481934})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 6.7793073654174805})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 6.041263580322266})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 6.312311172485352})
store['active_learning_steps'][10]['training']['best_epoch']=3
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.16352950215119852, 'crossentropy': 6.94084924323909}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 3.458509683609009})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 4.5047607421875})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 4.787642002105713})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 4.455057144165039})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 4.191669464111328})
store['active_learning_steps'][10]['eval_training']['best_epoch']=2
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 70505], ['id', 60528], ['id', 23678], ['id', 71744], ['id', 27286]], 'labels': [8, 3, 0, 7, 1], 'scores': [0.5574338802104, 1.0016256522528375, 1.4186784386350344, 1.7713468474812717, 2.0866523473634353]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 5.827353477478027})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 6.23201847076416})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 8.86722183227539})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 6.3968706130981445})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 5.8668532371521})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 7.279889106750488})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 7.336753845214844})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.15181315304240933, 'crossentropy': 7.00477417217271}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 3.4241719245910645})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 3.8119585514068604})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 3.925902843475342})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 3.62058162689209})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 4.344139099121094})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 4.067376136779785})
store['active_learning_steps'][11]['eval_training']['best_epoch']=3
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 11096], ['id', 33671], ['ood', 23148], ['ood', 28794], ['id', 17167]], 'labels': [-1, 1, -1, -1, 1], 'scores': [0.575815998851642, 1.0697256923059937, 1.4904377572651466, 1.8575145049504869, 2.181854435300054]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 6.653766632080078})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 6.259651184082031})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 6.453638076782227})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 6.939562797546387})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 6.972050666809082})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 7.047935485839844})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 7.302028656005859})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 7.423525810241699})
store['active_learning_steps'][12]['training']['best_epoch']=5
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.15699907805777505, 'crossentropy': 7.712449461240012}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 3.739701271057129})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 3.61641001701355})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 4.476939678192139})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 4.265856742858887})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 4.584054470062256})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 4.328721046447754})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 3.876908779144287})
store['active_learning_steps'][12]['eval_training']['best_epoch']=4
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 46541], ['id', 66056], ['id', 9673], ['id', 49829], ['id', 54255]], 'labels': [0, 1, 0, 6, 3], 'scores': [0.48942311534245153, 0.935670111217223, 1.2972296627684168, 1.6336130168305374, 1.9292749747110518]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 8.253780364990234})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 6.935467720031738})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 6.8307414054870605})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 7.172675132751465})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 7.9833455085754395})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 6.3036956787109375})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 6.885294437408447})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 9.566169738769531})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 8.848718643188477})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 7.166149139404297})
store['active_learning_steps'][13]['training']['best_epoch']=7
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.17493853718500307, 'crossentropy': 7.599544550937308}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 3.36258602142334})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 4.183690071105957})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 4.210058689117432})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 4.527841567993164})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 4.340662956237793})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 3.911956310272217})
store['active_learning_steps'][13]['eval_training']['best_epoch']=3
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 22334], ['ood', 24650], ['id', 4609], ['id', 60738], ['id', 59715]], 'labels': [9, -1, 1, 2, 1], 'scores': [0.5044768862646174, 0.9747329114559287, 1.4108560484261, 1.8075063932761841, 2.163910868588691]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 5.064614772796631})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 6.484015941619873})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 6.368088722229004})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 7.08449649810791})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.16122464658881377, 'crossentropy': 5.139629830593116}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 3.0844638347625732})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 3.3905091285705566})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 3.3035359382629395})
store['active_learning_steps'][14]['eval_training']['best_epoch']=1
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 48844], ['ood', 3789], ['id', 38287], ['id', 38529], ['id', 32330]], 'labels': [1, -1, 8, 8, 1], 'scores': [0.5058176569880157, 0.9912388143222897, 1.4181190608305867, 1.7635234234899109, 2.062785879202604]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 6.290909767150879})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 5.606812477111816})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 6.298128128051758})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 7.072514533996582})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 6.670347213745117})
store['active_learning_steps'][15]['training']['best_epoch']=2
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.1711739397664413, 'crossentropy': 5.637530251229256}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.7708847522735596})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 4.237246513366699})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 3.6480584144592285})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 3.7574706077575684})
store['active_learning_steps'][15]['eval_training']['best_epoch']=1
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 14947], ['id', 60228], ['id', 48501], ['ood', 45415], ['id', 50577]], 'labels': [1, 1, 5, -1, 2], 'scores': [0.4385138264560311, 0.8406421336372896, 1.2170680417049633, 1.5467829937317843, 1.8504951875483195]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 6.103916168212891})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.146484375, 'crossentropy': 6.725765228271484})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 5.856968879699707})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 6.574469566345215})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 6.349030494689941})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 6.797889709472656})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 7.086252212524414})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 6.934419631958008})
store['active_learning_steps'][16]['training']['best_epoch']=5
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.1531576521204671, 'crossentropy': 6.521451362745851}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 3.026515007019043})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 3.6571035385131836})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 4.129822731018066})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 3.919797420501709})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 3.7376694679260254})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 4.088916778564453})
store['active_learning_steps'][16]['eval_training']['best_epoch']=3
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 63887], ['id', 24669], ['ood', 12754], ['id', 38654], ['id', 7350]], 'labels': [7, 1, -1, 8, 6], 'scores': [0.5508948353802612, 0.9446063963281155, 1.3175324622597633, 1.636604661973442, 1.9389391429553569]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 7.187285423278809})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 8.444347381591797})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 5.806753158569336})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 5.243179798126221})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 5.995712757110596})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 6.47963285446167})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 5.92598295211792})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 5.627989292144775})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 5.886758804321289})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 5.987056732177734})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.918159484863281})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 6.238434791564941})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 6.596520900726318})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 6.370512008666992})
store['active_learning_steps'][17]['training']['best_epoch']=11
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.17943300553165334, 'crossentropy': 6.195726653733866}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 3.550098180770874})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 3.5773322582244873})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 3.5384340286254883})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 3.781674861907959})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 3.5537657737731934})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 3.5140867233276367})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 3.496567964553833})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.866116762161255})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.6100053787231445})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 3.472968578338623})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 3.426508665084839})
store['active_learning_steps'][17]['eval_training']['best_epoch']=8
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 43767], ['ood', 13223], ['ood', 27576], ['id', 48733], ['ood', 8627]], 'labels': [3, -1, -1, 1, -1], 'scores': [0.5547593434437036, 1.0704364124552064, 1.5272680816186446, 1.9434255850453672, 2.289759623214384]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 6.690479278564453})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 6.20867395401001})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 5.96500301361084})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 6.027491569519043})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 6.060046195983887})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 5.6218719482421875})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 5.736972808837891})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 6.4972381591796875})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 7.5043792724609375})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.17639827904118008, 'crossentropy': 5.773634373079287}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 3.908832550048828})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 3.702925205230713})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 3.548800468444824})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 3.864356279373169})
store['active_learning_steps'][18]['eval_training']['best_epoch']=1
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 5341], ['ood', 17617], ['id', 10783], ['id', 58712], ['id', 38958]], 'labels': [-1, -1, 1, 4, 9], 'scores': [0.5640866146789854, 1.062317106195696, 1.539711380674592, 1.9040359913022176, 2.2356425483565427]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 5.889360427856445})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 5.703120231628418})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 5.617228984832764})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 6.411159515380859})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 6.609861850738525})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.181640625, 'crossentropy': 5.964838981628418})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 7.081439018249512})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 6.1800432205200195})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 6.536358833312988})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 6.923264026641846})
store['active_learning_steps'][19]['training']['best_epoch']=7
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.18869084204056547, 'crossentropy': 6.899046726144745}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.987774133682251})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 3.739138603210449})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 4.1565728187561035})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 3.5989742279052734})
store['active_learning_steps'][19]['eval_training']['best_epoch']=1
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 48011], ['id', 9162], ['id', 9241], ['id', 40481], ['id', 69396]], 'labels': [6, 5, 1, 1, 8], 'scores': [0.5274674146916494, 1.0171326066920403, 1.4650868085012456, 1.8672574595050664, 2.2355698031689766]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.142578125, 'crossentropy': 6.30819034576416})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 6.60910701751709})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 5.985013008117676})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 6.169456481933594})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 6.833641052246094})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 5.968290328979492})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.15238936693300553, 'crossentropy': 6.303216353910572}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 3.4199283123016357})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 3.654900550842285})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 4.0417985916137695})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 4.004486083984375})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 3.9519009590148926})
store['active_learning_steps'][20]['eval_training']['best_epoch']=2
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 45412], ['id', 57075], ['id', 64865], ['id', 52189], ['id', 8017]], 'labels': [-1, 1, 6, 2, 6], 'scores': [0.5269942337174833, 1.0232126862122763, 1.4354458954906204, 1.8034074496250596, 2.0986736999359716]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 5.723659515380859})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 6.139422416687012})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 7.97894287109375})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 6.653903007507324})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 6.466666221618652})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 6.644207000732422})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.17628303626306085, 'crossentropy': 10.219634728411187}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 3.3863253593444824})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 4.739854335784912})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 4.224216938018799})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 4.66810417175293})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 4.571791648864746})
store['active_learning_steps'][21]['eval_training']['best_epoch']=2
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 60593], ['id', 6923], ['id', 56264], ['id', 29176], ['id', 35474]], 'labels': [1, 1, 2, 9, 0], 'scores': [0.4626966055933467, 0.8743388521202782, 1.24909798583047, 1.5783913294332361, 1.8845954471846422]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 6.107385635375977})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 6.522753715515137})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 7.745672702789307})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 7.549867153167725})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 6.936831474304199})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 6.684745788574219})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 8.684347152709961})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 6.939467906951904})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 6.976273059844971})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1513671875, 'crossentropy': 6.945387840270996})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.16064843269821757, 'crossentropy': 10.579901659496004}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.1552734375, 'crossentropy': 4.287245750427246})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 4.076107025146484})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 4.058597087860107})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 4.546534538269043})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 4.381711006164551})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 4.351192951202393})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 3.9967174530029297})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 4.589839458465576})
store['active_learning_steps'][22]['eval_training']['best_epoch']=5
store['active_learning_steps'][22]['acquisition']={'indices': [['ood', 38140], ['ood', 15672], ['id', 54236], ['id', 6386], ['id', 55898]], 'labels': [-1, -1, 5, 2, 1], 'scores': [0.556586933167962, 1.078838525408624, 1.5667957193784359, 1.986079147250459, 2.3459084783826025]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 5.413636207580566})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 6.0125555992126465})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 6.176556587219238})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 6.172080993652344})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.135133266448975})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 6.318535327911377})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 6.54164981842041})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 6.296712398529053})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 6.498414516448975})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.640586853027344})
store['active_learning_steps'][23]['training']['best_epoch']=7
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.19172556853103873, 'crossentropy': 6.469923435579287}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 3.4346776008605957})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 3.927475929260254})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 4.166701316833496})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 3.7880163192749023})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 4.228597164154053})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 3.908115863800049})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 4.098221778869629})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 3.9607315063476562})
store['active_learning_steps'][23]['eval_training']['best_epoch']=5
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 65516], ['id', 67041], ['id', 25250], ['id', 17511], ['ood', 7557]], 'labels': [1, 5, 1, 1, -1], 'scores': [0.4707482056293167, 0.9148948045244423, 1.3166258204762535, 1.6871372660149828, 2.025588943472185]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 5.414632797241211})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 5.415282249450684})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 5.85976505279541})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 5.9953460693359375})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 6.322503566741943})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 6.057586193084717})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 6.12247896194458})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 6.429698467254639})
store['active_learning_steps'][24]['training']['best_epoch']=5
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.17032882606023356, 'crossentropy': 6.547649887638292}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 3.530834197998047})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 3.683711528778076})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 3.7156624794006348})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 3.987968683242798})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 4.075135707855225})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 3.8456482887268066})
store['active_learning_steps'][24]['eval_training']['best_epoch']=3
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 5646], ['ood', 26722], ['id', 64027], ['id', 64480], ['id', 777]], 'labels': [0, -1, 5, 6, 5], 'scores': [0.4576546434100557, 0.8617819136951121, 1.2469534274886525, 1.5719574605587132, 1.8651885869203575]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 5.817098140716553})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 5.638568878173828})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 6.6952667236328125})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 5.201842308044434})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 5.990597724914551})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.18004763368162263, 'crossentropy': 6.308552334626613}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 4.864658832550049})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 3.2112276554107666})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.1572265625, 'crossentropy': 3.5473122596740723})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 3.841796398162842})
store['active_learning_steps'][25]['eval_training']['best_epoch']=1
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 29587], ['id', 69459], ['id', 9259], ['id', 40182], ['id', 26604]], 'labels': [-1, 3, 0, 8, 7], 'scores': [0.502528789910516, 0.9841101293701287, 1.365848194063135, 1.7107516021495286, 2.006794785779517]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 5.450127601623535})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.9017839431762695})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.590453624725342})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 5.519009590148926})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 5.253902435302734})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.864615440368652})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.952606201171875})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 6.812950134277344})
store['active_learning_steps'][26]['training']['best_epoch']=5
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.18684695759065764, 'crossentropy': 5.368778090427167}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 2.8419647216796875})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 3.3310739994049072})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 3.2059249877929688})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.6208252906799316})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 3.558820962905884})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.3090505599975586})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.2896485328674316})
store['active_learning_steps'][26]['eval_training']['best_epoch']=7
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 27160], ['ood', 24438], ['id', 58080], ['ood', 3614], ['id', 55054]], 'labels': [6, -1, 2, -1, 8], 'scores': [0.5428549140888168, 1.0440315779494176, 1.458286176430168, 1.8437772935924146, 2.135168894189997]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 4.636130332946777})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 5.894636154174805})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 5.4902801513671875})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 6.116184234619141})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 6.363729476928711})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 6.7534284591674805})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.18757682851874616, 'crossentropy': 5.619871696373694}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 2.9063875675201416})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 3.3913075923919678})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 3.538245677947998})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 3.4540622234344482})
store['active_learning_steps'][27]['eval_training']['best_epoch']=1
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 64358], ['id', 67718], ['id', 14259], ['id', 3048], ['id', 58367]], 'labels': [3, 8, 1, 1, 1], 'scores': [0.6338389794033426, 1.093841924210901, 1.5001572292889032, 1.8643127290752748, 2.192029194846457]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 4.987283706665039})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 5.208912372589111})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 5.819779396057129})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 6.087654113769531})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.749417304992676})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 5.01384162902832})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.6200971603393555})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.878884315490723})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 6.028493881225586})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 6.164421558380127})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 6.319766998291016})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 6.356435775756836})
store['active_learning_steps'][28]['training']['best_epoch']=9
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.21277658266748617, 'crossentropy': 6.2295852220344194}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 3.3250529766082764})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 3.1196999549865723})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.6135220527648926})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.8708767890930176})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.647059440612793})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 3.4358198642730713})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 3.5650477409362793})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 3.579401969909668})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.347454071044922})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 38900], ['ood', 20151], ['id', 4141], ['id', 50773], ['id', 22259]], 'labels': [1, -1, 6, 1, 2], 'scores': [0.5265733031744722, 1.018550772566127, 1.462846172735953, 1.8242746198739859, 2.1592183124063773]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 6.6695098876953125})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 4.945640563964844})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.4338579177856445})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.607634544372559})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.19403042409342347, 'crossentropy': 6.856259243431162}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 3.3047380447387695})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 3.581843852996826})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 3.757591724395752})
store['active_learning_steps'][29]['eval_training']['best_epoch']=1
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 39675], ['ood', 3049], ['id', 17046], ['id', 7728], ['id', 33528]], 'labels': [-1, -1, 9, 8, 9], 'scores': [0.5081717560065506, 0.9448708651724704, 1.339740948169175, 1.6938715930428163, 2.006192178522854]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 6.182085037231445})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 4.672297477722168})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 5.601229667663574})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 6.075445175170898})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.19833282114320835, 'crossentropy': 7.14567647510756}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.836421012878418})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 3.781560182571411})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 4.450936317443848})
store['active_learning_steps'][30]['eval_training']['best_epoch']=3
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 1580], ['id', 29361], ['id', 47329], ['id', 27100], ['id', 30826]], 'labels': [-1, 8, 4, 8, 0], 'scores': [0.6938981516936409, 1.2319362156004812, 1.610330400360823, 1.9468822257944858, 2.2553205285023936]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 5.1449480056762695})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.186415672302246})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 5.678894996643066})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 6.859612464904785})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 5.498993873596191})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 6.077960014343262})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 6.397027015686035})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 6.995612144470215})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 6.518609046936035})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.173828125, 'crossentropy': 6.56233024597168})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 6.5137104988098145})
store['active_learning_steps'][31]['training']['best_epoch']=8
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.2036724031960664, 'crossentropy': 7.612521968154579}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 3.3937902450561523})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 3.387199878692627})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 3.8381786346435547})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 3.7678709030151367})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 3.8285207748413086})
store['active_learning_steps'][31]['eval_training']['best_epoch']=2
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 18166], ['id', 50636], ['id', 41727], ['id', 32833], ['id', 3346]], 'labels': [-1, 4, 8, 1, 8], 'scores': [0.5251372457338916, 1.0193585318490244, 1.4620550393137663, 1.8813790579915368, 2.2108528811366437]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1669921875, 'crossentropy': 4.644764423370361})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 4.919259071350098})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 6.74220609664917})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.46649694442749})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 4.990438461303711})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.325198173522949})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.30140495300293})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 5.645715713500977})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 5.415661811828613})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.1988322065150584, 'crossentropy': 5.008081699927013}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 2.7794761657714844})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 3.054474353790283})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 3.0162315368652344})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 3.2648873329162598})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 3.1927108764648438})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 3.2424392700195312})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.12073016166687})
store['active_learning_steps'][32]['eval_training']['best_epoch']=4
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 47437], ['id', 34015], ['id', 59396], ['id', 48352], ['id', 58256]], 'labels': [-1, 2, 9, 2, 1], 'scores': [0.6039618501035001, 1.0961805584102908, 1.5166646876575645, 1.9089071445345924, 2.222703829499285]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 4.452814102172852})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 4.7305192947387695})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.275397300720215})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.485252380371094})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.8424224853515625})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 5.395016670227051})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.971289157867432})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.897524833679199})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 6.150190353393555})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 6.264035224914551})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.21892286416717885, 'crossentropy': 6.015363302858021}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 2.671633720397949})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.290832042694092})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 3.420152187347412})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 3.5674262046813965})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 3.506556987762451})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.5984249114990234})
store['active_learning_steps'][33]['eval_training']['best_epoch']=3
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 46431], ['id', 47171], ['ood', 9975], ['ood', 13774], ['id', 33928]], 'labels': [-1, 5, -1, -1, 0], 'scores': [0.5242991433892601, 0.997855987426149, 1.4038798773505443, 1.7711241537202733, 2.0937880468712393]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 4.701042175292969})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 5.3531694412231445})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 5.3366312980651855})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 6.668318748474121})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 6.485326766967773})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 6.554880142211914})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 4.952680587768555})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 5.6439313888549805})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.823812484741211})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 6.489051818847656})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.429375171661377})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.195635795593262})
store['active_learning_steps'][34]['training']['best_epoch']=9
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.2080900430239705, 'crossentropy': 5.7195566994468345}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 3.009537696838379})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 3.2083640098571777})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 3.2562570571899414})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.400261878967285})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 3.4185993671417236})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 3.797790765762329})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 3.5050201416015625})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 3.567662000656128})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 3.2724475860595703})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 3.736161231994629})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 3.541940689086914})
store['active_learning_steps'][34]['eval_training']['best_epoch']=8
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 13725], ['id', 34302], ['id', 51376], ['id', 49092], ['id', 59981]], 'labels': [-1, 0, 3, 2, 1], 'scores': [0.6386773903065064, 1.1932951758284744, 1.6469617370488958, 2.030273023857533, 2.374425100515941]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 5.295374870300293})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 5.145462989807129})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 5.111431121826172})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 6.056238651275635})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.936731815338135})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 4.684429168701172})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.654026031494141})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.8069257736206055})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 6.615652084350586})
store['active_learning_steps'][35]['training']['best_epoch']=6
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.19656576521204672, 'crossentropy': 5.046157733750769}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 3.327054500579834})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.208984375, 'crossentropy': 2.6996493339538574})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 3.2104504108428955})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 3.2032501697540283})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.187934398651123})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 3.1467666625976562})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.225694179534912})
store['active_learning_steps'][35]['eval_training']['best_epoch']=4
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 70410], ['id', 20093], ['ood', 44649], ['id', 34013], ['id', 40469]], 'labels': [1, 1, -1, 8, 4], 'scores': [0.4731068411590971, 0.8904749650289198, 1.2505530551754118, 1.5926349249597984, 1.8869142290388035]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 5.242462158203125})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 5.399812698364258})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 6.665501594543457})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.625235080718994})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.539862155914307})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.629189968109131})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 5.679211616516113})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.926440238952637})
store['active_learning_steps'][36]['training']['best_epoch']=5
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.19741087891825446, 'crossentropy': 6.251994540373387}
store['active_learning_steps'][36]['eval_training']={}
store['active_learning_steps'][36]['eval_training']['epochs']=[]
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 3.2429556846618652})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.001793384552002})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 3.580328941345215})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 3.5536108016967773})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 3.728750705718994})
store['active_learning_steps'][36]['eval_training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 3.6054728031158447})
store['active_learning_steps'][36]['eval_training']['best_epoch']=3
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 3109], ['id', 27534], ['id', 45048], ['id', 51167], ['id', 69391]], 'labels': [3, 1, 9, 1, 3], 'scores': [0.49235806973271834, 0.9623932919580651, 1.3606725564844449, 1.7202547090313947, 2.0491178438858904]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 4.571485996246338})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 4.994304180145264})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 4.717071533203125})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 6.802867889404297})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 6.206857681274414})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 5.889667987823486})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 6.048983573913574})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 6.204191207885742})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.191451549530029})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.606372833251953})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 5.5692949295043945})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.792771339416504})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.807673931121826})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.994085311889648})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 6.049483299255371})
store['active_learning_steps'][37]['training']['best_epoch']=12
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.2125845113706208, 'crossentropy': 5.685259968500307}
store['active_learning_steps'][37]['eval_training']={}
store['active_learning_steps'][37]['eval_training']['epochs']=[]
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 2.8905179500579834})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 2.8160128593444824})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 2.907166004180908})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 3.256265640258789})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 3.263261318206787})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 3.227905511856079})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 3.520514965057373})
store['active_learning_steps'][37]['eval_training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 3.308602809906006})
store['active_learning_steps'][37]['eval_training']['best_epoch']=5
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 33853], ['id', 42883], ['id', 37143], ['id', 12083], ['ood', 6504]], 'labels': [1, 2, 1, 0, -1], 'scores': [0.5624315839950399, 1.061716238352598, 1.531641491057703, 1.9371932602421635, 2.295180602883022]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 4.089698314666748})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.440512657165527})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 5.489493370056152})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 5.188472747802734})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 4.937229156494141})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.074339866638184})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.390874862670898})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 5.372023582458496})
store['active_learning_steps'][38]['training']['best_epoch']=5
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.22061309157959436, 'crossentropy': 4.851026501037185}
store['active_learning_steps'][38]['eval_training']={}
store['active_learning_steps'][38]['eval_training']['epochs']=[]
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 4.266277313232422})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 2.917173385620117})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 3.1655526161193848})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 3.0413575172424316})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 3.327800750732422})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 3.156940221786499})
store['active_learning_steps'][38]['eval_training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 3.319699764251709})
store['active_learning_steps'][38]['eval_training']['best_epoch']=5
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 3582], ['id', 59771], ['id', 12916], ['id', 6020], ['id', 60750]], 'labels': [2, 2, 8, 6, 2], 'scores': [0.5714182908641039, 1.0466323864513258, 1.4642204211246583, 1.7838215428517774, 2.0741487311049376]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 4.933505058288574})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.458223819732666})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 5.631251811981201})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.051506042480469})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 5.649385452270508})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.244140625, 'crossentropy': 6.093560695648193})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 6.019045829772949})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 4.371273994445801})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.956418037414551})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2763671875, 'crossentropy': 5.502039909362793})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 5.888866424560547})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 5.612719535827637})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.453256130218506})
store['active_learning_steps'][39]['training']['best_epoch']=10
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.26037185003073143, 'crossentropy': 5.82728828941303}
store['active_learning_steps'][39]['eval_training']={}
store['active_learning_steps'][39]['eval_training']['epochs']=[]
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 2.7429778575897217})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 2.8617377281188965})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 2.971108913421631})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 3.059828281402588})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.287109375, 'crossentropy': 2.9582693576812744})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.2783203125, 'crossentropy': 3.120818614959717})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.26171875, 'crossentropy': 3.0112314224243164})
store['active_learning_steps'][39]['eval_training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 3.025181293487549})
store['active_learning_steps'][39]['eval_training']['best_epoch']=5
store['active_learning_steps'][39]['acquisition']={'indices': [['ood', 22440], ['id', 39945], ['id', 8725], ['id', 7598], ['id', 51965]], 'labels': [-1, 1, 1, 4, 5], 'scores': [0.6004137056077661, 1.1080415606995506, 1.5572620902054242, 1.9430689308983613, 2.2927948380327807]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 3.906705141067505})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 5.155829429626465})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 6.308550834655762})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 5.344353199005127})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 7.518769264221191})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 6.1971964836120605})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 5.631600379943848})
store['active_learning_steps'][40]['training']['best_epoch']=4
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.218500307314075, 'crossentropy': 5.443965600030731}
store['active_learning_steps'][40]['eval_training']={}
store['active_learning_steps'][40]['eval_training']['epochs']=[]
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 3.0229082107543945})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 2.8344004154205322})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 2.8319361209869385})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 2.880082607269287})
store['active_learning_steps'][40]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 3.2054824829101562})
store['active_learning_steps'][40]['eval_training']['best_epoch']=2
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 72137], ['id', 38291], ['id', 50553], ['id', 59987], ['id', 27147]], 'labels': [5, 2, 1, 3, 5], 'scores': [0.6358247582154386, 1.120607667020872, 1.5758486694736167, 1.9862358222651872, 2.318051574112128]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 3.8373281955718994})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 4.237978935241699})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 4.86208438873291})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2626953125, 'crossentropy': 5.311635971069336})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2568359375, 'crossentropy': 5.378265380859375})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.437482833862305})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.24609375, 'crossentropy': 5.717820167541504})
store['active_learning_steps'][41]['training']['best_epoch']=4
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.256299938537185, 'crossentropy': 5.194969172556853}
store['active_learning_steps'][41]['eval_training']={}
store['active_learning_steps'][41]['eval_training']['epochs']=[]
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 3.285565137863159})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 3.16178560256958})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 2.8725318908691406})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 3.0430173873901367})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.265625, 'crossentropy': 3.12229061126709})
store['active_learning_steps'][41]['eval_training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 3.1349198818206787})
store['active_learning_steps'][41]['eval_training']['best_epoch']=4
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 22440], ['ood', 48893], ['id', 43380], ['id', 67735], ['id', 5686]], 'labels': [-1, -1, 1, 4, 1], 'scores': [0.557223699844654, 1.0054275499214147, 1.4260608992690558, 1.8131543941970136, 2.1613077727348893]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 4.338001251220703})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 4.647371292114258})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 5.115485668182373})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 5.238393783569336})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 6.187337875366211})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2412109375, 'crossentropy': 5.14817476272583})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 5.159236431121826})
store['active_learning_steps'][42]['training']['best_epoch']=4
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.22122771972956362, 'crossentropy': 5.324265567378611}
store['active_learning_steps'][42]['eval_training']={}
store['active_learning_steps'][42]['eval_training']['epochs']=[]
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 2.672999858856201})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 2.9606029987335205})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 3.069457769393921})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.248046875, 'crossentropy': 3.047293186187744})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.267578125, 'crossentropy': 3.407278060913086})
store['active_learning_steps'][42]['eval_training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 3.0514564514160156})
store['active_learning_steps'][42]['eval_training']['best_epoch']=5
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 9652], ['id', 13570], ['id', 12370], ['id', 34983], ['id', 70697]], 'labels': [1, 7, 9, 4, 1], 'scores': [0.5629818394707113, 1.0507202947263874, 1.5045772814106853, 1.915982156668088, 2.2622634145472587]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 3.491703987121582})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 4.78014612197876})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 5.912197113037109})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 5.340395927429199})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 5.037421703338623})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 5.8346405029296875})
store['active_learning_steps'][43]['training']['best_epoch']=3
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.2360940381069453, 'crossentropy': 6.259807040373387}
store['active_learning_steps'][43]['eval_training']={}
store['active_learning_steps'][43]['eval_training']['epochs']=[]
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 3.1130261421203613})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 3.2314281463623047})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 3.3337044715881348})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.2802133560180664})
store['active_learning_steps'][43]['eval_training']['epochs'].append({'accuracy': 0.2548828125, 'crossentropy': 3.414778232574463})
store['active_learning_steps'][43]['eval_training']['best_epoch']=3
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 68525], ['ood', 13592], ['id', 20944], ['id', 53072], ['id', 11707]], 'labels': [1, -1, 2, 2, 1], 'scores': [0.584961163958107, 1.0302993019010267, 1.4337703840844842, 1.7812958279535511, 2.077035433068428]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 4.228725433349609})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 4.318628311157227})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.392770290374756})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2509765625, 'crossentropy': 4.379355430603027})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 5.3149943351745605})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 6.064567565917969})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 4.421276569366455})
store['active_learning_steps'][44]['training']['best_epoch']=4
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.23148432698217578, 'crossentropy': 4.3564126003572525}
store['active_learning_steps'][44]['eval_training']={}
store['active_learning_steps'][44]['eval_training']['epochs']=[]
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 2.8136632442474365})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.23046875, 'crossentropy': 2.9400320053100586})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 2.8362903594970703})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 2.920616626739502})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 2.9276390075683594})
store['active_learning_steps'][44]['eval_training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 2.858887195587158})
store['active_learning_steps'][44]['eval_training']['best_epoch']=5
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 24577], ['id', 46013], ['id', 64034], ['id', 35573], ['id', 49950]], 'labels': [3, 1, 4, 1, 4], 'scores': [0.5749924449513508, 1.0087595436830563, 1.3989231252391257, 1.7391521156601364, 2.0524420743663963]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 4.493514060974121})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 5.068603515625})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.681950092315674})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.308355331420898})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 5.310091018676758})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 5.133211612701416})
store['active_learning_steps'][45]['training']['best_epoch']=3
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.23540258143822987, 'crossentropy': 4.71850811021051}
