store = {}
store['timestamp']=1620259916
store['cmdline']=['/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py', '--id=24']
store['commit']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['github_url']='8c7fc12bfba938daba445c0e68d9f8cf97c14443'
store['experiment']='/auto/users/andsch/github/active_learning_redux/batchbald_redux/uniform_target_ood_experiment.py'
store['job_id']=24
store['worker_id']=24
store['num_workers']=40
store['config']={'seed': 28, 'acquisition_size': 5, 'max_training_set': 450, 'num_pool_samples': 20, 'num_eval_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'validation_set_size': 1024, 'validation_split_random_state': 0, 'initial_training_set_size': 20, 'min_samples_per_epoch': 5056, 'mnist_repetitions': 1, 'ood_fmnist_repetitions': 1, 'add_dataset_noise': False, 'acquisition_function': 'batchbald_redux.acquisition_functions.Random', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationPoolModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 0.0}
store['log']={}
store['dataset_info']={'training': "(FastMNIST (train; 58976 samples) | one_hot_targets{'num_classes': 10}) + ('OoD Dataset (60000 samples)' | uniform_targets{'num_classes': 10})", 'test': "'FastMNIST (test, 10000 samples)'"}
store['initial_training_set_indices']=[30392, 53434, 12640, 8533, 22304, 37915, 58226, 44119, 3091, 14640, 58125, 39579, 43812, 53689, 52296, 46037, 22015, 40334, 57520, 43803]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.66796875, 'crossentropy': 2.0911107063293457})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.5415308475494385})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.681640625, 'crossentropy': 2.2463698387145996})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.712232828140259})
store['active_learning_steps'][0]['training']['best_epoch']=1
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.7058, 'crossentropy': 1.9501849609375}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 9958], ['id', 59986], ['id', 55551], ['id', 7167], ['ood', 30832]], 'labels': [5, 6, 6, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.1997323036193848})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.337614059448242})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.585773468017578})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 2.6754777431488037})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.6738, 'crossentropy': 2.0046091796875}
store['active_learning_steps'][1]['acquisition']={'indices': [['ood', 5177], ['id', 7399], ['id', 25753], ['id', 47114], ['id', 40714]], 'labels': [9, 4, 6, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6884765625, 'crossentropy': 1.570698857307434})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.8378009796142578})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.9697003364562988})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6962890625, 'crossentropy': 2.140777111053467})
store['active_learning_steps'][2]['training']['best_epoch']=1
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.7068, 'crossentropy': 1.45037802734375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 19723], ['ood', 12789], ['ood', 11717], ['ood', 19241], ['ood', 59708]], 'labels': [6, 1, 1, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6796875, 'crossentropy': 1.5762386322021484})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.591238021850586})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.697265625, 'crossentropy': 1.7709400653839111})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.7021484375, 'crossentropy': 2.066462516784668})
store['active_learning_steps'][3]['training']['best_epoch']=1
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.7014, 'crossentropy': 1.4323263671875}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 13888], ['id', 54811], ['id', 30360], ['id', 51466], ['id', 33374]], 'labels': [8, 5, 9, 0, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.671875, 'crossentropy': 1.3953649997711182})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.6336266994476318})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 1.9697716236114502})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.0277464389801025})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.6985, 'crossentropy': 1.34837392578125}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 4317], ['ood', 29450], ['id', 16832], ['ood', 36511], ['ood', 40012]], 'labels': [7, 3, 5, 0, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.67578125, 'crossentropy': 1.5290699005126953})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6787109375, 'crossentropy': 1.6492482423782349})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6943359375, 'crossentropy': 1.7010469436645508})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.693359375, 'crossentropy': 1.942399263381958})
store['active_learning_steps'][5]['training']['best_epoch']=1
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.702, 'crossentropy': 1.335110546875}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 8264], ['id', 1805], ['id', 58269], ['ood', 23545], ['id', 8855]], 'labels': [3, 3, 4, 3, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7197265625, 'crossentropy': 1.3089103698730469})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7255859375, 'crossentropy': 1.433797836303711})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.7353515625, 'crossentropy': 1.5554397106170654})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.734375, 'crossentropy': 1.7033286094665527})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.7443, 'crossentropy': 1.19388994140625}
store['active_learning_steps'][6]['acquisition']={'indices': [['ood', 30877], ['id', 45485], ['id', 24096], ['id', 29809], ['ood', 30435]], 'labels': [2, 4, 2, 0, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7041015625, 'crossentropy': 1.303248405456543})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7060546875, 'crossentropy': 1.5893880128860474})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7080078125, 'crossentropy': 1.6886074542999268})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.7138671875, 'crossentropy': 1.850264072418213})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.7379, 'crossentropy': 1.152658984375}
store['active_learning_steps'][7]['acquisition']={'indices': [['ood', 15539], ['ood', 46209], ['id', 17594], ['ood', 27697], ['ood', 36797]], 'labels': [2, 5, 8, 8, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.1572284698486328})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.7275390625, 'crossentropy': 1.471725583076477})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.732421875, 'crossentropy': 1.6118757724761963})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.73828125, 'crossentropy': 1.7336833477020264})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.7592, 'crossentropy': 1.10008662109375}
store['active_learning_steps'][8]['acquisition']={'indices': [['ood', 46047], ['ood', 31059], ['id', 55201], ['id', 26279], ['id', 2036]], 'labels': [9, 5, 9, 1, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.744140625, 'crossentropy': 1.1282892227172852})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.755859375, 'crossentropy': 1.1184132099151611})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7490234375, 'crossentropy': 1.274389386177063})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.7509765625, 'crossentropy': 1.4063129425048828})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 1.5053023099899292})
store['active_learning_steps'][9]['training']['best_epoch']=2
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.776, 'crossentropy': 1.07638134765625}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 4553], ['ood', 2686], ['id', 6295], ['id', 20597], ['id', 58406]], 'labels': [1, 7, 9, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7607421875, 'crossentropy': 1.132331132888794})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.1724295616149902})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.370496153831482})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.361061930656433})
store['active_learning_steps'][10]['training']['best_epoch']=1
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.7909, 'crossentropy': 1.01259267578125}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 54887], ['ood', 50594], ['id', 29503], ['id', 22946], ['id', 15405]], 'labels': [7, 9, 4, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 0.9602216482162476})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.0255533456802368})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0698060989379883})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.116213083267212})
store['active_learning_steps'][11]['training']['best_epoch']=1
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.794, 'crossentropy': 0.91835048828125}
store['active_learning_steps'][11]['acquisition']={'indices': [['ood', 54590], ['id', 26781], ['id', 9866], ['ood', 33636], ['ood', 21950]], 'labels': [5, 3, 8, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0553781986236572})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.0109659433364868})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.196305274963379})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.148640513420105})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 1.2527692317962646})
store['active_learning_steps'][12]['training']['best_epoch']=2
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.8068, 'crossentropy': 0.96335185546875}
store['active_learning_steps'][12]['acquisition']={'indices': [['ood', 9707], ['ood', 51530], ['id', 44145], ['id', 11442], ['ood', 3564]], 'labels': [2, 3, 7, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.0633349418640137})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.0794991254806519})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.211911916732788})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.2763960361480713})
store['active_learning_steps'][13]['training']['best_epoch']=1
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.7911, 'crossentropy': 0.94477412109375}
store['active_learning_steps'][13]['acquisition']={'indices': [['ood', 20231], ['id', 57143], ['ood', 42117], ['id', 16898], ['id', 37622]], 'labels': [4, 6, 1, 6, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7568359375, 'crossentropy': 1.0351449251174927})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.0353068113327026})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.1036773920059204})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.2437748908996582})
store['active_learning_steps'][14]['training']['best_epoch']=1
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.7894, 'crossentropy': 0.93446923828125}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 8465], ['id', 30394], ['ood', 40416], ['ood', 4173], ['id', 21751]], 'labels': [8, 9, 0, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.0243667364120483})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.1015187501907349})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.2460421323776245})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.1723577976226807})
store['active_learning_steps'][15]['training']['best_epoch']=1
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.8069, 'crossentropy': 0.91857333984375}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 8991], ['ood', 441], ['id', 1497], ['ood', 26221], ['id', 49250]], 'labels': [7, 0, 1, 1, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 1.0063493251800537})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.0198898315429688})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.7744140625, 'crossentropy': 1.16364586353302})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.1658499240875244})
store['active_learning_steps'][16]['training']['best_epoch']=1
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.8006, 'crossentropy': 0.89199931640625}
store['active_learning_steps'][16]['acquisition']={'indices': [['ood', 55798], ['ood', 50166], ['ood', 19934], ['ood', 28300], ['ood', 19231]], 'labels': [7, 2, 9, 4, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.0600379705429077})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.0704524517059326})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.261598825454712})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.791015625, 'crossentropy': 1.1654202938079834})
store['active_learning_steps'][17]['training']['best_epoch']=1
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.8054, 'crossentropy': 0.9542482421875}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 19121], ['ood', 50369], ['id', 23071], ['id', 58824], ['ood', 27290]], 'labels': [4, 3, 8, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.0436848402023315})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7734375, 'crossentropy': 1.080755352973938})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 1.0745468139648438})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.3189873695373535})
store['active_learning_steps'][18]['training']['best_epoch']=1
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.8037, 'crossentropy': 0.906896875}
store['active_learning_steps'][18]['acquisition']={'indices': [['ood', 26973], ['ood', 30880], ['id', 938], ['ood', 14742], ['ood', 52719]], 'labels': [3, 5, 2, 7, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.0802438259124756})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 0.9871463179588318})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.1420091390609741})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.8017578125, 'crossentropy': 1.187713861465454})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.7998046875, 'crossentropy': 1.2562353610992432})
store['active_learning_steps'][19]['training']['best_epoch']=2
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.8154, 'crossentropy': 0.91469306640625}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 29738], ['ood', 18928], ['ood', 51769], ['ood', 58173], ['id', 6668]], 'labels': [9, 3, 8, 9, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.993941605091095})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7841796875, 'crossentropy': 1.0169185400009155})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.138866901397705})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.1708823442459106})
store['active_learning_steps'][20]['training']['best_epoch']=1
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.808, 'crossentropy': 0.9028421875}
store['active_learning_steps'][20]['acquisition']={'indices': [['ood', 16871], ['ood', 8886], ['id', 9787], ['ood', 49837], ['id', 33634]], 'labels': [4, 6, 7, 3, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.01738703250885})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0396325588226318})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.1396230459213257})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.1179025173187256})
store['active_learning_steps'][21]['training']['best_epoch']=1
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.8113, 'crossentropy': 0.89802958984375}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 15860], ['ood', 8974], ['ood', 50118], ['id', 21833], ['ood', 2332]], 'labels': [9, 5, 9, 5, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.0384371280670166})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9464718103408813})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 1.0967644453048706})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.1547174453735352})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.1720821857452393})
store['active_learning_steps'][22]['training']['best_epoch']=2
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.8267, 'crossentropy': 0.8460373046875}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 22439], ['id', 14111], ['id', 20352], ['ood', 37688], ['id', 6955]], 'labels': [8, 7, 8, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0083415508270264})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9397768378257751})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.0708863735198975})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.0992363691329956})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.191118836402893})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.8239, 'crossentropy': 0.8456794921875}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 10048], ['id', 48846], ['id', 59726], ['ood', 2749], ['ood', 32985]], 'labels': [1, 4, 5, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.0446393489837646})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.1876392364501953})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.244089961051941})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.185370683670044})
store['active_learning_steps'][24]['training']['best_epoch']=1
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.7945, 'crossentropy': 0.94797099609375}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 49717], ['ood', 42539], ['id', 56597], ['id', 55032], ['ood', 19031]], 'labels': [1, 8, 9, 2, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.005361557006836})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.086045503616333})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.076977252960205})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.2042323350906372})
store['active_learning_steps'][25]['training']['best_epoch']=1
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.7997, 'crossentropy': 0.923441796875}
store['active_learning_steps'][25]['acquisition']={'indices': [['ood', 46194], ['id', 23562], ['id', 39223], ['id', 42320], ['id', 48705]], 'labels': [6, 8, 7, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.0101408958435059})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 1.0382647514343262})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 1.1108529567718506})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 1.2757439613342285})
store['active_learning_steps'][26]['training']['best_epoch']=1
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.8079, 'crossentropy': 0.90421728515625}
store['active_learning_steps'][26]['acquisition']={'indices': [['ood', 49687], ['id', 10555], ['ood', 3097], ['ood', 9878], ['id', 52388]], 'labels': [7, 1, 2, 3, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.751953125, 'crossentropy': 1.058973789215088})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.1480518579483032})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.25225031375885})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.765625, 'crossentropy': 1.391418218612671})
store['active_learning_steps'][27]['training']['best_epoch']=1
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.7919, 'crossentropy': 0.95850390625}
store['active_learning_steps'][27]['acquisition']={'indices': [['ood', 3994], ['id', 50661], ['id', 23385], ['id', 24091], ['ood', 42405]], 'labels': [5, 1, 5, 6, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.736328125, 'crossentropy': 1.112734079360962})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0663998126983643})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.2350363731384277})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.1703271865844727})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.310149908065796})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.8176, 'crossentropy': 0.925201171875}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 8347], ['ood', 57599], ['ood', 45078], ['id', 19865], ['id', 17227]], 'labels': [6, 7, 9, 3, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7216796875, 'crossentropy': 1.2068862915039062})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7626953125, 'crossentropy': 1.1077501773834229})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.7763671875, 'crossentropy': 1.2085506916046143})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.2312688827514648})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.771484375, 'crossentropy': 1.477398157119751})
store['active_learning_steps'][29]['training']['best_epoch']=2
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.8052, 'crossentropy': 0.9743330078125}
store['active_learning_steps'][29]['acquisition']={'indices': [['ood', 24909], ['id', 1320], ['ood', 53571], ['id', 57181], ['ood', 51011]], 'labels': [8, 3, 7, 7, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.062376856803894})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.0958878993988037})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7705078125, 'crossentropy': 1.1613359451293945})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.4289588928222656})
store['active_learning_steps'][30]['training']['best_epoch']=1
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.7929, 'crossentropy': 0.9576830078125}
store['active_learning_steps'][30]['acquisition']={'indices': [['ood', 12222], ['ood', 58255], ['id', 42464], ['id', 58680], ['id', 7761]], 'labels': [4, 5, 4, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.005415916442871})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7578125, 'crossentropy': 1.0817052125930786})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.775390625, 'crossentropy': 1.1609454154968262})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.271355152130127})
store['active_learning_steps'][31]['training']['best_epoch']=1
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.7904, 'crossentropy': 0.941658203125}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 53979], ['id', 39937], ['ood', 40359], ['id', 50669], ['ood', 55834]], 'labels': [8, 1, 0, 2, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.9738301634788513})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.018871784210205})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.1379976272583008})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.1119496822357178})
store['active_learning_steps'][32]['training']['best_epoch']=1
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.8062, 'crossentropy': 0.9068267578125}
store['active_learning_steps'][32]['acquisition']={'indices': [['ood', 51397], ['ood', 59659], ['id', 15748], ['id', 54151], ['ood', 15285]], 'labels': [0, 5, 2, 5, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.0273679494857788})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.779296875, 'crossentropy': 0.9744817018508911})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.0577127933502197})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.1211884021759033})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.087188720703125})
store['active_learning_steps'][33]['training']['best_epoch']=2
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.8224, 'crossentropy': 0.84605517578125}
store['active_learning_steps'][33]['acquisition']={'indices': [['ood', 19841], ['id', 17309], ['id', 46655], ['id', 49160], ['ood', 23094]], 'labels': [2, 6, 9, 2, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 0.9911117553710938})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7724609375, 'crossentropy': 1.0126333236694336})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 1.0741608142852783})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.7890625, 'crossentropy': 1.12605881690979})
store['active_learning_steps'][34]['training']['best_epoch']=1
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.8098, 'crossentropy': 0.89392158203125}
store['active_learning_steps'][34]['acquisition']={'indices': [['ood', 29126], ['id', 27078], ['ood', 29080], ['ood', 32523], ['ood', 10593]], 'labels': [6, 3, 1, 5, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.763671875, 'crossentropy': 1.055970311164856})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7666015625, 'crossentropy': 1.0642309188842773})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.0937016010284424})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 1.1796348094940186})
store['active_learning_steps'][35]['training']['best_epoch']=1
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.793, 'crossentropy': 0.91768642578125}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 33287], ['ood', 56556], ['id', 26398], ['id', 59038], ['id', 59742]], 'labels': [7, 6, 5, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.0149259567260742})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7822265625, 'crossentropy': 1.0375051498413086})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7783203125, 'crossentropy': 1.1886146068572998})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.7880859375, 'crossentropy': 1.1987591981887817})
store['active_learning_steps'][36]['training']['best_epoch']=1
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.7897, 'crossentropy': 0.92843818359375}
store['active_learning_steps'][36]['acquisition']={'indices': [['ood', 44373], ['id', 11946], ['ood', 38858], ['ood', 19097], ['ood', 6419]], 'labels': [6, 7, 9, 9, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7685546875, 'crossentropy': 1.0044326782226562})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.76953125, 'crossentropy': 0.9787259101867676})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 1.0767056941986084})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 1.1121798753738403})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 1.216477632522583})
store['active_learning_steps'][37]['training']['best_epoch']=2
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.8075, 'crossentropy': 0.87000068359375}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 50255], ['ood', 37915], ['id', 46132], ['ood', 23174], ['id', 7206]], 'labels': [7, 2, 7, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.759765625, 'crossentropy': 1.012341856956482})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9894407987594604})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.794921875, 'crossentropy': 1.1124306917190552})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.7919921875, 'crossentropy': 1.1664550304412842})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 1.1375617980957031})
store['active_learning_steps'][38]['training']['best_epoch']=2
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.8212, 'crossentropy': 0.874026953125}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 28942], ['id', 42385], ['id', 11812], ['id', 57668], ['id', 36264]], 'labels': [4, 9, 2, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.7802734375, 'crossentropy': 0.9594393372535706})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9403719902038574})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.9225338697433472})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 1.036210536956787})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 1.2097768783569336})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 1.0726264715194702})
store['active_learning_steps'][39]['training']['best_epoch']=3
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.8495, 'crossentropy': 0.786126513671875}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 30460], ['ood', 35897], ['id', 27054], ['ood', 56576], ['id', 40686]], 'labels': [8, 6, 7, 8, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.767578125, 'crossentropy': 0.9677785634994507})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.8762508630752563})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9276444911956787})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9557609558105469})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 1.0763925313949585})
store['active_learning_steps'][40]['training']['best_epoch']=2
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.8327, 'crossentropy': 0.78638623046875}
store['active_learning_steps'][40]['acquisition']={'indices': [['ood', 12062], ['id', 46239], ['id', 8987], ['ood', 48083], ['ood', 36134]], 'labels': [9, 2, 1, 7, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7646484375, 'crossentropy': 1.0288641452789307})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9426922798156738})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9504681825637817})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.796875, 'crossentropy': 1.0633244514465332})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 1.1275367736816406})
store['active_learning_steps'][41]['training']['best_epoch']=2
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.8293, 'crossentropy': 0.81275009765625}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 52280], ['ood', 30422], ['id', 47109], ['ood', 30069], ['id', 50194]], 'labels': [8, 2, 4, 7, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9259538650512695})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.7958984375, 'crossentropy': 0.9219332337379456})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9949226379394531})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.806640625, 'crossentropy': 1.128023624420166})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 1.0286235809326172})
store['active_learning_steps'][42]['training']['best_epoch']=2
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.8279, 'crossentropy': 0.7870626953125}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 18881], ['ood', 44981], ['id', 4156], ['ood', 56948], ['ood', 16001]], 'labels': [0, 1, 3, 3, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9562009572982788})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.8917015194892883})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8839097619056702})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.9086146354675293})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.9601154327392578})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 1.0505037307739258})
store['active_learning_steps'][43]['training']['best_epoch']=3
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.842, 'crossentropy': 0.799682421875}
store['active_learning_steps'][43]['acquisition']={'indices': [['ood', 24499], ['id', 6443], ['ood', 21490], ['ood', 8845], ['ood', 44500]], 'labels': [2, 1, 0, 1, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.78515625, 'crossentropy': 0.953179657459259})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8245449066162109})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9459846019744873})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.9237289428710938})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 1.0545692443847656})
store['active_learning_steps'][44]['training']['best_epoch']=2
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.837, 'crossentropy': 0.768307080078125}
store['active_learning_steps'][44]['acquisition']={'indices': [['ood', 42820], ['id', 4262], ['ood', 30269], ['ood', 10205], ['ood', 29790]], 'labels': [0, 3, 5, 4, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.7529296875, 'crossentropy': 1.0545234680175781})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.787109375, 'crossentropy': 0.9638701677322388})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.802734375, 'crossentropy': 0.9586517810821533})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.9926237463951111})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 1.2037206888198853})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 1.0275954008102417})
store['active_learning_steps'][45]['training']['best_epoch']=3
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.84, 'crossentropy': 0.83699619140625}
store['active_learning_steps'][45]['acquisition']={'indices': [['ood', 35087], ['ood', 24295], ['ood', 57956], ['id', 56452], ['ood', 23836]], 'labels': [6, 2, 7, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9732655882835388})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8426399827003479})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.888352632522583})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9495964646339417})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.8212890625, 'crossentropy': 0.9206892848014832})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.8447, 'crossentropy': 0.7643369140625}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 39579], ['ood', 47201], ['id', 31072], ['id', 18201], ['ood', 29989]], 'labels': [7, 0, 9, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.7861328125, 'crossentropy': 0.9342678785324097})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8046875, 'crossentropy': 0.8639625906944275})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 0.9292703866958618})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 1.0074844360351562})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.818359375, 'crossentropy': 0.9786868095397949})
store['active_learning_steps'][47]['training']['best_epoch']=2
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.8379, 'crossentropy': 0.771874365234375}
store['active_learning_steps'][47]['acquisition']={'indices': [['ood', 37996], ['id', 32857], ['ood', 18921], ['id', 28649], ['ood', 47827]], 'labels': [5, 9, 7, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.7900390625, 'crossentropy': 0.9025698900222778})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8115234375, 'crossentropy': 0.8549104928970337})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.9249140024185181})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.9024720191955566})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.810546875, 'crossentropy': 1.0351184606552124})
store['active_learning_steps'][48]['training']['best_epoch']=2
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.853, 'crossentropy': 0.731635400390625}
store['active_learning_steps'][48]['acquisition']={'indices': [['ood', 1728], ['id', 31661], ['id', 35818], ['ood', 38237], ['id', 25821]], 'labels': [5, 0, 4, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.78125, 'crossentropy': 0.9097113609313965})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8056640625, 'crossentropy': 0.8272603154182434})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8550631999969482})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9093184471130371})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.9674979448318481})
store['active_learning_steps'][49]['training']['best_epoch']=2
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.8414, 'crossentropy': 0.734981201171875}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 44767], ['ood', 22983], ['ood', 11705], ['id', 42379], ['ood', 6629]], 'labels': [2, 4, 4, 5, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9122511148452759})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8271484375, 'crossentropy': 0.8710684180259705})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.830078125, 'crossentropy': 0.8577554225921631})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.8797124624252319})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.8953568935394287})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9546264410018921})
store['active_learning_steps'][50]['training']['best_epoch']=3
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.8519, 'crossentropy': 0.759275634765625}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 44599], ['ood', 21441], ['ood', 56141], ['id', 23964], ['id', 36000]], 'labels': [0, 2, 8, 8, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.8476604223251343})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.7925969958305359})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.789718508720398})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.8913180828094482})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.850717306137085})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.9024121761322021})
store['active_learning_steps'][51]['training']['best_epoch']=3
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.8654, 'crossentropy': 0.6956369140625}
store['active_learning_steps'][51]['acquisition']={'indices': [['ood', 45833], ['ood', 33135], ['ood', 57321], ['id', 7041], ['ood', 36328]], 'labels': [2, 3, 7, 2, 0], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8154296875, 'crossentropy': 0.885147750377655})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.7518861293792725})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.808779239654541})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.7853747606277466})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7773388624191284})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.8723, 'crossentropy': 0.64491875}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 36212], ['ood', 45021], ['id', 51223], ['ood', 41124], ['id', 53850]], 'labels': [4, 8, 8, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.7978515625, 'crossentropy': 0.9252345561981201})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.7927243709564209})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8447265625, 'crossentropy': 0.7755987644195557})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.9145538806915283})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.8564453125, 'crossentropy': 0.8814857006072998})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.8999189138412476})
store['active_learning_steps'][53]['training']['best_epoch']=3
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.8671, 'crossentropy': 0.666897119140625}
store['active_learning_steps'][53]['acquisition']={'indices': [['ood', 8667], ['ood', 36393], ['ood', 56663], ['id', 15473], ['id', 7626]], 'labels': [3, 0, 0, 1, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.798828125, 'crossentropy': 0.9561342000961304})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8219287395477295})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8388671875, 'crossentropy': 0.8392254114151001})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9200642704963684})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.919100284576416})
store['active_learning_steps'][54]['training']['best_epoch']=2
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.8537, 'crossentropy': 0.756106787109375}
store['active_learning_steps'][54]['acquisition']={'indices': [['id', 35796], ['ood', 12434], ['ood', 33454], ['id', 4878], ['id', 12762]], 'labels': [3, 6, 8, 3, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][55]['training']={}
store['active_learning_steps'][55]['training']['epochs']=[]
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9268081784248352})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8008236885070801})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.841796875, 'crossentropy': 0.8879402875900269})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8486328125, 'crossentropy': 0.8139771819114685})
store['active_learning_steps'][55]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8554075360298157})
store['active_learning_steps'][55]['training']['best_epoch']=2
store['active_learning_steps'][55]['evaluation_metrics']={'accuracy': 0.8601, 'crossentropy': 0.711744580078125}
store['active_learning_steps'][55]['acquisition']={'indices': [['id', 55068], ['ood', 51799], ['ood', 10293], ['ood', 1800], ['ood', 16725]], 'labels': [9, 6, 5, 0, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][56]['training']={}
store['active_learning_steps'][56]['training']['epochs']=[]
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8134765625, 'crossentropy': 0.970431923866272})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.837890625, 'crossentropy': 0.8291884660720825})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.8111830949783325})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7992371320724487})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.8532582521438599})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8623046875, 'crossentropy': 0.880146861076355})
store['active_learning_steps'][56]['training']['epochs'].append({'accuracy': 0.8525390625, 'crossentropy': 0.8681870698928833})
store['active_learning_steps'][56]['training']['best_epoch']=4
store['active_learning_steps'][56]['evaluation_metrics']={'accuracy': 0.8717, 'crossentropy': 0.694278125}
store['active_learning_steps'][56]['acquisition']={'indices': [['id', 54349], ['id', 30384], ['ood', 51213], ['ood', 10732], ['id', 53119]], 'labels': [0, 0, 7, 9, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][57]['training']={}
store['active_learning_steps'][57]['training']['epochs']=[]
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.79296875, 'crossentropy': 0.9664672613143921})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7607395648956299})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8715811371803284})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.780175507068634})
store['active_learning_steps'][57]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.831153392791748})
store['active_learning_steps'][57]['training']['best_epoch']=2
store['active_learning_steps'][57]['evaluation_metrics']={'accuracy': 0.864, 'crossentropy': 0.69509931640625}
store['active_learning_steps'][57]['acquisition']={'indices': [['ood', 22305], ['id', 18308], ['id', 46099], ['id', 57765], ['ood', 41169]], 'labels': [9, 4, 8, 3, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][58]['training']={}
store['active_learning_steps'][58]['training']['epochs']=[]
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8095703125, 'crossentropy': 0.9201946258544922})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.859375, 'crossentropy': 0.7480815649032593})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.7466663122177124})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7852945923805237})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.8583984375, 'crossentropy': 0.8351207971572876})
store['active_learning_steps'][58]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.8547877669334412})
store['active_learning_steps'][58]['training']['best_epoch']=3
store['active_learning_steps'][58]['evaluation_metrics']={'accuracy': 0.8799, 'crossentropy': 0.661097119140625}
store['active_learning_steps'][58]['acquisition']={'indices': [['id', 28075], ['id', 20209], ['ood', 22714], ['ood', 26453], ['id', 40835]], 'labels': [3, 5, 9, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][59]['training']={}
store['active_learning_steps'][59]['training']['epochs']=[]
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9180487990379333})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7779121398925781})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.8165055513381958})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8544921875, 'crossentropy': 0.8487114906311035})
store['active_learning_steps'][59]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.8520760536193848})
store['active_learning_steps'][59]['training']['best_epoch']=2
store['active_learning_steps'][59]['evaluation_metrics']={'accuracy': 0.8767, 'crossentropy': 0.659347314453125}
store['active_learning_steps'][59]['acquisition']={'indices': [['ood', 16906], ['id', 34711], ['ood', 1126], ['ood', 11759], ['id', 44108]], 'labels': [9, 5, 7, 8, 1], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][60]['training']={}
store['active_learning_steps'][60]['training']['epochs']=[]
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8359375, 'crossentropy': 0.8628162741661072})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7127466797828674})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7444678544998169})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7307931780815125})
store['active_learning_steps'][60]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7490848302841187})
store['active_learning_steps'][60]['training']['best_epoch']=2
store['active_learning_steps'][60]['evaluation_metrics']={'accuracy': 0.8848, 'crossentropy': 0.6163107421875}
store['active_learning_steps'][60]['acquisition']={'indices': [['id', 47096], ['id', 45767], ['ood', 6943], ['ood', 8436], ['id', 35034]], 'labels': [0, 1, 6, 6, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][61]['training']={}
store['active_learning_steps'][61]['training']['epochs']=[]
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8173828125, 'crossentropy': 0.9443721175193787})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.7359088659286499})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7182220816612244})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.747094988822937})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7023309469223022})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7123590707778931})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7950319051742554})
store['active_learning_steps'][61]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7656941413879395})
store['active_learning_steps'][61]['training']['best_epoch']=5
store['active_learning_steps'][61]['evaluation_metrics']={'accuracy': 0.8956, 'crossentropy': 0.586907568359375}
store['active_learning_steps'][61]['acquisition']={'indices': [['id', 13960], ['ood', 44924], ['id', 44771], ['id', 5250], ['ood', 45281]], 'labels': [8, 4, 4, 2, 9], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][62]['training']={}
store['active_learning_steps'][62]['training']['epochs']=[]
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8614875078201294})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.7745335102081299})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8603515625, 'crossentropy': 0.6948000192642212})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.857421875, 'crossentropy': 0.7415711879730225})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7670433521270752})
store['active_learning_steps'][62]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.8273357152938843})
store['active_learning_steps'][62]['training']['best_epoch']=3
store['active_learning_steps'][62]['evaluation_metrics']={'accuracy': 0.889, 'crossentropy': 0.591046826171875}
store['active_learning_steps'][62]['acquisition']={'indices': [['id', 2952], ['ood', 9514], ['ood', 59031], ['ood', 8358], ['id', 57118]], 'labels': [0, 2, 7, 7, 8], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][63]['training']={}
store['active_learning_steps'][63]['training']['epochs']=[]
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.81640625, 'crossentropy': 0.9146842360496521})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.85546875, 'crossentropy': 0.776535153388977})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6703917384147644})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7248013019561768})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7226824760437012})
store['active_learning_steps'][63]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7266275882720947})
store['active_learning_steps'][63]['training']['best_epoch']=3
store['active_learning_steps'][63]['evaluation_metrics']={'accuracy': 0.887, 'crossentropy': 0.60287109375}
store['active_learning_steps'][63]['acquisition']={'indices': [['id', 14718], ['id', 41417], ['id', 41041], ['ood', 34792], ['id', 50533]], 'labels': [7, 2, 0, 0, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][64]['training']={}
store['active_learning_steps'][64]['training']['epochs']=[]
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.82421875, 'crossentropy': 0.8617244958877563})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6801779270172119})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7254228591918945})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6942200660705566})
store['active_learning_steps'][64]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.724180281162262})
store['active_learning_steps'][64]['training']['best_epoch']=2
store['active_learning_steps'][64]['evaluation_metrics']={'accuracy': 0.8894, 'crossentropy': 0.57573837890625}
store['active_learning_steps'][64]['acquisition']={'indices': [['id', 39319], ['id', 18136], ['ood', 47393], ['id', 18344], ['id', 48317]], 'labels': [9, 4, 2, 6, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][65]['training']={}
store['active_learning_steps'][65]['training']['epochs']=[]
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8251953125, 'crossentropy': 0.8708933591842651})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.7054011225700378})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7274122834205627})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7166295051574707})
store['active_learning_steps'][65]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7162939310073853})
store['active_learning_steps'][65]['training']['best_epoch']=2
store['active_learning_steps'][65]['evaluation_metrics']={'accuracy': 0.8788, 'crossentropy': 0.629003466796875}
store['active_learning_steps'][65]['acquisition']={'indices': [['id', 43011], ['ood', 18974], ['ood', 12780], ['id', 23911], ['id', 47852]], 'labels': [0, 3, 1, 1, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][66]['training']={}
store['active_learning_steps'][66]['training']['epochs']=[]
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.944769024848938})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6808674931526184})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7017873525619507})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7049649953842163})
store['active_learning_steps'][66]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.782248854637146})
store['active_learning_steps'][66]['training']['best_epoch']=2
store['active_learning_steps'][66]['evaluation_metrics']={'accuracy': 0.8874, 'crossentropy': 0.5746482421875}
store['active_learning_steps'][66]['acquisition']={'indices': [['ood', 46690], ['id', 51522], ['ood', 40855], ['ood', 45210], ['id', 57858]], 'labels': [0, 3, 2, 0, 7], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][67]['training']={}
store['active_learning_steps'][67]['training']['epochs']=[]
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8310546875, 'crossentropy': 0.8862805366516113})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.849609375, 'crossentropy': 0.7828280925750732})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6975390315055847})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6932926177978516})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7991556525230408})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6776902675628662})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7774885892868042})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.7692309021949768})
store['active_learning_steps'][67]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.7387109994888306})
store['active_learning_steps'][67]['training']['best_epoch']=6
store['active_learning_steps'][67]['evaluation_metrics']={'accuracy': 0.8997, 'crossentropy': 0.5823404296875}
store['active_learning_steps'][67]['acquisition']={'indices': [['id', 16396], ['ood', 29329], ['ood', 17813], ['id', 51390], ['id', 54796]], 'labels': [0, 5, 2, 1, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][68]['training']={}
store['active_learning_steps'][68]['training']['epochs']=[]
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9060341715812683})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7291043996810913})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.701946496963501})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7742347121238708})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.698312520980835})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.7760258913040161})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.8145961165428162})
store['active_learning_steps'][68]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7966294288635254})
store['active_learning_steps'][68]['training']['best_epoch']=5
store['active_learning_steps'][68]['evaluation_metrics']={'accuracy': 0.8973, 'crossentropy': 0.5947015625}
store['active_learning_steps'][68]['acquisition']={'indices': [['id', 43067], ['id', 44182], ['ood', 46287], ['id', 2406], ['ood', 3776]], 'labels': [3, 9, 0, 4, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][69]['training']={}
store['active_learning_steps'][69]['training']['epochs']=[]
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.7939453125, 'crossentropy': 0.9483179450035095})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.853515625, 'crossentropy': 0.7306024432182312})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7251889109611511})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.7401763200759888})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.7615789771080017})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6893149614334106})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7360532283782959})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7450527548789978})
store['active_learning_steps'][69]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.726656973361969})
store['active_learning_steps'][69]['training']['best_epoch']=6
store['active_learning_steps'][69]['evaluation_metrics']={'accuracy': 0.9078, 'crossentropy': 0.539170703125}
store['active_learning_steps'][69]['acquisition']={'indices': [['id', 16606], ['ood', 19714], ['ood', 33891], ['ood', 28725], ['ood', 7357]], 'labels': [0, 5, 5, 1, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][70]['training']={}
store['active_learning_steps'][70]['training']['epochs']=[]
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.83203125, 'crossentropy': 0.8424714803695679})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.6553847789764404})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8701171875, 'crossentropy': 0.6948118209838867})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6554129123687744})
store['active_learning_steps'][70]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6635991930961609})
store['active_learning_steps'][70]['training']['best_epoch']=2
store['active_learning_steps'][70]['evaluation_metrics']={'accuracy': 0.8947, 'crossentropy': 0.564925927734375}
store['active_learning_steps'][70]['acquisition']={'indices': [['ood', 39865], ['ood', 49701], ['ood', 1541], ['ood', 4808], ['ood', 37963]], 'labels': [6, 2, 1, 2, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][71]['training']={}
store['active_learning_steps'][71]['training']['epochs']=[]
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8203125, 'crossentropy': 0.8782232999801636})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6862659454345703})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.7091362476348877})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.869140625, 'crossentropy': 0.6700019836425781})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6707980632781982})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.7297375202178955})
store['active_learning_steps'][71]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.7784560918807983})
store['active_learning_steps'][71]['training']['best_epoch']=4
store['active_learning_steps'][71]['evaluation_metrics']={'accuracy': 0.9051, 'crossentropy': 0.52757060546875}
store['active_learning_steps'][71]['acquisition']={'indices': [['id', 18389], ['ood', 10355], ['ood', 43457], ['ood', 24279], ['id', 2499]], 'labels': [1, 4, 8, 9, 2], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][72]['training']={}
store['active_learning_steps'][72]['training']['epochs']=[]
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8125, 'crossentropy': 0.9082126617431641})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7557538747787476})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.66587233543396})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6727105379104614})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6646961569786072})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.8662109375, 'crossentropy': 0.7367660999298096})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.8228240609169006})
store['active_learning_steps'][72]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7838754653930664})
store['active_learning_steps'][72]['training']['best_epoch']=5
store['active_learning_steps'][72]['evaluation_metrics']={'accuracy': 0.9022, 'crossentropy': 0.55516005859375}
store['active_learning_steps'][72]['acquisition']={'indices': [['id', 48842], ['ood', 34862], ['ood', 49600], ['id', 20599], ['id', 34333]], 'labels': [8, 3, 1, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][73]['training']={}
store['active_learning_steps'][73]['training']['epochs']=[]
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.891547679901123})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.7015061378479004})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6878525614738464})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6764354705810547})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7179663181304932})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6664700508117676})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6676771640777588})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7008554339408875})
store['active_learning_steps'][73]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6975805163383484})
store['active_learning_steps'][73]['training']['best_epoch']=6
store['active_learning_steps'][73]['evaluation_metrics']={'accuracy': 0.9058, 'crossentropy': 0.5372689453125}
store['active_learning_steps'][73]['acquisition']={'indices': [['id', 1862], ['ood', 54190], ['id', 47116], ['id', 27896], ['id', 33448]], 'labels': [3, 4, 8, 1, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][74]['training']={}
store['active_learning_steps'][74]['training']['epochs']=[]
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9172335863113403})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.7219066619873047})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6506085395812988})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.7034897804260254})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.896484375, 'crossentropy': 0.6626337766647339})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6390728950500488})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.900390625, 'crossentropy': 0.6305497884750366})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6785647869110107})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7129156589508057})
store['active_learning_steps'][74]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.697509765625})
store['active_learning_steps'][74]['training']['best_epoch']=7
store['active_learning_steps'][74]['evaluation_metrics']={'accuracy': 0.9148, 'crossentropy': 0.528991650390625}
store['active_learning_steps'][74]['acquisition']={'indices': [['ood', 39899], ['ood', 32159], ['ood', 33199], ['ood', 50503], ['ood', 42812]], 'labels': [3, 7, 7, 9, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][75]['training']={}
store['active_learning_steps'][75]['training']['epochs']=[]
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.845703125, 'crossentropy': 0.8255937099456787})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6251059770584106})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.5851552486419678})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6121727228164673})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6229866147041321})
store['active_learning_steps'][75]['training']['epochs'].append({'accuracy': 0.8935546875, 'crossentropy': 0.6922682523727417})
store['active_learning_steps'][75]['training']['best_epoch']=3
store['active_learning_steps'][75]['evaluation_metrics']={'accuracy': 0.9157, 'crossentropy': 0.4776708984375}
store['active_learning_steps'][75]['acquisition']={'indices': [['ood', 43698], ['id', 36810], ['id', 15092], ['ood', 43400], ['ood', 47476]], 'labels': [1, 6, 4, 5, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][76]['training']={}
store['active_learning_steps'][76]['training']['epochs']=[]
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.80078125, 'crossentropy': 0.9482150077819824})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.7192537188529968})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6602652668952942})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.726972222328186})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6863943934440613})
store['active_learning_steps'][76]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7115415334701538})
store['active_learning_steps'][76]['training']['best_epoch']=3
store['active_learning_steps'][76]['evaluation_metrics']={'accuracy': 0.8967, 'crossentropy': 0.563851806640625}
store['active_learning_steps'][76]['acquisition']={'indices': [['id', 1158], ['id', 45411], ['ood', 46449], ['ood', 27994], ['id', 36291]], 'labels': [3, 7, 9, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][77]['training']={}
store['active_learning_steps'][77]['training']['epochs']=[]
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.833984375, 'crossentropy': 0.886377215385437})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8671875, 'crossentropy': 0.6730086207389832})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8759765625, 'crossentropy': 0.6748247146606445})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.643104076385498})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6834944486618042})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6436944007873535})
store['active_learning_steps'][77]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.711485743522644})
store['active_learning_steps'][77]['training']['best_epoch']=4
store['active_learning_steps'][77]['evaluation_metrics']={'accuracy': 0.9108, 'crossentropy': 0.521160009765625}
store['active_learning_steps'][77]['acquisition']={'indices': [['id', 38103], ['id', 43045], ['id', 11264], ['id', 40293], ['ood', 54885]], 'labels': [0, 0, 4, 9, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][78]['training']={}
store['active_learning_steps'][78]['training']['epochs']=[]
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8349609375, 'crossentropy': 0.9296908378601074})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.86328125, 'crossentropy': 0.6880539059638977})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8642578125, 'crossentropy': 0.6792935132980347})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6101391315460205})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.892578125, 'crossentropy': 0.6097363233566284})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6387614011764526})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6622428894042969})
store['active_learning_steps'][78]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6209955215454102})
store['active_learning_steps'][78]['training']['best_epoch']=5
store['active_learning_steps'][78]['evaluation_metrics']={'accuracy': 0.9106, 'crossentropy': 0.50519482421875}
store['active_learning_steps'][78]['acquisition']={'indices': [['id', 47346], ['id', 15136], ['id', 37816], ['id', 59441], ['ood', 12944]], 'labels': [0, 5, 1, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][79]['training']={}
store['active_learning_steps'][79]['training']['epochs']=[]
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8291015625, 'crossentropy': 0.8722296953201294})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6900672316551208})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6289700269699097})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8994140625, 'crossentropy': 0.6531872749328613})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.6260297894477844})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6317175030708313})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.605659544467926})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6622976064682007})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.8955078125, 'crossentropy': 0.6816352605819702})
store['active_learning_steps'][79]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.6766071319580078})
store['active_learning_steps'][79]['training']['best_epoch']=7
store['active_learning_steps'][79]['evaluation_metrics']={'accuracy': 0.9175, 'crossentropy': 0.49754013671875}
store['active_learning_steps'][79]['acquisition']={'indices': [['ood', 8938], ['ood', 26316], ['id', 14315], ['id', 26082], ['ood', 51210]], 'labels': [7, 9, 6, 9, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][80]['training']={}
store['active_learning_steps'][80]['training']['epochs']=[]
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.822265625, 'crossentropy': 0.8873977661132812})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.6420318484306335})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6343340873718262})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6868999004364014})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6736056804656982})
store['active_learning_steps'][80]['training']['epochs'].append({'accuracy': 0.8916015625, 'crossentropy': 0.6671656370162964})
store['active_learning_steps'][80]['training']['best_epoch']=3
store['active_learning_steps'][80]['evaluation_metrics']={'accuracy': 0.9007, 'crossentropy': 0.5515232421875}
store['active_learning_steps'][80]['acquisition']={'indices': [['id', 56710], ['ood', 33974], ['ood', 6375], ['ood', 42763], ['ood', 1952]], 'labels': [8, 6, 3, 6, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][81]['training']={}
store['active_learning_steps'][81]['training']['epochs']=[]
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.814453125, 'crossentropy': 0.9619134664535522})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8505859375, 'crossentropy': 0.7431930303573608})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8681640625, 'crossentropy': 0.6839171648025513})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.6386531591415405})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.6669994592666626})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.676862359046936})
store['active_learning_steps'][81]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7561055421829224})
store['active_learning_steps'][81]['training']['best_epoch']=4
store['active_learning_steps'][81]['evaluation_metrics']={'accuracy': 0.8985, 'crossentropy': 0.553440283203125}
store['active_learning_steps'][81]['acquisition']={'indices': [['id', 17930], ['id', 15724], ['id', 4298], ['id', 31582], ['id', 21935]], 'labels': [0, 8, 7, 3, 4], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][82]['training']={}
store['active_learning_steps'][82]['training']['epochs']=[]
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.826171875, 'crossentropy': 0.8970803022384644})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.87109375, 'crossentropy': 0.675537109375})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.6751915812492371})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6778964996337891})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8818359375, 'crossentropy': 0.6430060863494873})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7518067359924316})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.7745133638381958})
store['active_learning_steps'][82]['training']['epochs'].append({'accuracy': 0.888671875, 'crossentropy': 0.7063596248626709})
store['active_learning_steps'][82]['training']['best_epoch']=5
store['active_learning_steps'][82]['evaluation_metrics']={'accuracy': 0.9092, 'crossentropy': 0.53378466796875}
store['active_learning_steps'][82]['acquisition']={'indices': [['id', 39584], ['id', 38806], ['ood', 8700], ['id', 9190], ['id', 18225]], 'labels': [4, 1, 6, 4, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][83]['training']={}
store['active_learning_steps'][83]['training']['epochs']=[]
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.84375, 'crossentropy': 0.848157525062561})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6631285548210144})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6649748086929321})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6427077054977417})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.7048677802085876})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.6388330459594727})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6771779656410217})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.7523201704025269})
store['active_learning_steps'][83]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7484166026115417})
store['active_learning_steps'][83]['training']['best_epoch']=6
store['active_learning_steps'][83]['evaluation_metrics']={'accuracy': 0.9126, 'crossentropy': 0.510325732421875}
store['active_learning_steps'][83]['acquisition']={'indices': [['ood', 51326], ['id', 27982], ['id', 42087], ['id', 51643], ['id', 3576]], 'labels': [8, 0, 3, 7, 3], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][84]['training']={}
store['active_learning_steps'][84]['training']['epochs']=[]
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8427734375, 'crossentropy': 0.8623753786087036})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8720703125, 'crossentropy': 0.6926407814025879})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8828125, 'crossentropy': 0.6367248296737671})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8779296875, 'crossentropy': 0.5754054188728333})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.88671875, 'crossentropy': 0.6627391576766968})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.89453125, 'crossentropy': 0.591700553894043})
store['active_learning_steps'][84]['training']['epochs'].append({'accuracy': 0.8876953125, 'crossentropy': 0.7252882719039917})
store['active_learning_steps'][84]['training']['best_epoch']=4
store['active_learning_steps'][84]['evaluation_metrics']={'accuracy': 0.9093, 'crossentropy': 0.50104052734375}
store['active_learning_steps'][84]['acquisition']={'indices': [['ood', 33275], ['ood', 19978], ['ood', 10127], ['ood', 20364], ['ood', 21167]], 'labels': [1, 1, 6, 4, 5], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][85]['training']={}
store['active_learning_steps'][85]['training']['epochs']=[]
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8193359375, 'crossentropy': 0.8903285264968872})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.865234375, 'crossentropy': 0.717132568359375})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.6694622039794922})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8798828125, 'crossentropy': 0.6740677952766418})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.875, 'crossentropy': 0.698409378528595})
store['active_learning_steps'][85]['training']['epochs'].append({'accuracy': 0.8740234375, 'crossentropy': 0.7947954535484314})
store['active_learning_steps'][85]['training']['best_epoch']=3
store['active_learning_steps'][85]['evaluation_metrics']={'accuracy': 0.9056, 'crossentropy': 0.529632177734375}
store['active_learning_steps'][85]['acquisition']={'indices': [['ood', 38492], ['ood', 23305], ['id', 23435], ['ood', 53254], ['id', 6000]], 'labels': [5, 9, 4, 0, 6], 'scores': [0.0, 0.0, 0.0, 0.0, 0.0]}
store['active_learning_steps'].append({})
store['active_learning_steps'][86]['training']={}
store['active_learning_steps'][86]['training']['epochs']=[]
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.828125, 'crossentropy': 0.905552864074707})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.861328125, 'crossentropy': 0.6988954544067383})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.876953125, 'crossentropy': 0.6841083765029907})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8857421875, 'crossentropy': 0.6929631233215332})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.873046875, 'crossentropy': 0.6959416270256042})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.884765625, 'crossentropy': 0.6647448539733887})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.87890625, 'crossentropy': 0.7119313478469849})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.890625, 'crossentropy': 0.6365624070167542})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8896484375, 'crossentropy': 0.7586708068847656})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.880859375, 'crossentropy': 0.7356734275817871})
store['active_learning_steps'][86]['training']['epochs'].append({'accuracy': 0.8837890625, 'crossentropy': 0.7227754592895508})
store['active_learning_steps'][86]['training']['best_epoch']=8
store['active_learning_steps'][86]['evaluation_metrics']={'accuracy': 0.9143, 'crossentropy': 0.54089189453125}
