store = {}
store['timestamp']=1622116334
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py', '--id=21']
store['commit']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['github_url']='687a8dd5b631132403a94f206eb0a7ba2c3b7a98'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/experiment_ood.py'
store['job_id']=21
store['worker_id']=21
store['num_workers']=80
store['config']={'seed': 1256, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 256, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchEvalBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 40646, 10110, 32775, 33736, 27254, 306, 37354, 19689, 57811, 34482, 15494, 19215, 18819, 11554, 8108, 29048, 30362, 48953, 5588, 8719, 48602, 33140, 46397, 56710, 14640, 39579, 5573, 5715, 47420, 27135, 26129, 16927, 39050, 42295, 51555, 51600, 43234, 33891, 20917, 38856, 17032, 13036, 11228, 46700, 50498, 40741, 9834, 24971, 17759, 45567, 2728, 1774, 33486, 43252, 43803, 50036, 46861, 53831, 54003, 53362, 229, 767, 36270, 10432, 23451, 6612, 8710, 41077, 48498, 46683, 45260, 37098, 55148, 49775, 52801, 15969, 57520, 36797, 34198, 27145, 3029, 37047, 31965, 26501, 48519, 5803, 43415, 35794, 33581, 5897, 27573, 30980, 29614, 35237, 51755, 57690, 26516, 5380, 25589, 53689, 31444, 29950, 44803, 396, 56990, 24052, 12108, 54426, 42320, 35072, 21536, 49304, 49595, 44428, 72, 57175, 52679, 41082, 30184, 54017, 10232, 17968, 31935, 43587, 801, 48031, 2206, 2404, 58741, 29079, 49986, 46464, 17659, 30072, 39879, 29556, 52389, 13092, 37129, 11773, 15822, 37625, 7382, 7121, 17195, 32625, 43141, 28181, 50055, 55187, 34588, 38725, 50466, 40018, 37115, 20801, 23496, 4321, 42102, 12075, 54012, 28833, 18880, 26520, 27580, 14637, 40466, 54800, 24110, 13859, 51027, 45005, 57541, 34361, 26479, 43321, 44048, 45974, 15675, 10508, 49549, 28991, 13074, 9574, 44454, 36688, 8821, 12610, 54422, 34121, 27019, 21800, 44138, 36367, 44100, 33464, 51760, 15917, 495, 50997, 48032, 40334, 21423, 46870, 18137, 4701, 18693, 17506, 6968, 13359, 35372, 7356, 2289, 55733, 5481, 37157, 56054, 2400, 56137, 1005, 56096, 53538, 55783, 37709, 3792, 10664, 5616, 32972, 30013, 19757, 49169, 47417, 38430, 41512, 14035, 35714, 16068, 20076, 26853, 26428, 48521, 11261, 12917, 257, 43981, 8705, 27383, 10113, 7896]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5908203125, 'crossentropy': 2.387302875518799})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.123371124267578})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.2357213497161865})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 4.017779350280762})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.678365707397461})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.7867259979248047})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.5878, 'crossentropy': 3.7461109375}
store['active_learning_steps'][0]['eval_training']={}
store['active_learning_steps'][0]['eval_training']['epochs']=[]
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.595703125, 'crossentropy': 1.4945039749145508})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.5726866722106934})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 1.5709171295166016})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.5421133041381836})
store['active_learning_steps'][0]['eval_training']['epochs'].append({'accuracy': 0.5947265625, 'crossentropy': 1.5904145240783691})
store['active_learning_steps'][0]['eval_training']['best_epoch']=2
store['active_learning_steps'][0]['acquisition']={'indices': [['ood', 27090], ['ood', 45793], ['ood', 39855], ['id', 37620], ['ood', 2368]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.2379993250404837, 2.0647798391727776, 2.591551211866787, 2.8623253079160857, 3.001093117257393]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.761098861694336})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.478289842605591})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.829663038253784})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.9723222255706787})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.0495705604553223})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.9841127395629883})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.587890625, 'crossentropy': 3.502174139022827})
store['active_learning_steps'][1]['training']['best_epoch']=4
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5971, 'crossentropy': 3.322973828125}
store['active_learning_steps'][1]['eval_training']={}
store['active_learning_steps'][1]['eval_training']['epochs']=[]
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.4632327556610107})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.4861693382263184})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.4445104598999023})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.4174246788024902})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.4871892929077148})
store['active_learning_steps'][1]['eval_training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.4019336700439453})
store['active_learning_steps'][1]['eval_training']['best_epoch']=4
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 628], ['ood', 15751], ['ood', 41451], ['id', 16457], ['id', 3588]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.8259841750783263, 1.5725082102808745, 2.0945466742500107, 2.447986277134471, 2.6731921795325473]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.5157705545425415})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.000925064086914})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.4414796829223633})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.376128673553467})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.5795297622680664})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6333, 'crossentropy': 1.9624443359375}
store['active_learning_steps'][2]['eval_training']={}
store['active_learning_steps'][2]['eval_training']['epochs']=[]
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2842683792114258})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2248101234436035})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.1926791667938232})
store['active_learning_steps'][2]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.1409631967544556})
store['active_learning_steps'][2]['eval_training']['best_epoch']=3
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 47232], ['id', 4407], ['id', 55726], ['id', 34303], ['id', 38668]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5270123719888373, 1.00830087303819, 1.3851949611682102, 1.7091227661535893, 1.9762140570772289]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5791015625, 'crossentropy': 1.627903699874878})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.386744976043701})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 2.576575756072998})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.813607931137085})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.9255571365356445})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 3.5224993228912354})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.3032658100128174})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.1865010261535645})
store['active_learning_steps'][3]['training']['best_epoch']=5
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6125, 'crossentropy': 2.9031763671875}
store['active_learning_steps'][3]['eval_training']={}
store['active_learning_steps'][3]['eval_training']['epochs']=[]
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.4157859086990356})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.3029637336730957})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.4252115488052368})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.3627628087997437})
store['active_learning_steps'][3]['eval_training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 1.3852930068969727})
store['active_learning_steps'][3]['eval_training']['best_epoch']=2
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 5346], ['id', 16418], ['id', 10413], ['id', 11958], ['id', 5560]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.775618694010626, 1.4457740418831864, 1.9805240229159633, 2.3550161236800493, 2.588563749633642]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.525649070739746})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.063915252685547})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.726919651031494})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.5056867599487305})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.7493958473205566})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.9734983444213867})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.015427350997925})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.3866052627563477})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.863510847091675})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.9610178470611572})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.287029266357422})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.8744664192199707})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.7360191345214844})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 3.0253658294677734})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 3.083296775817871})
store['active_learning_steps'][4]['training']['best_epoch']=12
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6363, 'crossentropy': 3.2515552734375}
store['active_learning_steps'][4]['eval_training']={}
store['active_learning_steps'][4]['eval_training']['epochs']=[]
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.5032845735549927})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.5502116680145264})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.4710553884506226})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.5331034660339355})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.4063800573349})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.452617883682251})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.5400357246398926})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.532616138458252})
store['active_learning_steps'][4]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.5193047523498535})
store['active_learning_steps'][4]['eval_training']['best_epoch']=6
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 3553], ['id', 10100], ['id', 3801], ['id', 48954], ['id', 33801]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7776417798881115, 1.4917368311102779, 2.0641448761015218, 2.4331785978280527, 2.667587950200933]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.5834898948669434})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.106947660446167})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.6485772132873535})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.6632299423217773})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.9022884368896484})
store['active_learning_steps'][5]['training']['best_epoch']=2
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6163, 'crossentropy': 2.0464826171875}
store['active_learning_steps'][5]['eval_training']={}
store['active_learning_steps'][5]['eval_training']['epochs']=[]
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.3115131855010986})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.253035545349121})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.3415149450302124})
store['active_learning_steps'][5]['eval_training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 1.271313190460205})
store['active_learning_steps'][5]['eval_training']['best_epoch']=2
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 56635], ['id', 837], ['id', 2871], ['id', 49363], ['id', 24815]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4600892768502347, 0.8573675843477804, 1.2196896250238147, 1.5407823354916443, 1.7657731404346544]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 1.4505252838134766})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 1.8634157180786133})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.9957594871520996})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.325695037841797})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.4387192726135254})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 3.2450666427612305})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6362037658691406})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.8029093742370605})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.233391284942627})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.2593979835510254})
store['active_learning_steps'][6]['training']['best_epoch']=7
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6373, 'crossentropy': 2.707340234375}
store['active_learning_steps'][6]['eval_training']={}
store['active_learning_steps'][6]['eval_training']['epochs']=[]
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.239990472793579})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2260806560516357})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.2457706928253174})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.2540693283081055})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2498574256896973})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.22230064868927})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2222909927368164})
store['active_learning_steps'][6]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2687249183654785})
store['active_learning_steps'][6]['eval_training']['best_epoch']=5
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 1851], ['id', 52568], ['id', 3194], ['id', 22693], ['ood', 42413]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.6791495212321572, 1.3223467637532536, 1.8653639967792666, 2.272916163004629, 2.519800267111095]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.3901638984680176})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.7406957149505615})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.0672128200531006})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.520277738571167})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.3565566539764404})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.392996311187744})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.5429553985595703})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.5133843421936035})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.5120620727539062})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.637789249420166})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.8896074295043945})
store['active_learning_steps'][7]['training']['best_epoch']=8
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6439, 'crossentropy': 2.5664517578125}
store['active_learning_steps'][7]['eval_training']={}
store['active_learning_steps'][7]['eval_training']['epochs']=[]
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.3249307870864868})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.175305962562561})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 1.2410744428634644})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1876442432403564})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2859207391738892})
store['active_learning_steps'][7]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.2188124656677246})
store['active_learning_steps'][7]['eval_training']['best_epoch']=3
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 12143], ['ood', 29065], ['id', 44450], ['id', 14332], ['ood', 52358]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.7838924452103466, 1.4370060659809578, 1.9584417253057023, 2.3507591875351714, 2.6050066592030214]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.4783122539520264})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 1.998963475227356})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.244020938873291})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.5418972969055176})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.8438878059387207})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.7648637294769287})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.1948485374450684})
store['active_learning_steps'][8]['training']['best_epoch']=4
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6326, 'crossentropy': 2.52576484375}
store['active_learning_steps'][8]['eval_training']={}
store['active_learning_steps'][8]['eval_training']['epochs']=[]
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.2957402467727661})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2567706108093262})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 1.2972303628921509})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.3215274810791016})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 1.3058364391326904})
store['active_learning_steps'][8]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.2471086978912354})
store['active_learning_steps'][8]['eval_training']['best_epoch']=3
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 1462], ['ood', 56098], ['id', 36906], ['ood', 1742], ['id', 58374]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5839398169883923, 1.1143427123172924, 1.5694655142108882, 1.9281917179527097, 2.208845975735416]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 1.4716684818267822})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.8840038776397705})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.3937625885009766})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.3485071659088135})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.5993008613586426})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.024087429046631})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.8866374492645264})
store['active_learning_steps'][9]['training']['best_epoch']=4
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6433, 'crossentropy': 2.566746875}
store['active_learning_steps'][9]['eval_training']={}
store['active_learning_steps'][9]['eval_training']['epochs']=[]
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.339052677154541})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.2333232164382935})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 1.3877766132354736})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.3025860786437988})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.3597102165222168})
store['active_learning_steps'][9]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.3269658088684082})
store['active_learning_steps'][9]['eval_training']['best_epoch']=4
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 20668], ['id', 40723], ['id', 14442], ['id', 39838], ['id', 46999]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.5695586609067422, 1.0711517647788757, 1.5250076823333858, 1.9089509945475367, 2.219280773203466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.5546875, 'crossentropy': 1.5403273105621338})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 1.7203452587127686})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.1278343200683594})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.2130911350250244})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.538983106613159})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.4625964164733887})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.8114285469055176})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6413, 'crossentropy': 2.5454853515625}
store['active_learning_steps'][10]['eval_training']={}
store['active_learning_steps'][10]['eval_training']['epochs']=[]
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.35472571849823})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.263472557067871})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.312104344367981})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.2906259298324585})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.3242475986480713})
store['active_learning_steps'][10]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.309884786605835})
store['active_learning_steps'][10]['eval_training']['best_epoch']=4
store['active_learning_steps'][10]['acquisition']={'indices': [['ood', 27335], ['id', 50748], ['id', 1811], ['id', 23531], ['id', 31612]], 'labels': [[0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5841989570835997, 1.0710121877422867, 1.5030419077968435, 1.857152404194001, 2.1218644295672977]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 1.2621885538101196})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.4556204080581665})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.8479053974151611})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.8191134929656982})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.1217877864837646})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.0858840942382812})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 2.46012806892395})
store['active_learning_steps'][11]['training']['best_epoch']=4
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.6635, 'crossentropy': 2.0006306640625}
store['active_learning_steps'][11]['eval_training']={}
store['active_learning_steps'][11]['eval_training']['epochs']=[]
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.1617114543914795})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 1.18428373336792})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.113653302192688})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.1530818939208984})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 1.1406446695327759})
store['active_learning_steps'][11]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1375224590301514})
store['active_learning_steps'][11]['eval_training']['best_epoch']=5
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 11442], ['id', 4779], ['id', 32218], ['id', 55069], ['id', 9794]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6663311670938541, 1.249631369248326, 1.7179250849684866, 2.094705274549212, 2.353577318727263]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 1.364607572555542})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.5237650871276855})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.7891720533370972})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.9300975799560547})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.264897346496582})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.308262348175049})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6659, 'crossentropy': 1.865480078125}
store['active_learning_steps'][12]['eval_training']={}
store['active_learning_steps'][12]['eval_training']['epochs']=[]
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2230679988861084})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.1933618783950806})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.170229196548462})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1053612232208252})
store['active_learning_steps'][12]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.1554789543151855})
store['active_learning_steps'][12]['eval_training']['best_epoch']=5
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 2430], ['id', 8689], ['id', 40744], ['id', 7698], ['id', 3293]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.556540114077732, 1.0456502959100211, 1.4237163040875358, 1.7539906127896323, 2.0051484541845603]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.342365026473999})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 1.4175013303756714})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.8406407833099365})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.888619303703308})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.421668529510498})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.5025997161865234})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.454080820083618})
store['active_learning_steps'][13]['training']['best_epoch']=4
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6748, 'crossentropy': 2.07281640625}
store['active_learning_steps'][13]['eval_training']={}
store['active_learning_steps'][13]['eval_training']['epochs']=[]
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.2603585720062256})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 1.2675224542617798})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.2059695720672607})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1405961513519287})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.2457879781723022})
store['active_learning_steps'][13]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1623072624206543})
store['active_learning_steps'][13]['eval_training']['best_epoch']=6
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 4361], ['id', 54644], ['id', 30337], ['id', 58110], ['id', 11713]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5126992115989033, 0.9989394491631072, 1.4229479737253703, 1.7605951005097822, 2.0121141646268876]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.2800382375717163})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 1.2978172302246094})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.5180418491363525})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.6107938289642334})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.932248830795288})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.0251169204711914})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.3227767944335938})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 2.7142155170440674})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.473160743713379})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.2276134490966797})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.4775819778442383})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 2.5728373527526855})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.8095803260803223})
store['active_learning_steps'][14]['training']['best_epoch']=10
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6898, 'crossentropy': 2.3448435546875}
store['active_learning_steps'][14]['eval_training']={}
store['active_learning_steps'][14]['eval_training']['epochs']=[]
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 1.2257449626922607})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.14998459815979})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1837611198425293})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0874030590057373})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.0523627996444702})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0419373512268066})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1177334785461426})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.160430908203125})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1473796367645264})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.1033637523651123})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.1455481052398682})
store['active_learning_steps'][14]['eval_training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.053462266921997})
store['active_learning_steps'][14]['eval_training']['best_epoch']=12
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 54204], ['id', 1087], ['id', 25328], ['id', 52055], ['id', 38585]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.655723337444114, 1.2523203296701881, 1.7600168057027696, 2.1635009177163873, 2.450333298811664]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.1724655628204346})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.16621732711792})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.4992387294769287})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.81730055809021})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.767142415046692})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.1150240898132324})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.2946841716766357})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.3794126510620117})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.1138195991516113})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.764390468597412})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.369478702545166})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 2.3414316177368164})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.498425006866455})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.5699470043182373})
store['active_learning_steps'][15]['training']['best_epoch']=11
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6923, 'crossentropy': 2.4397869140625}
store['active_learning_steps'][15]['eval_training']={}
store['active_learning_steps'][15]['eval_training']['epochs']=[]
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 1.3027031421661377})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.2284271717071533})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.261393666267395})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.1762288808822632})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.3065426349639893})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.1469393968582153})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1962847709655762})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.1533868312835693})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.231995701789856})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.1506493091583252})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.1740787029266357})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.2607730627059937})
store['active_learning_steps'][15]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1190781593322754})
store['active_learning_steps'][15]['eval_training']['best_epoch']=10
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 26001], ['ood', 51382], ['id', 10567], ['id', 39812], ['id', 53807]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.73406136541846, 1.3227000347389186, 1.8110626884305097, 2.1950246991741285, 2.5027373797120926]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.273604154586792})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 1.1300978660583496})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.5449934005737305})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.6742441654205322})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 1.7981202602386475})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6651, 'crossentropy': 1.198791015625}
store['active_learning_steps'][16]['eval_training']={}
store['active_learning_steps'][16]['eval_training']['epochs']=[]
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.1256980895996094})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.0204763412475586})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 0.9661303162574768})
store['active_learning_steps'][16]['eval_training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 0.9630999565124512})
store['active_learning_steps'][16]['eval_training']['best_epoch']=3
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 47772], ['id', 15966], ['id', 16154], ['id', 4915], ['id', 386]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.40239186358321755, 0.7767128514175012, 1.1065170577706303, 1.3917654809447972, 1.6408238122421928]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.304133415222168})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 1.228611946105957})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.3679447174072266})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.6752419471740723})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.0019826889038086})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.9889311790466309})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.9354376792907715})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.3273911476135254})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.413468360900879})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.3583312034606934})
store['active_learning_steps'][17]['training']['best_epoch']=7
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6732, 'crossentropy': 2.0498025390625}
store['active_learning_steps'][17]['eval_training']={}
store['active_learning_steps'][17]['eval_training']['epochs']=[]
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.173593521118164})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.222853660583496})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.1331989765167236})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 1.1718928813934326})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.101259708404541})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1126024723052979})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 1.1640866994857788})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.1077581644058228})
store['active_learning_steps'][17]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0717997550964355})
store['active_learning_steps'][17]['eval_training']['best_epoch']=8
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 54813], ['id', 22638], ['id', 5963], ['id', 59511], ['id', 12637]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5961826822559302, 1.1620484423127153, 1.6154260970228602, 1.9739982145692059, 2.2268857534099364]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 1.2302615642547607})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 1.2337510585784912})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 1.2433617115020752})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.6634769439697266})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.8534455299377441})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.8062553405761719})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.8986018896102905})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.105327606201172})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.219318389892578})
store['active_learning_steps'][18]['training']['best_epoch']=6
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.681, 'crossentropy': 1.9236671875}
store['active_learning_steps'][18]['eval_training']={}
store['active_learning_steps'][18]['eval_training']['epochs']=[]
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.2524926662445068})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.1265463829040527})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.2156469821929932})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1188738346099854})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0927879810333252})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.1240105628967285})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.1437504291534424})
store['active_learning_steps'][18]['eval_training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.1168090105056763})
store['active_learning_steps'][18]['eval_training']['best_epoch']=7
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 6578], ['id', 4510], ['id', 36872], ['id', 995], ['id', 4611]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6461544787082669, 1.1826383837894001, 1.5950187068135904, 1.925561645772258, 2.1763723877018624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 1.276573896408081})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 1.1443068981170654})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.304894208908081})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.563416838645935})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.4649531841278076})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.6874444484710693})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 2.0600905418395996})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.685546875, 'crossentropy': 2.0444023609161377})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.856788992881775})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.057896614074707})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.142486095428467})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.20619535446167})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.049551486968994})
store['active_learning_steps'][19]['training']['best_epoch']=10
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6817, 'crossentropy': 2.21639609375}
store['active_learning_steps'][19]['eval_training']={}
store['active_learning_steps'][19]['eval_training']['epochs']=[]
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 1.1843457221984863})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.144684076309204})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 1.1353368759155273})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.1385612487792969})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.090461254119873})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0466523170471191})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.1415996551513672})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.0936484336853027})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.0808985233306885})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.0564296245574951})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.118647813796997})
store['active_learning_steps'][19]['eval_training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.0890438556671143})
store['active_learning_steps'][19]['eval_training']['best_epoch']=12
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 13237], ['id', 19842], ['id', 7775], ['id', 36671], ['id', 19809]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.7177911204354293, 1.3640637190994296, 1.8955723139975884, 2.3319400484114707, 2.661042124214715]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 1.2740349769592285})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.0573184490203857})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 1.3697785139083862})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.2632994651794434})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.4290199279785156})
store['active_learning_steps'][20]['training']['best_epoch']=2
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.7089, 'crossentropy': 1.06706005859375}
store['active_learning_steps'][20]['eval_training']={}
store['active_learning_steps'][20]['eval_training']['epochs']=[]
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 1.0622103214263916})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 0.9991447925567627})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.9547643661499023})
store['active_learning_steps'][20]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9519138336181641})
store['active_learning_steps'][20]['eval_training']['best_epoch']=4
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 39750], ['id', 50381], ['id', 3410], ['id', 47164], ['id', 4267]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.43880936588573016, 0.8503692315777154, 1.1698355341758253, 1.4422848565829982, 1.6613986711909607]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.5888671875, 'crossentropy': 1.257049798965454})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 1.06931471824646})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.1923291683197021})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.3515677452087402})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 1.5285576581954956})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.5359854698181152})
store['active_learning_steps'][21]['training']['best_epoch']=3
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6958, 'crossentropy': 1.17117470703125}
store['active_learning_steps'][21]['eval_training']={}
store['active_learning_steps'][21]['eval_training']['epochs']=[]
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.043475866317749})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.936307430267334})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.941382646560669})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 0.9306079745292664})
store['active_learning_steps'][21]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.935807466506958})
store['active_learning_steps'][21]['eval_training']['best_epoch']=5
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 45306], ['id', 24305], ['id', 58130], ['id', 22937], ['id', 59703]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [0.5051224603051849, 0.9260827876635891, 1.2749618155570488, 1.5784990036203705, 1.821571130455542]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.2269327640533447})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.1014255285263062})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.1207234859466553})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.295207142829895})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.3155229091644287})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.3960621356964111})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.3977054357528687})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 1.8310201168060303})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 1.8191425800323486})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.579869031906128})
store['active_learning_steps'][22]['training']['best_epoch']=7
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.7139, 'crossentropy': 1.586389453125}
store['active_learning_steps'][22]['eval_training']={}
store['active_learning_steps'][22]['eval_training']['epochs']=[]
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 1.1124449968338013})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 1.0076453685760498})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 0.9555262327194214})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 0.9959419965744019})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6865234375, 'crossentropy': 0.9676264524459839})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 0.9870272874832153})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9580116271972656})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9406014680862427})
store['active_learning_steps'][22]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9443288445472717})
store['active_learning_steps'][22]['eval_training']['best_epoch']=7
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 39951], ['id', 21064], ['id', 4492], ['id', 33405], ['id', 46793]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.7068391268054026, 1.3271547557636365, 1.7818099106786294, 2.155520704569076, 2.4254000666375655]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.591796875, 'crossentropy': 1.2789798974990845})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.1065361499786377})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.0929601192474365})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.2183103561401367})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 1.3600527048110962})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.4246498346328735})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.6233808994293213})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.723689079284668})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.5075047016143799})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.9361892938613892})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.684981346130371})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.836611270904541})
store['active_learning_steps'][23]['training']['best_epoch']=9
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7098, 'crossentropy': 1.6687578125}
store['active_learning_steps'][23]['eval_training']={}
store['active_learning_steps'][23]['eval_training']['epochs']=[]
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 1.1281635761260986})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 0.9799847602844238})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9363771677017212})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 0.9119257926940918})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 0.961338222026825})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9487875699996948})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 0.949695348739624})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.936202883720398})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9640242457389832})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9611301422119141})
store['active_learning_steps'][23]['eval_training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9069867134094238})
store['active_learning_steps'][23]['eval_training']['best_epoch']=11
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 29026], ['id', 3913], ['id', 1191], ['id', 21902], ['id', 45656]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6739587619474172, 1.286135125280163, 1.7695324194636486, 2.1886762913268276, 2.494477051367901]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.2851722240447998})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.11314058303833})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.1269474029541016})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1844234466552734})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 1.2888786792755127})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.3893470764160156})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.651442050933838})
store['active_learning_steps'][24]['training']['best_epoch']=4
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6928, 'crossentropy': 1.2214908203125}
store['active_learning_steps'][24]['eval_training']={}
store['active_learning_steps'][24]['eval_training']['epochs']=[]
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.1334805488586426})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 0.9968233108520508})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 0.9549918174743652})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 0.9426566958427429})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 0.9492499828338623})
store['active_learning_steps'][24]['eval_training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 0.8939657211303711})
store['active_learning_steps'][24]['eval_training']['best_epoch']=6
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 57962], ['id', 29915], ['id', 43277], ['id', 28130], ['id', 31008]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [0.590667095292517, 1.1064279332621307, 1.5328321184471214, 1.878648513391803, 2.1384310708022722]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.5068359375, 'crossentropy': 1.3417444229125977})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 1.063348650932312})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0844032764434814})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.0964412689208984})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.1848971843719482})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.2754440307617188})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.353905200958252})
store['active_learning_steps'][25]['training']['best_epoch']=4
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.7129, 'crossentropy': 1.15047568359375}
store['active_learning_steps'][25]['eval_training']={}
store['active_learning_steps'][25]['eval_training']['epochs']=[]
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 1.093489408493042})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.0249983072280884})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 0.9403179883956909})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 0.93531334400177})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 0.9042178392410278})
store['active_learning_steps'][25]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.8876422047615051})
store['active_learning_steps'][25]['eval_training']['best_epoch']=6
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 1248], ['id', 22224], ['ood', 10217], ['id', 55165], ['ood', 6612]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5678559200889275, 1.0602433658390442, 1.464948456565871, 1.7955406518632202, 2.0527187586283215]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.2795023918151855})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.0414342880249023})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.0422300100326538})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0770947933197021})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.1309499740600586})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.1781059503555298})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.3408501148223877})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.504341959953308})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.5298209190368652})
store['active_learning_steps'][26]['training']['best_epoch']=6
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.72, 'crossentropy': 1.28386201171875}
store['active_learning_steps'][26]['eval_training']={}
store['active_learning_steps'][26]['eval_training']['epochs']=[]
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 1.0882065296173096})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 0.937684178352356})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 0.9396984577178955})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 0.9114497303962708})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 0.8967247009277344})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9073280096054077})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9134498238563538})
store['active_learning_steps'][26]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.8872564435005188})
store['active_learning_steps'][26]['eval_training']['best_epoch']=8
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 52509], ['id', 6175], ['ood', 1440], ['id', 54465], ['id', 5912]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6483051131802273, 1.2038981430888915, 1.6548072285631275, 2.0033723364172618, 2.265975082144486]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.3011220693588257})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0509560108184814})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.0655118227005005})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.1612348556518555})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.409226417541504})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 1.4431421756744385})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.5479711294174194})
store['active_learning_steps'][27]['training']['best_epoch']=4
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.7273, 'crossentropy': 1.11762998046875}
store['active_learning_steps'][27]['eval_training']={}
store['active_learning_steps'][27]['eval_training']['epochs']=[]
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 1.0951025485992432})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 0.9678382873535156})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 0.9281618595123291})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 0.8726309537887573})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 0.8925957679748535})
store['active_learning_steps'][27]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.8902572393417358})
store['active_learning_steps'][27]['eval_training']['best_epoch']=6
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 59771], ['id', 35456], ['id', 59518], ['id', 16858], ['ood', 15951]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [0.5293416387477299, 0.9959758966630243, 1.423993031480609, 1.7573561298184925, 1.9960998542730914]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 1.2732858657836914})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.0776896476745605})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.0408669710159302})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.059230089187622})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.0869295597076416})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.1936814785003662})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 1.379783272743225})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.4375989437103271})
store['active_learning_steps'][28]['training']['best_epoch']=5
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.7333, 'crossentropy': 1.07614580078125}
store['active_learning_steps'][28]['eval_training']={}
store['active_learning_steps'][28]['eval_training']['epochs']=[]
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 1.0737051963806152})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 0.9566750526428223})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 0.9614973664283752})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 0.910254716873169})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9048856496810913})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 0.9261000156402588})
store['active_learning_steps'][28]['eval_training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 0.9120831489562988})
store['active_learning_steps'][28]['eval_training']['best_epoch']=6
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 21333], ['id', 53294], ['id', 10461], ['id', 56414], ['id', 33357]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.46977535481962396, 0.9197741293526853, 1.3271172813537238, 1.6388172953406972, 1.8877174212504437]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 1.2417433261871338})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 1.0702316761016846})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.9990483522415161})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.0948047637939453})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.1999642848968506})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.2568962574005127})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.3338665962219238})
store['active_learning_steps'][29]['training']['best_epoch']=4
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.7366, 'crossentropy': 1.07108173828125}
store['active_learning_steps'][29]['eval_training']={}
store['active_learning_steps'][29]['eval_training']['epochs']=[]
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 1.0737087726593018})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9369364976882935})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.9222701191902161})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 0.882116973400116})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 0.8816062808036804})
store['active_learning_steps'][29]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.9206019639968872})
store['active_learning_steps'][29]['eval_training']['best_epoch']=5
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 19888], ['id', 56348], ['ood', 37058], ['id', 2434], ['id', 3530]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [0.597578991617409, 1.079842657477668, 1.4995181906607975, 1.7724850725846997, 1.99000747180009]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.3210160732269287})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.02980375289917})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.1048762798309326})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.0874547958374023})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 1.166429877281189})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.1826255321502686})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.342673420906067})
store['active_learning_steps'][30]['training']['best_epoch']=4
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7295, 'crossentropy': 1.08919384765625}
store['active_learning_steps'][30]['eval_training']={}
store['active_learning_steps'][30]['eval_training']['epochs']=[]
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.0983755588531494})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 0.9354091882705688})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 0.8771893978118896})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.8818033933639526})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 0.8630467653274536})
store['active_learning_steps'][30]['eval_training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 0.8775879144668579})
store['active_learning_steps'][30]['eval_training']['best_epoch']=3
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 29741], ['id', 46507], ['id', 19771], ['id', 54881], ['id', 36843]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.4910745272565411, 0.9276010611888359, 1.3153156827783086, 1.6620809111268615, 1.926076206648644]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.2676258087158203})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 1.0577490329742432})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 1.008294701576233})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.71484375, 'crossentropy': 1.0738646984100342})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 1.1948838233947754})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.174703598022461})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.3947219848632812})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.285213828086853})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.3762342929840088})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 1.4021785259246826})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.4131958484649658})
store['active_learning_steps'][31]['training']['best_epoch']=8
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7534, 'crossentropy': 1.26814091796875}
store['active_learning_steps'][31]['eval_training']={}
store['active_learning_steps'][31]['eval_training']['epochs']=[]
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 1.0639102458953857})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.9230114221572876})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 0.8650195002555847})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 0.8794946670532227})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 0.8498255014419556})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 0.8863220810890198})
store['active_learning_steps'][31]['eval_training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 0.9030457735061646})
store['active_learning_steps'][31]['eval_training']['best_epoch']=4
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 4730], ['id', 9199], ['id', 10452], ['id', 50437], ['id', 46543]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.6082776777809472, 1.143633909621661, 1.619116898552723, 2.005026223495528, 2.3197011813254624]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.3176581859588623})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 1.0540884733200073})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.0417994260787964})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 0.9778565764427185})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.1324329376220703})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.1470582485198975})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 1.3715596199035645})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 1.4361873865127563})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.589134693145752})
store['active_learning_steps'][32]['training']['best_epoch']=6
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.7427, 'crossentropy': 1.15308564453125}
store['active_learning_steps'][32]['eval_training']={}
store['active_learning_steps'][32]['eval_training']['epochs']=[]
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.112973690032959})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6640625, 'crossentropy': 0.9880088567733765})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 0.9070720672607422})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 0.8906106948852539})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 0.8590792417526245})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.8817958831787109})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 0.8568077087402344})
store['active_learning_steps'][32]['eval_training']['epochs'].append({'accuracy': 0.701171875, 'crossentropy': 0.8839092254638672})
store['active_learning_steps'][32]['eval_training']['best_epoch']=5
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 9624], ['id', 19995], ['id', 36117], ['id', 8193], ['id', 18183]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5227297840008394, 0.9767569545917505, 1.3823201792569062, 1.7176120628802822, 1.971180155520761]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.3198349475860596})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.677734375, 'crossentropy': 1.0279481410980225})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 1.0212006568908691})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.017154574394226})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.136343002319336})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.1575170755386353})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.1905399560928345})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.3125420808792114})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.3105672597885132})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.3744949102401733})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.372553825378418})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 1.420778512954712})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.728515625, 'crossentropy': 1.607253909111023})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.5231006145477295})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.4371088743209839})
store['active_learning_steps'][33]['training']['best_epoch']=12
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7427, 'crossentropy': 1.47898251953125}
store['active_learning_steps'][33]['eval_training']={}
store['active_learning_steps'][33]['eval_training']['epochs']=[]
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.151313066482544})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 0.9950040578842163})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 0.9481185674667358})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 0.9488115310668945})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.9101766347885132})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 0.8911542892456055})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 0.8794881105422974})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.9245737195014954})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 0.9257290959358215})
store['active_learning_steps'][33]['eval_training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 0.9228025674819946})
store['active_learning_steps'][33]['eval_training']['best_epoch']=7
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 34743], ['id', 15389], ['id', 21355], ['id', 43430], ['id', 39409]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5897237013823153, 1.132822424478741, 1.6167039039162043, 2.0026267082979947, 2.2817262705433112]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 1.335184097290039})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.0291839838027954})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 1.0227769613265991})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7294921875, 'crossentropy': 1.0085358619689941})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7314453125, 'crossentropy': 1.065993309020996})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.139467477798462})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.1744239330291748})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7431640625, 'crossentropy': 1.30235755443573})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.4833815097808838})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.4044897556304932})
store['active_learning_steps'][34]['training']['best_epoch']=7
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.7369, 'crossentropy': 1.218017578125}
store['active_learning_steps'][34]['eval_training']={}
store['active_learning_steps'][34]['eval_training']['epochs']=[]
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.6728515625, 'crossentropy': 1.0672001838684082})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9490906000137329})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 0.9394831657409668})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 0.8457834720611572})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 0.8726080060005188})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 0.8472365140914917})
store['active_learning_steps'][34]['eval_training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 0.8709317445755005})
store['active_learning_steps'][34]['eval_training']['best_epoch']=4
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 5758], ['id', 52948], ['id', 57392], ['id', 16490], ['id', 22551]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.5475995429376641, 1.0636011710819564, 1.4917349970817302, 1.8355057228476221, 2.100730214893094]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 1.3175188302993774})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.1144264936447144})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9992191791534424})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 0.9933583736419678})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.039357304573059})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.1254115104675293})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 1.1076511144638062})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7236328125, 'crossentropy': 1.1982618570327759})
store['active_learning_steps'][35]['training']['best_epoch']=5
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.7318, 'crossentropy': 1.0267421875}
store['active_learning_steps'][35]['eval_training']={}
store['active_learning_steps'][35]['eval_training']['epochs']=[]
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 1.0837147235870361})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.666015625, 'crossentropy': 0.9760996103286743})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 0.9036136269569397})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 0.8671201467514038})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 0.8610494136810303})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 0.883065938949585})
store['active_learning_steps'][35]['eval_training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 0.8803999423980713})
store['active_learning_steps'][35]['eval_training']['best_epoch']=7
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 23444], ['id', 26871], ['id', 51599], ['id', 32065], ['id', 19607]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.45284232090608234, 0.8816728112420416, 1.273419349555093, 1.5807427076772882, 1.8328652430630612]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.53515625, 'crossentropy': 1.3116425275802612})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 1.0375711917877197})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 0.9487484693527222})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 0.9682152271270752})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.038968801498413})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.0398730039596558})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 1.1141029596328735})
store['active_learning_steps'][36]['training']['best_epoch']=4
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7433, 'crossentropy': 0.97175673828125}
