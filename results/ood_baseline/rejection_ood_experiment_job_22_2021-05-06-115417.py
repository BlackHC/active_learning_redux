store = {}
store['timestamp']=1620298457
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=22']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=22
store['worker_id']=22
store['num_workers']=40
store['config']={'seed': 24, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.2948968410491943})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6708984375, 'crossentropy': 2.566664218902588})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.695650339126587})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.797071933746338})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7067, 'crossentropy': 1.9093046875}
store['active_learning_steps'][0]['acquisition']={'indices': [22724, 58580, 10346, 54771, 5160], 'labels': [8, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.512892723083496})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.0749874114990234})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.201324462890625})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.774510145187378})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6845, 'crossentropy': 2.13034453125}
store['active_learning_steps'][1]['acquisition']={'indices': [17198, 58393, 41760, 15112, 32124], 'labels': [-1, 7, 7, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.148406982421875})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 2.3130245208740234})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7587890625, 'crossentropy': 2.0502278804779053})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.750896692276001})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.4593465328216553})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 2.5311076641082764})
store['active_learning_steps'][2]['training']['best_epoch']=3
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7725, 'crossentropy': 1.9138013671875}
store['active_learning_steps'][2]['acquisition']={'indices': [18906, 47471, 15999, 17617, 26015], 'labels': [1, 5, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.03794002532959})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.3173670768737793})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.219909191131592})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.6412224769592285})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7082, 'crossentropy': 1.7737041015625}
store['active_learning_steps'][3]['acquisition']={'indices': [32748, 32268, 30894, 2848, 29643], 'labels': [-1, -1, -1, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.072230339050293})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.0924525260925293})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.689453125, 'crossentropy': 2.699160575866699})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.2432920932769775})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.7105, 'crossentropy': 1.8222544921875}
store['active_learning_steps'][4]['acquisition']={'indices': [20976, 40423, 56949, 32542, 28038], 'labels': [5, -1, 0, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.2428855895996094})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6748046875, 'crossentropy': 2.618607997894287})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 3.0194625854492188})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.8332176208496094})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6948, 'crossentropy': 2.0041310546875}
store['active_learning_steps'][5]['acquisition']={'indices': [29460, 46981, 6434, 45584, 13090], 'labels': [-1, -1, 5, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.133492946624756})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 2.134857654571533})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.7108891010284424})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.937000274658203})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7014, 'crossentropy': 1.89056640625}
store['active_learning_steps'][6]['acquisition']={'indices': [20668, 8025, 8998, 50615, 20181], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.5229344367980957})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.510338068008423})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.256685256958008})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.783646583557129})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.972039222717285})
store['active_learning_steps'][7]['training']['best_epoch']=2
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.6807, 'crossentropy': 2.292209765625}
store['active_learning_steps'][7]['acquisition']={'indices': [30579, 42951, 51060, 55825, 40849], 'labels': [7, 3, 1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.0532286167144775})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.6267504692077637})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.6882481575012207})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.0989789962768555})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6866, 'crossentropy': 1.9466419921875}
store['active_learning_steps'][8]['acquisition']={'indices': [18073, 57286, 13338, 18682, 17500], 'labels': [0, -1, 1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.1699204444885254})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.560142993927002})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.3014044761657715})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 2.5523996353149414})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.6859, 'crossentropy': 1.8590013671875}
store['active_learning_steps'][9]['acquisition']={'indices': [16001, 28727, 2582, 9546, 40662], 'labels': [-1, 6, 0, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6953125, 'crossentropy': 1.883000135421753})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 2.3906521797180176})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.532991409301758})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.708984375, 'crossentropy': 2.6913461685180664})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7266, 'crossentropy': 1.6850265625}
store['active_learning_steps'][10]['acquisition']={'indices': [34185, 39972, 36359, 19418, 17805], 'labels': [4, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6923828125, 'crossentropy': 1.9927620887756348})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6767578125, 'crossentropy': 2.3943891525268555})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.598237991333008})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 2.850775718688965})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.7211, 'crossentropy': 1.631515234375}
store['active_learning_steps'][11]['acquisition']={'indices': [26047, 31789, 43610, 50630, 28486], 'labels': [-1, 2, 0, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6845703125, 'crossentropy': 1.9480149745941162})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6826171875, 'crossentropy': 2.505016326904297})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.4430153369903564})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.69921875, 'crossentropy': 2.4627418518066406})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7132, 'crossentropy': 1.746512890625}
store['active_learning_steps'][12]['acquisition']={'indices': [24453, 281, 54966, 9360, 42925], 'labels': [6, -1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 1.7128338813781738})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.68359375, 'crossentropy': 2.1678690910339355})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.0017008781433105})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 2.339160442352295})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7187, 'crossentropy': 1.5611125}
store['active_learning_steps'][13]['acquisition']={'indices': [57540, 31184, 13973, 16498, 58659], 'labels': [7, -1, 1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.703125, 'crossentropy': 1.907485842704773})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 2.0072007179260254})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7373046875, 'crossentropy': 2.3141252994537354})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 2.147495985031128})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7252, 'crossentropy': 1.7266232421875}
store['active_learning_steps'][14]['acquisition']={'indices': [35658, 14897, 44741, 34399, 52437], 'labels': [3, 0, 9, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7333984375, 'crossentropy': 1.73222017288208})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 2.0960283279418945})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7470703125, 'crossentropy': 2.001445770263672})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7412109375, 'crossentropy': 2.233590841293335})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7518, 'crossentropy': 1.58231025390625}
store['active_learning_steps'][15]['acquisition']={'indices': [56346, 46808, 22334, 45863, 16600], 'labels': [7, 5, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7001953125, 'crossentropy': 1.6816496849060059})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7548828125, 'crossentropy': 1.8685553073883057})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 2.034393787384033})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.9813250303268433})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7497, 'crossentropy': 1.4936166015625}
store['active_learning_steps'][16]['acquisition']={'indices': [21781, 46720, 41063, 23740, 13136], 'labels': [6, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.7107845544815063})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7109375, 'crossentropy': 2.2236874103546143})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 2.281538486480713})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.740234375, 'crossentropy': 2.1568048000335693})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.7337, 'crossentropy': 1.57915751953125}
store['active_learning_steps'][17]['acquisition']={'indices': [3009, 7474, 22269, 49418, 19169], 'labels': [4, 9, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.5054035186767578})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.7497193813323975})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.9603440761566162})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 2.0518510341644287})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.7716, 'crossentropy': 1.39303193359375}
store['active_learning_steps'][18]['acquisition']={'indices': [48345, 19154, 35501, 54841, 52771], 'labels': [-1, 2, 8, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.1992754936218262})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.2748916149139404})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.4108357429504395})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.6710487604141235})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8122, 'crossentropy': 1.08756845703125}
store['active_learning_steps'][19]['acquisition']={'indices': [33074, 43612, 56544, 22884, 57131], 'labels': [8, -1, -1, 2, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.2561097145080566})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.6555479764938354})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.6931487321853638})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.822279453277588})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.7879, 'crossentropy': 1.20393349609375}
store['active_learning_steps'][20]['acquisition']={'indices': [13923, 59304, 28456, 16707, 21711], 'labels': [-1, -1, 0, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.270361304283142})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.5283901691436768})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.562312126159668})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.8028697967529297})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.7985, 'crossentropy': 1.21160869140625}
store['active_learning_steps'][21]['acquisition']={'indices': [50861, 2130, 56613, 1431, 21314], 'labels': [-1, 3, 8, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.23598313331604})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.280069351196289})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.3905832767486572})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.4958505630493164})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8308, 'crossentropy': 1.04523125}
store['active_learning_steps'][22]['acquisition']={'indices': [19715, 58780, 41763, 31719, 3540], 'labels': [9, -1, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.3036370277404785})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.4406828880310059})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.6635816097259521})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.6636548042297363})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.7877, 'crossentropy': 1.2781220703125}
store['active_learning_steps'][23]['acquisition']={'indices': [52127, 36029, 38762, 56090, 7783], 'labels': [9, 9, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.20841646194458})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.3135945796966553})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.4816679954528809})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.6273977756500244})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8067, 'crossentropy': 1.1401630859375}
store['active_learning_steps'][24]['acquisition']={'indices': [43350, 44745, 56975, 28615, 29154], 'labels': [-1, 1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.3336470127105713})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.783203125, 'crossentropy': 1.7089223861694336})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.7214202880859375})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.6635000705718994})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8098, 'crossentropy': 1.16669375}
store['active_learning_steps'][25]['acquisition']={'indices': [42844, 25715, 16590, 290, 30625], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.3038220405578613})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.4926133155822754})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.8062992095947266})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.7787799835205078})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.7909, 'crossentropy': 1.23721162109375}
store['active_learning_steps'][26]['acquisition']={'indices': [25580, 5807, 37912, 34536, 6558], 'labels': [-1, -1, 3, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.3074569702148438})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.643342137336731})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.7979975938796997})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.9364984035491943})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.7814, 'crossentropy': 1.26657587890625}
store['active_learning_steps'][27]['acquisition']={'indices': [44198, 11121, 40560, 5571, 22614], 'labels': [-1, 8, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1120696067810059})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.3488596677780151})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.772810459136963})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.6440623998641968})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8114, 'crossentropy': 1.0289150390625}
store['active_learning_steps'][28]['acquisition']={'indices': [46736, 56548, 48722, 22356, 27931], 'labels': [3, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.2931437492370605})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.561981439590454})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.7797975540161133})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.88426673412323})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8012, 'crossentropy': 1.227436328125}
store['active_learning_steps'][29]['acquisition']={'indices': [4973, 34345, 58027, 47074, 43347], 'labels': [9, 0, -1, 8, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.3078292608261108})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.3795862197875977})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.485588788986206})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.6172316074371338})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8002, 'crossentropy': 1.14370322265625}
store['active_learning_steps'][30]['acquisition']={'indices': [38950, 39799, 40033, 29032, 19681], 'labels': [-1, -1, 1, 7, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.1685497760772705})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.3231754302978516})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.527388095855713})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.4859299659729004})
store['active_learning_steps'][31]['training']['best_epoch']=1
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8026, 'crossentropy': 1.10161640625}
store['active_learning_steps'][31]['acquisition']={'indices': [1021, 21108, 55688, 46052, 5600], 'labels': [3, 9, 3, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.152336835861206})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.4295718669891357})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 1.3964258432388306})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.5685590505599976})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8181, 'crossentropy': 1.09860966796875}
store['active_learning_steps'][32]['acquisition']={'indices': [49213, 10870, 33361, 10059, 11847], 'labels': [9, 4, -1, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.2006001472473145})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.3097178936004639})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.5124092102050781})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.6095836162567139})
store['active_learning_steps'][33]['training']['best_epoch']=1
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.7946, 'crossentropy': 1.15534169921875}
store['active_learning_steps'][33]['acquisition']={'indices': [35948, 19273, 18034, 29954, 10428], 'labels': [-1, 1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0604751110076904})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.2390546798706055})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.4947614669799805})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.5633654594421387})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.823, 'crossentropy': 0.99391181640625}
store['active_learning_steps'][34]['acquisition']={'indices': [43376, 20907, 12325, 38195, 52222], 'labels': [2, -1, 0, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0154836177825928})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.29459547996521})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.28767991065979})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.4732539653778076})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8204, 'crossentropy': 0.99184716796875}
store['active_learning_steps'][35]['acquisition']={'indices': [10247, 7000, 44164, 59531, 58107], 'labels': [-1, -1, 5, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0640292167663574})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.1174829006195068})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1765748262405396})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.3357198238372803})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8309, 'crossentropy': 0.9381787109375}
store['active_learning_steps'][36]['acquisition']={'indices': [54714, 26031, 56196, 46495, 27968], 'labels': [-1, -1, 7, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.08228600025177})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0820400714874268})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.2393416166305542})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.3958090543746948})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.6944172382354736})
store['active_learning_steps'][37]['training']['best_epoch']=2
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8372, 'crossentropy': 1.09213232421875}
store['active_learning_steps'][37]['acquisition']={'indices': [56658, 11689, 2310, 51713, 47704], 'labels': [5, -1, 0, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.063425064086914})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.2000950574874878})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.206646203994751})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.2989048957824707})
store['active_learning_steps'][38]['training']['best_epoch']=1
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.7915, 'crossentropy': 1.07813251953125}
store['active_learning_steps'][38]['acquisition']={'indices': [39183, 59903, 30924, 54999, 52175], 'labels': [-1, -1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.1211559772491455})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.2966943979263306})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 1.2162895202636719})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.3606314659118652})
store['active_learning_steps'][39]['training']['best_epoch']=1
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8052, 'crossentropy': 1.0592814453125}
store['active_learning_steps'][39]['acquisition']={'indices': [53281, 52757, 58925, 33368, 57493], 'labels': [8, -1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.0630278587341309})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.2863578796386719})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.4242489337921143})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.3992927074432373})
store['active_learning_steps'][40]['training']['best_epoch']=1
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8182, 'crossentropy': 1.0144513671875}
store['active_learning_steps'][40]['acquisition']={'indices': [13728, 58271, 39623, 11479, 22185], 'labels': [-1, -1, -1, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9181731939315796})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1885427236557007})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.1522010564804077})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 1.2221723794937134})
store['active_learning_steps'][41]['training']['best_epoch']=1
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8183, 'crossentropy': 0.97443046875}
store['active_learning_steps'][41]['acquisition']={'indices': [58276, 59888, 27447, 33132, 1021], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9710561037063599})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.1619386672973633})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.1525578498840332})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.2184785604476929})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8185, 'crossentropy': 0.97301064453125}
store['active_learning_steps'][42]['acquisition']={'indices': [59751, 10127, 9820, 54779, 27307], 'labels': [-1, 2, 0, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9664355516433716})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0332353115081787})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0480449199676514})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.1752105951309204})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8218, 'crossentropy': 0.96890830078125}
store['active_learning_steps'][43]['acquisition']={'indices': [42947, 26097, 5617, 1242, 31194], 'labels': [1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9340752363204956})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.0056447982788086})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0930203199386597})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.2800416946411133})
store['active_learning_steps'][44]['training']['best_epoch']=1
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8123, 'crossentropy': 0.9544373046875}
store['active_learning_steps'][44]['acquisition']={'indices': [28829, 54308, 12339, 34616, 52516], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9909799695014954})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.1123148202896118})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.0958445072174072})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.109633445739746})
store['active_learning_steps'][45]['training']['best_epoch']=1
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8216, 'crossentropy': 0.9810638671875}
store['active_learning_steps'][45]['acquisition']={'indices': [33825, 46096, 7916, 13904, 27906], 'labels': [5, 6, 2, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.8948554396629333})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9568686485290527})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.0737276077270508})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.1935737133026123})
store['active_learning_steps'][46]['training']['best_epoch']=1
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8233, 'crossentropy': 0.90328857421875}
store['active_learning_steps'][46]['acquisition']={'indices': [5143, 21342, 30099, 57833, 46790], 'labels': [3, 1, 9, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8972048759460449})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 0.9952664375305176})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9992086887359619})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.028639316558838})
store['active_learning_steps'][47]['training']['best_epoch']=1
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.834, 'crossentropy': 0.8359890625}
store['active_learning_steps'][47]['acquisition']={'indices': [45910, 5214, 32928, 13797, 33308], 'labels': [6, 7, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8665189743041992})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9176188707351685})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9518355131149292})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.0869104862213135})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8429, 'crossentropy': 0.83528583984375}
store['active_learning_steps'][48]['acquisition']={'indices': [8729, 29011, 39977, 54317, 100], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9749395847320557})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9678177833557129})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.1181418895721436})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.1005704402923584})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 1.207524061203003})
store['active_learning_steps'][49]['training']['best_epoch']=2
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8616, 'crossentropy': 0.9071994140625}
store['active_learning_steps'][49]['acquisition']={'indices': [27203, 17957, 17267, 42969, 13676], 'labels': [7, 8, 7, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.8604347109794617})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.020691990852356})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9336365461349487})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.1000969409942627})
store['active_learning_steps'][50]['training']['best_epoch']=1
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8479, 'crossentropy': 0.8486130859375}
store['active_learning_steps'][50]['acquisition']={'indices': [30090, 28900, 43304, 35418, 3327], 'labels': [-1, 3, 6, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 0.8411104083061218})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9270838499069214})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9629414081573486})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.1857051849365234})
store['active_learning_steps'][51]['training']['best_epoch']=1
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8494, 'crossentropy': 0.802931787109375}
store['active_learning_steps'][51]['acquisition']={'indices': [59649, 48200, 46985, 53160, 10423], 'labels': [8, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8729884028434753})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.9720492362976074})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9203073978424072})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.0013177394866943})
store['active_learning_steps'][52]['training']['best_epoch']=1
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8364, 'crossentropy': 0.8237728515625}
store['active_learning_steps'][52]['acquisition']={'indices': [39075, 57259, 10838, 54665, 953], 'labels': [-1, 9, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9788686037063599})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8937805891036987})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0469927787780762})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 1.0461280345916748})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.1310107707977295})
store['active_learning_steps'][53]['training']['best_epoch']=2
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8798, 'crossentropy': 0.769848095703125}
store['active_learning_steps'][53]['acquisition']={'indices': [57465, 45918, 55353, 37921, 17332], 'labels': [7, -1, 3, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8483742475509644})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8897453546524048})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9909697771072388})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.1825697422027588})
store['active_learning_steps'][54]['training']['best_epoch']=1
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8584, 'crossentropy': 0.757333447265625}
store['active_learning_steps'][54]['acquisition']={'indices': [10876, 29600, 33575, 55833, 58976], 'labels': [-1, 4, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7960449457168579})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8868939280509949})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.977336585521698})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.008805751800537})
store['active_learning_steps'][55]['training']['best_epoch']=1
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8536, 'crossentropy': 0.79177353515625}
store['active_learning_steps'][55]['acquisition']={'indices': [54686, 28369, 32672, 55672, 15297], 'labels': [-1, -1, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8350455164909363})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9402500987052917})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9392478466033936})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.0121794939041138})
store['active_learning_steps'][56]['training']['best_epoch']=1
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8495, 'crossentropy': 0.765139794921875}
store['active_learning_steps'][56]['acquisition']={'indices': [12704, 15007, 43559, 14191, 17751], 'labels': [1, -1, -1, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9292258024215698})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.9265965819358826})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8989764451980591})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9881068468093872})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 1.1499379873275757})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0739203691482544})
store['active_learning_steps'][57]['training']['best_epoch']=3
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8867, 'crossentropy': 0.78852763671875}
store['active_learning_steps'][57]['acquisition']={'indices': [22366, 24220, 30062, 46245, 11137], 'labels': [3, 6, 3, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8923054933547974})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8947818279266357})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9184888601303101})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9706484079360962})
store['active_learning_steps'][58]['training']['best_epoch']=1
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8422, 'crossentropy': 0.83122001953125}
store['active_learning_steps'][58]['acquisition']={'indices': [20800, 40766, 14577, 43061, 50872], 'labels': [3, -1, 3, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8259700536727905})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8285059928894043})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9624758958816528})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 1.0184390544891357})
store['active_learning_steps'][59]['training']['best_epoch']=1
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8647, 'crossentropy': 0.747791015625}
store['active_learning_steps'][59]['acquisition']={'indices': [25072, 24896, 34085, 8824, 44892], 'labels': [-1, -1, 3, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.8683464527130127})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7743372917175293})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9449924230575562})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 1.0001237392425537})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9550763368606567})
store['active_learning_steps'][60]['training']['best_epoch']=2
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.895, 'crossentropy': 0.664363037109375}
store['active_learning_steps'][60]['acquisition']={'indices': [40561, 18267, 6851, 16507, 23991], 'labels': [-1, -1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8397083282470703})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.9210971593856812})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8982413411140442})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 1.0030016899108887})
store['active_learning_steps'][61]['training']['best_epoch']=1
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8523, 'crossentropy': 0.783290869140625}
store['active_learning_steps'][61]['acquisition']={'indices': [50382, 37261, 41205, 57271, 16433], 'labels': [-1, 0, -1, 5, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8271676301956177})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.817695140838623})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9294322729110718})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9172649383544922})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9219541549682617})
store['active_learning_steps'][62]['training']['best_epoch']=2
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.8778, 'crossentropy': 0.751394677734375}
store['active_learning_steps'][62]['acquisition']={'indices': [3176, 40493, 24688, 9484, 21436], 'labels': [-1, -1, 1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8464586138725281})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.9779931902885437})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.9742830991744995})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.9304478764533997})
store['active_learning_steps'][63]['training']['best_epoch']=1
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8663, 'crossentropy': 0.76823212890625}
store['active_learning_steps'][63]['acquisition']={'indices': [51076, 21663, 51095, 2395, 4852], 'labels': [4, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7643564343452454})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9093296527862549})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9154915809631348})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9398362636566162})
store['active_learning_steps'][64]['training']['best_epoch']=1
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.867, 'crossentropy': 0.759786376953125}
store['active_learning_steps'][64]['acquisition']={'indices': [15094, 55800, 46418, 55380, 1441], 'labels': [2, 5, 5, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9218969941139221})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9623445868492126})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9495911598205566})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9494650363922119})
store['active_learning_steps'][65]['training']['best_epoch']=1
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8404, 'crossentropy': 0.84970322265625}
store['active_learning_steps'][65]['acquisition']={'indices': [7999, 39117, 18696, 42429, 47005], 'labels': [4, 4, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8365152478218079})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8547396659851074})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8139514327049255})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9260945320129395})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9419969916343689})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 1.136060118675232})
store['active_learning_steps'][66]['training']['best_epoch']=3
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8971, 'crossentropy': 0.724467626953125}
store['active_learning_steps'][66]['acquisition']={'indices': [24169, 35252, 44103, 30117, 27504], 'labels': [4, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8335608243942261})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.776435136795044})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8165274858474731})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9847581386566162})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9524002075195312})
store['active_learning_steps'][67]['training']['best_epoch']=2
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.892, 'crossentropy': 0.6812724609375}
store['active_learning_steps'][67]['acquisition']={'indices': [1556, 57788, 13870, 39660, 45948], 'labels': [-1, 3, 4, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7982414960861206})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.801111102104187})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8115432858467102})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8986027240753174})
store['active_learning_steps'][68]['training']['best_epoch']=1
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8685, 'crossentropy': 0.73802314453125}
store['active_learning_steps'][68]['acquisition']={'indices': [52181, 42981, 23247, 51192, 34702], 'labels': [7, -1, -1, 9, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8151638507843018})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8690481781959534})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8302320241928101})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.9509119987487793})
store['active_learning_steps'][69]['training']['best_epoch']=1
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.864, 'crossentropy': 0.730872607421875}
store['active_learning_steps'][69]['acquisition']={'indices': [6805, 45581, 24140, 29556, 8020], 'labels': [-1, 6, 7, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7853256464004517})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7960407137870789})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.91557776927948})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8990021347999573})
store['active_learning_steps'][70]['training']['best_epoch']=1
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8641, 'crossentropy': 0.743904638671875}
store['active_learning_steps'][70]['acquisition']={'indices': [35735, 537, 3502, 36303, 12672], 'labels': [-1, -1, 8, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8363058567047119})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7822583317756653})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.864106297492981})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.9052226543426514})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9885117411613464})
store['active_learning_steps'][71]['training']['best_epoch']=2
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9037, 'crossentropy': 0.67887099609375}
store['active_learning_steps'][71]['acquisition']={'indices': [22855, 30990, 20314, 28094, 12271], 'labels': [-1, 7, -1, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7463394999504089})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.709105372428894})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8020472526550293})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9902003407478333})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.9506937265396118})
store['active_learning_steps'][72]['training']['best_epoch']=2
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.8985, 'crossentropy': 0.638639990234375}
store['active_learning_steps'][72]['acquisition']={'indices': [47547, 45452, 6165, 45002, 37269], 'labels': [-1, -1, 1, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7857655882835388})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8006806373596191})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7308604717254639})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8884512186050415})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.957513689994812})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9123108386993408})
store['active_learning_steps'][73]['training']['best_epoch']=3
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9112, 'crossentropy': 0.654879833984375}
store['active_learning_steps'][73]['acquisition']={'indices': [40458, 6187, 53393, 44128, 5969], 'labels': [9, 8, -1, 6, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.806882381439209})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.8624216318130493})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.9758718013763428})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.9612898826599121})
store['active_learning_steps'][74]['training']['best_epoch']=1
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.8573, 'crossentropy': 0.755410009765625}
store['active_learning_steps'][74]['acquisition']={'indices': [40615, 17982, 54615, 7469, 48917], 'labels': [-1, 6, 3, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8175063133239746})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7979338765144348})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8538429141044617})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8736498951911926})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8646767139434814})
store['active_learning_steps'][75]['training']['best_epoch']=2
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.899, 'crossentropy': 0.685601416015625}
store['active_learning_steps'][75]['acquisition']={'indices': [26658, 44366, 23020, 39897, 14083], 'labels': [-1, -1, 2, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7652949690818787})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7104852795600891})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7775653600692749})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9541391134262085})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8426551818847656})
store['active_learning_steps'][76]['training']['best_epoch']=2
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.9068, 'crossentropy': 0.615190283203125}
store['active_learning_steps'][76]['acquisition']={'indices': [37621, 35144, 17394, 45313, 17360], 'labels': [6, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7753607034683228})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7434633374214172})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8694368004798889})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.878406286239624})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8936827778816223})
store['active_learning_steps'][77]['training']['best_epoch']=2
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9004, 'crossentropy': 0.643284912109375}
store['active_learning_steps'][77]['acquisition']={'indices': [38986, 35514, 33317, 4016, 47981], 'labels': [-1, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8477069139480591})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8006137609481812})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8600705862045288})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.932437539100647})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9833553433418274})
store['active_learning_steps'][78]['training']['best_epoch']=2
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.8866, 'crossentropy': 0.71533505859375}
store['active_learning_steps'][78]['acquisition']={'indices': [52385, 26634, 1128, 10536, 35154], 'labels': [-1, 4, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8070029616355896})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7607904672622681})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7457357048988342})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8909860849380493})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.8404358625411987})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9620957374572754})
store['active_learning_steps'][79]['training']['best_epoch']=3
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9037, 'crossentropy': 0.652814990234375}
store['active_learning_steps'][79]['acquisition']={'indices': [34215, 24284, 43369, 37197, 30680], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8687409162521362})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8557349443435669})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8023035526275635})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.909525990486145})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8369660377502441})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 1.0258610248565674})
store['active_learning_steps'][80]['training']['best_epoch']=3
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.8987, 'crossentropy': 0.687652734375}
store['active_learning_steps'][80]['acquisition']={'indices': [53138, 4056, 45880, 12944, 39825], 'labels': [-1, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8214589953422546})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7688772678375244})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7873164415359497})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8176881670951843})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9157403707504272})
store['active_learning_steps'][81]['training']['best_epoch']=2
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.8944, 'crossentropy': 0.70685673828125}
store['active_learning_steps'][81]['acquisition']={'indices': [29384, 37079, 27561, 17831, 5189], 'labels': [5, 0, 7, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7949249744415283})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.8240684270858765})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.9012316465377808})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.9281637668609619})
store['active_learning_steps'][82]['training']['best_epoch']=1
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.8677, 'crossentropy': 0.7220484375}
store['active_learning_steps'][82]['acquisition']={'indices': [33910, 51672, 50687, 34854, 29868], 'labels': [-1, -1, -1, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8182076215744019})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7858715057373047})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8218923807144165})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8381791114807129})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.9179869890213013})
store['active_learning_steps'][83]['training']['best_epoch']=2
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.8834, 'crossentropy': 0.73536181640625}
store['active_learning_steps'][83]['acquisition']={'indices': [57549, 22401, 9038, 43356, 47234], 'labels': [7, -1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.818928062915802})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7348045110702515})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8011819124221802})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9304841756820679})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8247084617614746})
store['active_learning_steps'][84]['training']['best_epoch']=2
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.8922, 'crossentropy': 0.691687890625}
store['active_learning_steps'][84]['acquisition']={'indices': [38070, 44823, 56111, 29363, 37768], 'labels': [2, -1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7868423461914062})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7573633193969727})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8150953054428101})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8622633218765259})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8491715788841248})
store['active_learning_steps'][85]['training']['best_epoch']=2
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.8904, 'crossentropy': 0.688309765625}
store['active_learning_steps'][85]['acquisition']={'indices': [46826, 20779, 6146, 32205, 34775], 'labels': [0, -1, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8490016460418701})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8849692940711975})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.918297290802002})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9266430139541626})
store['active_learning_steps'][86]['training']['best_epoch']=1
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.8592, 'crossentropy': 0.7873251953125}
store['active_learning_steps'][86]['acquisition']={'indices': [6874, 49706, 9826, 38818, 16950], 'labels': [-1, 1, 2, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7775942087173462})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.8235111236572266})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7970591187477112})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8424011468887329})
store['active_learning_steps'][87]['training']['best_epoch']=1
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.8635, 'crossentropy': 0.728927587890625}
store['active_learning_steps'][87]['acquisition']={'indices': [59088, 10434, 24412, 9046, 6158], 'labels': [-1, 5, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7885931730270386})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7371953725814819})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7939016819000244})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8375555276870728})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.9311413764953613})
store['active_learning_steps'][88]['training']['best_epoch']=2
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.885, 'crossentropy': 0.6616541015625}
store['active_learning_steps'][88]['acquisition']={'indices': [55887, 13006, 48121, 39420, 8130], 'labels': [-1, -1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7811048626899719})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7093883156776428})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8250855207443237})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.843725323677063})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.982440710067749})
store['active_learning_steps'][89]['training']['best_epoch']=2
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.8938, 'crossentropy': 0.672814111328125}
store['active_learning_steps'][89]['acquisition']={'indices': [42513, 53822, 26444, 42749, 52882], 'labels': [-1, 5, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.7859488725662231})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.68212890625})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7596235871315002})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7508509159088135})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7995721101760864})
store['active_learning_steps'][90]['training']['best_epoch']=2
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9091, 'crossentropy': 0.565692041015625}
store['active_learning_steps'][90]['acquisition']={'indices': [54457, 24613, 19626, 45482, 6401], 'labels': [2, 9, 1, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7430780529975891})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.730236291885376})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7566218376159668})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.754409909248352})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.768215537071228})
store['active_learning_steps'][91]['training']['best_epoch']=2
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.8915, 'crossentropy': 0.661860693359375}
store['active_learning_steps'][91]['acquisition']={'indices': [42565, 10984, 39977, 614, 9095], 'labels': [-1, 3, 1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7679589986801147})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7444653511047363})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8132672309875488})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.893946647644043})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7791129350662231})
store['active_learning_steps'][92]['training']['best_epoch']=2
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.9015, 'crossentropy': 0.650396875}
store['active_learning_steps'][92]['acquisition']={'indices': [45576, 53593, 10478, 44787, 14568], 'labels': [-1, 1, 9, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.745975136756897})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7937400341033936})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.774881899356842})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7502928376197815})
store['active_learning_steps'][93]['training']['best_epoch']=1
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.8758, 'crossentropy': 0.680739990234375}
store['active_learning_steps'][93]['acquisition']={'indices': [13190, 47486, 10600, 40764, 20940], 'labels': [-1, -1, 6, 9, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7902281284332275})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7182201743125916})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8301063776016235})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7244645357131958})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7432458400726318})
store['active_learning_steps'][94]['training']['best_epoch']=2
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.8976, 'crossentropy': 0.61912021484375}
store['active_learning_steps'][94]['acquisition']={'indices': [29041, 35544, 52876, 14909, 53355], 'labels': [-1, -1, -1, 6, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7373390197753906})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7006466388702393})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8479759693145752})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7869538068771362})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8181827068328857})
store['active_learning_steps'][95]['training']['best_epoch']=2
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9083, 'crossentropy': 0.582086328125}
store['active_learning_steps'][95]['acquisition']={'indices': [23992, 24810, 15941, 11330, 5161], 'labels': [4, -1, -1, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7839051485061646})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6900020837783813})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7530511617660522})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7897331714630127})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 1.0700774192810059})
store['active_learning_steps'][96]['training']['best_epoch']=2
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.8996, 'crossentropy': 0.6059845703125}
store['active_learning_steps'][96]['acquisition']={'indices': [34632, 57060, 57450, 33276, 54030], 'labels': [1, 8, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.8274797201156616})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6999994516372681})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7651193737983704})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.8040311336517334})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7999454736709595})
store['active_learning_steps'][97]['training']['best_epoch']=2
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9013, 'crossentropy': 0.62186669921875}
store['active_learning_steps'][97]['acquisition']={'indices': [31242, 35277, 35050, 36508, 21123], 'labels': [5, 7, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8227421045303345})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.716584324836731})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7777582406997681})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7787703275680542})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.9433038830757141})
store['active_learning_steps'][98]['training']['best_epoch']=2
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.8944, 'crossentropy': 0.609229931640625}
store['active_learning_steps'][98]['acquisition']={'indices': [21014, 56030, 9497, 16948, 36697], 'labels': [2, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8142062425613403})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6925652623176575})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7657960057258606})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7423306107521057})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8408406972885132})
store['active_learning_steps'][99]['training']['best_epoch']=2
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.902, 'crossentropy': 0.61992919921875}
store['active_learning_steps'][99]['acquisition']={'indices': [18268, 55088, 11092, 13598, 31752], 'labels': [3, -1, 7, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7982165217399597})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7041175365447998})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7570267915725708})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8557162284851074})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7989316582679749})
store['active_learning_steps'][100]['training']['best_epoch']=2
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.9047, 'crossentropy': 0.597827294921875}
store['active_learning_steps'][100]['acquisition']={'indices': [54976, 16535, 37374, 40552, 31520], 'labels': [-1, -1, 3, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7787704467773438})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7713921666145325})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7406107187271118})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.824867308139801})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7716854810714722})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7750457525253296})
store['active_learning_steps'][101]['training']['best_epoch']=3
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9088, 'crossentropy': 0.60289990234375}
store['active_learning_steps'][101]['acquisition']={'indices': [56503, 8914, 48619, 44482, 31149], 'labels': [-1, 4, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7452198266983032})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6229479312896729})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6536794900894165})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8161768317222595})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.73945552110672})
store['active_learning_steps'][102]['training']['best_epoch']=2
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.9097, 'crossentropy': 0.57498671875}
store['active_learning_steps'][102]['acquisition']={'indices': [527, 14288, 38781, 39935, 38212], 'labels': [0, 7, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7447721362113953})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6889199018478394})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6885873675346375})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7011498212814331})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.878989577293396})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.8485221862792969})
store['active_learning_steps'][103]['training']['best_epoch']=3
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.9137, 'crossentropy': 0.628213134765625}
store['active_learning_steps'][103]['acquisition']={'indices': [53247, 27763, 20623, 48110, 39077], 'labels': [9, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6884788274765015})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6643857955932617})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6912121772766113})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7034643888473511})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.739709734916687})
store['active_learning_steps'][104]['training']['best_epoch']=2
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9107, 'crossentropy': 0.565058447265625}
store['active_learning_steps'][104]['acquisition']={'indices': [4462, 14400, 28943, 18936, 12233], 'labels': [-1, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7797784805297852})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.648209273815155})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.716455340385437})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6882977485656738})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7453581094741821})
store['active_learning_steps'][105]['training']['best_epoch']=2
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.9014, 'crossentropy': 0.6060888671875}
store['active_learning_steps'][105]['acquisition']={'indices': [19204, 3578, 19334, 40185, 874], 'labels': [-1, 2, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8091357946395874})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6909936666488647})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7048639059066772})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7843962907791138})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7456945180892944})
store['active_learning_steps'][106]['training']['best_epoch']=2
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.905, 'crossentropy': 0.57150439453125}
store['active_learning_steps'][106]['acquisition']={'indices': [49173, 50555, 10128, 37048, 25424], 'labels': [6, -1, 0, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7806748151779175})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7215307950973511})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.712549090385437})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7463985681533813})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7719576954841614})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7382639646530151})
store['active_learning_steps'][107]['training']['best_epoch']=3
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9123, 'crossentropy': 0.5909294921875}
store['active_learning_steps'][107]['acquisition']={'indices': [4308, 28068, 57429, 51354, 14667], 'labels': [-1, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8063541650772095})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7270457744598389})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7127453088760376})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6766800880432129})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8253425359725952})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7323256731033325})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7863857746124268})
store['active_learning_steps'][108]['training']['best_epoch']=4
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9212, 'crossentropy': 0.571786962890625}
store['active_learning_steps'][108]['acquisition']={'indices': [29440, 25985, 19333, 42593, 46000], 'labels': [7, 7, 3, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7078966498374939})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6565169095993042})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7408109903335571})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7014798521995544})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7483989596366882})
store['active_learning_steps'][109]['training']['best_epoch']=2
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.9055, 'crossentropy': 0.5924712890625}
store['active_learning_steps'][109]['acquisition']={'indices': [48640, 33840, 2121, 1496, 41020], 'labels': [2, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7695682048797607})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.716254711151123})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.675918459892273})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7110770344734192})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8155564069747925})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8030570149421692})
store['active_learning_steps'][110]['training']['best_epoch']=3
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9162, 'crossentropy': 0.58829169921875}
store['active_learning_steps'][110]['acquisition']={'indices': [49906, 58141, 39218, 45679, 4397], 'labels': [-1, -1, 4, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.751391589641571})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6839210987091064})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.70792555809021})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7123132944107056})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7599443197250366})
store['active_learning_steps'][111]['training']['best_epoch']=2
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9084, 'crossentropy': 0.603992724609375}
store['active_learning_steps'][111]['acquisition']={'indices': [25352, 10741, 56770, 35993, 54631], 'labels': [1, -1, 4, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7377783060073853})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6490500569343567})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6569464206695557})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7088149785995483})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6980684399604797})
store['active_learning_steps'][112]['training']['best_epoch']=2
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.9125, 'crossentropy': 0.548614794921875}
store['active_learning_steps'][112]['acquisition']={'indices': [56739, 54263, 52519, 779, 27162], 'labels': [-1, 0, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.745742917060852})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6499890089035034})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6482352614402771})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6347126960754395})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8773258924484253})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7810388803482056})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8160444498062134})
store['active_learning_steps'][113]['training']['best_epoch']=4
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9235, 'crossentropy': 0.5496771484375}
store['active_learning_steps'][113]['acquisition']={'indices': [9761, 33458, 33286, 18694, 4859], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6771773099899292})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6548355221748352})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6775928735733032})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7820765972137451})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7733587026596069})
store['active_learning_steps'][114]['training']['best_epoch']=2
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.9067, 'crossentropy': 0.583241845703125}
store['active_learning_steps'][114]['acquisition']={'indices': [49052, 14656, 26548, 28780, 56372], 'labels': [8, -1, -1, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7631683349609375})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6757094860076904})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7293236255645752})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7998752593994141})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8498198986053467})
store['active_learning_steps'][115]['training']['best_epoch']=2
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.9048, 'crossentropy': 0.562580419921875}
store['active_learning_steps'][115]['acquisition']={'indices': [11315, 42729, 5571, 12387, 17572], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7751740217208862})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6810808181762695})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6550716161727905})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7257044315338135})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7516831159591675})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7650916576385498})
store['active_learning_steps'][116]['training']['best_epoch']=3
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.9089, 'crossentropy': 0.57822724609375}
store['active_learning_steps'][116]['acquisition']={'indices': [33797, 41345, 4627, 54709, 31105], 'labels': [7, 7, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7613253593444824})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6679191589355469})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6667890548706055})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6321016550064087})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7484854459762573})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7845830917358398})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7836048603057861})
store['active_learning_steps'][117]['training']['best_epoch']=4
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.9211, 'crossentropy': 0.55903896484375}
store['active_learning_steps'][117]['acquisition']={'indices': [12647, 2087, 36015, 18402, 32745], 'labels': [-1, 3, 5, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7240468859672546})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7281601428985596})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6632139682769775})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6872135400772095})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7578649520874023})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.8273618221282959})
store['active_learning_steps'][118]['training']['best_epoch']=3
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.9147, 'crossentropy': 0.550930078125}
store['active_learning_steps'][118]['acquisition']={'indices': [51189, 14969, 25645, 34356, 41670], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7688092589378357})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6842692494392395})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7113696336746216})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6810942888259888})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6481735706329346})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.739827036857605})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7359669208526611})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7487611770629883})
store['active_learning_steps'][119]['training']['best_epoch']=5
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.924, 'crossentropy': 0.54664892578125}
store['active_learning_steps'][119]['acquisition']={'indices': [19168, 37172, 8777, 57297, 17575], 'labels': [-1, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6815844774246216})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6212564706802368})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6148102283477783})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6416527032852173})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7038047313690186})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6617141962051392})
store['active_learning_steps'][120]['training']['best_epoch']=3
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.9208, 'crossentropy': 0.521979345703125}
store['active_learning_steps'][120]['acquisition']={'indices': [30361, 57547, 21099, 30969, 12570], 'labels': [-1, -1, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7534077167510986})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7301977872848511})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7877458930015564})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7420952320098877})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8066260814666748})
store['active_learning_steps'][121]['training']['best_epoch']=2
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.8917, 'crossentropy': 0.6110029296875}
store['active_learning_steps'][121]['acquisition']={'indices': [57662, 6974, 4826, 37497, 30462], 'labels': [5, 2, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7417277097702026})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.655769944190979})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7551895380020142})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7111412286758423})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6833902597427368})
store['active_learning_steps'][122]['training']['best_epoch']=2
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.906, 'crossentropy': 0.5357181640625}
store['active_learning_steps'][122]['acquisition']={'indices': [31421, 20832, 21572, 59258, 16522], 'labels': [1, -1, 7, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7000430822372437})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6113981604576111})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.657382071018219})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7296605110168457})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7292365431785583})
store['active_learning_steps'][123]['training']['best_epoch']=2
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9051, 'crossentropy': 0.578382861328125}
store['active_learning_steps'][123]['acquisition']={'indices': [44195, 9000, 36599, 28425, 26024], 'labels': [2, 6, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7119643688201904})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6377954483032227})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6350095272064209})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7310360670089722})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7736464142799377})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7185769081115723})
store['active_learning_steps'][124]['training']['best_epoch']=3
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.9187, 'crossentropy': 0.565039453125}
store['active_learning_steps'][124]['acquisition']={'indices': [6042, 9496, 42248, 32627, 52121], 'labels': [9, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7160047888755798})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6271779537200928})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6271047592163086})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6727465391159058})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7694258093833923})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7231302261352539})
store['active_learning_steps'][125]['training']['best_epoch']=3
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.9178, 'crossentropy': 0.525532666015625}
store['active_learning_steps'][125]['acquisition']={'indices': [8691, 5761, 28840, 42721, 11747], 'labels': [-1, 7, 0, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7186006307601929})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6885175704956055})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6247875690460205})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.704486608505249})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7473880052566528})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6547544598579407})
store['active_learning_steps'][126]['training']['best_epoch']=3
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.9165, 'crossentropy': 0.52158935546875}
store['active_learning_steps'][126]['acquisition']={'indices': [56529, 11711, 36897, 29496, 59701], 'labels': [-1, -1, 4, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8077098727226257})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5992066860198975})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6523253321647644})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5826002359390259})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7101758718490601})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6712625026702881})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7367825508117676})
store['active_learning_steps'][127]['training']['best_epoch']=4
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.9269, 'crossentropy': 0.484899609375}
store['active_learning_steps'][127]['acquisition']={'indices': [4072, 24979, 6085, 27028, 35195], 'labels': [-1, 8, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7031550407409668})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6185072660446167})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6270751953125})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6400604844093323})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6486462354660034})
store['active_learning_steps'][128]['training']['best_epoch']=2
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.9167, 'crossentropy': 0.52492666015625}
store['active_learning_steps'][128]['acquisition']={'indices': [11840, 38254, 3380, 15948, 9492], 'labels': [-1, 5, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6980376243591309})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.590983510017395})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6032143235206604})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.615405797958374})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6538794040679932})
store['active_learning_steps'][129]['training']['best_epoch']=2
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.912, 'crossentropy': 0.54229453125}
store['active_learning_steps'][129]['acquisition']={'indices': [26031, 15250, 10948, 29819, 4481], 'labels': [-1, 3, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.701195478439331})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6228830814361572})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.570893406867981})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5834293365478516})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6484142541885376})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7275227904319763})
store['active_learning_steps'][130]['training']['best_epoch']=3
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.9245, 'crossentropy': 0.495536376953125}
store['active_learning_steps'][130]['acquisition']={'indices': [51207, 56980, 43588, 41416, 21289], 'labels': [-1, 1, 8, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6764571070671082})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6059345006942749})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6158973574638367})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5632652044296265})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6690460443496704})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5927138328552246})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6257685422897339})
store['active_learning_steps'][131]['training']['best_epoch']=4
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.9302, 'crossentropy': 0.465286669921875}
store['active_learning_steps'][131]['acquisition']={'indices': [43142, 19038, 40521, 22195, 23400], 'labels': [1, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.8003731966018677})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5825392007827759})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6449224948883057})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6151489019393921})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7305891513824463})
store['active_learning_steps'][132]['training']['best_epoch']=2
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.9155, 'crossentropy': 0.50935830078125}
store['active_learning_steps'][132]['acquisition']={'indices': [25812, 38417, 8902, 13197, 40299], 'labels': [1, 2, -1, 0, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7268670797348022})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5940182209014893})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6082740426063538})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.630531907081604})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.604533851146698})
store['active_learning_steps'][133]['training']['best_epoch']=2
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9112, 'crossentropy': 0.52486923828125}
store['active_learning_steps'][133]['acquisition']={'indices': [38012, 35386, 3698, 37732, 35345], 'labels': [-1, 1, 0, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.720830500125885})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.600696325302124})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5976389646530151})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6336809992790222})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6765824556350708})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6737955212593079})
store['active_learning_steps'][134]['training']['best_epoch']=3
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.9212, 'crossentropy': 0.533974609375}
store['active_learning_steps'][134]['acquisition']={'indices': [44701, 38590, 57138, 49338, 18367], 'labels': [9, -1, -1, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7021251916885376})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6078299283981323})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6033533811569214})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6367286443710327})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6923338770866394})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6334470510482788})
store['active_learning_steps'][135]['training']['best_epoch']=3
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.9225, 'crossentropy': 0.527906494140625}
store['active_learning_steps'][135]['acquisition']={'indices': [48661, 2202, 59534, 3077, 21700], 'labels': [-1, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7587659358978271})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5957387685775757})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5959956049919128})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6355239152908325})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7450920343399048})
store['active_learning_steps'][136]['training']['best_epoch']=2
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.9145, 'crossentropy': 0.5262830078125}
store['active_learning_steps'][136]['acquisition']={'indices': [14575, 16287, 48991, 59374, 47522], 'labels': [-1, -1, -1, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6965744495391846})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5797131061553955})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6162819862365723})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6113062500953674})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.646772027015686})
store['active_learning_steps'][137]['training']['best_epoch']=2
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.9191, 'crossentropy': 0.510380029296875}
store['active_learning_steps'][137]['acquisition']={'indices': [48653, 20694, 36458, 31282, 13279], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7429680824279785})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6019607782363892})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.50230872631073})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5694783329963684})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5774924755096436})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5736826658248901})
store['active_learning_steps'][138]['training']['best_epoch']=3
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.9345, 'crossentropy': 0.447609375}
store['active_learning_steps'][138]['acquisition']={'indices': [43280, 29894, 13756, 3717, 461], 'labels': [3, 3, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7049412727355957})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.5994243621826172})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6487741470336914})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.667360782623291})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6784212589263916})
store['active_learning_steps'][139]['training']['best_epoch']=2
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.9136, 'crossentropy': 0.510070654296875}
store['active_learning_steps'][139]['acquisition']={'indices': [9578, 55223, 13199, 51258, 55453], 'labels': [5, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6806070804595947})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5618066191673279})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5715823173522949})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5949954986572266})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6781702041625977})
store['active_learning_steps'][140]['training']['best_epoch']=2
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.9224, 'crossentropy': 0.52272978515625}
store['active_learning_steps'][140]['acquisition']={'indices': [31845, 8639, 16213, 1861, 31650], 'labels': [-1, 5, 5, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6814596652984619})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5730298161506653})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5475612282752991})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5828108787536621})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5717644691467285})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6293090581893921})
store['active_learning_steps'][141]['training']['best_epoch']=3
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.931, 'crossentropy': 0.46119599609375}
store['active_learning_steps'][141]['acquisition']={'indices': [37448, 39212, 14511, 18028, 43023], 'labels': [-1, -1, 0, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7095940709114075})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5989486575126648})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.60094153881073})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6083033084869385})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5950419902801514})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5417578220367432})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5868701934814453})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6460320949554443})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.6156474351882935})
store['active_learning_steps'][142]['training']['best_epoch']=6
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9337, 'crossentropy': 0.469537939453125}
store['active_learning_steps'][142]['acquisition']={'indices': [35570, 44962, 4162, 48916, 41682], 'labels': [5, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7013140916824341})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5742393732070923})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.573348343372345})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6563519239425659})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5998208522796631})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7111112475395203})
store['active_learning_steps'][143]['training']['best_epoch']=3
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.9233, 'crossentropy': 0.5089318359375}
store['active_learning_steps'][143]['acquisition']={'indices': [43345, 60, 41245, 30845, 48521], 'labels': [-1, -1, 0, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6580379009246826})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5027395486831665})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5647354125976562})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5876661539077759})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.586143970489502})
store['active_learning_steps'][144]['training']['best_epoch']=2
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.9274, 'crossentropy': 0.45070146484375}
store['active_learning_steps'][144]['acquisition']={'indices': [1645, 26347, 8023, 59220, 545], 'labels': [-1, 6, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.724199652671814})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5608212947845459})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5006771683692932})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5879547595977783})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.602935791015625})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5520702600479126})
store['active_learning_steps'][145]['training']['best_epoch']=3
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.9218, 'crossentropy': 0.47350205078125}
store['active_learning_steps'][145]['acquisition']={'indices': [32302, 52310, 30146, 26833, 29707], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6918689608573914})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5438696146011353})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.537389874458313})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.570722222328186})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5362495183944702})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.59470534324646})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6120620965957642})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5526996850967407})
store['active_learning_steps'][146]['training']['best_epoch']=5
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.9338, 'crossentropy': 0.472737939453125}
store['active_learning_steps'][146]['acquisition']={'indices': [50013, 56191, 10757, 49873, 23058], 'labels': [-1, 3, 3, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7493271827697754})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.5641086101531982})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5517741441726685})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4975012540817261})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5562556982040405})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6510730981826782})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5354712009429932})
store['active_learning_steps'][147]['training']['best_epoch']=4
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.9367, 'crossentropy': 0.44083271484375}
store['active_learning_steps'][147]['acquisition']={'indices': [14366, 58997, 27204, 55114, 56651], 'labels': [-1, 6, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6613047122955322})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6297173500061035})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5691747069358826})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.638282835483551})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.57561856508255})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6225700974464417})
store['active_learning_steps'][148]['training']['best_epoch']=3
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.923, 'crossentropy': 0.51697578125}
store['active_learning_steps'][148]['acquisition']={'indices': [16854, 7679, 42460, 45350, 45336], 'labels': [9, 7, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7903518676757812})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6002415418624878})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5829359292984009})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6253476142883301})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5352510213851929})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6161166429519653})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5677295327186584})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6020816564559937})
store['active_learning_steps'][149]['training']['best_epoch']=5
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.9283, 'crossentropy': 0.514095068359375}
store['active_learning_steps'][149]['acquisition']={'indices': [52673, 25994, 13203, 27922, 52198], 'labels': [-1, -1, -1, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6944339275360107})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6163667440414429})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5548690557479858})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5959542989730835})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5653378963470459})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6343001127243042})
store['active_learning_steps'][150]['training']['best_epoch']=3
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.9216, 'crossentropy': 0.51614814453125}
store['active_learning_steps'][150]['acquisition']={'indices': [31186, 36553, 11694, 39576, 53373], 'labels': [-1, 2, 0, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7345459461212158})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5724625587463379})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.610788881778717})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6033248901367188})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6156220436096191})
store['active_learning_steps'][151]['training']['best_epoch']=2
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9172, 'crossentropy': 0.52562333984375}
store['active_learning_steps'][151]['acquisition']={'indices': [19993, 1097, 41743, 24019, 3171], 'labels': [-1, -1, 0, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7609598636627197})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6063523292541504})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5322776436805725})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5914623141288757})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6335189342498779})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6167974472045898})
store['active_learning_steps'][152]['training']['best_epoch']=3
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9273, 'crossentropy': 0.4679}
store['active_learning_steps'][152]['acquisition']={'indices': [28500, 27393, 47781, 8932, 23967], 'labels': [4, -1, -1, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7415288686752319})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6045440435409546})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5194711685180664})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5190539956092834})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5628783702850342})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6047741174697876})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6171233057975769})
store['active_learning_steps'][153]['training']['best_epoch']=4
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9333, 'crossentropy': 0.462491845703125}
store['active_learning_steps'][153]['acquisition']={'indices': [49480, 18669, 49094, 41411, 37167], 'labels': [4, 9, 5, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6459609270095825})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5941892862319946})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.538974404335022})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5764355659484863})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5611812472343445})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5436161756515503})
store['active_learning_steps'][154]['training']['best_epoch']=3
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.9169, 'crossentropy': 0.49686181640625}
store['active_learning_steps'][154]['acquisition']={'indices': [5180, 48409, 56353, 13011, 46948], 'labels': [4, 6, -1, 6, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.807974100112915})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5528028011322021})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5897818207740784})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5324740409851074})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5556713342666626})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6362090110778809})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6223768591880798})
store['active_learning_steps'][155]['training']['best_epoch']=4
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9302, 'crossentropy': 0.46761015625}
store['active_learning_steps'][155]['acquisition']={'indices': [59618, 59643, 42154, 47095, 43098], 'labels': [5, 3, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6989817023277283})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5523401498794556})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5453933477401733})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5661942958831787})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.49036717414855957})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5373082756996155})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.581925094127655})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5781062841415405})
store['active_learning_steps'][156]['training']['best_epoch']=5
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.9371, 'crossentropy': 0.4208826171875}
store['active_learning_steps'][156]['acquisition']={'indices': [7818, 48566, 51705, 19888, 48877], 'labels': [2, 9, 8, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6862382888793945})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5739341974258423})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.533263087272644})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5747230052947998})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5761631727218628})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6662284135818481})
store['active_learning_steps'][157]['training']['best_epoch']=3
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.9263, 'crossentropy': 0.482013525390625}
store['active_learning_steps'][157]['acquisition']={'indices': [10084, 33099, 50943, 44244, 16689], 'labels': [2, 3, 7, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7039519548416138})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5580599308013916})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5071775913238525})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.4696933329105377})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5149816274642944})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5825743675231934})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5398895144462585})
store['active_learning_steps'][158]['training']['best_epoch']=4
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9338, 'crossentropy': 0.4290859375}
store['active_learning_steps'][158]['acquisition']={'indices': [35582, 398, 45069, 31140, 6269], 'labels': [-1, -1, -1, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.67048180103302})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.563322126865387})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5161067247390747})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5152140259742737})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.46662479639053345})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5502705574035645})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5715888738632202})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5920710563659668})
store['active_learning_steps'][159]['training']['best_epoch']=5
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.9359, 'crossentropy': 0.40982822265625}
store['active_learning_steps'][159]['acquisition']={'indices': [23531, 46528, 20656, 5481, 16932], 'labels': [-1, 8, 6, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5817348957061768})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5463188886642456})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5850073099136353})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.553365170955658})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5216349363327026})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.5248458385467529})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5034962296485901})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5855503082275391})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5498046278953552})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5386767387390137})
store['active_learning_steps'][160]['training']['best_epoch']=7
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.9391, 'crossentropy': 0.44642138671875}
store['active_learning_steps'][160]['acquisition']={'indices': [6992, 54870, 54693, 29006, 41598], 'labels': [2, 8, 1, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6284091472625732})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.573745608329773})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5329077243804932})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5754818916320801})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.515500545501709})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5559418201446533})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5408422350883484})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5595752596855164})
store['active_learning_steps'][161]['training']['best_epoch']=5
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9387, 'crossentropy': 0.453922802734375}
store['active_learning_steps'][161]['acquisition']={'indices': [31569, 17943, 21511, 10143, 43014], 'labels': [-1, 1, -1, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7532678842544556})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5187214612960815})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5275247693061829})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5361706018447876})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6364743709564209})
store['active_learning_steps'][162]['training']['best_epoch']=2
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9272, 'crossentropy': 0.47034384765625}
store['active_learning_steps'][162]['acquisition']={'indices': [42966, 3358, 33245, 7447, 6721], 'labels': [3, -1, 5, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][163]['training']={}
store['active_learning_steps'][163]['training']['epochs']=[]
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6748299598693848})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5342491865158081})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5095354914665222})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.494258850812912})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5136614441871643})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.49143415689468384})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.46088024973869324})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5261789560317993})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5460553169250488})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5755348205566406})
store['active_learning_steps'][163]['training']['best_epoch']=7
store['active_learning_steps'][163]['evaluation_metrics']={'accuracy': 0.9426, 'crossentropy': 0.4312833984375}
store['active_learning_steps'][163]['acquisition']={'indices': [25948, 9006, 33079, 27523, 45621], 'labels': [1, 3, 0, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][164]['training']={}
store['active_learning_steps'][164]['training']['epochs']=[]
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7149727940559387})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5094146132469177})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.48803603649139404})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6186138391494751})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5233385562896729})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.515365481376648})
store['active_learning_steps'][164]['training']['best_epoch']=3
store['active_learning_steps'][164]['evaluation_metrics']={'accuracy': 0.9288, 'crossentropy': 0.46209208984375}
store['active_learning_steps'][164]['acquisition']={'indices': [55607, 51743, 59760, 49264, 2312], 'labels': [-1, -1, 3, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][165]['training']={}
store['active_learning_steps'][165]['training']['epochs']=[]
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6798208951950073})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5745115280151367})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5549092292785645})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5747256278991699})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5266847610473633})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.588566780090332})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.524480938911438})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5675618648529053})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.596616268157959})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5775595903396606})
store['active_learning_steps'][165]['training']['best_epoch']=7
store['active_learning_steps'][165]['evaluation_metrics']={'accuracy': 0.9367, 'crossentropy': 0.450101318359375}
store['active_learning_steps'][165]['acquisition']={'indices': [23597, 538, 38647, 37888, 8859], 'labels': [5, -1, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][166]['training']={}
store['active_learning_steps'][166]['training']['epochs']=[]
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7577193975448608})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5234537720680237})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5620633959770203})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5670503377914429})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5875897407531738})
store['active_learning_steps'][166]['training']['best_epoch']=2
store['active_learning_steps'][166]['evaluation_metrics']={'accuracy': 0.9279, 'crossentropy': 0.472465771484375}
store['active_learning_steps'][166]['acquisition']={'indices': [56535, 2666, 9710, 31838, 47397], 'labels': [3, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][167]['training']={}
store['active_learning_steps'][167]['training']['epochs']=[]
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7294957637786865})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5463548898696899})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5895720720291138})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5386451482772827})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5965883731842041})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.4921952486038208})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5709037780761719})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5474126935005188})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5272461771965027})
store['active_learning_steps'][167]['training']['best_epoch']=6
store['active_learning_steps'][167]['evaluation_metrics']={'accuracy': 0.9372, 'crossentropy': 0.461319677734375}
store['active_learning_steps'][167]['acquisition']={'indices': [36199, 22819, 51573, 48146, 36850], 'labels': [8, 5, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][168]['training']={}
store['active_learning_steps'][168]['training']['epochs']=[]
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6922282576560974})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5427241325378418})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.48348814249038696})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5143948793411255})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.562893271446228})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.4794313311576843})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5484870672225952})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5932316780090332})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5200830698013306})
store['active_learning_steps'][168]['training']['best_epoch']=6
store['active_learning_steps'][168]['evaluation_metrics']={'accuracy': 0.9408, 'crossentropy': 0.4232611328125}
store['active_learning_steps'][168]['acquisition']={'indices': [40077, 44260, 59999, 45107, 49556], 'labels': [-1, 2, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][169]['training']={}
store['active_learning_steps'][169]['training']['epochs']=[]
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6944496035575867})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5279585123062134})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.478304922580719})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5683076977729797})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5462406277656555})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5262705087661743})
store['active_learning_steps'][169]['training']['best_epoch']=3
store['active_learning_steps'][169]['evaluation_metrics']={'accuracy': 0.9273, 'crossentropy': 0.4414658203125}
store['active_learning_steps'][169]['acquisition']={'indices': [905, 38872, 32580, 48475, 37528], 'labels': [1, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][170]['training']={}
store['active_learning_steps'][170]['training']['epochs']=[]
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7286016941070557})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5808557271957397})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.4833158850669861})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.47698551416397095})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.615527868270874})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5085591077804565})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.4898762106895447})
store['active_learning_steps'][170]['training']['best_epoch']=4
store['active_learning_steps'][170]['evaluation_metrics']={'accuracy': 0.9335, 'crossentropy': 0.43231767578125}
store['active_learning_steps'][170]['acquisition']={'indices': [52691, 34945, 20477, 40366, 41895], 'labels': [-1, 1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][171]['training']={}
store['active_learning_steps'][171]['training']['epochs']=[]
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6772259473800659})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5994064807891846})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5563968420028687})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5607211589813232})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5854203701019287})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6140685677528381})
store['active_learning_steps'][171]['training']['best_epoch']=3
store['active_learning_steps'][171]['evaluation_metrics']={'accuracy': 0.9314, 'crossentropy': 0.44444609375}
store['active_learning_steps'][171]['acquisition']={'indices': [27486, 2985, 18106, 22130, 47960], 'labels': [3, 7, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][172]['training']={}
store['active_learning_steps'][172]['training']['epochs']=[]
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6879353523254395})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5255846977233887})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5288937091827393})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.559592604637146})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5925277471542358})
store['active_learning_steps'][172]['training']['best_epoch']=2
store['active_learning_steps'][172]['evaluation_metrics']={'accuracy': 0.925, 'crossentropy': 0.500742333984375}
store['active_learning_steps'][172]['acquisition']={'indices': [41950, 47423, 11811, 44188, 13323], 'labels': [4, 7, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][173]['training']={}
store['active_learning_steps'][173]['training']['epochs']=[]
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7011376023292542})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.5405468940734863})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.516993522644043})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5200262665748596})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5431945323944092})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.576225757598877})
store['active_learning_steps'][173]['training']['best_epoch']=3
store['active_learning_steps'][173]['evaluation_metrics']={'accuracy': 0.9304, 'crossentropy': 0.460576904296875}
store['active_learning_steps'][173]['acquisition']={'indices': [39979, 53216, 3079, 37555, 37338], 'labels': [-1, 9, 7, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][174]['training']={}
store['active_learning_steps'][174]['training']['epochs']=[]
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6346365809440613})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.533423900604248})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5011204481124878})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9296875, 'crossentropy': 0.49421271681785583})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.46071839332580566})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.4937840700149536})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5405365228652954})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5254325866699219})
store['active_learning_steps'][174]['training']['best_epoch']=5
store['active_learning_steps'][174]['evaluation_metrics']={'accuracy': 0.9413, 'crossentropy': 0.404697998046875}
