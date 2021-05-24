store = {}
store['timestamp']=1621608562
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py', '--id=7']
store['commit']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['github_url']='682214513771357d0cdd3c2eb17f027e50839d3c'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/svhn_cifar10_ood_experiment.py'
store['job_id']=7
store['worker_id']=7
store['num_workers']=24
store['config']={'seed': 1241, 'uniform_ood': False, 'id_dataset_name': 'SVHN', 'ood_dataset_name': 'CIFAR-10', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 1024, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 60, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.resnet_models.Cifar10BayesianResnetFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(Augmentation Node) + ('CIFAR-10 (Train, seed=0, 50000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'SVHN (Test)'"}
store['initial_training_set_indices']=[38482, 18819, 58066, 14663, 39799, 53509, 12901, 26100, 61523, 67745, 57808, 69963, 69909, 45371, 37280, 48685, 26877, 52249, 66762, 14073]
store['evaluation_set_indices']=[9356, 52217, 13204, 15153, 14643, 13323, 68768, 23207, 25999, 62719, 62312, 67969, 24256, 39281, 37692, 459, 50826, 51277, 57053, 2584, 51764, 14758, 22887, 43685, 53675, 71612, 55166, 16551, 62820, 4535, 12102, 2976, 62920, 41178, 65425, 24347, 41886, 15904, 4242, 38591, 69801, 8821, 58682, 26825, 58891, 26239, 12097, 25295, 62111, 31755, 35768, 26368, 42500, 34271, 27190, 19058, 51104, 6911, 30075, 67867, 33661, 68699, 33542, 20892, 66108, 65071, 38221, 28545, 4922, 712, 69652, 9859, 30961, 51019, 29978, 24859, 3266, 17700, 8635, 6353, 5221, 42961, 38139, 71930, 52654, 10503, 21854, 36516, 30504, 22436, 45904, 30936, 48527, 39826, 3646, 58802, 10195, 14513, 6465, 6942, 57592, 56379, 26009, 61985, 2559, 12661, 12013, 46596, 22602, 4480, 17051, 33111, 8443, 71520, 63570, 69611, 25877, 35431, 68255, 42429, 25233, 38864, 11350, 35991, 55649, 57177, 7278, 4769, 20349, 2614, 44954, 59941, 37367, 65209, 17027, 19532, 53043, 65575, 20118, 14547, 5357, 36375, 13466, 33485, 25546, 9095, 13754, 12356, 31308, 21474, 7790, 60533, 72158, 29121, 42063, 39774, 8251, 53403, 49392, 11194, 9155, 41513, 66798, 65593, 59814, 15932, 37576, 11589, 53361, 63564, 23612, 39344, 15174, 35048, 32969, 69692, 25106, 48838, 47004, 4184, 853, 45864, 56849, 67982, 15528, 22376, 35245, 45656, 59597, 66590, 54076, 16022, 11813, 65618, 9234, 51953, 9766, 41955, 44395, 39226, 40025, 41050, 18973, 65107, 47464, 33366, 60380, 2486, 33728, 17384, 20252, 502, 5733, 4780, 8085, 20338, 65499, 16532, 46969, 7202, 65103, 41400, 26582, 27643, 8071, 55598, 37396, 44808, 26291, 28417, 36402, 28726, 22517, 69815, 36383, 23607, 23033, 27971, 2408, 2278, 41478, 44310, 22574, 36584, 20402, 39412, 4629, 15386, 62095, 71458, 33017, 16110, 17249, 12926, 3490, 47863, 57175, 70171, 64841, 69552, 16738, 53687, 49215, 68777, 42356, 44008, 58581, 4015, 25552, 6585, 63976, 21856, 22022, 55859, 646, 40666, 20229, 54017, 19316, 47715, 63714, 56139, 20095, 56198, 49498, 71125, 37745, 28370, 447, 16265, 16217, 31553, 42330, 39800, 4708, 41610, 26365, 29555, 39014, 12058, 57716, 30264, 19834, 44802, 28557, 41674, 58223, 69197, 20831, 68939, 58071, 61613, 908, 66783, 49048, 8901, 8366, 43877, 27035, 5594, 16712, 65988, 44267, 68598, 18916, 55473, 13995, 8035, 35402, 49125, 1977, 30455, 18722, 28193, 13172, 50182, 7501, 13256, 30190, 3792, 2123, 1945, 578, 46527, 39552, 67117, 42833, 5445, 46094, 33919, 17401, 32440, 65698, 21803, 1135, 10541, 46967, 10104, 10938, 63683, 40034, 50634, 69388, 36184, 19463, 34004, 28951, 14855, 64729, 14756, 22150, 21459, 17111, 16346, 43426, 67098, 33904, 31401, 7659, 48749, 63155, 2295, 10885, 35729, 19327, 37233, 62037, 43673, 32598, 17664, 54682, 26311, 47139, 39399, 39716, 12071, 64933, 24857, 5906, 55259, 19820, 50768, 64273, 5453, 68989, 5148, 32502, 26332, 21086, 2537, 56917, 2572, 33746, 12667, 67185, 22625, 22488, 46950, 11323, 7732, 4099, 66265, 45874, 44873, 50645, 54736, 27587, 37633, 20063, 1608, 10391, 69839, 40026, 23753, 16692, 70616, 33037, 36107, 60644, 10024, 70725, 42517, 59766, 63776, 5240, 4298, 48682, 2647, 31850, 35911, 50647, 29464, 44634, 59672, 65002, 63792, 17766, 62198, 24020, 42922, 58463, 65717, 23905, 3709, 24462, 16997, 57309, 37223, 66400, 62492, 47056, 40814, 21985, 72066, 40550, 18131, 28968, 4841, 27091, 18456, 30336, 57899, 48912, 37103, 49194, 47247, 54365, 28077, 55585, 49073, 62608, 17950, 33176, 69058, 59000, 33429, 19825, 69851, 24553, 14100, 52015, 34854, 8384, 22221, 35886, 67782, 48319, 56320, 19629, 42327, 58156, 24662, 57555, 36936, 69589, 3895, 49861, 58546, 37408, 20865, 9547, 2308, 60654, 64334, 29058, 57610, 3713, 22067, 67083, 55907, 60300, 36206, 2137, 31864, 59454, 62125, 3472, 61684, 53364, 19002, 5961, 5119, 54575, 21647, 10117, 2063, 45076, 7655, 17649, 16183, 34516, 22281, 64009, 1482, 45897, 16054, 26453, 54529, 22123, 51161, 56473, 51275, 58255, 30056, 58472, 25031, 45022, 19772, 18227, 61247, 64229, 33494, 42705, 32892, 7643, 6554, 38114, 71630, 50256, 48460, 12647, 41199, 26273, 45698, 52378, 67419, 39957, 34025, 21810, 36037, 46937, 32002, 68859, 22312, 38228, 49463, 32134, 43593, 12976, 48518, 29540, 49660, 65445, 20048, 50377, 55745, 48666, 34187, 14797, 1090, 9866, 49432, 16623, 66209, 29260, 52431, 20003, 17847, 51378, 16023, 68062, 44305, 16631, 27731, 24784, 39156, 11115, 28872, 68835, 23709, 69182, 55249, 51867, 58062, 15447, 54267, 22358, 11689, 32422, 17668, 70285, 14630, 66794, 3930, 48981, 53416, 52758, 259, 46199, 29534, 64541, 17082, 44746, 25437, 49288, 43065, 30764, 38017, 51276, 30890, 65349, 52566, 50133, 43793, 30313, 16596, 24263, 5825, 59782, 46247, 12714, 31550, 66659, 56183, 15363, 28327, 17799, 7985, 57408, 63114, 5656, 45109, 8170, 71088, 44865, 5179, 33238, 67850, 59037, 70356, 57561, 5224, 54748, 48857, 57920, 64313, 61094, 24227, 27540, 48418, 49627, 5977, 47424, 49350, 2294, 51114, 31731, 68660, 48657, 47982, 5572, 67954, 72131, 38419, 5584, 43252, 9618, 23545, 33898, 68204, 52186, 24178, 19915, 6776, 31485, 32593, 19584, 19419, 27692, 8249, 34767, 43187, 21199, 9445, 58948, 11805, 31566, 23275, 48477, 70581, 468, 60975, 35599, 51011, 23731, 62929, 52127, 43105, 47132, 37098, 36682, 66718, 11836, 18937, 8353, 39475, 25066, 3810, 42035, 61047, 31409, 53353, 43799, 66218, 33732, 13353, 60944, 44114, 63746, 58818, 58308, 71199, 34872, 33651, 31320, 10155, 22562, 26256, 588, 650, 11367, 32284, 59309, 47102, 12778, 23277, 11903, 57880, 27145, 31297, 29703, 71945, 51586, 46004, 3819, 11022, 9807, 13278, 4765, 14868, 45323, 64881, 49532, 21786, 27694, 4261, 4225, 19091, 72034, 55698, 45428, 10685, 53402, 56253, 46547, 71757, 51782, 51907, 35547, 4933, 17159, 55552, 42654, 15891, 18290, 60649, 12688, 14180, 27824, 31768, 58640, 10644, 65690, 49127, 6096, 11685, 19904, 65825, 9756, 69122, 22560, 15354, 7212, 69075, 32862, 40238, 51753, 2289, 15439, 32940, 48616, 33630, 61582, 59003, 31277, 69455, 15225, 6524, 12255, 35631, 19799, 939, 19052, 51599, 33349, 15648, 53478, 48461, 57688, 16560, 29049, 42225, 52412, 16140, 40390, 32570, 24745, 64558, 36783, 6915, 47728, 965, 11449, 5116, 5323, 60583, 65003, 49946, 14668, 41788, 22684, 41248, 57017, 35386, 56663, 11333, 6235, 14545, 57849, 48023, 18451, 52781, 55872, 12166, 65210, 42135, 45704, 22159, 13433, 43848, 57952, 67211, 13469, 11047, 5020, 42097, 20945, 63525, 38029, 4448, 12645, 67581, 29111, 8657, 67780, 64513, 18251, 17888, 32040, 59868, 23404, 9423, 1799, 42360, 38722, 2521, 70901, 20614, 58004, 61052, 52510, 1767, 18118, 63984, 8997, 7359, 57822, 51575, 1154, 20732, 22093, 36091, 65675, 30482, 18517, 58191, 41454, 56022, 42315, 16818, 29430, 51625, 52715, 19267, 60460, 50887, 71829, 53823, 20360, 60961, 45356, 39961, 39474, 66779, 32959, 45573, 36984, 2876, 30770, 34908, 12101, 10839, 42028, 42187, 29776, 30785, 65134, 31096, 13346, 32978, 29254, 50953, 33172, 13798, 22658, 32286, 20308, 15277, 9517, 18525, 14838, 14280, 35505, 71679, 35497, 51264, 15149, 15077, 19660, 2980, 11973, 61547, 51033, 60741, 11385, 19913, 68557, 23524, 68591, 9114]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.11328125, 'crossentropy': 11.731828689575195})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.12109375, 'crossentropy': 10.411102294921875})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.11328125, 'crossentropy': 10.842066764831543})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.107421875, 'crossentropy': 10.257452011108398})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.1103515625, 'crossentropy': 9.9376802444458})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.10233558696988322, 'crossentropy': 11.32116481637984}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 54405], ['id', 48643], ['id', 61884], ['ood', 12073], ['ood', 19062]], 'labels': [0, 1, 8, -1, -1], 'scores': [0.6623382864512686, 1.2717654409566994, 1.8364152893358634, 2.3201594644154255, 2.735520725053446]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1103515625, 'crossentropy': 16.67017364501953})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 11.955427169799805})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.0849609375, 'crossentropy': 11.642656326293945})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.1259765625, 'crossentropy': 9.64607048034668})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 9.880094528198242})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 10.139774322509766})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 11.712675094604492})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.130859375, 'crossentropy': 12.092966079711914})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.123046875, 'crossentropy': 12.682746887207031})
store['active_learning_steps'][1]['training']['best_epoch']=6
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.1183159188690842, 'crossentropy': 11.033096285341118}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 13223], ['id', 0], ['id', 1], ['id', 2], ['id', 3]], 'labels': [-1, 2, 3, 0, 6], 'scores': [nan, nan, nan, nan, nan]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.115234375, 'crossentropy': 7.375242233276367})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.095703125, 'crossentropy': 8.85962200164795})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.1142578125, 'crossentropy': 8.043074607849121})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.109375, 'crossentropy': 9.45634651184082})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.10049170251997541, 'crossentropy': 7.022659011024892}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 63807], ['id', 43380], ['id', 29914], ['ood', 16219], ['id', 37718]], 'labels': [1, 1, 2, -1, 2], 'scores': [0.7201908182411936, 1.2839077934528556, 1.7898863644475833, 2.2388538017359334, 2.6265598102093186]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.109375, 'crossentropy': 11.343305587768555})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1015625, 'crossentropy': 8.444994926452637})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1044921875, 'crossentropy': 8.545036315917969})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 8.152770042419434})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.109375, 'crossentropy': 8.402154922485352})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.1083984375, 'crossentropy': 8.022197723388672})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.107421875, 'crossentropy': 8.156494140625})
store['active_learning_steps'][3]['training']['best_epoch']=4
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.11862323294406883, 'crossentropy': 8.373042073217578}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 55029], ['id', 69798], ['id', 56981], ['id', 17652], ['ood', 36955]], 'labels': [6, 1, 0, 1, -1], 'scores': [0.7893898868297806, 1.3931303103923618, 1.934302195511651, 2.4213154283433607, 2.853576214845254]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.125, 'crossentropy': 8.514034271240234})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 9.92602825164795})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 7.353982925415039})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 7.052395820617676})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 7.3430352210998535})
store['active_learning_steps'][4]['training']['best_epoch']=2
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.12031346035648433, 'crossentropy': 11.016119583589429}
store['active_learning_steps'][4]['acquisition']={'indices': [['ood', 7243], ['ood', 45076], ['id', 70107], ['id', 43953], ['id', 33703]], 'labels': [-1, -1, 5, 8, 1], 'scores': [0.6887906165489041, 1.289758516700418, 1.822734269467151, 2.2757243124915245, 2.6709323549669612]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.11328125, 'crossentropy': 7.005560874938965})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.140625, 'crossentropy': 7.59221887588501})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 8.365352630615234})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 8.424236297607422})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 8.925480842590332})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.12890625, 'crossentropy': 9.10521125793457})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 8.915040969848633})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.12119698832206514, 'crossentropy': 9.095183932275662}
store['active_learning_steps'][5]['acquisition']={'indices': [['ood', 34862], ['id', 39563], ['id', 56170], ['id', 71193], ['id', 62829]], 'labels': [-1, 9, 1, 8, 1], 'scores': [0.626524014108961, 1.2387175181852341, 1.7674576794938952, 2.2089441620866426, 2.601240012559021]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1181640625, 'crossentropy': 7.484922409057617})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 6.420998573303223})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 8.330577850341797})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1201171875, 'crossentropy': 9.102949142456055})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 7.924490928649902})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.1240234375, 'crossentropy': 7.097753524780273})
store['active_learning_steps'][6]['training']['best_epoch']=3
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.1372157344806392, 'crossentropy': 8.414283381991396}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 19594], ['id', 5208], ['id', 11569], ['id', 30048], ['ood', 36737]], 'labels': [5, 3, 6, 5, -1], 'scores': [0.8649179816235684, 1.5923698220151237, 2.1170710668625468, 2.5769062642676204, 2.958304703269768]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 6.256446838378906})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.14453125, 'crossentropy': 7.096855163574219})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 6.898638725280762})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 7.584360122680664})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.138671875, 'crossentropy': 6.329391956329346})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.150390625, 'crossentropy': 6.872343063354492})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 6.9944257736206055})
store['active_learning_steps'][7]['training']['best_epoch']=4
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.16180086047940995, 'crossentropy': 7.385165373386601}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 23259], ['id', 19244], ['ood', 10790], ['id', 40145], ['ood', 40193]], 'labels': [3, 4, -1, 9, -1], 'scores': [0.6459779456022163, 1.2265222806850433, 1.7569143482279954, 2.2160899039840425, 2.6409196820124077]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1474609375, 'crossentropy': 7.37709903717041})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1220703125, 'crossentropy': 7.374049186706543})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 6.510402202606201})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1591796875, 'crossentropy': 6.195859909057617})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 6.687504768371582})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 6.590047836303711})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 6.727083683013916})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.13053165334972341, 'crossentropy': 5.857107358251383}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 53879], ['id', 31614], ['id', 61217], ['id', 54399], ['ood', 8847]], 'labels': [0, 5, 1, 9, -1], 'scores': [0.7177244809253096, 1.2614641561286364, 1.7458818572276202, 2.1974947895028922, 2.5942759370455786]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 6.799699783325195})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.10546875, 'crossentropy': 6.870450973510742})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1005859375, 'crossentropy': 9.431798934936523})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1455078125, 'crossentropy': 5.9747724533081055})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1162109375, 'crossentropy': 5.895111083984375})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.1376953125, 'crossentropy': 7.132857322692871})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.134765625, 'crossentropy': 7.096376419067383})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.11793177627535341, 'crossentropy': 7.201405361670252}
store['active_learning_steps'][9]['acquisition']={'indices': [['ood', 32131], ['id', 59015], ['id', 17418], ['id', 4976], ['id', 25953]], 'labels': [-1, 5, 0, 5, 7], 'scores': [0.5525422999885392, 1.0783558497928047, 1.571397619017299, 2.0147321471034805, 2.415097124147829]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 7.100826740264893})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 6.1317901611328125})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 6.081910133361816})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.1328125, 'crossentropy': 6.7917070388793945})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.12473110018438845, 'crossentropy': 7.562443579056546}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 19557], ['id', 58408], ['id', 22191], ['id', 45510], ['id', 56202]], 'labels': [1, 1, 0, 1, 1], 'scores': [0.7356598234239096, 1.3986431865865487, 1.9989419870997285, 2.4461277188014634, 2.8419794992504377]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 6.595337867736816})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1689453125, 'crossentropy': 5.012119770050049})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 6.461213111877441})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 6.352339744567871})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 8.357158660888672})
store['active_learning_steps'][11]['training']['best_epoch']=2
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.14270897357098955, 'crossentropy': 5.262422211124769}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 43508], ['id', 25397], ['id', 58433], ['id', 32087], ['id', 54745]], 'labels': [-1, 0, 1, 3, 9], 'scores': [0.5541433912889622, 1.0384012811094356, 1.4637579974088748, 1.861241233670465, 2.203759151390879]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1416015625, 'crossentropy': 5.494978904724121})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.13671875, 'crossentropy': 6.714199066162109})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 6.42659854888916})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 6.105165958404541})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1533203125, 'crossentropy': 6.144580841064453})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.1494140625, 'crossentropy': 6.783684730529785})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.14332360172095882, 'crossentropy': 6.675705021704056}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 40154], ['id', 34140], ['id', 21026], ['ood', 5904], ['id', 61317]], 'labels': [-1, 5, 0, -1, 8], 'scores': [0.8136054156635621, 1.3785116344567925, 1.9031818264917049, 2.3728648103762993, 2.7795400357882336]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 5.325611114501953})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1337890625, 'crossentropy': 6.6984124183654785})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1484375, 'crossentropy': 5.600697994232178})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 6.020954608917236})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1357421875, 'crossentropy': 6.110212802886963})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.1396484375, 'crossentropy': 6.011210918426514})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.13210663798401967, 'crossentropy': 6.085694409764905}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 34990], ['id', 6529], ['id', 49292], ['id', 57334], ['id', 13615]], 'labels': [1, 1, 1, 5, 1], 'scores': [0.6174385136793266, 1.1806340723253257, 1.7028584261381026, 2.127061380236869, 2.5024324877497754]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.16015625, 'crossentropy': 6.89352560043335})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.15234375, 'crossentropy': 5.24068546295166})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1767578125, 'crossentropy': 5.969674110412598})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1630859375, 'crossentropy': 6.090522766113281})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.162109375, 'crossentropy': 6.656010150909424})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.1728515625, 'crossentropy': 6.034296989440918})
store['active_learning_steps'][14]['training']['best_epoch']=3
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.15884296250768284, 'crossentropy': 5.826129859403811}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 51669], ['ood', 20923], ['id', 63126], ['id', 35437], ['id', 68704]], 'labels': [6, -1, 1, 3, 6], 'scores': [0.525452337970937, 1.0358993289934983, 1.4609392531892937, 1.8544086404479057, 2.2221890726680256]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 5.511144638061523})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 5.513147354125977})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.755600929260254})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 6.202726364135742})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 4.716914176940918})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.914376258850098})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 5.910714626312256})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 6.387876510620117})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 5.8235578536987305})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.169921875, 'crossentropy': 5.969809055328369})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 5.408524513244629})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 5.741811752319336})
store['active_learning_steps'][15]['training']['best_epoch']=9
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.16602642901044867, 'crossentropy': 6.698364632951752}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 46733], ['id', 61522], ['id', 32595], ['id', 4549], ['id', 52401]], 'labels': [1, 6, 4, 3, 1], 'scores': [0.8194780568416664, 1.5837298107115334, 2.2029898645442696, 2.713523882966859, 3.138548577758984]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 5.432772636413574})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 5.429716110229492})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 5.395720481872559})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 5.8332319259643555})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.297854900360107})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.17113552550706823, 'crossentropy': 5.503193185310387}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 43381], ['id', 67223], ['id', 13542], ['id', 12750], ['ood', 25189]], 'labels': [0, 1, 5, 1, -1], 'scores': [0.7155949978838854, 1.3109716097652493, 1.8081556249420947, 2.2271356969188165, 2.600983254317404]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.1611328125, 'crossentropy': 5.506324768066406})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.674283981323242})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 6.3657355308532715})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 6.200762748718262})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.166015625, 'crossentropy': 6.212035179138184})
store['active_learning_steps'][17]['training']['best_epoch']=2
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.16948371235402582, 'crossentropy': 5.785981556353718}
store['active_learning_steps'][17]['acquisition']={'indices': [['ood', 4169], ['id', 1283], ['id', 61235], ['id', 64490], ['id', 25127]], 'labels': [-1, 5, 5, 3, 8], 'scores': [0.7232713530647008, 1.3712978438264125, 1.8942243401361551, 2.361926780134688, 2.764795663935022]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 6.400997638702393})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1748046875, 'crossentropy': 6.091499328613281})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 5.851868629455566})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 5.134018898010254})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 7.063206672668457})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 6.168034076690674})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 5.299933433532715})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.18131530424093423, 'crossentropy': 5.454501310886601}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 66365], ['id', 36740], ['id', 48033], ['id', 41809], ['id', 56140]], 'labels': [3, 1, 5, 5, 4], 'scores': [0.6920102589724744, 1.2993053932566747, 1.827603284428422, 2.2788590012815204, 2.6702454911249447]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 6.654269218444824})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 5.901607036590576})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 7.1425323486328125})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 5.640738487243652})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.602501392364502})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.680243492126465})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.925585746765137})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.934380531311035})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 6.146606922149658})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 6.259550094604492})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 6.114429473876953})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 6.338813304901123})
store['active_learning_steps'][19]['training']['best_epoch']=9
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.19783343577135834, 'crossentropy': 6.143794776621082}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 42815], ['id', 69044], ['id', 31969], ['id', 69804], ['id', 49563]], 'labels': [3, 9, 1, 4, 1], 'scores': [0.6914962963081059, 1.2510184144512135, 1.7777654713076467, 2.235496654542896, 2.650498142578795]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1650390625, 'crossentropy': 5.651718616485596})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 5.852935791015625})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 6.01766300201416})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.267297744750977})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.19140625, 'crossentropy': 5.774527072906494})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.203125, 'crossentropy': 6.070638179779053})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.1943377381684081, 'crossentropy': 6.2621305028426555}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 7635], ['id', 41338], ['id', 40701], ['ood', 11835], ['ood', 46833]], 'labels': [-1, 9, 3, -1, -1], 'scores': [0.757643731699778, 1.3428953388763913, 1.8855258057722053, 2.351181653066835, 2.749658860446477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.223841667175293})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 5.317968845367432})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 6.403692722320557})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 6.462090492248535})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.366497039794922})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 6.584782600402832})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.9571428298950195})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 6.359000205993652})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 6.441428184509277})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 8.363344192504883})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 6.3214826583862305})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 7.895612716674805})
store['active_learning_steps'][21]['training']['best_epoch']=9
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.1954517516902274, 'crossentropy': 7.084430940765212}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 17731], ['id', 34132], ['id', 32174], ['id', 22011], ['id', 48574]], 'labels': [3, 8, 7, 5, 1], 'scores': [0.7957533176132028, 1.3762620763835685, 1.9097112283774451, 2.404414907164689, 2.7894073819716834]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.154296875, 'crossentropy': 5.300992965698242})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 5.465775012969971})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 6.169670581817627})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.119389533996582})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 6.391172409057617})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.792450428009033})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 6.760632038116455})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 6.662163734436035})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2041015625, 'crossentropy': 5.7495198249816895})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 5.592742443084717})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 5.702794075012207})
store['active_learning_steps'][22]['training']['best_epoch']=8
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.21077904118008606, 'crossentropy': 6.9554784736094035}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 33369], ['id', 42645], ['id', 26301], ['ood', 7847], ['id', 70505]], 'labels': [0, 1, 8, -1, 8], 'scores': [0.5788393428314151, 1.1352359925411064, 1.6229854582100032, 2.0795628524690786, 2.4897501427431514]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 6.030436038970947})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 6.365147113800049})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1640625, 'crossentropy': 7.155266761779785})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.813313007354736})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 5.470194339752197})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.240415573120117})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.430657863616943})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 5.531852722167969})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.93425178527832})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 6.125049591064453})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 6.070415019989014})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 6.096635818481445})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 6.165307998657227})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.216796875, 'crossentropy': 6.148935317993164})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.228515625, 'crossentropy': 6.162415504455566})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 6.526365280151367})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 6.262692928314209})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 6.5524492263793945})
store['active_learning_steps'][23]['training']['best_epoch']=15
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.1878841425937308, 'crossentropy': 6.371595536263061}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 42283], ['id', 23562], ['id', 45099], ['ood', 31906], ['id', 61948]], 'labels': [5, 1, 6, -1, 6], 'scores': [0.6907414648286507, 1.3517875966950101, 1.9200453207949018, 2.4117144472546084, 2.837236823034525]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.922183990478516})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 4.711333751678467})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 6.15074348449707})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 7.545506000518799})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.298275470733643})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2431640625, 'crossentropy': 5.266921043395996})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.620865345001221})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.794366359710693})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 5.840880393981934})
store['active_learning_steps'][24]['training']['best_epoch']=6
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.20793638598647818, 'crossentropy': 5.733836600145974}
store['active_learning_steps'][24]['acquisition']={'indices': [['ood', 20841], ['id', 51621], ['id', 14920], ['id', 64200], ['id', 2224]], 'labels': [-1, 3, 9, 3, 1], 'scores': [0.6234855317447687, 1.1841178652533646, 1.6800079672747037, 2.13081872418374, 2.53508987145002]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.15625, 'crossentropy': 9.640030860900879})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 6.413064956665039})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1826171875, 'crossentropy': 5.353043079376221})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.934043884277344})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.19921875, 'crossentropy': 6.095577239990234})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 6.007896423339844})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 7.682378768920898})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 5.568143844604492})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 5.2544755935668945})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.21004917025199754, 'crossentropy': 6.179158103488015}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 53849], ['id', 26643], ['id', 42281], ['id', 58126], ['id', 29668]], 'labels': [4, 7, 2, 9, 5], 'scores': [0.6719212596189068, 1.2903005454991243, 1.8054833275104496, 2.272111474193487, 2.6728700905513243]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.16796875, 'crossentropy': 6.5369181632995605})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 4.759936332702637})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.841625213623047})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 4.910773277282715})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.554479122161865})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.946885108947754})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.1787109375, 'crossentropy': 6.385219573974609})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.19145666871542716, 'crossentropy': 4.945958939958513}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 13223], ['ood', 592], ['id', 42414], ['id', 21041], ['id', 64286]], 'labels': [-1, -1, 8, 0, 5], 'scores': [0.5642890178188771, 1.084723401534742, 1.5390222926896069, 1.9567262092180941, 2.3200181483671063]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.255349636077881})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 6.496972560882568})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.1865234375, 'crossentropy': 6.252120494842529})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 5.208681106567383})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 5.4565606117248535})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 6.059720993041992})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 7.952537536621094})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.808045387268066})
store['active_learning_steps'][27]['training']['best_epoch']=5
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.18976644130301168, 'crossentropy': 5.75326041026429}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 12017], ['id', 22386], ['id', 56651], ['id', 13436], ['id', 69316]], 'labels': [1, 8, 8, 9, 3], 'scores': [0.5705287150470808, 1.0874793989340663, 1.567372035723892, 1.9939063468776332, 2.391699874170431]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.158203125, 'crossentropy': 5.313621997833252})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 4.994349479675293})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 4.969386100769043})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.146295547485352})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 5.71203088760376})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.782464027404785})
store['active_learning_steps'][28]['training']['best_epoch']=3
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.18968961278426552, 'crossentropy': 5.134160600414874}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 71531], ['id', 27187], ['id', 3604], ['id', 11097], ['id', 67103]], 'labels': [1, 0, 9, 2, 1], 'scores': [0.5578898832298562, 1.0369826957228088, 1.479799725306548, 1.902693305966908, 2.285035981038366]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.1884765625, 'crossentropy': 5.130023002624512})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 5.6429829597473145})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 4.813564300537109})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.240234375, 'crossentropy': 5.2964372634887695})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 5.12747049331665})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 6.075436592102051})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.394660472869873})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.20805162876459743, 'crossentropy': 5.889792490972649}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 44096], ['id', 5270], ['ood', 42666], ['id', 8108], ['id', 19159]], 'labels': [-1, 9, -1, 7, 1], 'scores': [0.6062500660976848, 1.1778539561610026, 1.666010522055747, 2.1126589062173915, 2.530162879510539]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 4.256551742553711})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 6.202519416809082})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 5.567217826843262})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.0089545249938965})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 4.838541030883789})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.1904296875, 'crossentropy': 5.0829877853393555})
store['active_learning_steps'][30]['training']['best_epoch']=3
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.1988322065150584, 'crossentropy': 5.670251397318685}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 68326], ['id', 38807], ['ood', 21257], ['id', 32839], ['ood', 33448]], 'labels': [4, 8, -1, 5, -1], 'scores': [0.6101969768328703, 1.1515059082507264, 1.6487355516596813, 2.0494435098251857, 2.417032185570818]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 6.677192211151123})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 6.078516483306885})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.560183525085449})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2275390625, 'crossentropy': 5.593406677246094})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 6.286561012268066})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 5.3028411865234375})
store['active_learning_steps'][31]['training']['best_epoch']=3
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.20013829133374308, 'crossentropy': 4.6045522097802705}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 24566], ['id', 54970], ['id', 34506], ['id', 29283], ['ood', 40813]], 'labels': [8, 8, 0, 5, -1], 'scores': [0.5079913623715013, 0.9853606091852432, 1.4051463757696938, 1.7935115781739883, 2.1564804676681923]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.123838901519775})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 5.194346904754639})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 4.4234771728515625})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 4.8850998878479})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.19598955132145052, 'crossentropy': 4.936095478641672}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 33088], ['id', 26655], ['id', 31163], ['id', 12866], ['id', 57637]], 'labels': [0, 5, 1, 2, 4], 'scores': [0.5168379984858542, 0.9882569789669597, 1.4217844050222266, 1.7978082237153217, 2.1195425627071813]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.232421875, 'crossentropy': 4.014388084411621})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 5.881158828735352})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 5.768245697021484})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 5.643719673156738})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.434541702270508})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2666015625, 'crossentropy': 5.962392807006836})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 4.937727451324463})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 4.9795708656311035})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 4.962153434753418})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.25, 'crossentropy': 5.358423233032227})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.24343116164720344, 'crossentropy': 5.163749183696988}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 35938], ['id', 59164], ['id', 54772], ['ood', 25428], ['ood', 27180]], 'labels': [-1, 1, 6, -1, -1], 'scores': [0.6733862071058676, 1.266298178547813, 1.784090645275573, 2.2407985456077553, 2.652149816038456]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 4.842757701873779})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.189453125, 'crossentropy': 5.024340629577637})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2236328125, 'crossentropy': 5.547271728515625})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.20703125, 'crossentropy': 5.426495552062988})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 6.492295265197754})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.098926067352295})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2294921875, 'crossentropy': 6.157971382141113})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 6.058441162109375})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.2265625, 'crossentropy': 5.477510929107666})
store['active_learning_steps'][34]['training']['best_epoch']=6
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.217539950829748, 'crossentropy': 5.355798272318685}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 8627], ['ood', 7792], ['id', 41792], ['id', 5857], ['id', 66630]], 'labels': [-1, -1, 8, 5, 5], 'scores': [0.7441025732999642, 1.3659111868781872, 1.9431277699995881, 2.40152835722645, 2.808478576125488]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.1435546875, 'crossentropy': 5.148258209228516})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.17578125, 'crossentropy': 5.239428520202637})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 4.849434852600098})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.1923828125, 'crossentropy': 6.008610725402832})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.368377685546875})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 6.114821434020996})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2197265625, 'crossentropy': 4.795618057250977})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 5.086099624633789})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.2333984375, 'crossentropy': 5.282923221588135})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.23828125, 'crossentropy': 5.329983711242676})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 7.07356071472168})
store['active_learning_steps'][35]['training']['best_epoch']=8
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.22337891825445605, 'crossentropy': 5.4037320653426555}
store['active_learning_steps'][35]['acquisition']={'indices': [['ood', 1853], ['id', 50051], ['ood', 13436], ['id', 12676], ['id', 65987]], 'labels': [-1, 5, -1, 6, 5], 'scores': [0.8054296778453796, 1.4612061712563231, 2.053422873155222, 2.5198000229400357, 2.90925891319049]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.1708984375, 'crossentropy': 5.218175888061523})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 4.622734069824219})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 4.320390224456787})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.292587757110596})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.6046905517578125})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.2940826416015625})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.1962890625, 'crossentropy': 5.035344123840332})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.18588660110633068, 'crossentropy': 5.541072646166257}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 14054], ['id', 67318], ['id', 1051], ['id', 52244], ['id', 28271]], 'labels': [0, 7, 5, 2, 8], 'scores': [0.5938291909722837, 1.1744259561647206, 1.618130836474947, 2.02470544135587, 2.3906176676886455]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.1796875, 'crossentropy': 4.492889881134033})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.1982421875, 'crossentropy': 5.003070831298828})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.207942008972168})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.1806640625, 'crossentropy': 6.084160327911377})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 5.3090972900390625})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2109375, 'crossentropy': 5.874220848083496})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 6.5184526443481445})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 5.527069091796875})
store['active_learning_steps'][37]['training']['best_epoch']=5
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.1928779963122311, 'crossentropy': 5.666160278695452}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 69655], ['id', 61245], ['id', 23739], ['id', 23747], ['id', 51944]], 'labels': [4, 6, 3, 9, 3], 'scores': [0.5536433365910258, 1.0600351220082365, 1.5156964271337552, 1.93868488354033, 2.3312019340053993]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.1875, 'crossentropy': 4.342292785644531})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.177734375, 'crossentropy': 5.8029069900512695})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 5.149591445922852})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2021484375, 'crossentropy': 5.112097263336182})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2060546875, 'crossentropy': 5.006875038146973})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.152420997619629})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2373046875, 'crossentropy': 5.369585990905762})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.22265625, 'crossentropy': 5.305276870727539})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2158203125, 'crossentropy': 6.0452423095703125})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.2001953125, 'crossentropy': 6.078106880187988})
store['active_learning_steps'][38]['training']['best_epoch']=7
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.19080362630608483, 'crossentropy': 5.712890024777197}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 6239], ['ood', 27405], ['id', 32716], ['id', 5510], ['id', 34882]], 'labels': [9, -1, 0, 1, 2], 'scores': [0.58475937174319, 1.1420067126636377, 1.621083366636272, 2.042187265964138, 2.4341617563775717]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2138671875, 'crossentropy': 4.162352561950684})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.193359375, 'crossentropy': 5.0766096115112305})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.087471008300781})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.1953125, 'crossentropy': 6.7119598388671875})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.2177734375, 'crossentropy': 6.413972854614258})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.711123466491699})
store['active_learning_steps'][39]['training']['best_epoch']=3
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.18945912722802705, 'crossentropy': 5.075150295789797}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 69677], ['id', 6782], ['id', 13197], ['id', 72150], ['id', 39741]], 'labels': [0, 1, 1, 6, 6], 'scores': [0.5741579114058499, 1.0674057245880428, 1.52082659578328, 1.9253850839694788, 2.3031524387378166]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 4.644885063171387})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2099609375, 'crossentropy': 4.668780326843262})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.236328125, 'crossentropy': 3.897554874420166})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 4.309432506561279})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.28515625, 'crossentropy': 4.336212158203125})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2880859375, 'crossentropy': 4.444439888000488})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2890625, 'crossentropy': 4.76029109954834})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 5.628230094909668})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 4.636929512023926})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.3232421875, 'crossentropy': 4.067158222198486})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 5.220284461975098})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.3349609375, 'crossentropy': 4.4534912109375})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.330078125, 'crossentropy': 4.594169616699219})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.3408203125, 'crossentropy': 4.59683895111084})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.314453125, 'crossentropy': 4.842187404632568})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.333984375, 'crossentropy': 3.903930187225342})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.337890625, 'crossentropy': 3.9235787391662598})
store['active_learning_steps'][40]['training']['best_epoch']=14
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.3045098340503995, 'crossentropy': 4.840598230063}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 14093], ['ood', 17922], ['id', 12651], ['ood', 13305], ['id', 48322]], 'labels': [6, -1, 1, -1, 6], 'scores': [0.6810090884144737, 1.3426144730730347, 1.9425409402794114, 2.452625276597457, 2.901430667843111]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.185546875, 'crossentropy': 3.468879222869873})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 4.870840072631836})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2353515625, 'crossentropy': 5.526275634765625})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 5.9127583503723145})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 5.793699741363525})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2470703125, 'crossentropy': 6.655219078063965})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 5.561104774475098})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 7.594664573669434})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2529296875, 'crossentropy': 6.08465576171875})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.2421875, 'crossentropy': 6.059858322143555})
store['active_learning_steps'][41]['training']['best_epoch']=7
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.22710510141364473, 'crossentropy': 5.8974003149969265}
store['active_learning_steps'][41]['acquisition']={'indices': [['ood', 4636], ['ood', 48061], ['id', 47824], ['id', 61076], ['id', 13575]], 'labels': [-1, -1, 1, 2, 8], 'scores': [0.7951707412615514, 1.4565807899321497, 2.0577675541108458, 2.4940472537191027, 2.8890856804208918]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.201171875, 'crossentropy': 4.966287612915039})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.171875, 'crossentropy': 5.197530269622803})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 4.9914937019348145})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 5.032896041870117})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.1845703125, 'crossentropy': 6.565802574157715})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.220703125, 'crossentropy': 5.388096332550049})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.2451171875, 'crossentropy': 5.149473190307617})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.205078125, 'crossentropy': 5.118359565734863})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.21875, 'crossentropy': 5.5476226806640625})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.212890625, 'crossentropy': 5.379746437072754})
store['active_learning_steps'][42]['training']['best_epoch']=7
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.18838352796558083, 'crossentropy': 5.584863101183159}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 37391], ['id', 55301], ['id', 70931], ['id', 65709], ['id', 5363]], 'labels': [8, 1, 0, 1, 2], 'scores': [0.6292702467689728, 1.1616280222065862, 1.653135824567301, 2.1129917227893884, 2.530137670545267]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.18359375, 'crossentropy': 3.337367534637451})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2314453125, 'crossentropy': 4.372769355773926})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2607421875, 'crossentropy': 4.615922927856445})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.224609375, 'crossentropy': 4.383906364440918})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.259765625, 'crossentropy': 5.529877662658691})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2802734375, 'crossentropy': 4.773930549621582})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2734375, 'crossentropy': 4.4157328605651855})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.25390625, 'crossentropy': 4.484771728515625})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.2578125, 'crossentropy': 5.533425331115723})
store['active_learning_steps'][43]['training']['best_epoch']=6
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.25956515058389673, 'crossentropy': 4.952887011658728}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 8863], ['id', 70827], ['id', 13228], ['id', 15173], ['id', 30559]], 'labels': [-1, 8, 9, 7, 8], 'scores': [0.6299086326939791, 1.225738785647641, 1.7509679736431538, 2.205630694560975, 2.6038689104428503]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2255859375, 'crossentropy': 4.583555698394775})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.251953125, 'crossentropy': 4.252873420715332})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.296875, 'crossentropy': 3.716611385345459})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2958984375, 'crossentropy': 4.2260541915893555})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.294921875, 'crossentropy': 4.171224594116211})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.2685546875, 'crossentropy': 4.8745222091674805})
store['active_learning_steps'][44]['training']['best_epoch']=3
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.2759680393362016, 'crossentropy': 3.9831055287722803}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 23728], ['ood', 110], ['id', 15370], ['ood', 23766], ['id', 66067]], 'labels': [-1, -1, 2, -1, 6], 'scores': [0.7395453673581565, 1.2884978560437288, 1.7698204117728134, 2.203433289814428, 2.572207277626916]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.197265625, 'crossentropy': 3.428706645965576})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2216796875, 'crossentropy': 4.586705207824707})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.255859375, 'crossentropy': 5.17780065536499})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.1943359375, 'crossentropy': 5.502975940704346})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 5.6723785400390625})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.2490234375, 'crossentropy': 5.471841812133789})
store['active_learning_steps'][45]['training']['best_epoch']=3
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.23271358328211433, 'crossentropy': 5.116462430854333}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 24121], ['id', 40818], ['ood', 16779], ['id', 53453], ['id', 34619]], 'labels': [-1, 8, -1, 5, 1], 'scores': [0.6176993507144894, 1.2042791248857911, 1.704404116931339, 2.149111469719367, 2.5478144276083636]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2080078125, 'crossentropy': 3.8871827125549316})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2119140625, 'crossentropy': 4.602546691894531})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.21484375, 'crossentropy': 5.0675153732299805})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2392578125, 'crossentropy': 4.306964874267578})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.27734375, 'crossentropy': 4.257165908813477})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.234375, 'crossentropy': 4.676603317260742})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2587890625, 'crossentropy': 4.756895065307617})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2900390625, 'crossentropy': 4.082663536071777})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.3037109375, 'crossentropy': 4.068001747131348})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.263671875, 'crossentropy': 4.51658821105957})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.271484375, 'crossentropy': 4.579113006591797})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.2861328125, 'crossentropy': 4.588474273681641})
store['active_learning_steps'][46]['training']['best_epoch']=9
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.2878380454824831, 'crossentropy': 4.258418725030731}
