store = {}
store['timestamp']=1621478786
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=56']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=56
store['worker_id']=56
store['num_workers']=80
store['config']={'seed': 1293, 'uniform_ood': True, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('FastFashionMNIST Train (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[53434, 8533, 14640, 39579, 30392, 58125, 37915, 3091, 57520, 43803, 44119, 52296, 58226, 40334, 46037, 22015, 22304, 43812, 12640, 53689]
store['evaluation_set_indices']=[29974, 3792, 5573, 45567, 10508, 2728, 21423, 396, 49512, 31444]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.1730222702026367})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6669921875, 'crossentropy': 2.3892016410827637})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.659334182739258})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.8237171173095703})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6591796875, 'crossentropy': 2.708402633666992})
store['active_learning_steps'][0]['training']['best_epoch']=2
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6893, 'crossentropy': 2.330014453125}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 27130], ['id', 13203], ['id', 14655], ['id', 24968], ['id', 4799]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.3505651822844653, 2.395922785140782, 3.1812678282065807, 3.7302818952915606, 4.09870286360963]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.7749258279800415})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.1753087043762207})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.4562790393829346})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.5655860900878906})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.7154, 'crossentropy': 1.6704767578125}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 14484], ['id', 30064], ['id', 37089], ['id', 54461], ['id', 26022]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.1047470227781973, 2.074097465726397, 2.8501434704710125, 3.4177102514477165, 3.8304846472592002]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.790252685546875})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 2.110456705093384})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.2092933654785156})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.055225372314453})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.5815258026123047})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.4245753288269043})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 2.4634346961975098})
store['active_learning_steps'][2]['training']['best_epoch']=4
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7507, 'crossentropy': 1.934373828125}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 14329], ['id', 48752], ['id', 9588], ['id', 49784], ['id', 11625]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.2866606934568745, 2.4097879747358593, 3.2405888543678847, 3.8262307537964677, 4.18538082421823]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 1.6016618013381958})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.7838976383209229})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7392578125, 'crossentropy': 1.906806230545044})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.061440944671631})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7177734375, 'crossentropy': 2.3159890174865723})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.491098642349243})
store['active_learning_steps'][3]['training']['best_epoch']=3
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7571, 'crossentropy': 1.7771494140625}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 42139], ['id', 12117], ['id', 28199], ['id', 17855], ['id', 19298]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.2043302117828996, 2.24499226683907, 3.1250038387619243, 3.7297257718677272, 4.092073759270702]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.558010220527649})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 1.8126134872436523})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 2.0768778324127197})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 2.0008232593536377})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.025096893310547})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7158203125, 'crossentropy': 2.247812509536743})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.2023370265960693})
store['active_learning_steps'][4]['training']['best_epoch']=4
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7717, 'crossentropy': 1.73688671875}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 53170], ['id', 12155], ['id', 56474], ['id', 23584], ['id', 24716]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.2614826285832261, 2.340013841359306, 3.2151775707267225, 3.7813397859076296, 4.147697553613947]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.3712053298950195})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.393388271331787})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.7809617519378662})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.5554296970367432})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.9054601192474365})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.9118633270263672})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.9021694660186768})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.9420242309570312})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.8801846504211426})
store['active_learning_steps'][5]['training']['best_epoch']=6
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.8115, 'crossentropy': 1.57283173828125}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 20470], ['id', 40595], ['id', 49438], ['id', 41255], ['id', 54240]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.247830451235813, 2.301158925035118, 3.186516090627329, 3.7688960756724583, 4.1374467016458585]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.378647804260254})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.748046875, 'crossentropy': 1.487597942352295})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.75, 'crossentropy': 1.5742249488830566})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.5196902751922607})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 1.6871105432510376})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.7683521509170532})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 2.06558895111084})
store['active_learning_steps'][6]['training']['best_epoch']=4
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.784, 'crossentropy': 1.4173353515625}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 40657], ['id', 31264], ['id', 42709], ['id', 57523], ['id', 52086]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0763984784794398, 2.0233487462704676, 2.831988825029666, 3.4558710411822684, 3.8811309057349668]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.1903858184814453})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.0790413618087769})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.199951410293579})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.2137811183929443})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.297333002090454})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.4000585079193115})
store['active_learning_steps'][7]['training']['best_epoch']=3
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.8461, 'crossentropy': 1.08847783203125}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 47081], ['id', 28313], ['id', 47674], ['id', 9664], ['id', 31883]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1401372696049883, 2.1775381446498776, 3.0051720740666745, 3.6278416247787284, 4.024050617745123]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.0034406185150146})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0548405647277832})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.092585563659668})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.271285057067871})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.2347986698150635})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.3851702213287354})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 1.2649614810943604})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.2822613716125488})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.3379050493240356})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.4777276515960693})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.4963250160217285})
store['active_learning_steps'][8]['training']['best_epoch']=8
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.8668, 'crossentropy': 1.15464287109375}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 1075], ['id', 28512], ['id', 59380], ['id', 57433], ['id', 50233]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.2154252595623274, 2.2759575678584554, 3.1832491620612338, 3.803085224345721, 4.176966747958825]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9119186401367188})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9653981924057007})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9643937945365906})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.0798656940460205})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.0031071901321411})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.1013926267623901})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.1985950469970703})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.17578125})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1437567472457886})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.1814749240875244})
store['active_learning_steps'][9]['training']['best_epoch']=7
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.8739, 'crossentropy': 1.06176455078125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 40894], ['id', 28469], ['id', 14749], ['id', 24462], ['id', 22648]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.236951459396519, 2.3813512353911124, 3.316179733170486, 3.8898346297895063, 4.2223522980901755]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9562115669250488})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8903483152389526})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9827470779418945})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8802160024642944})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9174193739891052})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9616683721542358})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9510561227798462})
store['active_learning_steps'][10]['training']['best_epoch']=4
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.8807, 'crossentropy': 0.846683984375}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 1356], ['id', 8045], ['id', 25732], ['id', 21174], ['id', 43176]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.190239196563904, 2.2353004375136356, 3.0704302500515137, 3.6732895283833704, 4.0608118732220895]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9300988912582397})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8069021701812744})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7893189191818237})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8726245164871216})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.914784848690033})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7942401170730591})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8751801252365112})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8127702474594116})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0181388854980469})
store['active_learning_steps'][11]['training']['best_epoch']=6
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.9, 'crossentropy': 0.77705107421875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 43609], ['id', 27795], ['id', 50294], ['id', 23041], ['id', 11711]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1564861425778172, 2.1729626549934102, 3.0429705921309758, 3.684841929652464, 4.079774150300298]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.8932363986968994})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6899604201316833})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7463500499725342})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7614378929138184})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7400902509689331})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8194242119789124})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7971526384353638})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.8092465400695801})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8119460344314575})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.8668515682220459})
store['active_learning_steps'][12]['training']['best_epoch']=7
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.9052, 'crossentropy': 0.71411904296875}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 17213], ['id', 14769], ['id', 33338], ['id', 14305], ['id', 55618]], 'labels': [[0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612]], 'scores': [1.0890482790087574, 2.1052335385244314, 2.97476322506399, 3.591118239605681, 4.001327674351074]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9459201097488403})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.74796462059021})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7104249000549316})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.813734769821167})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8362131118774414})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7346292734146118})
store['active_learning_steps'][13]['training']['best_epoch']=3
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.8924, 'crossentropy': 0.699937939453125}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 32427], ['id', 37508], ['id', 8210], ['id', 19942], ['id', 48384]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.012012903344109, 1.9532549351330246, 2.7827353974001223, 3.423460607015592, 3.8639783436072355]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8867753148078918})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6889867782592773})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.776543378829956})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6841106414794922})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7070909738540649})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7693854570388794})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.827168345451355})
store['active_learning_steps'][14]['training']['best_epoch']=4
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.9038, 'crossentropy': 0.67872841796875}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 24887], ['id', 3691], ['id', 55906], ['id', 28215], ['id', 58560]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9965974238865476, 1.9436879290285427, 2.7646686856593004, 3.371322677074379, 3.8059897336088415]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0906651020050049})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8314248323440552})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7783008813858032})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.9021179676055908})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8837103843688965})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 1.0522115230560303})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.114332675933838})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9476913213729858})
store['active_learning_steps'][15]['training']['best_epoch']=5
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8919, 'crossentropy': 0.84443427734375}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 16025], ['id', 52697], ['id', 16302], ['id', 1074], ['id', 4666]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1292223361159417, 2.1716686458734524, 3.0419505903102335, 3.6808080182021925, 4.0717833360415145]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.958255410194397})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6885414719581604})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7099497318267822})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6967882513999939})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.796467661857605})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8577841520309448})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7533284425735474})
store['active_learning_steps'][16]['training']['best_epoch']=4
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8983, 'crossentropy': 0.643752490234375}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 45005], ['id', 32047], ['id', 46187], ['id', 1642], ['id', 47741]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0220032133543284, 1.976845174994064, 2.7449855395750564, 3.3561553249166556, 3.79388757677646]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.1164422035217285})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8199750781059265})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8343697786331177})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9124473333358765})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8437499403953552})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8368719816207886})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9924219846725464})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 1.033639669418335})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0949758291244507})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.9042, 'crossentropy': 0.740685009765625}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 11007], ['id', 22139], ['id', 7833], ['id', 36892], ['id', 51764]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0963301552698725, 2.116944571227374, 2.969013201620653, 3.5970998848791744, 4.014859867793904]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.0145725011825562})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6725513935089111})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7304638624191284})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.690774142742157})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6923997402191162})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8252943754196167})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.79115891456604})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.750638484954834})
store['active_learning_steps'][18]['training']['best_epoch']=5
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.9045, 'crossentropy': 0.6935185546875}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 49537], ['id', 45026], ['id', 52462], ['id', 25873], ['id', 42437]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.1892008116657917, 2.192923549860801, 3.031290883570575, 3.6280661369299434, 4.020131682248794]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.1482815742492676})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.829006016254425})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7699460983276367})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.73616623878479})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8039299249649048})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7903108596801758})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8754141330718994})
store['active_learning_steps'][19]['training']['best_epoch']=4
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8962, 'crossentropy': 0.687882861328125}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 33162], ['id', 39778], ['id', 8978], ['id', 55282], ['id', 49493]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0462586034011725, 1.9975231969398326, 2.7707137214054587, 3.377794485699525, 3.8391149120516967]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9836410284042358})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7586033344268799})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6899386644363403})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7431612014770508})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7956376075744629})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.8632971048355103})
store['active_learning_steps'][20]['training']['best_epoch']=3
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.9006, 'crossentropy': 0.673883642578125}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 40873], ['id', 46878], ['id', 31624], ['id', 11074], ['id', 32445]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9784053326747038, 1.8829911223587237, 2.651934678400119, 3.2450937481801425, 3.6891218278538602]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.1997917890548706})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6969062685966492})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6963514685630798})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6816556453704834})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.765360951423645})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8208568096160889})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7687270641326904})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8049204349517822})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7874191403388977})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8017844557762146})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8107081651687622})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7949166297912598})
store['active_learning_steps'][21]['training']['best_epoch']=9
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.9067, 'crossentropy': 0.7083181640625}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 34520], ['id', 38920], ['id', 13743], ['id', 15832], ['id', 2845]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.311372805265787, 2.3717031286469545, 3.252610297801527, 3.8362541943219473, 4.194695638134778]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.9988446831703186})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6901796460151672})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6677653789520264})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6690574884414673})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6672689914703369})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6477248668670654})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6824709177017212})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7462265491485596})
store['active_learning_steps'][22]['training']['best_epoch']=5
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.9064, 'crossentropy': 0.65600087890625}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 35246], ['id', 7681], ['id', 42415], ['id', 12956], ['id', 31738]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'scores': [1.0143521946649545, 1.960367657065695, 2.7959157162539654, 3.435509849771859, 3.874418910115147]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.170947790145874})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6371268630027771})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6380870938301086})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7331820726394653})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5933035612106323})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6806373000144958})
store['active_learning_steps'][23]['training']['best_epoch']=3
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.9126, 'crossentropy': 0.582342529296875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 48006], ['id', 3719], ['id', 51004], ['id', 24513], ['id', 52708]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [0.9152716891893067, 1.7755741383589068, 2.496173930397955, 3.0836664538900216, 3.531962079419867]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7265625, 'crossentropy': 1.2616641521453857})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6744793653488159})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.671916127204895})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6904114484786987})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6756247282028198})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7280796766281128})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6491032838821411})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6678588390350342})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6479314565658569})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6526830196380615})
store['active_learning_steps'][24]['training']['best_epoch']=7
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.9211, 'crossentropy': 0.6126359375}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 59314], ['id', 27739], ['id', 5013], ['id', 30932], ['id', 17684]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1084524511325848, 2.143967200380141, 3.035192642737808, 3.65926938525309, 4.068343586613498]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.1548635959625244})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6805047988891602})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6000041961669922})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6481530070304871})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7681716680526733})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6850695610046387})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.658745288848877})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7214783430099487})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6850649118423462})
store['active_learning_steps'][25]['training']['best_epoch']=6
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.9202, 'crossentropy': 0.62606611328125}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 47409], ['id', 3762], ['id', 44350], ['id', 8116], ['id', 55881]], 'labels': [[0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0609927874808465, 2.0659329836970883, 2.933786497188093, 3.576615028416761, 3.98628024570308]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7421875, 'crossentropy': 1.266843557357788})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6939188241958618})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6438695192337036})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5808367133140564})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5997627973556519})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6446642279624939})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6766314506530762})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.700447678565979})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7062654495239258})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.69806307554245})
store['active_learning_steps'][26]['training']['best_epoch']=7
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.908, 'crossentropy': 0.682848486328125}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 40732], ['id', 48], ['id', 28536], ['id', 52624], ['id', 38698]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0705611261520167, 2.0730924658715493, 2.9300264218511547, 3.573411379286087, 3.988128356834986]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.1209604740142822})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7057111263275146})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7694860696792603})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6704131960868835})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7699759006500244})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6682089567184448})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7378833293914795})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7957078218460083})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7835466861724854})
store['active_learning_steps'][27]['training']['best_epoch']=6
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.9099, 'crossentropy': 0.6225552734375}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 5175], ['id', 46406], ['id', 7851], ['id', 2548], ['id', 49517]], 'labels': [[0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'scores': [1.0176993405534605, 1.9232447168976, 2.735866571036687, 3.378746243031717, 3.8303859887509972]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.073617696762085})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7044626474380493})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6412033438682556})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5901565551757812})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6144832372665405})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6979149580001831})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6920455694198608})
store['active_learning_steps'][28]['training']['best_epoch']=4
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.913, 'crossentropy': 0.56204384765625}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 28272], ['id', 12372], ['id', 9778], ['id', 52149], ['id', 7160]], 'labels': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0042830879597513, 1.9565609634908858, 2.684531573515807, 3.277812964595281, 3.714385619403542]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.2258062362670898})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6603413820266724})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5827308893203735})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6714155673980713})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5943868160247803})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5821777582168579})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.649297833442688})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6132194995880127})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6629244089126587})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7523678541183472})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5930109620094299})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7718491554260254})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.768476128578186})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6653336882591248})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6779300570487976})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.6875847578048706})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7408650517463684})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.8573945760726929})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.7715998291969299})
store['active_learning_steps'][29]['training']['best_epoch']=16
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.9261, 'crossentropy': 0.67791240234375}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 49082], ['id', 53979], ['id', 42438], ['id', 24934], ['id', 51452]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [1.2356319295734337, 2.286990022298526, 3.1561910240417195, 3.792756456247451, 4.186070936757551]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.0093233585357666})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6540799140930176})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5288268327713013})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5425077676773071})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6135781407356262})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5917737483978271})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5471173524856567})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6264501810073853})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6401191353797913})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.619231104850769})
store['active_learning_steps'][30]['training']['best_epoch']=7
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.9289, 'crossentropy': 0.529688623046875}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 18598], ['id', 20171], ['id', 37450], ['id', 49567], ['id', 33364]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.0844888045017826, 2.096920716817116, 2.944999711344714, 3.5620008217383035, 3.9744244043069177]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 1.2114226818084717})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.666691780090332})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6125867366790771})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6220829486846924})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5525708794593811})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5481653213500977})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6101100444793701})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6213850975036621})
store['active_learning_steps'][31]['training']['best_epoch']=5
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.9245, 'crossentropy': 0.544977880859375}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 55054], ['id', 57718], ['id', 31562], ['id', 28757], ['id', 34916]], 'labels': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612, 0.10000000149011612], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0]], 'scores': [0.9423177419048556, 1.830599753973848, 2.605518227240009, 3.243387256566706, 3.72160447338039]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.1297073364257812})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6694296598434448})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6348636746406555})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6192328929901123})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5620641708374023})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.658880352973938})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5774482488632202})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6497331857681274})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5863447189331055})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.607130765914917})
store['active_learning_steps'][32]['training']['best_epoch']=7
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.9265, 'crossentropy': 0.552117431640625}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 45602], ['id', 36818], ['id', 8668], ['id', 28412], ['id', 56152]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.040514764358166, 1.9745649156411207, 2.781964422349529, 3.430093466601149, 3.864187716931692]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 1.3174288272857666})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7226786613464355})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5760678052902222})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5303854942321777})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5790060758590698})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5041640400886536})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5026705265045166})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5073797702789307})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.5691647529602051})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5391432642936707})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5490765571594238})
store['active_learning_steps'][33]['training']['best_epoch']=8
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.9338, 'crossentropy': 0.5196529296875}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 8892], ['id', 11572], ['id', 30680], ['id', 52014], ['id', 47278]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.108169630337846, 2.0539166002013567, 2.85368474133817, 3.4798271354766737, 3.9342182203287477]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.2133595943450928})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7408815622329712})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.583588719367981})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5021480321884155})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.93359375, 'crossentropy': 0.4896440804004669})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9404296875, 'crossentropy': 0.49121174216270447})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5537136793136597})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5203899145126343})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5681473016738892})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5947024822235107})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.5305068492889404})
store['active_learning_steps'][34]['training']['best_epoch']=8
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.9372, 'crossentropy': 0.523836376953125}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 59747], ['id', 3644], ['id', 6582], ['id', 52138], ['id', 32776]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'scores': [1.1506435281792784, 2.1179543631479305, 2.952865295088264, 3.575295714879532, 4.006089740395431]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.3418912887573242})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.712897539138794})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5858677625656128})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5525184869766235})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.6299523711204529})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9365234375, 'crossentropy': 0.5261346101760864})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5633217692375183})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5740630626678467})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.939453125, 'crossentropy': 0.5371518135070801})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9375, 'crossentropy': 0.571560800075531})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5860086679458618})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.9443359375, 'crossentropy': 0.5460180044174194})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5674455165863037})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6141841411590576})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.94140625, 'crossentropy': 0.5793166160583496})
store['active_learning_steps'][35]['training']['best_epoch']=12
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.9345, 'crossentropy': 0.555849658203125}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 57728], ['id', 7924], ['id', 37118], ['id', 12305], ['id', 16488]], 'labels': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'scores': [1.2190891379882078, 2.2477034754910856, 3.103809159298798, 3.7175941475724805, 4.110285948710528]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.75390625, 'crossentropy': 1.4144823551177979})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7722667455673218})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6137987375259399})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5854779481887817})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4844125509262085})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5488837361335754})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5130963325500488})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.935546875, 'crossentropy': 0.5211697816848755})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5640366077423096})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5582721829414368})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5752317905426025})
store['active_learning_steps'][36]['training']['best_epoch']=8
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.9339, 'crossentropy': 0.519098193359375}
