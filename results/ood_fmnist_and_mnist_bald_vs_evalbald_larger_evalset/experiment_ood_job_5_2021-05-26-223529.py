store = {}
store['timestamp']=1622064929
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=5']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=5
store['worker_id']=5
store['num_workers']=80
store['config']={'seed': 1239, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 2.5092897415161133})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.3695240020751953})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 3.4138526916503906})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.59765625, 'crossentropy': 3.6056056022644043})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 4.133161544799805})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5986, 'crossentropy': 3.385106640625}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.269957184791565})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.2976007461547852})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.2911157608032227})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.2756409645080566})
store['active_learning_steps'][0]['eval_training']['best_epoch']=4
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 38442], ['ood', 7958], ['ood', 12312], ['ood', 5331], ['id', 55411]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1714298610518359, 2.1037099203489755, 2.6758423413133103, 3.0178859370562794, 3.2058939786068326]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 1.4331419467926025})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.2886898517608643})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.167452335357666})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.2398293018341064})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.606630325317383})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.627272844314575})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.774623155593872})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6085, 'crossentropy': 2.554291796875}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.235169768333435})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2089834213256836})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.2153832912445068})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.2050371170043945})
store['active_learning_steps'][1]['eval_training']['best_epoch']=1
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 24408], ['id', 37549], ['ood', 16027], ['id', 43308], ['id', 29318]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6939009450655984, 1.2827496495397628, 1.772737379631442, 2.146245857251129, 2.396922464664023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.4231345653533936})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.7512905597686768})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.328836441040039})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.403500556945801})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6291, 'crossentropy': 1.432442578125}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1234314441680908})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.1072896718978882})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.0921545028686523})
store['active_learning_steps'][2]['eval_training']['best_epoch']=1
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 43746], ['id', 48804], ['id', 43699], ['id', 40744], ['id', 39560]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.4804909523010985, 0.8995838574750694, 1.2323928776776354, 1.52429712900111, 1.772690195406823]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.3507548570632935})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.9599626064300537})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.197437047958374})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.1332790851593018})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.406306505203247})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6285, 'crossentropy': 1.9725486328125}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.1824432611465454})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.125502109527588})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.1279858350753784})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.20704984664917})
store['active_learning_steps'][3]['eval_training']['best_epoch']=3
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 8302], ['id', 21615], ['id', 30046], ['id', 57979], ['id', 10299]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.650254989403324, 1.1856356105868215, 1.6454177709775113, 2.044296530411902, 2.332888676063451]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.4839696884155273})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.0981435775756836})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.276360034942627})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.448777437210083})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.347993850708008})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.723989725112915})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.537790298461914})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 3.0680997371673584})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.6616063117980957})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.6336350440979004})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.65151309967041})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.5527431964874268})
store['active_learning_steps'][4]['training']['best_epoch']=9
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6431, 'crossentropy': 2.8094923828125}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.2499375343322754})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2755804061889648})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1919831037521362})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2530606985092163})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2201989889144897})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.309093713760376})
store['active_learning_steps'][4]['eval_training']['best_epoch']=3
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 51903], ['id', 33766], ['id', 11108], ['ood', 45494], ['id', 18048]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6674925509711436, 1.2518580014497052, 1.7612141965265713, 2.1209226339140166, 2.359709793015626]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.5159106254577637})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.9468271732330322})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.2468624114990234})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.310946464538574})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.3885135650634766})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.3886051177978516})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.662519931793213})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.4911510944366455})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.641535758972168})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.9120101928710938})
store['active_learning_steps'][5]['training']['best_epoch']=7
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6523, 'crossentropy': 2.8201513671875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.263869285583496})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2727222442626953})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1843012571334839})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2659766674041748})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2796871662139893})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.305187463760376})
store['active_learning_steps'][5]['eval_training']['best_epoch']=3
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 42409], ['id', 46393], ['id', 40886], ['id', 16154], ['id', 35340]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6893462852437442, 1.3239377966331043, 1.8656563654746336, 2.270795790135238, 2.5530795770111734]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.389067530632019})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.599982500076294})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.100353717803955})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.2961668968200684})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 2.245279312133789})
store['active_learning_steps'][6]['training']['best_epoch']=2
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6545, 'crossentropy': 1.74799453125}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.1797351837158203})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.192054271697998})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1647968292236328})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1191012859344482})
store['active_learning_steps'][6]['eval_training']['best_epoch']=4
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 20282], ['id', 44011], ['id', 30887], ['id', 1191], ['id', 17836]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4857773367684426, 0.9304693560022268, 1.3036010813550973, 1.6012529255694252, 1.8370465939668286]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.3825764656066895})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.899454116821289})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.258716106414795})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.1990654468536377})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.459153175354004})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.438556671142578})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 3.1417007446289062})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.6755619049072266})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 3.447012424468994})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.9259252548217773})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 3.062222719192505})
store['active_learning_steps'][7]['training']['best_epoch']=8
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.659, 'crossentropy': 2.9434853515625}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2031798362731934})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.3847204446792603})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.3669657707214355})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3313531875610352})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.4297490119934082})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.427936315536499})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.3389593362808228})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.5157973766326904})
store['active_learning_steps'][7]['eval_training']['best_epoch']=5
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 54424], ['id', 661], ['id', 57976], ['id', 32759], ['id', 49828]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6552470510653194, 1.2115236541529857, 1.6685077515445332, 2.027557733262281, 2.286108966485875]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.3182693719863892})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.6739253997802734})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.130601644515991})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.0830676555633545})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.4964070320129395})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.690915107727051})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.4225194454193115})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6621, 'crossentropy': 2.280455859375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.211646318435669})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2102750539779663})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2862653732299805})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.3360087871551514})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.420771598815918})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.2972033023834229})
store['active_learning_steps'][8]['eval_training']['best_epoch']=6
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 33406], ['id', 32176], ['id', 39750], ['ood', 8978], ['id', 1444]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5662098052062168, 1.0812074902338185, 1.5123419975159202, 1.8617748381292705, 2.1055732558160694]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 1.302433729171753})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.6093533039093018})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.9578732252120972})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.3244223594665527})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.5248727798461914})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.5882163047790527})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.4272327423095703})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.807278633117676})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.7427053451538086})
store['active_learning_steps'][9]['training']['best_epoch']=6
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6615, 'crossentropy': 2.6014333984375}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2093850374221802})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2895488739013672})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.2582247257232666})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.2890682220458984})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3949830532073975})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2274739742279053})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.319617509841919})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3162853717803955})
store['active_learning_steps'][9]['eval_training']['best_epoch']=8
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 30379], ['id', 29220], ['id', 19398], ['id', 18414], ['id', 21904]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.591425306987722, 1.1342295407816354, 1.5974625720561022, 1.9773324358554172, 2.220651450674856]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.3012992143630981})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.5761570930480957})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.7688624858856201})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.904325008392334})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 2.2217788696289062})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.505340099334717})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.568941593170166})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.4911065101623535})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.6785969734191895})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.6194019317626953})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.7241859436035156})
store['active_learning_steps'][10]['training']['best_epoch']=8
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6785, 'crossentropy': 2.49943203125}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.263096809387207})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.195518970489502})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3188502788543701})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.263853669166565})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.2754371166229248})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2624452114105225})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.3801536560058594})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 26588], ['id', 3194], ['id', 271], ['ood', 25669], ['id', 35709]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.6499499965401951, 1.2353628863780002, 1.7401930017440006, 2.1150670333520347, 2.373562426491393]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2185969352722168})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.6352900266647339})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 1.7909777164459229})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.7441394329071045})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.2035305500030518})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 2.061049461364746})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.198774814605713})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6694, 'crossentropy': 1.9331537109375}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1745026111602783})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1113121509552002})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1031126976013184})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1343932151794434})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.1649348735809326})
store['active_learning_steps'][11]['eval_training']['best_epoch']=2
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 53479], ['id', 3694], ['id', 24345], ['id', 48019], ['id', 21502]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5625907751341392, 1.0954006839856838, 1.588258454654234, 1.9510500945952884, 2.217675193638181]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2367802858352661})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.4035954475402832})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.8172333240509033})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.8255133628845215})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.106201171875})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.001903533935547})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.434495687484741})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.4580800533294678})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.4655075073242188})
store['active_learning_steps'][12]['training']['best_epoch']=6
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6854, 'crossentropy': 2.151963671875}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1663599014282227})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.178473949432373})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1285557746887207})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.124514102935791})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.105286955833435})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.142927646636963})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1525920629501343})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.146422028541565})
store['active_learning_steps'][12]['eval_training']['best_epoch']=6
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 40160], ['id', 45573], ['id', 43342], ['id', 5712], ['id', 58170]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6092461590990514, 1.1803160763776548, 1.6527162245402645, 2.0222107234259266, 2.2809581012033044]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.2148032188415527})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.3951845169067383})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.6154558658599854})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.9808244705200195})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.91871976852417})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.4192280769348145})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6783, 'crossentropy': 1.642901171875}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1154625415802002})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1018426418304443})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1014161109924316})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0920844078063965})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1231718063354492})
store['active_learning_steps'][13]['eval_training']['best_epoch']=5
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 5555], ['id', 8506], ['id', 43510], ['id', 56680], ['id', 53447]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5216022380900718, 1.0063877668282926, 1.4199720609934339, 1.7657140041398645, 2.014494122278726]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.2405189275741577})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.2591922283172607})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.7467896938323975})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.6423890590667725})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.7856577634811401})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.033379554748535})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.1046130657196045})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.2770018577575684})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.1483535766601562})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.3242545127868652})
store['active_learning_steps'][14]['training']['best_epoch']=7
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6862, 'crossentropy': 2.0907751953125}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1464438438415527})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1113879680633545})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1658905744552612})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.1242728233337402})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.140232801437378})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.2056567668914795})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1368632316589355})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.1390044689178467})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.1402175426483154})
store['active_learning_steps'][14]['eval_training']['best_epoch']=9
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 11306], ['id', 14196], ['id', 35467], ['id', 34393], ['id', 23771]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.6227319505768567, 1.1938443476991107, 1.6926692612925924, 2.0975043805129365, 2.4175983064824402]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.3558353185653687})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1757797002792358})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.4549217224121094})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.735296368598938})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.8136050701141357})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.7670643329620361})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.216052770614624})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.1233792304992676})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.1323671340942383})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6891, 'crossentropy': 1.9621021484375}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.0861525535583496})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0300761461257935})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0101590156555176})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.0320408344268799})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.0374562740325928})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0471477508544922})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.0329035520553589})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.0307250022888184})
store['active_learning_steps'][15]['eval_training']['best_epoch']=7
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 55510], ['id', 36668], ['id', 5359], ['id', 23637], ['id', 55478]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5930370240784346, 1.149800767046857, 1.6383426333608018, 2.008146985490055, 2.2881606218971138]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.2224841117858887})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0960049629211426})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.3859410285949707})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.4457274675369263})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.5500822067260742})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.7714195251464844})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.672714352607727})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7117, 'crossentropy': 1.49045107421875}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.03580641746521})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9592127799987793})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9965896010398865})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9404685497283936})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9445480108261108})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9373835325241089})
store['active_learning_steps'][16]['eval_training']['best_epoch']=6
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 10259], ['id', 44498], ['id', 32498], ['id', 18533], ['id', 29358]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6367873254754528, 1.1848339144545492, 1.664916018019854, 2.0223276998839017, 2.284456828423875]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.1455186605453491})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0779458284378052})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.2746614217758179})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.4419828653335571})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.4515504837036133})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.5735324621200562})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.7315495014190674})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.6907240152359009})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.723910927772522})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.6763508319854736})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.9248580932617188})
store['active_learning_steps'][17]['training']['best_epoch']=8
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7297, 'crossentropy': 1.868526953125}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.1179027557373047})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9615756273269653})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9420607089996338})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9249798059463501})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.0032587051391602})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.925003170967102})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.0016093254089355})
store['active_learning_steps'][17]['eval_training']['best_epoch']=4
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 13133], ['id', 39685], ['id', 35971], ['id', 17030], ['id', 11193]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5649406066911788, 1.1090321580768112, 1.5887769839167198, 1.9394702689191732, 2.174256057954479]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1816351413726807})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.0945422649383545})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.136643409729004})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.3328843116760254})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.4273314476013184})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.4303481578826904})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.7247483730316162})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.8158543109893799})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.696922779083252})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.9645123481750488})
store['active_learning_steps'][18]['training']['best_epoch']=7
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.7163, 'crossentropy': 1.8379427734375}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1050060987472534})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.963214635848999})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9705385565757751})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.9691492319107056})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0216896533966064})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0212352275848389})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.940990686416626})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9848728775978088})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.971420168876648})
store['active_learning_steps'][18]['eval_training']['best_epoch']=8
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 5154], ['id', 25420], ['id', 35562], ['id', 56952], ['id', 51511]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6903683513232841, 1.2326273210840184, 1.6893855716611923, 2.051344440686176, 2.2938238862304647]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2432234287261963})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.0720875263214111})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.115630865097046})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.3647054433822632})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.470426082611084})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.604884386062622})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.6783974170684814})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.7224, 'crossentropy': 1.37362451171875}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.1276657581329346})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 0.9573349356651306})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 0.9609342813491821})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9287382364273071})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9064858555793762})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.8957960605621338})
store['active_learning_steps'][19]['eval_training']['best_epoch']=6
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 1305], ['id', 43587], ['id', 2099], ['id', 29755], ['id', 43735]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6379672556235749, 1.1688772369598674, 1.6468316611909932, 2.007701718898148, 2.2437761784236683]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.259315848350525})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.0334376096725464})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.2406337261199951})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.2996665239334106})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.3821461200714111})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.542750358581543})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.5913245677947998})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.7944402694702148})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.8905768394470215})
store['active_learning_steps'][20]['training']['best_epoch']=6
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.7228, 'crossentropy': 1.6580556640625}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0515167713165283})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 0.9759032130241394})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9803823232650757})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9969149827957153})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9727840423583984})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.9488164782524109})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9621614217758179})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.915614664554596})
store['active_learning_steps'][20]['eval_training']['best_epoch']=6
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 54960], ['id', 34817], ['id', 13825], ['id', 20138], ['id', 48025]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.5917876896018976, 1.0936211157129123, 1.512871051762243, 1.8397761437477156, 2.0959960588592903]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.1878488063812256})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.1230075359344482})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.1668695211410522})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.2941858768463135})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.3871333599090576})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.610359787940979})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.672832727432251})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.7671095132827759})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.7318198680877686})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.8633759021759033})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.0209176540374756})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 2.257235527038574})
store['active_learning_steps'][21]['training']['best_epoch']=9
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7267, 'crossentropy': 1.8502427734375}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0915223360061646})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.986986517906189})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.9622589945793152})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.9614598155021667})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.9792340397834778})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.9945639967918396})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.0063130855560303})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.0141433477401733})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.9960092306137085})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 0.966790497303009})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.9996449947357178})
store['active_learning_steps'][21]['eval_training']['best_epoch']=10
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 18190], ['id', 2324], ['id', 33801], ['id', 12482], ['id', 30547]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7108159045439821, 1.302144365208156, 1.8400725494496362, 2.203260013296296, 2.443575705119394]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.168919324874878})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 0.9994333386421204})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.1541084051132202})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.297419786453247})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.438283920288086})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.4056087732315063})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.50461745262146})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.6980921030044556})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.9030883312225342})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.5983542203903198})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7266, 'crossentropy': 1.5457607421875}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.0074788331985474})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9217474460601807})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.931072473526001})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 0.9119062423706055})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.8853706121444702})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.8562482595443726})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.8960416316986084})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.8880358934402466})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.8641464114189148})
store['active_learning_steps'][22]['eval_training']['best_epoch']=6
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 49008], ['id', 54405], ['id', 23339], ['id', 58392], ['id', 18882]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7091028349123787, 1.3028472309505879, 1.798672245503755, 2.194283706113267, 2.4578334616334088]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.568359375, 'crossentropy': 1.2867965698242188})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.128068447113037})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.079056978225708})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.201751470565796})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.3013745546340942})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.5176289081573486})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.5191338062286377})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.599057674407959})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.8155049085617065})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.7834084033966064})
store['active_learning_steps'][23]['training']['best_epoch']=7
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7251, 'crossentropy': 1.50085419921875}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1341276168823242})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.002215027809143})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 0.9949655532836914})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9374996423721313})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 0.9477889537811279})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.924328088760376})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9043628573417664})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.8950479030609131})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.8994598388671875})
store['active_learning_steps'][23]['eval_training']['best_epoch']=9
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 33420], ['id', 47079], ['id', 30810], ['id', 20141], ['id', 20702]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.6247530581628719, 1.1854700569201762, 1.658982426166061, 2.050913086300776, 2.3278415708173865]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2417782545089722})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.037140130996704})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.0925414562225342})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.297324538230896})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.4506922960281372})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.4979147911071777})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.6728463172912598})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.7450828552246094})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.7835347652435303})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.8487801551818848})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.8218711614608765})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.809951901435852})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 2.086535692214966})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.8811976909637451})
store['active_learning_steps'][24]['training']['best_epoch']=11
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.7214, 'crossentropy': 1.9575013671875}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0682225227355957})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9574369192123413})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9766020178794861})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.961770236492157})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 0.9855691194534302})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.0210280418395996})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.0029029846191406})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.0007719993591309})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.0208553075790405})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.9944642782211304})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.065568208694458})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.0143905878067017})
store['active_learning_steps'][24]['eval_training']['best_epoch']=9
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 4702], ['id', 45824], ['id', 3893], ['id', 12076], ['id', 52590]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6813215726432846, 1.289484059650595, 1.8110019543205533, 2.218445360871515, 2.505169568608469]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.2460646629333496})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.0360336303710938})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.0859549045562744})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.163224697113037})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.3172943592071533})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.3534132242202759})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.475640058517456})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.7254, 'crossentropy': 1.15846904296875}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0455830097198486})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 0.9958798885345459})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 0.9444961547851562})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9155328273773193})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9099950194358826})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.8628734350204468})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 18913], ['id', 28501], ['id', 33277], ['id', 30553], ['ood', 22958]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5683107363651296, 1.0335648180005341, 1.4368846214324602, 1.7900940496958375, 2.0506151530085477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 1.2991803884506226})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.0280182361602783})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.109914779663086})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.221399188041687})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.3080542087554932})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.6335569620132446})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.5237975120544434})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.627778172492981})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.9118767976760864})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.9913685321807861})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.7369, 'crossentropy': 1.57771787109375}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.0771574974060059})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.968632698059082})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.9709908962249756})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.9285669922828674})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.9547786116600037})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.9172308444976807})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.91614830493927})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.9192834496498108})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.9356564283370972})
store['active_learning_steps'][26]['eval_training']['best_epoch']=8
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 30029], ['id', 8485], ['id', 58078], ['id', 34162], ['id', 46975]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.5756030735790183, 1.116913735716289, 1.54030239368263, 1.8850053173459944, 2.1290626411281135]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.2652068138122559})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.1764845848083496})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.1489564180374146})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.319575548171997})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.4440279006958008})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.5779147148132324})
store['active_learning_steps'][27]['training']['best_epoch']=3
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.7177, 'crossentropy': 1.1395380859375}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.1255581378936768})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 0.9710787534713745})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9344024062156677})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.9097093939781189})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.8849174976348877})
store['active_learning_steps'][27]['eval_training']['best_epoch']=5
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 11274], ['id', 1999], ['id', 54580], ['id', 44285], ['id', 13979]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5206953232441951, 0.9650070844869338, 1.3330264699431424, 1.6329249779825652, 1.8725658556493485]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.274205207824707})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0079236030578613})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.00188148021698})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.107251763343811})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.2521624565124512})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.287811040878296})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.5295109748840332})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.659438967704773})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.6395705938339233})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.7424640655517578})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.7619097232818604})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.7979860305786133})
store['active_learning_steps'][28]['training']['best_epoch']=9
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.7315, 'crossentropy': 1.736767578125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.097843050956726})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 0.9871264696121216})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.9331234693527222})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.8989617824554443})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.9286885857582092})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.8856931924819946})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.9250478744506836})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.9359339475631714})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 0.9002538919448853})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.9088714718818665})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.9810836911201477})
store['active_learning_steps'][28]['eval_training']['best_epoch']=9
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 19870], ['id', 57965], ['id', 1625], ['id', 19842], ['id', 4924]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.631550281869941, 1.197711222517829, 1.6624571513487814, 2.032612692563962, 2.2765208236838106]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.301353931427002})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.044018030166626})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.9669734239578247})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.0339562892913818})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.2025091648101807})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.29599928855896})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.3717377185821533})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.3780410289764404})
store['active_learning_steps'][29]['training']['best_epoch']=5
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.7345, 'crossentropy': 1.18137109375}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1548635959625244})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.9561762809753418})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.9155186414718628})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.8638075590133667})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 0.8354718089103699})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.8786963224411011})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 0.8625892996788025})
store['active_learning_steps'][29]['eval_training']['best_epoch']=7
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 32578], ['ood', 21936], ['ood', 27396], ['id', 5893], ['id', 35995]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.554595086288957, 1.0740227543353673, 1.493836694551323, 1.8025897143092315, 2.0487328752749914]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2919983863830566})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0504114627838135})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.963922381401062})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.051023244857788})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.1483469009399414})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.2468206882476807})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.3198363780975342})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.322488784790039})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.4356603622436523})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.536698579788208})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.5946465730667114})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.5677214860916138})
store['active_learning_steps'][30]['training']['best_epoch']=9
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7394, 'crossentropy': 1.43904189453125}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0175797939300537})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.885069727897644})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 0.8659347295761108})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.8659965395927429})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 0.8577037453651428})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.8930385112762451})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 0.8910192251205444})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.8897892832756042})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 0.8513109683990479})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 0.878395676612854})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 0.8604090213775635})
store['active_learning_steps'][30]['eval_training']['best_epoch']=9
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 53825], ['id', 58038], ['id', 26336], ['id', 15233], ['id', 29705]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5912885017959815, 1.1103355152633556, 1.5777120593762355, 1.9600771706090008, 2.229655182505728]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.2570033073425293})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.004395842552185})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.0173137187957764})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.0679490566253662})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.1099154949188232})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.2305223941802979})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.2890058755874634})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.3998777866363525})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.3864719867706299})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.4989041090011597})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.6328150033950806})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.5766022205352783})
store['active_learning_steps'][31]['training']['best_epoch']=9
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7429, 'crossentropy': 1.38226220703125}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.0541050434112549})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9706680774688721})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.9479732513427734})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9179376363754272})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 0.9055395126342773})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 0.9063977003097534})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.9063074588775635})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 0.9271440505981445})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 0.904854953289032})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 0.9004942774772644})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 0.8983139991760254})
store['active_learning_steps'][31]['eval_training']['best_epoch']=10
store['active_learning_steps'][31]['acquisition']={'indices': [['ood', 11711], ['id', 17345], ['id', 4147], ['id', 49410], ['id', 17505]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.632570895420042, 1.213573378457209, 1.718664683685415, 2.113569583209082, 2.4021286889187667]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.3149759769439697})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0687909126281738})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.075177550315857})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.0564446449279785})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.1468555927276611})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.1200898885726929})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.2949371337890625})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.3537784814834595})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.4635882377624512})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.7421, 'crossentropy': 1.1948365234375}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1200010776519775})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9338266849517822})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 0.845753014087677})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 0.8626282215118408})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.8587261438369751})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 0.8582310676574707})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 0.8479938507080078})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.8312608003616333})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 788], ['id', 7475], ['id', 58130], ['id', 22656], ['id', 29038]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5852452388444158, 1.0962572544671683, 1.5514638873606188, 1.8943953349183804, 2.162037210731807]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.2803237438201904})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.04814875125885})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 0.9814422130584717})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.0327318906784058})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.1783356666564941})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.3007696866989136})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.5589828491210938})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.438349962234497})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.5620864629745483})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.6357091665267944})
store['active_learning_steps'][33]['training']['best_epoch']=7
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7257, 'crossentropy': 1.50824189453125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0101075172424316})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.9648299217224121})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 0.9887606501579285})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 0.893134593963623})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 0.9530217051506042})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.9362175464630127})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 0.9853205680847168})
store['active_learning_steps'][33]['eval_training']['best_epoch']=4
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 32065], ['id', 45783], ['id', 8347], ['id', 17383], ['id', 22547]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5808246928814732, 1.1106984828334778, 1.582360080838316, 1.971711355121772, 2.265442454503523]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.2951514720916748})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0390745401382446})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.010263204574585})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.0183329582214355})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.1126829385757446})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.1297571659088135})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.2632896900177002})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.3689754009246826})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.4383249282836914})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.4279283285140991})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.5513486862182617})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.458073616027832})
store['active_learning_steps'][34]['training']['best_epoch']=9
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.7471, 'crossentropy': 1.40756201171875}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1181657314300537})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 0.9454372525215149})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 0.887237548828125})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 0.9360671043395996})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 0.9244628548622131})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 0.8925219178199768})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 0.883012056350708})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 0.8855541944503784})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 0.8878362774848938})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 0.8883829116821289})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 0.8714264631271362})
store['active_learning_steps'][34]['eval_training']['best_epoch']=11
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 55037], ['id', 17703], ['id', 56674], ['id', 10971], ['id', 21074]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.6086311121468349, 1.1805008459508333, 1.665884059027713, 2.0140464959221136, 2.2762162379481223]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.2503771781921387})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0463168621063232})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 0.9945979118347168})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.1205339431762695})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.2149620056152344})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.1873502731323242})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.2898685932159424})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7183, 'crossentropy': 1.1323794921875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.0919215679168701})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.9474823474884033})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9110689163208008})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.8831092119216919})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9000929594039917})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.85982346534729})
store['active_learning_steps'][35]['eval_training']['best_epoch']=6
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 41355], ['id', 44716], ['id', 18729], ['id', 26279], ['id', 33266]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5817720381883633, 1.059848668364645, 1.4755015267952754, 1.8002220027993552, 2.049284932048872]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.2529346942901611})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9615403413772583})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 0.9408009052276611})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.053969383239746})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.1201560497283936})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.2940700054168701})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.2523088455200195})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.3900151252746582})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.3398332595825195})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.419958233833313})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.4244428873062134})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.5259963274002075})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.5643913745880127})
store['active_learning_steps'][36]['training']['best_epoch']=10
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7423, 'crossentropy': 1.45224287109375}
