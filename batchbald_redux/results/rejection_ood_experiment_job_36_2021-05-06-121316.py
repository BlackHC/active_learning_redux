store = {}
store['timestamp']=1620299596
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py', '--id=36']
store['commit']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['github_url']='2edd2424ec449a84ea20a7324261784a7627b78d'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/rejection_ood_experiment.py'
store['job_id']=36
store['worker_id']=36
store['num_workers']=40
store['config']={'seed': 52, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'samples_per_epoch': 5056, 'mnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples)) + ('OoD Dataset (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.382150173187256})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.741635799407959})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.7662415504455566})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.0805437564849854})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.659, 'crossentropy': 2.160066796875}
store['active_learning_steps'][0]['acquisition']={'indices': [28642, 19691, 42491, 8773, 40820], 'labels': [7, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.481421709060669})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.8092217445373535})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.865900993347168})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.2956151962280273})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6246, 'crossentropy': 2.2220919921875}
store['active_learning_steps'][1]['acquisition']={'indices': [57049, 8060, 8752, 46069, 50072], 'labels': [1, -1, 2, 0, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.271868944168091})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.6118345260620117})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.772160053253174})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.187028408050537})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6649, 'crossentropy': 2.1241791015625}
store['active_learning_steps'][2]['acquisition']={'indices': [44312, 57972, 36475, 25739, 6293], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.206773281097412})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6875, 'crossentropy': 2.2618050575256348})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.8910417556762695})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 3.0461394786834717})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6807, 'crossentropy': 1.9896158203125}
store['active_learning_steps'][3]['acquisition']={'indices': [8913, 19947, 35297, 9251, 31972], 'labels': [-1, -1, 6, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.71875, 'crossentropy': 2.1862242221832275})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.716796875, 'crossentropy': 2.6540520191192627})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 2.5377142429351807})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 2.8192176818847656})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.719, 'crossentropy': 2.0088455078125}
store['active_learning_steps'][4]['acquisition']={'indices': [49770, 26029, 58335, 51546, 19274], 'labels': [0, -1, 1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6689453125, 'crossentropy': 2.2522170543670654})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 2.4363346099853516})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.662109375, 'crossentropy': 2.7184271812438965})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6806640625, 'crossentropy': 2.7447218894958496})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.6997, 'crossentropy': 2.02788046875}
store['active_learning_steps'][5]['acquisition']={'indices': [27106, 5171, 12155, 33723, 48752], 'labels': [8, 2, 6, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.8726067543029785})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.720703125, 'crossentropy': 1.9497798681259155})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.74609375, 'crossentropy': 1.9405410289764404})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 2.3806581497192383})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7419, 'crossentropy': 1.59658720703125}
store['active_learning_steps'][6]['acquisition']={'indices': [10730, 22488, 45305, 16141, 28259], 'labels': [-1, 3, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.7144687175750732})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.2066354751586914})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7119140625, 'crossentropy': 2.350961446762085})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.70703125, 'crossentropy': 2.5557432174682617})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7358, 'crossentropy': 1.5277724609375}
store['active_learning_steps'][7]['acquisition']={'indices': [1129, 49680, 36680, 39203, 20971], 'labels': [-1, 1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 1.7633206844329834})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.0346295833587646})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.705078125, 'crossentropy': 2.3372132778167725})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7099609375, 'crossentropy': 2.37709379196167})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7311, 'crossentropy': 1.5869923828125}
store['active_learning_steps'][8]['acquisition']={'indices': [49407, 59987, 35077, 58815, 45288], 'labels': [-1, 0, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6904296875, 'crossentropy': 1.8485101461410522})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.2884230613708496})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6982421875, 'crossentropy': 2.442254066467285})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.69140625, 'crossentropy': 2.5283846855163574})
store['active_learning_steps'][9]['training']['best_epoch']=1
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.7256, 'crossentropy': 1.6781720703125}
store['active_learning_steps'][9]['acquisition']={'indices': [13649, 1374, 12504, 51133, 18500], 'labels': [-1, 2, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.724609375, 'crossentropy': 1.6474356651306152})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.73046875, 'crossentropy': 2.1057796478271484})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.712890625, 'crossentropy': 2.30118989944458})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.72265625, 'crossentropy': 2.2835841178894043})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7417, 'crossentropy': 1.5808201171875}
store['active_learning_steps'][10]['acquisition']={'indices': [54827, 44515, 18926, 17045, 40950], 'labels': [9, 4, 0, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.4632072448730469})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.8300132751464844})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 2.1215097904205322})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 2.0039095878601074})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.766, 'crossentropy': 1.41082587890625}
store['active_learning_steps'][11]['acquisition']={'indices': [52038, 5287, 58117, 19311, 27744], 'labels': [3, 4, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.5612130165100098})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.5750526189804077})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.7955864667892456})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.77734375, 'crossentropy': 1.9670779705047607})
store['active_learning_steps'][12]['training']['best_epoch']=1
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.7839, 'crossentropy': 1.3672439453125}
store['active_learning_steps'][12]['acquisition']={'indices': [56647, 53723, 46563, 28107, 21923], 'labels': [8, -1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.4677973985671997})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7451171875, 'crossentropy': 1.657436490058899})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.7811592817306519})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.9175567626953125})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7715, 'crossentropy': 1.3707896484375}
store['active_learning_steps'][13]['acquisition']={'indices': [9656, 44016, 43638, 13615, 6330], 'labels': [-1, -1, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.76171875, 'crossentropy': 1.4005697965621948})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.6065106391906738})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.7773553133010864})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.8218564987182617})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7853, 'crossentropy': 1.2839712890625}
store['active_learning_steps'][14]['acquisition']={'indices': [34013, 41386, 23524, 49659, 44426], 'labels': [9, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.4223675727844238})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.7129966020584106})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.87985098361969})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.865551471710205})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.7986, 'crossentropy': 1.21849970703125}
store['active_learning_steps'][15]['acquisition']={'indices': [53211, 15854, 8829, 51434, 27290], 'labels': [9, 0, 6, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.5454084873199463})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.584282398223877})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.78759765625})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 2.023008346557617})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.7801, 'crossentropy': 1.36107353515625}
store['active_learning_steps'][16]['acquisition']={'indices': [10872, 34519, 42190, 15523, 30500], 'labels': [-1, 0, -1, -1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.197913408279419})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.80859375, 'crossentropy': 1.290281057357788})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.4453918933868408})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.3149425983428955})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.788, 'crossentropy': 1.14633662109375}
store['active_learning_steps'][17]['acquisition']={'indices': [58930, 12119, 15300, 56160, 34348], 'labels': [-1, 0, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.2602627277374268})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.5730993747711182})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.551888108253479})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.579829216003418})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.7911, 'crossentropy': 1.1314818359375}
store['active_learning_steps'][18]['acquisition']={'indices': [33403, 32276, 52928, 1424, 5440], 'labels': [-1, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.2986299991607666})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.4705281257629395})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.506220817565918})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.7089534997940063})
store['active_learning_steps'][19]['training']['best_epoch']=1
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8051, 'crossentropy': 1.1587658203125}
store['active_learning_steps'][19]['acquisition']={'indices': [55239, 23217, 10055, 19794, 31771], 'labels': [4, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.2309327125549316})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.2940268516540527})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.3755109310150146})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.5253071784973145})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.812, 'crossentropy': 1.0976720703125}
store['active_learning_steps'][20]['acquisition']={'indices': [47735, 36902, 51535, 11156, 8100], 'labels': [1, 7, 6, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 1.1481064558029175})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.3855364322662354})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.6483979225158691})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.571739912033081})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8284, 'crossentropy': 1.04087626953125}
store['active_learning_steps'][21]['acquisition']={'indices': [13735, 57239, 41623, 10701, 31890], 'labels': [-1, -1, 1, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.1282753944396973})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.227675437927246})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.5136563777923584})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.4480597972869873})
store['active_learning_steps'][22]['training']['best_epoch']=1
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8146, 'crossentropy': 1.04484599609375}
store['active_learning_steps'][22]['acquisition']={'indices': [41216, 55168, 55654, 15424, 7526], 'labels': [-1, 6, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0834722518920898})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 1.3375723361968994})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.4341871738433838})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.4915573596954346})
store['active_learning_steps'][23]['training']['best_epoch']=1
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8163, 'crossentropy': 0.98277236328125}
store['active_learning_steps'][23]['acquisition']={'indices': [5125, 17599, 23011, 32485, 46786], 'labels': [-1, 1, 5, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 1.1319580078125})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.1454050540924072})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.4699102640151978})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.3448842763900757})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.8315, 'crossentropy': 0.97479658203125}
store['active_learning_steps'][24]['acquisition']={'indices': [25675, 14724, 3309, 12776, 28674], 'labels': [-1, -1, -1, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.268926739692688})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 1.1731009483337402})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.484103798866272})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.5255494117736816})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.657577395439148})
store['active_learning_steps'][25]['training']['best_epoch']=2
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.8438, 'crossentropy': 1.03910869140625}
store['active_learning_steps'][25]['acquisition']={'indices': [18650, 39125, 51917, 41733, 8695], 'labels': [0, -1, 0, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.2032471895217896})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.3881897926330566})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.4590864181518555})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.4640028476715088})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.7982, 'crossentropy': 1.1009109375}
store['active_learning_steps'][26]['acquisition']={'indices': [24080, 53240, 45140, 57067, 40240], 'labels': [-1, 8, -1, 0, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1180572509765625})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.3029212951660156})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.3960461616516113})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.6889734268188477})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.8239, 'crossentropy': 0.99536123046875}
store['active_learning_steps'][27]['acquisition']={'indices': [14732, 33539, 21764, 32118, 26885], 'labels': [6, 8, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.101404070854187})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.2366421222686768})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 1.2150602340698242})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.4429947137832642})
store['active_learning_steps'][28]['training']['best_epoch']=1
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.816, 'crossentropy': 0.980665625}
store['active_learning_steps'][28]['acquisition']={'indices': [42066, 53314, 53237, 4935, 49896], 'labels': [-1, 1, 2, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.190614104270935})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.2753033638000488})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.6612586975097656})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.5357391834259033})
store['active_learning_steps'][29]['training']['best_epoch']=1
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.7924, 'crossentropy': 1.06419150390625}
store['active_learning_steps'][29]['acquisition']={'indices': [23973, 35357, 57823, 745, 25096], 'labels': [1, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.0431973934173584})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.3128509521484375})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.2355778217315674})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 1.1957330703735352})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.8209, 'crossentropy': 0.95833828125}
store['active_learning_steps'][30]['acquisition']={'indices': [21040, 23444, 18761, 41862, 53869], 'labels': [-1, 1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.1896151304244995})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.1390655040740967})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.2015373706817627})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.4605884552001953})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 1.4148633480072021})
store['active_learning_steps'][31]['training']['best_epoch']=2
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.8576, 'crossentropy': 1.0001439453125}
store['active_learning_steps'][31]['acquisition']={'indices': [58891, 36042, 81, 15388, 32430], 'labels': [-1, -1, 0, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.1199226379394531})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.2077468633651733})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 1.1228713989257812})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.302769660949707})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8155, 'crossentropy': 0.98125126953125}
store['active_learning_steps'][32]['acquisition']={'indices': [43113, 53826, 26530, 40175, 26413], 'labels': [-1, 5, 6, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.2563447952270508})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.2103357315063477})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 1.316296100616455})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.4534387588500977})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.8369140625, 'crossentropy': 1.431787133216858})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8472, 'crossentropy': 1.00907236328125}
store['active_learning_steps'][33]['acquisition']={'indices': [40351, 47580, 44874, 41465, 57237], 'labels': [-1, 1, 8, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.1447652578353882})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.2194026708602905})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0469026565551758})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.198720932006836})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.2563844919204712})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.1012959480285645})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.864, 'crossentropy': 0.90938369140625}
store['active_learning_steps'][34]['acquisition']={'indices': [17901, 44547, 43005, 17450, 19278], 'labels': [3, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.146885871887207})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8232421875, 'crossentropy': 1.161959171295166})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 1.327821969985962})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.3966987133026123})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.8131, 'crossentropy': 1.023732421875}
store['active_learning_steps'][35]['acquisition']={'indices': [51831, 11871, 56053, 39168, 27486], 'labels': [0, -1, 3, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1208360195159912})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 1.1662650108337402})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.2198610305786133})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.2353332042694092})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.8128, 'crossentropy': 0.96854453125}
store['active_learning_steps'][36]['acquisition']={'indices': [46914, 22209, 57536, 19457, 39156], 'labels': [-1, -1, -1, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 1.0288877487182617})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1157569885253906})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.1139079332351685})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1367509365081787})
store['active_learning_steps'][37]['training']['best_epoch']=1
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8374, 'crossentropy': 0.9490455078125}
store['active_learning_steps'][37]['acquisition']={'indices': [38471, 59009, 51382, 31568, 26061], 'labels': [-1, -1, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.1189498901367188})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.1235665082931519})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.2158591747283936})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.3126089572906494})
store['active_learning_steps'][38]['training']['best_epoch']=1
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8195, 'crossentropy': 0.9820607421875}
store['active_learning_steps'][38]['acquisition']={'indices': [46354, 42534, 35514, 59927, 38623], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0760457515716553})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 1.1522362232208252})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 1.0340487957000732})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.259834885597229})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.3252696990966797})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 1.396808385848999})
store['active_learning_steps'][39]['training']['best_epoch']=3
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8736, 'crossentropy': 0.91603759765625}
store['active_learning_steps'][39]['acquisition']={'indices': [19503, 50014, 9688, 20134, 11688], 'labels': [6, -1, 0, 7, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.983995795249939})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.9196885824203491})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 1.0920162200927734})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.1828346252441406})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.3096339702606201})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8751, 'crossentropy': 0.786701513671875}
store['active_learning_steps'][40]['acquisition']={'indices': [49747, 51507, 7021, 44516, 58958], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.0603508949279785})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 1.2604389190673828})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 1.2428648471832275})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 1.2054660320281982})
store['active_learning_steps'][41]['training']['best_epoch']=1
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8245, 'crossentropy': 0.94021982421875}
store['active_learning_steps'][41]['acquisition']={'indices': [19024, 54458, 57530, 8137, 59294], 'labels': [9, 1, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9577774405479431})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 1.0948936939239502})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 1.0168758630752563})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.102050542831421})
store['active_learning_steps'][42]['training']['best_epoch']=1
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8483, 'crossentropy': 0.802432568359375}
store['active_learning_steps'][42]['acquisition']={'indices': [21604, 18633, 53056, 13778, 57451], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 1.0133583545684814})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0476908683776855})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.2177138328552246})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.83984375, 'crossentropy': 1.1757187843322754})
store['active_learning_steps'][43]['training']['best_epoch']=1
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.8338, 'crossentropy': 0.87862568359375}
store['active_learning_steps'][43]['acquisition']={'indices': [25584, 47697, 12274, 44193, 9978], 'labels': [-1, -1, -1, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9837337732315063})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 1.003006935119629})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0890825986862183})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.1453598737716675})
store['active_learning_steps'][44]['training']['best_epoch']=1
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.8395, 'crossentropy': 0.869967578125}
store['active_learning_steps'][44]['acquisition']={'indices': [19514, 42948, 16085, 30100, 41050], 'labels': [4, -1, -1, -1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.0143992900848389})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.069576382637024})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 1.0508521795272827})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.2711018323898315})
store['active_learning_steps'][45]['training']['best_epoch']=1
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.8264, 'crossentropy': 0.883963671875}
store['active_learning_steps'][45]['acquisition']={'indices': [55139, 5387, 1651, 3784, 32559], 'labels': [3, -1, -1, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0216805934906006})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 1.0195077657699585})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 1.1356701850891113})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 1.362548828125})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 1.2937629222869873})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8601, 'crossentropy': 0.888697265625}
store['active_learning_steps'][46]['acquisition']={'indices': [21021, 21649, 46763, 52654, 14714], 'labels': [7, 8, 0, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 0.9717886447906494})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9254014492034912})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 1.091170072555542})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.0082415342330933})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 1.1118385791778564})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8825, 'crossentropy': 0.753424072265625}
store['active_learning_steps'][47]['acquisition']={'indices': [14910, 1294, 56125, 42472, 28384], 'labels': [-1, 8, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8740661144256592})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.9900952577590942})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 1.15911865234375})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 1.2361160516738892})
store['active_learning_steps'][48]['training']['best_epoch']=1
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.8535, 'crossentropy': 0.79571279296875}
store['active_learning_steps'][48]['acquisition']={'indices': [15487, 33878, 37448, 42573, 37678], 'labels': [8, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8076171875, 'crossentropy': 0.9504616856575012})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.9515093564987183})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 1.055617332458496})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.9852278232574463})
store['active_learning_steps'][49]['training']['best_epoch']=1
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8339, 'crossentropy': 0.883193359375}
store['active_learning_steps'][49]['acquisition']={'indices': [22298, 32495, 8525, 52398, 22041], 'labels': [6, -1, 9, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.896866500377655})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.977250337600708})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 1.0820852518081665})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 1.1189548969268799})
store['active_learning_steps'][50]['training']['best_epoch']=1
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8607, 'crossentropy': 0.776445654296875}
store['active_learning_steps'][50]['acquisition']={'indices': [48412, 58441, 28918, 32218, 45398], 'labels': [-1, 2, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8646271228790283})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9108071327209473})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0863628387451172})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 1.0242905616760254})
store['active_learning_steps'][51]['training']['best_epoch']=1
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8534, 'crossentropy': 0.7732314453125}
store['active_learning_steps'][51]['acquisition']={'indices': [40305, 46848, 46750, 9867, 765], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9401941299438477})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9497514963150024})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.0084989070892334})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.019883632659912})
store['active_learning_steps'][52]['training']['best_epoch']=1
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8511, 'crossentropy': 0.80400419921875}
store['active_learning_steps'][52]['acquisition']={'indices': [35595, 46995, 3418, 33810, 23951], 'labels': [1, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 0.9646149277687073})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.9088739156723022})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.9630881547927856})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 1.0062613487243652})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0130727291107178})
store['active_learning_steps'][53]['training']['best_epoch']=2
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8785, 'crossentropy': 0.798010888671875}
store['active_learning_steps'][53]['acquisition']={'indices': [44688, 58666, 23591, 29764, 22885], 'labels': [-1, 8, 8, 4, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8341822624206543})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9243953227996826})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9160857796669006})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9868868589401245})
store['active_learning_steps'][54]['training']['best_epoch']=1
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8536, 'crossentropy': 0.7659388671875}
store['active_learning_steps'][54]['acquisition']={'indices': [27487, 41811, 15643, 50715, 21099], 'labels': [-1, 0, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8822060823440552})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.9838980436325073})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 1.0179204940795898})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 1.063969612121582})
store['active_learning_steps'][55]['training']['best_epoch']=1
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8664, 'crossentropy': 0.793546533203125}
store['active_learning_steps'][55]['acquisition']={'indices': [11391, 38189, 31135, 43804, 37936], 'labels': [-1, 5, 8, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9108821153640747})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.946589469909668})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.9243974089622498})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.9351432919502258})
store['active_learning_steps'][56]['training']['best_epoch']=1
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8615, 'crossentropy': 0.7771857421875}
store['active_learning_steps'][56]['acquisition']={'indices': [6325, 47743, 41254, 48063, 22237], 'labels': [0, 2, 9, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.9052872657775879})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.948033332824707})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.9842808842658997})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.9370254874229431})
store['active_learning_steps'][57]['training']['best_epoch']=1
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.8555, 'crossentropy': 0.79078759765625}
store['active_learning_steps'][57]['acquisition']={'indices': [23037, 48229, 34980, 57717, 26774], 'labels': [1, 1, 1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8859670162200928})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.9160489439964294})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8408203125, 'crossentropy': 1.0112804174423218})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 1.1167478561401367})
store['active_learning_steps'][58]['training']['best_epoch']=1
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8331, 'crossentropy': 0.88117080078125}
store['active_learning_steps'][58]['acquisition']={'indices': [53038, 31403, 52161, 41689, 29529], 'labels': [-1, 4, 0, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8894143104553223})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8829655647277832})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9445184469223022})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9045101404190063})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 1.0002837181091309})
store['active_learning_steps'][59]['training']['best_epoch']=2
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.887, 'crossentropy': 0.731333251953125}
store['active_learning_steps'][59]['acquisition']={'indices': [27012, 3037, 47338, 50457, 12442], 'labels': [-1, 4, -1, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.9152336716651917})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8814204931259155})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.9570799469947815})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 1.108751893043518})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.1602847576141357})
store['active_learning_steps'][60]['training']['best_epoch']=2
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8758, 'crossentropy': 0.7630521484375}
store['active_learning_steps'][60]['acquisition']={'indices': [29194, 23757, 45661, 46873, 24167], 'labels': [8, 2, 2, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8628458976745605})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.803656816482544})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8145532011985779})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9707218408584595})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9308822154998779})
store['active_learning_steps'][61]['training']['best_epoch']=2
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8831, 'crossentropy': 0.685194580078125}
store['active_learning_steps'][61]['acquisition']={'indices': [38843, 55495, 28632, 30496, 41988], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7955043315887451})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.824562668800354})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.9686098694801331})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9697843790054321})
store['active_learning_steps'][62]['training']['best_epoch']=1
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.869, 'crossentropy': 0.72164912109375}
store['active_learning_steps'][62]['acquisition']={'indices': [50669, 8189, 29092, 24460, 52816], 'labels': [-1, 1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8606301546096802})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.8532136082649231})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 1.0348461866378784})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.918152391910553})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9676859378814697})
store['active_learning_steps'][63]['training']['best_epoch']=2
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.8829, 'crossentropy': 0.7718439453125}
store['active_learning_steps'][63]['acquisition']={'indices': [54013, 7540, 31346, 3326, 59573], 'labels': [-1, -1, 5, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6937617659568787})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.735219419002533})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8559921979904175})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8924477100372314})
store['active_learning_steps'][64]['training']['best_epoch']=1
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8713, 'crossentropy': 0.696926611328125}
store['active_learning_steps'][64]['acquisition']={'indices': [31175, 34970, 57723, 15501, 27530], 'labels': [6, -1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8080048561096191})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.9691370725631714})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.9188358783721924})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9250597953796387})
store['active_learning_steps'][65]['training']['best_epoch']=1
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8461, 'crossentropy': 0.80393203125}
store['active_learning_steps'][65]['acquisition']={'indices': [6384, 10248, 1780, 15756, 5893], 'labels': [-1, 1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8097823858261108})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7958672046661377})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8909162282943726})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9886634945869446})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.9864740371704102})
store['active_learning_steps'][66]['training']['best_epoch']=2
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8869, 'crossentropy': 0.680186669921875}
store['active_learning_steps'][66]['acquisition']={'indices': [37597, 29490, 58535, 54811, 23208], 'labels': [-1, 0, -1, 5, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.7837821245193481})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.8449358940124512})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.9290156960487366})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9292999505996704})
store['active_learning_steps'][67]['training']['best_epoch']=1
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.8672, 'crossentropy': 0.693347509765625}
store['active_learning_steps'][67]['acquisition']={'indices': [16479, 37281, 35981, 671, 44289], 'labels': [-1, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.876224935054779})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.78798508644104})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8759666681289673})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0111935138702393})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 1.0023066997528076})
store['active_learning_steps'][68]['training']['best_epoch']=2
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8864, 'crossentropy': 0.692073388671875}
store['active_learning_steps'][68]['acquisition']={'indices': [23714, 13579, 52141, 47458, 44813], 'labels': [4, -1, -1, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.830451488494873})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.8836543560028076})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8471609354019165})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8645086288452148})
store['active_learning_steps'][69]['training']['best_epoch']=1
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.8539, 'crossentropy': 0.7351150390625}
store['active_learning_steps'][69]['acquisition']={'indices': [9344, 15834, 57367, 22794, 17485], 'labels': [-1, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7785557508468628})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8365110158920288})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9449954032897949})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.9344339370727539})
store['active_learning_steps'][70]['training']['best_epoch']=1
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8709, 'crossentropy': 0.703038818359375}
store['active_learning_steps'][70]['acquisition']={'indices': [10682, 1579, 23543, 10468, 52805], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.7877019643783569})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.8583199381828308})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.8039078712463379})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8893322944641113})
store['active_learning_steps'][71]['training']['best_epoch']=1
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.8656, 'crossentropy': 0.72358974609375}
store['active_learning_steps'][71]['acquisition']={'indices': [9914, 33448, 13319, 57257, 7537], 'labels': [0, 5, 7, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8435928821563721})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.814041793346405})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7871346473693848})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8460556268692017})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.9767467975616455})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.931105375289917})
store['active_learning_steps'][72]['training']['best_epoch']=3
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.896, 'crossentropy': 0.718130615234375}
store['active_learning_steps'][72]['acquisition']={'indices': [11141, 44088, 32856, 38617, 45976], 'labels': [-1, -1, -1, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8330078125, 'crossentropy': 0.8125047087669373})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7255591154098511})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9107456803321838})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.9750262498855591})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.9071667194366455})
store['active_learning_steps'][73]['training']['best_epoch']=2
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.8853, 'crossentropy': 0.722973486328125}
store['active_learning_steps'][73]['acquisition']={'indices': [45228, 29174, 55047, 31626, 50733], 'labels': [6, 5, -1, 6, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7747896909713745})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7554489374160767})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8619647026062012})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.8472344279289246})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8585301637649536})
store['active_learning_steps'][74]['training']['best_epoch']=2
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.8928, 'crossentropy': 0.6939330078125}
store['active_learning_steps'][74]['acquisition']={'indices': [56063, 2250, 20574, 4250, 56026], 'labels': [-1, 5, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7587110996246338})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.70979905128479})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8244211077690125})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.8421116471290588})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.8856292366981506})
store['active_learning_steps'][75]['training']['best_epoch']=2
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.8809, 'crossentropy': 0.697115869140625}
store['active_learning_steps'][75]['acquisition']={'indices': [44232, 42226, 29089, 3725, 56227], 'labels': [-1, 8, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8500828742980957})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7716355323791504})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8002645969390869})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8294519782066345})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.8210577964782715})
store['active_learning_steps'][76]['training']['best_epoch']=2
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.8912, 'crossentropy': 0.645474609375}
store['active_learning_steps'][76]['acquisition']={'indices': [18371, 19644, 33778, 35401, 22924], 'labels': [0, 9, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7747980356216431})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7471553087234497})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8297412395477295})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8260847330093384})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.8779615759849548})
store['active_learning_steps'][77]['training']['best_epoch']=2
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.8969, 'crossentropy': 0.657379638671875}
store['active_learning_steps'][77]['acquisition']={'indices': [22211, 6682, 1837, 58702, 54260], 'labels': [5, 1, 0, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8086071610450745})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7846838235855103})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8592451810836792})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.9151766896247864})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.9487956762313843})
store['active_learning_steps'][78]['training']['best_epoch']=2
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.8798, 'crossentropy': 0.7015099609375}
store['active_learning_steps'][78]['acquisition']={'indices': [47951, 23373, 18636, 45392, 21557], 'labels': [-1, -1, 4, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8786182403564453})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8701798915863037})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.8809614181518555})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.9976325631141663})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 1.0376434326171875})
store['active_learning_steps'][79]['training']['best_epoch']=2
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.8875, 'crossentropy': 0.731257763671875}
store['active_learning_steps'][79]['acquisition']={'indices': [14941, 34237, 20635, 26305, 51120], 'labels': [8, -1, 5, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8327218294143677})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.8450160026550293})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.8005664348602295})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.8986589312553406})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8727412223815918})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 1.0581834316253662})
store['active_learning_steps'][80]['training']['best_epoch']=3
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.8906, 'crossentropy': 0.7140080078125}
store['active_learning_steps'][80]['acquisition']={'indices': [24740, 44081, 52608, 36353, 58731], 'labels': [8, 9, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8052689433097839})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.7271509170532227})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7283958196640015})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.87005615234375})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8475970029830933})
store['active_learning_steps'][81]['training']['best_epoch']=2
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.893, 'crossentropy': 0.632780615234375}
store['active_learning_steps'][81]['acquisition']={'indices': [33344, 45207, 26044, 28899, 40706], 'labels': [-1, -1, 0, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7410999536514282})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6992502212524414})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7923972010612488})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7992323637008667})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8547677397727966})
store['active_learning_steps'][82]['training']['best_epoch']=2
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9049, 'crossentropy': 0.582802587890625}
store['active_learning_steps'][82]['acquisition']={'indices': [4884, 7272, 14028, 51367, 51201], 'labels': [1, -1, -1, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7970828413963318})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7390036582946777})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7737765312194824})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8523218631744385})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8873801231384277})
store['active_learning_steps'][83]['training']['best_epoch']=2
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.8904, 'crossentropy': 0.669048681640625}
store['active_learning_steps'][83]['acquisition']={'indices': [812, 34705, 50893, 21291, 22914], 'labels': [-1, -1, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8225295543670654})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7078392505645752})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.730546772480011})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8568010926246643})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.874800443649292})
store['active_learning_steps'][84]['training']['best_epoch']=2
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9031, 'crossentropy': 0.629417626953125}
store['active_learning_steps'][84]['acquisition']={'indices': [4018, 18653, 23706, 15857, 55536], 'labels': [6, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7640902996063232})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.692778468132019})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.8122060298919678})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7350709438323975})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.8744990825653076})
store['active_learning_steps'][85]['training']['best_epoch']=2
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.8942, 'crossentropy': 0.650215576171875}
store['active_learning_steps'][85]['acquisition']={'indices': [59179, 26609, 34903, 38807, 21622], 'labels': [4, 9, 9, -1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8870185613632202})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.701225757598877})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7466380596160889})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.8534835577011108})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.8726730346679688})
store['active_learning_steps'][86]['training']['best_epoch']=2
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.902, 'crossentropy': 0.616000341796875}
store['active_learning_steps'][86]['acquisition']={'indices': [59679, 37150, 58879, 31858, 2060], 'labels': [6, 9, -1, 4, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][87]['training']={}
store['active_learning_steps'][87]['training']['epochs']=[]
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8483573198318481})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.8216079473495483})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.819881021976471})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7833161354064941})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.9070396423339844})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7955371141433716})
store['active_learning_steps'][87]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.9311418533325195})
store['active_learning_steps'][87]['training']['best_epoch']=4
store['active_learning_steps'][87]['evaluation_metrics']={'accuracy': 0.8973, 'crossentropy': 0.691395458984375}
store['active_learning_steps'][87]['acquisition']={'indices': [38593, 15942, 44494, 13865, 46051], 'labels': [3, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][88]['training']={}
store['active_learning_steps'][88]['training']['epochs']=[]
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7569437026977539})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7001961469650269})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.781131386756897})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.9047148823738098})
store['active_learning_steps'][88]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8975681066513062})
store['active_learning_steps'][88]['training']['best_epoch']=2
store['active_learning_steps'][88]['evaluation_metrics']={'accuracy': 0.8937, 'crossentropy': 0.64370283203125}
store['active_learning_steps'][88]['acquisition']={'indices': [54180, 30850, 32251, 19346, 20447], 'labels': [-1, -1, 9, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][89]['training']={}
store['active_learning_steps'][89]['training']['epochs']=[]
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7441203594207764})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7710394859313965})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.801045835018158})
store['active_learning_steps'][89]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8971609473228455})
store['active_learning_steps'][89]['training']['best_epoch']=1
store['active_learning_steps'][89]['evaluation_metrics']={'accuracy': 0.8836, 'crossentropy': 0.655593994140625}
store['active_learning_steps'][89]['acquisition']={'indices': [16964, 3105, 58330, 45823, 12309], 'labels': [-1, -1, 5, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][90]['training']={}
store['active_learning_steps'][90]['training']['epochs']=[]
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7280848026275635})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7162222266197205})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.76683509349823})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.74957275390625})
store['active_learning_steps'][90]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8465840220451355})
store['active_learning_steps'][90]['training']['best_epoch']=2
store['active_learning_steps'][90]['evaluation_metrics']={'accuracy': 0.9025, 'crossentropy': 0.57742763671875}
store['active_learning_steps'][90]['acquisition']={'indices': [28337, 35751, 9959, 49433, 48905], 'labels': [7, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][91]['training']={}
store['active_learning_steps'][91]['training']['epochs']=[]
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7668394446372986})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7057169675827026})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7635437250137329})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6799495816230774})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.828840434551239})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.8089561462402344})
store['active_learning_steps'][91]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8806988000869751})
store['active_learning_steps'][91]['training']['best_epoch']=4
store['active_learning_steps'][91]['evaluation_metrics']={'accuracy': 0.9115, 'crossentropy': 0.636033203125}
store['active_learning_steps'][91]['acquisition']={'indices': [53963, 655, 50708, 4524, 22683], 'labels': [-1, -1, 7, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][92]['training']={}
store['active_learning_steps'][92]['training']['epochs']=[]
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7410731315612793})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6714708805084229})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7685065865516663})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8734956979751587})
store['active_learning_steps'][92]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8218754529953003})
store['active_learning_steps'][92]['training']['best_epoch']=2
store['active_learning_steps'][92]['evaluation_metrics']={'accuracy': 0.8995, 'crossentropy': 0.61315771484375}
store['active_learning_steps'][92]['acquisition']={'indices': [49041, 45839, 5831, 1614, 8943], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][93]['training']={}
store['active_learning_steps'][93]['training']['epochs']=[]
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7164915800094604})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6753697395324707})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7410142421722412})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.864571213722229})
store['active_learning_steps'][93]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.8685010671615601})
store['active_learning_steps'][93]['training']['best_epoch']=2
store['active_learning_steps'][93]['evaluation_metrics']={'accuracy': 0.8898, 'crossentropy': 0.62678994140625}
store['active_learning_steps'][93]['acquisition']={'indices': [58793, 51109, 16054, 44058, 13986], 'labels': [3, 6, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][94]['training']={}
store['active_learning_steps'][94]['training']['epochs']=[]
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7609752416610718})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7618115544319153})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7785183787345886})
store['active_learning_steps'][94]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.8070065975189209})
store['active_learning_steps'][94]['training']['best_epoch']=1
store['active_learning_steps'][94]['evaluation_metrics']={'accuracy': 0.8722, 'crossentropy': 0.698238818359375}
store['active_learning_steps'][94]['acquisition']={'indices': [25106, 8178, 5682, 19440, 43914], 'labels': [-1, -1, 6, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][95]['training']={}
store['active_learning_steps'][95]['training']['epochs']=[]
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7078644037246704})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6961438655853271})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7115728259086609})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7999427914619446})
store['active_learning_steps'][95]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.7720469832420349})
store['active_learning_steps'][95]['training']['best_epoch']=2
store['active_learning_steps'][95]['evaluation_metrics']={'accuracy': 0.9009, 'crossentropy': 0.6126744140625}
store['active_learning_steps'][95]['acquisition']={'indices': [8530, 46491, 1378, 1720, 35749], 'labels': [1, -1, 3, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][96]['training']={}
store['active_learning_steps'][96]['training']['epochs']=[]
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.7355809211730957})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.7124675512313843})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7471785545349121})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.8126481175422668})
store['active_learning_steps'][96]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8392481803894043})
store['active_learning_steps'][96]['training']['best_epoch']=2
store['active_learning_steps'][96]['evaluation_metrics']={'accuracy': 0.899, 'crossentropy': 0.647573291015625}
store['active_learning_steps'][96]['acquisition']={'indices': [16937, 25167, 22493, 6539, 32722], 'labels': [-1, -1, -1, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][97]['training']={}
store['active_learning_steps'][97]['training']['epochs']=[]
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8045543432235718})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7345079183578491})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.7315300703048706})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.8138418793678284})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8777022957801819})
store['active_learning_steps'][97]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.9024862051010132})
store['active_learning_steps'][97]['training']['best_epoch']=3
store['active_learning_steps'][97]['evaluation_metrics']={'accuracy': 0.9099, 'crossentropy': 0.625229345703125}
store['active_learning_steps'][97]['acquisition']={'indices': [43835, 43459, 58311, 24733, 29175], 'labels': [4, 5, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][98]['training']={}
store['active_learning_steps'][98]['training']['epochs']=[]
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7555030584335327})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7212111949920654})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7829639911651611})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7678360939025879})
store['active_learning_steps'][98]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.8213019967079163})
store['active_learning_steps'][98]['training']['best_epoch']=2
store['active_learning_steps'][98]['evaluation_metrics']={'accuracy': 0.8907, 'crossentropy': 0.652762841796875}
store['active_learning_steps'][98]['acquisition']={'indices': [37614, 13945, 37996, 42928, 43888], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][99]['training']={}
store['active_learning_steps'][99]['training']['epochs']=[]
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.8093384504318237})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6808035969734192})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7081982493400574})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.8457415103912354})
store['active_learning_steps'][99]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7137014269828796})
store['active_learning_steps'][99]['training']['best_epoch']=2
store['active_learning_steps'][99]['evaluation_metrics']={'accuracy': 0.9059, 'crossentropy': 0.58523818359375}
store['active_learning_steps'][99]['acquisition']={'indices': [51318, 35940, 49578, 36445, 38703], 'labels': [-1, -1, 8, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][100]['training']={}
store['active_learning_steps'][100]['training']['epochs']=[]
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8811106085777283})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6801422834396362})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.7275668978691101})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7448062300682068})
store['active_learning_steps'][100]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7220667004585266})
store['active_learning_steps'][100]['training']['best_epoch']=2
store['active_learning_steps'][100]['evaluation_metrics']={'accuracy': 0.905, 'crossentropy': 0.596364697265625}
store['active_learning_steps'][100]['acquisition']={'indices': [37861, 24969, 56362, 8228, 29347], 'labels': [2, -1, -1, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][101]['training']={}
store['active_learning_steps'][101]['training']['epochs']=[]
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.84765625, 'crossentropy': 0.8378328680992126})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6441354751586914})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.7911891937255859})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7995421886444092})
store['active_learning_steps'][101]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.7905418276786804})
store['active_learning_steps'][101]['training']['best_epoch']=2
store['active_learning_steps'][101]['evaluation_metrics']={'accuracy': 0.9026, 'crossentropy': 0.6073328125}
store['active_learning_steps'][101]['acquisition']={'indices': [7127, 13104, 36529, 14803, 49715], 'labels': [0, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][102]['training']={}
store['active_learning_steps'][102]['training']['epochs']=[]
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.7033021450042725})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7233759164810181})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7790922522544861})
store['active_learning_steps'][102]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7606785893440247})
store['active_learning_steps'][102]['training']['best_epoch']=1
store['active_learning_steps'][102]['evaluation_metrics']={'accuracy': 0.879, 'crossentropy': 0.636411865234375}
store['active_learning_steps'][102]['acquisition']={'indices': [41725, 2650, 31618, 57999, 41309], 'labels': [7, 7, 5, 2, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][103]['training']={}
store['active_learning_steps'][103]['training']['epochs']=[]
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7404323816299438})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7239744663238525})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6930816173553467})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.74855637550354})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.8704395890235901})
store['active_learning_steps'][103]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.816041111946106})
store['active_learning_steps'][103]['training']['best_epoch']=3
store['active_learning_steps'][103]['evaluation_metrics']={'accuracy': 0.8994, 'crossentropy': 0.648942333984375}
store['active_learning_steps'][103]['acquisition']={'indices': [27376, 27857, 56433, 47576, 15947], 'labels': [2, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][104]['training']={}
store['active_learning_steps'][104]['training']['epochs']=[]
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6956765651702881})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6152770519256592})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.7274848222732544})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7118571996688843})
store['active_learning_steps'][104]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7612042427062988})
store['active_learning_steps'][104]['training']['best_epoch']=2
store['active_learning_steps'][104]['evaluation_metrics']={'accuracy': 0.9136, 'crossentropy': 0.559982568359375}
store['active_learning_steps'][104]['acquisition']={'indices': [7548, 12191, 9603, 11775, 17165], 'labels': [-1, 6, -1, 9, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][105]['training']={}
store['active_learning_steps'][105]['training']['epochs']=[]
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7345241904258728})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6799747943878174})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6866708993911743})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.7078921794891357})
store['active_learning_steps'][105]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7760735154151917})
store['active_learning_steps'][105]['training']['best_epoch']=2
store['active_learning_steps'][105]['evaluation_metrics']={'accuracy': 0.8973, 'crossentropy': 0.609945849609375}
store['active_learning_steps'][105]['acquisition']={'indices': [20050, 30227, 19404, 58242, 25554], 'labels': [-1, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][106]['training']={}
store['active_learning_steps'][106]['training']['epochs']=[]
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7310414910316467})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6943932771682739})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.740157425403595})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6821844577789307})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6884016990661621})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7205908298492432})
store['active_learning_steps'][106]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7819204330444336})
store['active_learning_steps'][106]['training']['best_epoch']=4
store['active_learning_steps'][106]['evaluation_metrics']={'accuracy': 0.9106, 'crossentropy': 0.633409716796875}
store['active_learning_steps'][106]['acquisition']={'indices': [23268, 10151, 6044, 46946, 3580], 'labels': [2, 8, -1, 9, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][107]['training']={}
store['active_learning_steps'][107]['training']['epochs']=[]
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6961019039154053})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5599442720413208})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6347190737724304})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6704462766647339})
store['active_learning_steps'][107]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7054218649864197})
store['active_learning_steps'][107]['training']['best_epoch']=2
store['active_learning_steps'][107]['evaluation_metrics']={'accuracy': 0.9172, 'crossentropy': 0.547245458984375}
store['active_learning_steps'][107]['acquisition']={'indices': [20473, 1762, 45880, 835, 24937], 'labels': [2, 4, 2, -1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][108]['training']={}
store['active_learning_steps'][108]['training']['epochs']=[]
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7125933766365051})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7048308253288269})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6919733285903931})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6881632804870605})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7019498348236084})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7521092295646667})
store['active_learning_steps'][108]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.7973102331161499})
store['active_learning_steps'][108]['training']['best_epoch']=4
store['active_learning_steps'][108]['evaluation_metrics']={'accuracy': 0.9222, 'crossentropy': 0.59438125}
store['active_learning_steps'][108]['acquisition']={'indices': [38833, 7467, 57940, 18703, 96], 'labels': [6, 2, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][109]['training']={}
store['active_learning_steps'][109]['training']['epochs']=[]
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7085045576095581})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6239761114120483})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.666641354560852})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6647483110427856})
store['active_learning_steps'][109]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6774709820747375})
store['active_learning_steps'][109]['training']['best_epoch']=2
store['active_learning_steps'][109]['evaluation_metrics']={'accuracy': 0.9059, 'crossentropy': 0.54644609375}
store['active_learning_steps'][109]['acquisition']={'indices': [11207, 5323, 23046, 43016, 34446], 'labels': [7, 3, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][110]['training']={}
store['active_learning_steps'][110]['training']['epochs']=[]
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7114872932434082})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6853033304214478})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6312189102172852})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6036627888679504})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7323483824729919})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.7768239974975586})
store['active_learning_steps'][110]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7585428953170776})
store['active_learning_steps'][110]['training']['best_epoch']=4
store['active_learning_steps'][110]['evaluation_metrics']={'accuracy': 0.9223, 'crossentropy': 0.58115126953125}
store['active_learning_steps'][110]['acquisition']={'indices': [52809, 53757, 59886, 20231, 37726], 'labels': [0, 3, 3, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][111]['training']={}
store['active_learning_steps'][111]['training']['epochs']=[]
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6750328540802002})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.6512131690979004})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6493448615074158})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6830453872680664})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7786126136779785})
store['active_learning_steps'][111]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.773364245891571})
store['active_learning_steps'][111]['training']['best_epoch']=3
store['active_learning_steps'][111]['evaluation_metrics']={'accuracy': 0.9186, 'crossentropy': 0.555863916015625}
store['active_learning_steps'][111]['acquisition']={'indices': [32099, 18751, 42820, 48355, 40211], 'labels': [-1, -1, 8, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][112]['training']={}
store['active_learning_steps'][112]['training']['epochs']=[]
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7380967140197754})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6388162970542908})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.65147864818573})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7167037725448608})
store['active_learning_steps'][112]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6809654235839844})
store['active_learning_steps'][112]['training']['best_epoch']=2
store['active_learning_steps'][112]['evaluation_metrics']={'accuracy': 0.8931, 'crossentropy': 0.6074267578125}
store['active_learning_steps'][112]['acquisition']={'indices': [58500, 24452, 59390, 21354, 53569], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][113]['training']={}
store['active_learning_steps'][113]['training']['epochs']=[]
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6583237051963806})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5673648118972778})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6178594827651978})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.564848780632019})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.656554639339447})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6322609186172485})
store['active_learning_steps'][113]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6827749013900757})
store['active_learning_steps'][113]['training']['best_epoch']=4
store['active_learning_steps'][113]['evaluation_metrics']={'accuracy': 0.9256, 'crossentropy': 0.511762890625}
store['active_learning_steps'][113]['acquisition']={'indices': [28999, 23871, 59326, 59458, 50786], 'labels': [8, -1, 2, 9, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][114]['training']={}
store['active_learning_steps'][114]['training']['epochs']=[]
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7523905038833618})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6588393449783325})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6551965475082397})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.7175571918487549})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6886928677558899})
store['active_learning_steps'][114]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6794471740722656})
store['active_learning_steps'][114]['training']['best_epoch']=3
store['active_learning_steps'][114]['evaluation_metrics']={'accuracy': 0.9161, 'crossentropy': 0.562727001953125}
store['active_learning_steps'][114]['acquisition']={'indices': [23248, 51972, 9289, 39659, 31202], 'labels': [7, 5, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][115]['training']={}
store['active_learning_steps'][115]['training']['epochs']=[]
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.7045419216156006})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.7028263211250305})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.7283015847206116})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6365872621536255})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7586272358894348})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.7544788122177124})
store['active_learning_steps'][115]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.799390971660614})
store['active_learning_steps'][115]['training']['best_epoch']=4
store['active_learning_steps'][115]['evaluation_metrics']={'accuracy': 0.9214, 'crossentropy': 0.544329736328125}
store['active_learning_steps'][115]['acquisition']={'indices': [44080, 55566, 16857, 30665, 26699], 'labels': [-1, 3, -1, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][116]['training']={}
store['active_learning_steps'][116]['training']['epochs']=[]
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7135539054870605})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6239960789680481})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6417609453201294})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6441683173179626})
store['active_learning_steps'][116]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6805455684661865})
store['active_learning_steps'][116]['training']['best_epoch']=2
store['active_learning_steps'][116]['evaluation_metrics']={'accuracy': 0.9077, 'crossentropy': 0.584190087890625}
store['active_learning_steps'][116]['acquisition']={'indices': [41273, 30344, 303, 10683, 45745], 'labels': [6, -1, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][117]['training']={}
store['active_learning_steps'][117]['training']['epochs']=[]
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7429317235946655})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6304450035095215})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6633093357086182})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6825752258300781})
store['active_learning_steps'][117]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.7513145804405212})
store['active_learning_steps'][117]['training']['best_epoch']=2
store['active_learning_steps'][117]['evaluation_metrics']={'accuracy': 0.9151, 'crossentropy': 0.5390939453125}
store['active_learning_steps'][117]['acquisition']={'indices': [17233, 7333, 58253, 54544, 28066], 'labels': [8, 4, 1, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][118]['training']={}
store['active_learning_steps'][118]['training']['epochs']=[]
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.756666898727417})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6982285380363464})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6184976100921631})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.625957190990448})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6666250228881836})
store['active_learning_steps'][118]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6463114619255066})
store['active_learning_steps'][118]['training']['best_epoch']=3
store['active_learning_steps'][118]['evaluation_metrics']={'accuracy': 0.9192, 'crossentropy': 0.51577666015625}
store['active_learning_steps'][118]['acquisition']={'indices': [1794, 22234, 24816, 29886, 53912], 'labels': [-1, -1, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][119]['training']={}
store['active_learning_steps'][119]['training']['epochs']=[]
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6597598791122437})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6754318475723267})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7326523065567017})
store['active_learning_steps'][119]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.7567608952522278})
store['active_learning_steps'][119]['training']['best_epoch']=1
store['active_learning_steps'][119]['evaluation_metrics']={'accuracy': 0.8951, 'crossentropy': 0.608962890625}
store['active_learning_steps'][119]['acquisition']={'indices': [2060, 25899, 49151, 33104, 5496], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][120]['training']={}
store['active_learning_steps'][120]['training']['epochs']=[]
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7224792242050171})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.689555287361145})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6663689017295837})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.7142459154129028})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6677974462509155})
store['active_learning_steps'][120]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.7020249366760254})
store['active_learning_steps'][120]['training']['best_epoch']=3
store['active_learning_steps'][120]['evaluation_metrics']={'accuracy': 0.9153, 'crossentropy': 0.571933642578125}
store['active_learning_steps'][120]['acquisition']={'indices': [12766, 53667, 48399, 58766, 1940], 'labels': [2, 1, 4, 6, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][121]['training']={}
store['active_learning_steps'][121]['training']['epochs']=[]
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.6678359508514404})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6452932357788086})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6875767707824707})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6277956962585449})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6724852323532104})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.7420629262924194})
store['active_learning_steps'][121]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7112724781036377})
store['active_learning_steps'][121]['training']['best_epoch']=4
store['active_learning_steps'][121]['evaluation_metrics']={'accuracy': 0.9191, 'crossentropy': 0.548150634765625}
store['active_learning_steps'][121]['acquisition']={'indices': [42091, 34916, 42246, 4800, 48686], 'labels': [0, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][122]['training']={}
store['active_learning_steps'][122]['training']['epochs']=[]
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7366147041320801})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6744248867034912})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6299666166305542})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.8172105550765991})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7624730467796326})
store['active_learning_steps'][122]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.8422631025314331})
store['active_learning_steps'][122]['training']['best_epoch']=3
store['active_learning_steps'][122]['evaluation_metrics']={'accuracy': 0.9117, 'crossentropy': 0.561777783203125}
store['active_learning_steps'][122]['acquisition']={'indices': [29397, 31001, 51678, 31436, 37274], 'labels': [-1, -1, -1, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][123]['training']={}
store['active_learning_steps'][123]['training']['epochs']=[]
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6531491279602051})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6522893905639648})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6552591919898987})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.7854509353637695})
store['active_learning_steps'][123]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.7867594957351685})
store['active_learning_steps'][123]['training']['best_epoch']=2
store['active_learning_steps'][123]['evaluation_metrics']={'accuracy': 0.9036, 'crossentropy': 0.56956494140625}
store['active_learning_steps'][123]['acquisition']={'indices': [25555, 11578, 54536, 4833, 31637], 'labels': [4, 4, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][124]['training']={}
store['active_learning_steps'][124]['training']['epochs']=[]
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6679219603538513})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6401933431625366})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6758387684822083})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6595662832260132})
store['active_learning_steps'][124]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.7306737899780273})
store['active_learning_steps'][124]['training']['best_epoch']=2
store['active_learning_steps'][124]['evaluation_metrics']={'accuracy': 0.9111, 'crossentropy': 0.544692626953125}
store['active_learning_steps'][124]['acquisition']={'indices': [29694, 32761, 25519, 56568, 52624], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][125]['training']={}
store['active_learning_steps'][125]['training']['epochs']=[]
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.8515625, 'crossentropy': 0.7873224020004272})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6570652723312378})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.7261682152748108})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6807860732078552})
store['active_learning_steps'][125]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.7379797697067261})
store['active_learning_steps'][125]['training']['best_epoch']=2
store['active_learning_steps'][125]['evaluation_metrics']={'accuracy': 0.9051, 'crossentropy': 0.544158642578125}
store['active_learning_steps'][125]['acquisition']={'indices': [3860, 43298, 56274, 19992, 12477], 'labels': [5, 3, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][126]['training']={}
store['active_learning_steps'][126]['training']['epochs']=[]
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6834119558334351})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.604155957698822})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6112213730812073})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6655440330505371})
store['active_learning_steps'][126]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6629295349121094})
store['active_learning_steps'][126]['training']['best_epoch']=2
store['active_learning_steps'][126]['evaluation_metrics']={'accuracy': 0.9114, 'crossentropy': 0.527511572265625}
store['active_learning_steps'][126]['acquisition']={'indices': [3517, 46320, 57860, 33569, 2878], 'labels': [8, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][127]['training']={}
store['active_learning_steps'][127]['training']['epochs']=[]
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.73713219165802})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6410973072052002})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6564599275588989})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.7031575441360474})
store['active_learning_steps'][127]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.7699194550514221})
store['active_learning_steps'][127]['training']['best_epoch']=2
store['active_learning_steps'][127]['evaluation_metrics']={'accuracy': 0.9129, 'crossentropy': 0.5481333984375}
store['active_learning_steps'][127]['acquisition']={'indices': [47842, 17350, 56355, 33453, 1394], 'labels': [2, 7, 2, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][128]['training']={}
store['active_learning_steps'][128]['training']['epochs']=[]
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6980855464935303})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6481417417526245})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6102063655853271})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.6684561371803284})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.669355571269989})
store['active_learning_steps'][128]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.695675253868103})
store['active_learning_steps'][128]['training']['best_epoch']=3
store['active_learning_steps'][128]['evaluation_metrics']={'accuracy': 0.9181, 'crossentropy': 0.552780224609375}
store['active_learning_steps'][128]['acquisition']={'indices': [38578, 4705, 3029, 34733, 8834], 'labels': [-1, -1, 8, 4, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][129]['training']={}
store['active_learning_steps'][129]['training']['epochs']=[]
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6598160266876221})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6500506401062012})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6124805212020874})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6346743702888489})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6858509182929993})
store['active_learning_steps'][129]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6593047380447388})
store['active_learning_steps'][129]['training']['best_epoch']=3
store['active_learning_steps'][129]['evaluation_metrics']={'accuracy': 0.9188, 'crossentropy': 0.535667919921875}
store['active_learning_steps'][129]['acquisition']={'indices': [32329, 32142, 47819, 30574, 46497], 'labels': [8, -1, 2, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][130]['training']={}
store['active_learning_steps'][130]['training']['epochs']=[]
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.6863417625427246})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6499703526496887})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.643547773361206})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.653304934501648})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6314692497253418})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6965939402580261})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.7057880759239197})
store['active_learning_steps'][130]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.784647524356842})
store['active_learning_steps'][130]['training']['best_epoch']=5
store['active_learning_steps'][130]['evaluation_metrics']={'accuracy': 0.9271, 'crossentropy': 0.53816455078125}
store['active_learning_steps'][130]['acquisition']={'indices': [35306, 29683, 42434, 31786, 12310], 'labels': [-1, -1, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][131]['training']={}
store['active_learning_steps'][131]['training']['epochs']=[]
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7204397916793823})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6075588464736938})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6180709600448608})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6324316263198853})
store['active_learning_steps'][131]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.693006157875061})
store['active_learning_steps'][131]['training']['best_epoch']=2
store['active_learning_steps'][131]['evaluation_metrics']={'accuracy': 0.9134, 'crossentropy': 0.5187595703125}
store['active_learning_steps'][131]['acquisition']={'indices': [44372, 23714, 56872, 48604, 30160], 'labels': [0, -1, 8, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][132]['training']={}
store['active_learning_steps'][132]['training']['epochs']=[]
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.632489800453186})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6137462854385376})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6037380695343018})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.7097470760345459})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.6901066899299622})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5944597721099854})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.7118761539459229})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.679125964641571})
store['active_learning_steps'][132]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.7221502065658569})
store['active_learning_steps'][132]['training']['best_epoch']=6
store['active_learning_steps'][132]['evaluation_metrics']={'accuracy': 0.9275, 'crossentropy': 0.550509814453125}
store['active_learning_steps'][132]['acquisition']={'indices': [39034, 17116, 26895, 15496, 520], 'labels': [9, 3, 9, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][133]['training']={}
store['active_learning_steps'][133]['training']['epochs']=[]
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6823842525482178})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5925866365432739})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6181207895278931})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6131201982498169})
store['active_learning_steps'][133]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6998127698898315})
store['active_learning_steps'][133]['training']['best_epoch']=2
store['active_learning_steps'][133]['evaluation_metrics']={'accuracy': 0.9177, 'crossentropy': 0.489157373046875}
store['active_learning_steps'][133]['acquisition']={'indices': [32769, 31435, 40093, 28559, 31617], 'labels': [4, -1, 6, -1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][134]['training']={}
store['active_learning_steps'][134]['training']['epochs']=[]
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6764853000640869})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.5804320573806763})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6674302816390991})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5701829195022583})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.670085072517395})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.681291937828064})
store['active_learning_steps'][134]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6808968782424927})
store['active_learning_steps'][134]['training']['best_epoch']=4
store['active_learning_steps'][134]['evaluation_metrics']={'accuracy': 0.9248, 'crossentropy': 0.49068349609375}
store['active_learning_steps'][134]['acquisition']={'indices': [55401, 56977, 49047, 54062, 12105], 'labels': [-1, -1, -1, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][135]['training']={}
store['active_learning_steps'][135]['training']['epochs']=[]
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.733390212059021})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6254099607467651})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6387122869491577})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6628979444503784})
store['active_learning_steps'][135]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6273282766342163})
store['active_learning_steps'][135]['training']['best_epoch']=2
store['active_learning_steps'][135]['evaluation_metrics']={'accuracy': 0.9055, 'crossentropy': 0.561185205078125}
store['active_learning_steps'][135]['acquisition']={'indices': [53685, 39478, 14826, 29225, 19925], 'labels': [-1, -1, 8, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][136]['training']={}
store['active_learning_steps'][136]['training']['epochs']=[]
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.7127903699874878})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6406192779541016})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6120544075965881})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5854210257530212})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6379910707473755})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6965129375457764})
store['active_learning_steps'][136]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.7302930355072021})
store['active_learning_steps'][136]['training']['best_epoch']=4
store['active_learning_steps'][136]['evaluation_metrics']={'accuracy': 0.9241, 'crossentropy': 0.518076953125}
store['active_learning_steps'][136]['acquisition']={'indices': [29868, 46366, 4013, 20060, 25359], 'labels': [-1, -1, 1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][137]['training']={}
store['active_learning_steps'][137]['training']['epochs']=[]
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.696809709072113})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5989903211593628})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5996659994125366})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5743525624275208})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5852309465408325})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6760058403015137})
store['active_learning_steps'][137]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6601859331130981})
store['active_learning_steps'][137]['training']['best_epoch']=4
store['active_learning_steps'][137]['evaluation_metrics']={'accuracy': 0.9255, 'crossentropy': 0.5151197265625}
store['active_learning_steps'][137]['acquisition']={'indices': [51353, 45517, 12246, 44429, 3623], 'labels': [-1, 3, -1, 9, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][138]['training']={}
store['active_learning_steps'][138]['training']['epochs']=[]
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7300562858581543})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6826062798500061})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6100978851318359})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6462034583091736})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6790093779563904})
store['active_learning_steps'][138]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.7177642583847046})
store['active_learning_steps'][138]['training']['best_epoch']=3
store['active_learning_steps'][138]['evaluation_metrics']={'accuracy': 0.918, 'crossentropy': 0.56119609375}
store['active_learning_steps'][138]['acquisition']={'indices': [58626, 13854, 47931, 14019, 59977], 'labels': [6, -1, -1, -1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][139]['training']={}
store['active_learning_steps'][139]['training']['epochs']=[]
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7073069214820862})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6234500408172607})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6336414813995361})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.6933944225311279})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6093740463256836})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.678875207901001})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6887484192848206})
store['active_learning_steps'][139]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6892697811126709})
store['active_learning_steps'][139]['training']['best_epoch']=5
store['active_learning_steps'][139]['evaluation_metrics']={'accuracy': 0.9284, 'crossentropy': 0.512451953125}
store['active_learning_steps'][139]['acquisition']={'indices': [25818, 38879, 19040, 30593, 5080], 'labels': [0, 2, 6, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][140]['training']={}
store['active_learning_steps'][140]['training']['epochs']=[]
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7110669016838074})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5956424474716187})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.6186865568161011})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6636049151420593})
store['active_learning_steps'][140]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6685075163841248})
store['active_learning_steps'][140]['training']['best_epoch']=2
store['active_learning_steps'][140]['evaluation_metrics']={'accuracy': 0.9129, 'crossentropy': 0.535812890625}
store['active_learning_steps'][140]['acquisition']={'indices': [7703, 51097, 30802, 2567, 23006], 'labels': [-1, -1, 2, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][141]['training']={}
store['active_learning_steps'][141]['training']['epochs']=[]
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.7606480121612549})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6153609156608582})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6490527391433716})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5889248847961426})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6017922163009644})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.6901595592498779})
store['active_learning_steps'][141]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.7224398851394653})
store['active_learning_steps'][141]['training']['best_epoch']=4
store['active_learning_steps'][141]['evaluation_metrics']={'accuracy': 0.928, 'crossentropy': 0.49530185546875}
store['active_learning_steps'][141]['acquisition']={'indices': [37328, 50606, 48777, 52426, 46857], 'labels': [4, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][142]['training']={}
store['active_learning_steps'][142]['training']['epochs']=[]
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.731606125831604})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5797514915466309})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6482284069061279})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.6385623216629028})
store['active_learning_steps'][142]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.625054121017456})
store['active_learning_steps'][142]['training']['best_epoch']=2
store['active_learning_steps'][142]['evaluation_metrics']={'accuracy': 0.9097, 'crossentropy': 0.5242466796875}
store['active_learning_steps'][142]['acquisition']={'indices': [19817, 14691, 57145, 25006, 6108], 'labels': [7, 3, 9, 4, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][143]['training']={}
store['active_learning_steps'][143]['training']['epochs']=[]
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6162929534912109})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5212659239768982})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5272634625434875})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5609053373336792})
store['active_learning_steps'][143]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5932452082633972})
store['active_learning_steps'][143]['training']['best_epoch']=2
store['active_learning_steps'][143]['evaluation_metrics']={'accuracy': 0.9211, 'crossentropy': 0.456941064453125}
store['active_learning_steps'][143]['acquisition']={'indices': [46024, 28963, 20996, 39675, 14711], 'labels': [6, 4, 7, 3, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][144]['training']={}
store['active_learning_steps'][144]['training']['epochs']=[]
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6838765144348145})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6332603693008423})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6574501991271973})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.589469313621521})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6544584035873413})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.6114299297332764})
store['active_learning_steps'][144]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6508274078369141})
store['active_learning_steps'][144]['training']['best_epoch']=4
store['active_learning_steps'][144]['evaluation_metrics']={'accuracy': 0.9259, 'crossentropy': 0.51410517578125}
store['active_learning_steps'][144]['acquisition']={'indices': [3858, 57183, 33911, 22482, 43924], 'labels': [6, -1, 3, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][145]['training']={}
store['active_learning_steps'][145]['training']['epochs']=[]
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6570413112640381})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5563032031059265})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.597248375415802})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5894726514816284})
store['active_learning_steps'][145]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6008307933807373})
store['active_learning_steps'][145]['training']['best_epoch']=2
store['active_learning_steps'][145]['evaluation_metrics']={'accuracy': 0.9173, 'crossentropy': 0.479602587890625}
store['active_learning_steps'][145]['acquisition']={'indices': [55939, 6040, 36060, 36627, 35779], 'labels': [1, 3, 5, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][146]['training']={}
store['active_learning_steps'][146]['training']['epochs']=[]
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6620091199874878})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6669413447380066})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5565185546875})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.627639889717102})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6616249084472656})
store['active_learning_steps'][146]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5797760486602783})
store['active_learning_steps'][146]['training']['best_epoch']=3
store['active_learning_steps'][146]['evaluation_metrics']={'accuracy': 0.9238, 'crossentropy': 0.500297119140625}
store['active_learning_steps'][146]['acquisition']={'indices': [22060, 39154, 16882, 41421, 4566], 'labels': [8, -1, 7, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][147]['training']={}
store['active_learning_steps'][147]['training']['epochs']=[]
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7082734107971191})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5579845905303955})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.6045680046081543})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5444818735122681})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5737063884735107})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6465733051300049})
store['active_learning_steps'][147]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6671029329299927})
store['active_learning_steps'][147]['training']['best_epoch']=4
store['active_learning_steps'][147]['evaluation_metrics']={'accuracy': 0.928, 'crossentropy': 0.480277783203125}
store['active_learning_steps'][147]['acquisition']={'indices': [19259, 1607, 47690, 18558, 28096], 'labels': [-1, -1, 0, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][148]['training']={}
store['active_learning_steps'][148]['training']['epochs']=[]
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.7469226121902466})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.5790319442749023})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5617035627365112})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.604650616645813})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.5957987308502197})
store['active_learning_steps'][148]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6750168204307556})
store['active_learning_steps'][148]['training']['best_epoch']=3
store['active_learning_steps'][148]['evaluation_metrics']={'accuracy': 0.9197, 'crossentropy': 0.52012109375}
store['active_learning_steps'][148]['acquisition']={'indices': [55775, 47390, 50780, 5622, 47297], 'labels': [5, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][149]['training']={}
store['active_learning_steps'][149]['training']['epochs']=[]
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7392520904541016})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.5957746505737305})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5949829816818237})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.6540600657463074})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.636093020439148})
store['active_learning_steps'][149]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.671391487121582})
store['active_learning_steps'][149]['training']['best_epoch']=3
store['active_learning_steps'][149]['evaluation_metrics']={'accuracy': 0.9199, 'crossentropy': 0.53997138671875}
store['active_learning_steps'][149]['acquisition']={'indices': [43207, 45857, 19993, 34604, 41583], 'labels': [-1, -1, -1, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][150]['training']={}
store['active_learning_steps'][150]['training']['epochs']=[]
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7196349501609802})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.574770450592041})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5511054992675781})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.588639497756958})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6169780492782593})
store['active_learning_steps'][150]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.630878210067749})
store['active_learning_steps'][150]['training']['best_epoch']=3
store['active_learning_steps'][150]['evaluation_metrics']={'accuracy': 0.9242, 'crossentropy': 0.50217783203125}
store['active_learning_steps'][150]['acquisition']={'indices': [17778, 18647, 25933, 37309, 22486], 'labels': [3, 1, -1, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][151]['training']={}
store['active_learning_steps'][151]['training']['epochs']=[]
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.689635157585144})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6133180856704712})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5597434043884277})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6090853214263916})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5594663023948669})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6748324632644653})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6315329074859619})
store['active_learning_steps'][151]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.602867841720581})
store['active_learning_steps'][151]['training']['best_epoch']=5
store['active_learning_steps'][151]['evaluation_metrics']={'accuracy': 0.9231, 'crossentropy': 0.528405419921875}
store['active_learning_steps'][151]['acquisition']={'indices': [40676, 41389, 20747, 57430, 15741], 'labels': [6, -1, -1, 1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][152]['training']={}
store['active_learning_steps'][152]['training']['epochs']=[]
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7047260999679565})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5493556261062622})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5498120784759521})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5467156767845154})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5777311325073242})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5817841291427612})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5466333031654358})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5888048410415649})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6175326108932495})
store['active_learning_steps'][152]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.617611289024353})
store['active_learning_steps'][152]['training']['best_epoch']=7
store['active_learning_steps'][152]['evaluation_metrics']={'accuracy': 0.9336, 'crossentropy': 0.474991357421875}
store['active_learning_steps'][152]['acquisition']={'indices': [40777, 325, 37376, 37367, 42762], 'labels': [8, 2, 9, 2, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][153]['training']={}
store['active_learning_steps'][153]['training']['epochs']=[]
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.6872943639755249})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.5863603949546814})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5403985381126404})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5443073511123657})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5637626647949219})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5336321592330933})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6117825508117676})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6121839880943298})
store['active_learning_steps'][153]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5733636617660522})
store['active_learning_steps'][153]['training']['best_epoch']=6
store['active_learning_steps'][153]['evaluation_metrics']={'accuracy': 0.9362, 'crossentropy': 0.470248876953125}
store['active_learning_steps'][153]['acquisition']={'indices': [55899, 2207, 58735, 3888, 49440], 'labels': [-1, -1, 9, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][154]['training']={}
store['active_learning_steps'][154]['training']['epochs']=[]
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7269903421401978})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5664263367652893})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5751749277114868})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.5714132785797119})
store['active_learning_steps'][154]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5836082100868225})
store['active_learning_steps'][154]['training']['best_epoch']=2
store['active_learning_steps'][154]['evaluation_metrics']={'accuracy': 0.9115, 'crossentropy': 0.510365234375}
store['active_learning_steps'][154]['acquisition']={'indices': [45516, 15428, 36212, 19820, 20518], 'labels': [-1, -1, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][155]['training']={}
store['active_learning_steps'][155]['training']['epochs']=[]
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6522859334945679})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.5276825428009033})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5551935434341431})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5965113639831543})
store['active_learning_steps'][155]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5346170663833618})
store['active_learning_steps'][155]['training']['best_epoch']=2
store['active_learning_steps'][155]['evaluation_metrics']={'accuracy': 0.9142, 'crossentropy': 0.49564599609375}
store['active_learning_steps'][155]['acquisition']={'indices': [50130, 14711, 41794, 7514, 26607], 'labels': [1, 2, 2, 8, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][156]['training']={}
store['active_learning_steps'][156]['training']['epochs']=[]
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6494771242141724})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5283540487289429})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.5935405492782593})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5932002663612366})
store['active_learning_steps'][156]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.5694959759712219})
store['active_learning_steps'][156]['training']['best_epoch']=2
store['active_learning_steps'][156]['evaluation_metrics']={'accuracy': 0.9215, 'crossentropy': 0.488060302734375}
store['active_learning_steps'][156]['acquisition']={'indices': [39823, 2522, 22368, 21357, 56195], 'labels': [0, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][157]['training']={}
store['active_learning_steps'][157]['training']['epochs']=[]
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.671699047088623})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.5601183176040649})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5589199066162109})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6084276437759399})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.552763819694519})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.6260372996330261})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5563125610351562})
store['active_learning_steps'][157]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.6414511203765869})
store['active_learning_steps'][157]['training']['best_epoch']=5
store['active_learning_steps'][157]['evaluation_metrics']={'accuracy': 0.931, 'crossentropy': 0.486518310546875}
store['active_learning_steps'][157]['acquisition']={'indices': [45338, 20124, 59282, 42970, 8689], 'labels': [6, -1, -1, 5, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][158]['training']={}
store['active_learning_steps'][158]['training']['epochs']=[]
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.61017906665802})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5273414254188538})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.4823056161403656})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5501835346221924})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5171267986297607})
store['active_learning_steps'][158]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5594931840896606})
store['active_learning_steps'][158]['training']['best_epoch']=3
store['active_learning_steps'][158]['evaluation_metrics']={'accuracy': 0.9288, 'crossentropy': 0.438380517578125}
store['active_learning_steps'][158]['acquisition']={'indices': [11131, 58850, 19071, 43075, 19830], 'labels': [-1, 9, 1, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][159]['training']={}
store['active_learning_steps'][159]['training']['epochs']=[]
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6629152297973633})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5261427164077759})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.514717698097229})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5804071426391602})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.8974609375, 'crossentropy': 0.6499743461608887})
store['active_learning_steps'][159]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5247219800949097})
store['active_learning_steps'][159]['training']['best_epoch']=3
store['active_learning_steps'][159]['evaluation_metrics']={'accuracy': 0.9268, 'crossentropy': 0.474336083984375}
store['active_learning_steps'][159]['acquisition']={'indices': [18942, 50095, 36355, 19556, 40658], 'labels': [-1, 7, -1, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][160]['training']={}
store['active_learning_steps'][160]['training']['epochs']=[]
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.6870465874671936})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5729181170463562})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.904296875, 'crossentropy': 0.6130791902542114})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.6071663498878479})
store['active_learning_steps'][160]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.6951730251312256})
store['active_learning_steps'][160]['training']['best_epoch']=2
store['active_learning_steps'][160]['evaluation_metrics']={'accuracy': 0.9172, 'crossentropy': 0.476513720703125}
store['active_learning_steps'][160]['acquisition']={'indices': [29037, 8610, 11537, 54492, 22272], 'labels': [5, -1, -1, 8, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][161]['training']={}
store['active_learning_steps'][161]['training']['epochs']=[]
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.8466796875, 'crossentropy': 0.7069511413574219})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6290673017501831})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5868702530860901})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.6173555850982666})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.560779333114624})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6194659471511841})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.6253963708877563})
store['active_learning_steps'][161]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.7041544914245605})
store['active_learning_steps'][161]['training']['best_epoch']=5
store['active_learning_steps'][161]['evaluation_metrics']={'accuracy': 0.9317, 'crossentropy': 0.475494140625}
store['active_learning_steps'][161]['acquisition']={'indices': [15707, 29788, 32123, 46017, 54507], 'labels': [8, -1, -1, 0, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][162]['training']={}
store['active_learning_steps'][162]['training']['epochs']=[]
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7162004709243774})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5969282388687134})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5303358435630798})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5752238631248474})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5828220248222351})
store['active_learning_steps'][162]['training']['epochs'].append({'accuracy': 0.90625, 'crossentropy': 0.6868664622306824})
store['active_learning_steps'][162]['training']['best_epoch']=3
store['active_learning_steps'][162]['evaluation_metrics']={'accuracy': 0.9241, 'crossentropy': 0.49018623046875}
store['active_learning_steps'][162]['acquisition']={'indices': [36607, 1932, 19627, 46933, 38516], 'labels': [9, 4, 6, -1, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][163]['training']={}
store['active_learning_steps'][163]['training']['epochs']=[]
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.7794933319091797})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9013671875, 'crossentropy': 0.5525406002998352})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5760700702667236})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5402960777282715})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5650275945663452})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.9287109375, 'crossentropy': 0.5933840870857239})
store['active_learning_steps'][163]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.6291993260383606})
store['active_learning_steps'][163]['training']['best_epoch']=4
store['active_learning_steps'][163]['evaluation_metrics']={'accuracy': 0.9241, 'crossentropy': 0.488560693359375}
store['active_learning_steps'][163]['acquisition']={'indices': [12828, 16713, 38109, 52337, 8648], 'labels': [3, -1, -1, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][164]['training']={}
store['active_learning_steps'][164]['training']['epochs']=[]
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.7330328226089478})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.5840214490890503})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5282758474349976})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5667250156402588})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5905236601829529})
store['active_learning_steps'][164]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6489553451538086})
store['active_learning_steps'][164]['training']['best_epoch']=3
store['active_learning_steps'][164]['evaluation_metrics']={'accuracy': 0.9219, 'crossentropy': 0.48663740234375}
store['active_learning_steps'][164]['acquisition']={'indices': [25651, 22786, 54417, 52719, 32865], 'labels': [-1, 4, -1, -1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][165]['training']={}
store['active_learning_steps'][165]['training']['epochs']=[]
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6493086814880371})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.5312992930412292})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5100452899932861})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5457127094268799})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.5436289310455322})
store['active_learning_steps'][165]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6079434156417847})
store['active_learning_steps'][165]['training']['best_epoch']=3
store['active_learning_steps'][165]['evaluation_metrics']={'accuracy': 0.9245, 'crossentropy': 0.457463916015625}
store['active_learning_steps'][165]['acquisition']={'indices': [31786, 33592, 44869, 58351, 49443], 'labels': [-1, 9, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][166]['training']={}
store['active_learning_steps'][166]['training']['epochs']=[]
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6654016971588135})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.6185491681098938})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5394065380096436})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5932120084762573})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5825483202934265})
store['active_learning_steps'][166]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6274539232254028})
store['active_learning_steps'][166]['training']['best_epoch']=3
store['active_learning_steps'][166]['evaluation_metrics']={'accuracy': 0.9225, 'crossentropy': 0.47772607421875}
store['active_learning_steps'][166]['acquisition']={'indices': [1802, 3329, 35299, 54489, 52180], 'labels': [-1, 2, -1, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][167]['training']={}
store['active_learning_steps'][167]['training']['epochs']=[]
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6846129894256592})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5483371615409851})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.557870626449585})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.6102312803268433})
store['active_learning_steps'][167]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5944620966911316})
store['active_learning_steps'][167]['training']['best_epoch']=2
store['active_learning_steps'][167]['evaluation_metrics']={'accuracy': 0.9131, 'crossentropy': 0.501153955078125}
store['active_learning_steps'][167]['acquisition']={'indices': [39391, 55674, 54676, 18628, 35109], 'labels': [-1, -1, 2, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][168]['training']={}
store['active_learning_steps'][168]['training']['epochs']=[]
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6205531358718872})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9140625, 'crossentropy': 0.5369874238967896})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5609742403030396})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.6255202889442444})
store['active_learning_steps'][168]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5762503147125244})
store['active_learning_steps'][168]['training']['best_epoch']=2
store['active_learning_steps'][168]['evaluation_metrics']={'accuracy': 0.9144, 'crossentropy': 0.505665234375}
store['active_learning_steps'][168]['acquisition']={'indices': [57140, 3436, 57414, 13080, 3257], 'labels': [6, 4, 7, 1, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][169]['training']={}
store['active_learning_steps'][169]['training']['epochs']=[]
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7286229133605957})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.5655174255371094})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.555388331413269})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5260412693023682})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.548720121383667})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.608564019203186})
store['active_learning_steps'][169]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5612208247184753})
store['active_learning_steps'][169]['training']['best_epoch']=4
store['active_learning_steps'][169]['evaluation_metrics']={'accuracy': 0.9248, 'crossentropy': 0.476174609375}
store['active_learning_steps'][169]['acquisition']={'indices': [48660, 38242, 58173, 7949, 40412], 'labels': [-1, -1, -1, -1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][170]['training']={}
store['active_learning_steps'][170]['training']['epochs']=[]
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7802411913871765})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9072265625, 'crossentropy': 0.5491786003112793})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9111328125, 'crossentropy': 0.5051047801971436})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5573802590370178})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.6273177862167358})
store['active_learning_steps'][170]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6045889854431152})
store['active_learning_steps'][170]['training']['best_epoch']=3
store['active_learning_steps'][170]['evaluation_metrics']={'accuracy': 0.9238, 'crossentropy': 0.466906884765625}
store['active_learning_steps'][170]['acquisition']={'indices': [37133, 11224, 45766, 30067, 11454], 'labels': [-1, 9, -1, 8, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][171]['training']={}
store['active_learning_steps'][171]['training']['epochs']=[]
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.607743501663208})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5935919284820557})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5617409944534302})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.923828125, 'crossentropy': 0.5577751994132996})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5702813863754272})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.5809373259544373})
store['active_learning_steps'][171]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.588959813117981})
store['active_learning_steps'][171]['training']['best_epoch']=4
store['active_learning_steps'][171]['evaluation_metrics']={'accuracy': 0.9299, 'crossentropy': 0.468988037109375}
store['active_learning_steps'][171]['acquisition']={'indices': [13112, 35974, 7223, 38688, 13207], 'labels': [1, 2, -1, 7, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][172]['training']={}
store['active_learning_steps'][172]['training']['epochs']=[]
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.701408863067627})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.557532787322998})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.916015625, 'crossentropy': 0.5227923393249512})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.48303481936454773})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5705884695053101})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5486677289009094})
store['active_learning_steps'][172]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5216618180274963})
store['active_learning_steps'][172]['training']['best_epoch']=4
store['active_learning_steps'][172]['evaluation_metrics']={'accuracy': 0.9361, 'crossentropy': 0.4507240234375}
store['active_learning_steps'][172]['acquisition']={'indices': [2059, 2277, 30151, 8037, 40363], 'labels': [-1, 4, 4, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][173]['training']={}
store['active_learning_steps'][173]['training']['epochs']=[]
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.6938538551330566})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.8984375, 'crossentropy': 0.5614919662475586})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.541858434677124})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.5155172944068909})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5570727586746216})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.921875, 'crossentropy': 0.5405507683753967})
store['active_learning_steps'][173]['training']['epochs'].append({'accuracy': 0.9267578125, 'crossentropy': 0.5675398111343384})
store['active_learning_steps'][173]['training']['best_epoch']=4
store['active_learning_steps'][173]['evaluation_metrics']={'accuracy': 0.9291, 'crossentropy': 0.45322802734375}
store['active_learning_steps'][173]['acquisition']={'indices': [27154, 24931, 32854, 25630, 10607], 'labels': [-1, 3, -1, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][174]['training']={}
store['active_learning_steps'][174]['training']['epochs']=[]
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6951759457588196})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9091796875, 'crossentropy': 0.5328744649887085})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.4972584843635559})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9208984375, 'crossentropy': 0.5902751684188843})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9169921875, 'crossentropy': 0.5143727660179138})
store['active_learning_steps'][174]['training']['epochs'].append({'accuracy': 0.9306640625, 'crossentropy': 0.5380129814147949})
store['active_learning_steps'][174]['training']['best_epoch']=3
store['active_learning_steps'][174]['evaluation_metrics']={'accuracy': 0.9288, 'crossentropy': 0.4532439453125}
store['active_learning_steps'][174]['acquisition']={'indices': [25192, 11767, 43315, 58952, 36057], 'labels': [-1, -1, 1, 0, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][175]['training']={}
store['active_learning_steps'][175]['training']['epochs']=[]
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6695464253425598})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5419306755065918})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5424232482910156})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5408414602279663})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.9189453125, 'crossentropy': 0.5341407060623169})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.931640625, 'crossentropy': 0.5626528263092041})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.927734375, 'crossentropy': 0.6380089521408081})
store['active_learning_steps'][175]['training']['epochs'].append({'accuracy': 0.919921875, 'crossentropy': 0.6493101716041565})
store['active_learning_steps'][175]['training']['best_epoch']=5
store['active_learning_steps'][175]['evaluation_metrics']={'accuracy': 0.9323, 'crossentropy': 0.456107666015625}
store['active_learning_steps'][175]['acquisition']={'indices': [19081, 34124, 13134, 30508, 56641], 'labels': [5, 6, -1, -1, -1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][176]['training']={}
store['active_learning_steps'][176]['training']['epochs']=[]
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.666980504989624})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9033203125, 'crossentropy': 0.5484093427658081})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.912109375, 'crossentropy': 0.58388352394104})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9052734375, 'crossentropy': 0.6089527606964111})
store['active_learning_steps'][176]['training']['epochs'].append({'accuracy': 0.9130859375, 'crossentropy': 0.5810793042182922})
store['active_learning_steps'][176]['training']['best_epoch']=2
store['active_learning_steps'][176]['evaluation_metrics']={'accuracy': 0.9111, 'crossentropy': 0.499120166015625}
store['active_learning_steps'][176]['acquisition']={'indices': [23647, 2999, 52806, 54770, 28040], 'labels': [1, -1, -1, -1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][177]['training']={}
store['active_learning_steps'][177]['training']['epochs']=[]
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6924364566802979})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.90234375, 'crossentropy': 0.6124967932701111})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.908203125, 'crossentropy': 0.5504213571548462})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.91015625, 'crossentropy': 0.5796709060668945})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.92578125, 'crossentropy': 0.5686652064323425})
store['active_learning_steps'][177]['training']['epochs'].append({'accuracy': 0.9228515625, 'crossentropy': 0.6022888422012329})
store['active_learning_steps'][177]['training']['best_epoch']=3
store['active_learning_steps'][177]['evaluation_metrics']={'accuracy': 0.928, 'crossentropy': 0.46269423828125}
store['active_learning_steps'][177]['acquisition']={'indices': [33997, 58706, 1980, 16659, 22507], 'labels': [8, -1, 6, 8, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][178]['training']={}
store['active_learning_steps'][178]['training']['epochs']=[]
store['active_learning_steps'][178]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6220170855522156})
store['active_learning_steps'][178]['training']['epochs'].append({'accuracy': 0.9150390625, 'crossentropy': 0.5108098387718201})
store['active_learning_steps'][178]['training']['epochs'].append({'accuracy': 0.91796875, 'crossentropy': 0.4851122498512268})
store['active_learning_steps'][178]['training']['epochs'].append({'accuracy': 0.9248046875, 'crossentropy': 0.48652851581573486})
store['active_learning_steps'][178]['training']['epochs'].append({'accuracy': 0.9345703125, 'crossentropy': 0.5453262329101562})
store['active_learning_steps'][178]['training']['epochs'].append({'accuracy': 0.9326171875, 'crossentropy': 0.49333325028419495})
store['active_learning_steps'][178]['training']['best_epoch']=3
store['active_learning_steps'][178]['evaluation_metrics']={'accuracy': 0.9291, 'crossentropy': 0.425222314453125}
